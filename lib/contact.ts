/* Validation du formulaire de contact et limite d'envois par adresse IP. */

export const FILIALES_CONTACT = ["Maria BTP", "Maria Gold", "Maria Group (général)"] as const;

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function clean(value: unknown, max: number): string {
  return typeof value === "string" ? value.trim().slice(0, max) : "";
}

export type ContactData = {
  nom: string;
  societe: string;
  email: string;
  telephone: string;
  filiale: string;
  message: string;
};

export function validateContact(body: Record<string, unknown>): { data: ContactData; errors: string[] } {
  const data: ContactData = {
    nom: clean(body.nom, 120),
    societe: clean(body.societe, 160),
    email: clean(body.email, 200),
    telephone: clean(body.telephone, 40),
    filiale: clean(body.pole, 60),
    message: clean(body.message, 5000),
  };
  const errors: string[] = [];
  if (!data.nom) errors.push("nom");
  if (!EMAIL_RE.test(data.email)) errors.push("email");
  if (!(FILIALES_CONTACT as readonly string[]).includes(data.filiale)) errors.push("pole");
  if (data.message.length < 5) errors.push("message");
  if (body.consent !== true) errors.push("consent");
  return { data, errors };
}

/* 5 envois par adresse IP toutes les 10 minutes ; 10 000 adresses suivies au maximum. */
const RATE_WINDOW_MS = 10 * 60 * 1000;
const RATE_MAX = 5;
const RATE_MAX_TRACKED = 10_000;
const hits = new Map<string, { count: number; reset: number }>();

function purgeExpired(now: number) {
  for (const [ip, entry] of hits) if (entry.reset < now) hits.delete(ip);
}

export function rateLimited(ip: string): boolean {
  const now = Date.now();
  const entry = hits.get(ip);
  if (!entry || entry.reset < now) {
    if (!entry && hits.size >= RATE_MAX_TRACKED) {
      purgeExpired(now);
      if (hits.size >= RATE_MAX_TRACKED) {
        const oldest = hits.keys().next().value;
        if (oldest !== undefined) hits.delete(oldest);
      }
    }
    hits.set(ip, { count: 1, reset: now + RATE_WINDOW_MS });
    return false;
  }
  entry.count += 1;
  return entry.count > RATE_MAX;
}

/**
 * Adresse du visiteur : dernière valeur de X-Forwarded-For, ajoutée par le proxy Traefik.
 * (Les valeurs précédentes peuvent être envoyées par le client et ne sont pas fiables.)
 */
export function clientIp(headers: Headers): string {
  const forwarded = headers.get("x-forwarded-for");
  if (forwarded) {
    const parts = forwarded.split(",").map((p) => p.trim()).filter(Boolean);
    if (parts.length) return parts[parts.length - 1];
  }
  return headers.get("x-real-ip") ?? "inconnue";
}

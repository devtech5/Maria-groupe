import { NextResponse, type NextRequest } from "next/server";
import { clientIp, rateLimited, validateContact } from "@/lib/contact";
import { ensureSchema, getPool } from "@/lib/db";

const MAX_BODY_BYTES = 20 * 1024;

export async function POST(request: NextRequest) {
  if (!request.headers.get("content-type")?.includes("application/json")) {
    return NextResponse.json({ ok: false, error: "Requête invalide." }, { status: 415 });
  }

  const declared = Number(request.headers.get("content-length") ?? 0);
  if (declared > MAX_BODY_BYTES) {
    return NextResponse.json({ ok: false, error: "Requête trop volumineuse." }, { status: 413 });
  }

  const raw = await request.text();
  if (raw.length > MAX_BODY_BYTES) {
    return NextResponse.json({ ok: false, error: "Requête trop volumineuse." }, { status: 413 });
  }

  let body: Record<string, unknown>;
  try {
    const parsed: unknown = JSON.parse(raw);
    if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) throw new Error();
    body = parsed as Record<string, unknown>;
  } catch {
    return NextResponse.json({ ok: false, error: "Requête invalide." }, { status: 400 });
  }

  // Champ piège anti-robot : réponse « ok » sans rien enregistrer.
  if (body.website) return NextResponse.json({ ok: true });

  if (rateLimited(clientIp(request.headers))) {
    return NextResponse.json({ ok: false, error: "Trop de demandes, réessayez plus tard." }, { status: 429 });
  }

  const { data, errors } = validateContact(body);
  if (errors.length) {
    return NextResponse.json({ ok: false, error: "Champs invalides.", fields: errors }, { status: 400 });
  }

  const pool = getPool();
  if (!pool) return NextResponse.json({ ok: false, error: "Service indisponible." }, { status: 503 });

  try {
    await ensureSchema();
    await pool.query(
      `INSERT INTO contact_messages (nom, societe, email, telephone, filiale, message)
       VALUES ($1, $2, $3, $4, $5, $6)`,
      [data.nom, data.societe || null, data.email, data.telephone || null, data.filiale, data.message]
    );
    return NextResponse.json({ ok: true }, { status: 201 });
  } catch (err) {
    console.error("[api] enregistrement du message impossible :", (err as Error).message);
    return NextResponse.json({ ok: false, error: "Erreur serveur." }, { status: 500 });
  }
}

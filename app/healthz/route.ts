export const dynamic = "force-dynamic";

/* Vérification de vie du conteneur (ne dépend pas de la base). */
export function GET() {
  return new Response("ok", { headers: { "content-type": "text/plain; charset=utf-8" } });
}

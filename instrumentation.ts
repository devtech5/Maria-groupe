/* Au démarrage du serveur : vérifie la connexion à PostgreSQL et crée les tables. */
export async function register() {
  if (process.env.NEXT_RUNTIME !== "nodejs") return;
  const { getPool, ensureSchema } = await import("./lib/db");
  if (!getPool()) {
    console.warn("[db] DATABASE_URL non défini : contenu par défaut, formulaire de contact désactivé.");
    return;
  }
  const attempt = () =>
    ensureSchema()
      .then(() => console.log("[db] connecté, schéma à jour."))
      .catch((err: Error) => {
        console.error("[db] initialisation impossible, nouvelle tentative dans 5 s :", err.message);
        setTimeout(attempt, 5000).unref();
      });
  attempt();
}

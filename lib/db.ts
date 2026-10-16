import fs from "node:fs";
import path from "node:path";
import { Pool } from "pg";

/*
 * Connexion PostgreSQL partagée (DATABASE_URL).
 * Sans DATABASE_URL, getPool() renvoie null : le site s'affiche avec son contenu par défaut.
 */

const globalForDb = globalThis as unknown as { mariaPool?: Pool | null; mariaSchema?: Promise<void> | null };

export function getPool(): Pool | null {
  if (globalForDb.mariaPool !== undefined) return globalForDb.mariaPool;
  const url = process.env.DATABASE_URL;
  if (!url) {
    globalForDb.mariaPool = null;
    return null;
  }
  const pool = new Pool({ connectionString: url, max: 5, connectionTimeoutMillis: 5000 });
  pool.on("error", (err) => console.error("[db] erreur de connexion :", err.message));
  globalForDb.mariaPool = pool;
  return pool;
}

/** Crée les tables si besoin (une seule fois par processus ; réessaie après un échec). */
export function ensureSchema(): Promise<void> {
  const pool = getPool();
  if (!pool) return Promise.reject(new Error("DATABASE_URL non défini"));
  if (!globalForDb.mariaSchema) {
    const sql = fs.readFileSync(path.join(process.cwd(), "db", "schema.sql"), "utf8");
    globalForDb.mariaSchema = pool.query(sql).then(
      () => undefined,
      (err) => {
        globalForDb.mariaSchema = null;
        throw err;
      }
    );
  }
  return globalForDb.mariaSchema;
}

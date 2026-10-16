/*
 * Lecture des données affichées sur le site (projets, réalisations, chiffres clés).
 * Source : PostgreSQL. Repli sur le contenu par défaut si la base est absente, vide ou en erreur.
 * Les résultats sont gardés en mémoire 60 secondes pour limiter les requêtes.
 */
import type { Filiale } from "@/components/icons";
import {
  DEFAULT_CHIFFRES,
  DEFAULT_PROJETS,
  DEFAULT_REALISATIONS,
  type ChiffreCle,
  type Projet,
  type ProjetType,
} from "@/lib/content";
import { ensureSchema, getPool } from "@/lib/db";
import { photo } from "@/lib/photos";

const TTL_MS = 60_000;
const cache = new Map<string, { expires: number; value: unknown }>();

async function cached<T>(key: string, load: () => Promise<T>): Promise<T> {
  const hit = cache.get(key);
  if (hit && hit.expires > Date.now()) return hit.value as T;
  const value = await load();
  cache.set(key, { expires: Date.now() + TTL_MS, value });
  return value;
}

async function query<R>(sql: string, params: unknown[] = []): Promise<R[] | null> {
  const pool = getPool();
  if (!pool) return null;
  try {
    await ensureSchema();
    const result = await pool.query(sql, params);
    return result.rows as R[];
  } catch (err) {
    console.error("[data] lecture impossible :", (err as Error).message);
    return null;
  }
}

/* Seuls les chemins locaux simples sont acceptés pour les images (protège l'attribut style). */
const SAFE_IMAGE = /^\/[A-Za-z0-9/_.-]+\.(jpe?g|png|webp)$/;

type ProjetRow = {
  id: string;
  type: ProjetType;
  filiale: Filiale;
  categorie: string;
  statut: string | null;
  titre: string;
  description: string;
  lieu: string | null;
  annee: number | null;
  image_url: string | null;
};

function toProjet(row: ProjetRow): Projet {
  return {
    id: String(row.id),
    type: row.type,
    filiale: row.filiale,
    categorie: row.categorie,
    statut: row.statut,
    titre: row.titre,
    description: row.description,
    lieu: row.lieu,
    annee: row.annee,
    imageUrl: row.image_url && SAFE_IMAGE.test(row.image_url) ? row.image_url : null,
  };
}

export async function getProjets(type: ProjetType): Promise<Projet[]> {
  return cached(`projets:${type}`, async () => {
    const rows = await query<ProjetRow>(
      `SELECT id, type, filiale, categorie, statut, titre, description, lieu, annee, image_url
         FROM projets
        WHERE publie AND type = $1
        ORDER BY ordre, created_at DESC`,
      [type]
    );
    if (rows && rows.length) return rows.map(toProjet);
    // Contenu par défaut : photos facultatives projet-N.jpg / realisation-N.jpg
    const defaults = type === "projet" ? DEFAULT_PROJETS : DEFAULT_REALISATIONS;
    return defaults.map((p, i) => ({ ...p, imageUrl: photo(`${type}-${i + 1}.jpg`) }));
  });
}

export async function getChiffresCles(): Promise<ChiffreCle[]> {
  return cached("chiffres", async () => {
    const rows = await query<ChiffreCle>(
      `SELECT valeur, suffixe, libelle FROM chiffres_cles WHERE publie ORDER BY ordre, id LIMIT 4`
    );
    return rows && rows.length ? rows : DEFAULT_CHIFFRES;
  });
}

/** Sélection courte pour un aperçu : alterne les filiales, dans l'ordre d'affichage. */
export function apercu(projets: Projet[], n = 3): Projet[] {
  const btp = projets.filter((p) => p.filiale === "btp");
  const gold = projets.filter((p) => p.filiale === "gold");
  const out: Projet[] = [];
  while (out.length < n && (btp.length || gold.length)) {
    const next = (out.length % 2 === 0 ? btp.shift() ?? gold.shift() : gold.shift() ?? btp.shift()) as Projet;
    out.push(next);
  }
  return out;
}

/*
 * Serveur du site Maria Group
 * - sert les pages statiques du dossier public/
 * - expose l'API du formulaire de contact, qui enregistre les messages dans PostgreSQL
 *
 * Variables d'environnement :
 *   DATABASE_URL  chaîne de connexion PostgreSQL (ex. postgresql://user:pass@hote:5432/base)
 *   PORT          port d'écoute (défaut : 3000)
 */
"use strict";

const path = require("node:path");
const fs = require("node:fs");
const express = require("express");
const compression = require("compression");
const { Pool } = require("pg");

const PORT = Number(process.env.PORT) || 3000;
const PUBLIC_DIR = path.join(__dirname, "public");
const SCHEMA = fs.readFileSync(path.join(__dirname, "db", "schema.sql"), "utf8");

/* ------------------------------------------------------------------ */
/* Base de données                                                     */
/* ------------------------------------------------------------------ */
const pool = process.env.DATABASE_URL
  ? new Pool({ connectionString: process.env.DATABASE_URL, max: 5, connectionTimeoutMillis: 5000 })
  : null;

let dbReady = false;

if (pool) {
  pool.on("error", (err) => console.error("[db] erreur de connexion :", err.message));
} else {
  console.warn("[db] DATABASE_URL non défini : le formulaire de contact est désactivé.");
}

/* Crée les tables au démarrage ; réessaie tant que la base n'est pas joignable. */
async function initDb() {
  if (!pool) return;
  try {
    await pool.query(SCHEMA);
    dbReady = true;
    console.log("[db] connecté, schéma à jour.");
  } catch (err) {
    console.error("[db] initialisation impossible, nouvelle tentative dans 5 s :", err.message);
    setTimeout(initDb, 5000).unref();
  }
}

/* ------------------------------------------------------------------ */
/* Validation du formulaire                                            */
/* ------------------------------------------------------------------ */
const FILIALES = ["Maria BTP", "Maria Gold", "Maria Group (général)"];
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function clean(value, max) {
  if (typeof value !== "string") return "";
  return value.trim().slice(0, max);
}

function validateContact(body) {
  const data = {
    nom: clean(body.nom, 120),
    societe: clean(body.societe, 160),
    email: clean(body.email, 200),
    telephone: clean(body.telephone, 40),
    filiale: clean(body.pole, 60),
    message: clean(body.message, 5000),
  };
  const errors = [];
  if (!data.nom) errors.push("nom");
  if (!EMAIL_RE.test(data.email)) errors.push("email");
  if (!FILIALES.includes(data.filiale)) errors.push("pole");
  if (data.message.length < 5) errors.push("message");
  if (body.consent !== true && body.consent !== "on") errors.push("consent");
  return { data, errors };
}

/* Limite simple : 5 envois par adresse IP toutes les 10 minutes. */
const RATE_WINDOW_MS = 10 * 60 * 1000;
const RATE_MAX = 5;
const hits = new Map();

function rateLimited(ip) {
  const now = Date.now();
  const entry = hits.get(ip);
  if (!entry || entry.reset < now) {
    hits.set(ip, { count: 1, reset: now + RATE_WINDOW_MS });
    return false;
  }
  entry.count += 1;
  return entry.count > RATE_MAX;
}

setInterval(() => {
  const now = Date.now();
  for (const [ip, entry] of hits) if (entry.reset < now) hits.delete(ip);
}, RATE_WINDOW_MS).unref();

/* ------------------------------------------------------------------ */
/* Application                                                         */
/* ------------------------------------------------------------------ */
const app = express();
app.disable("x-powered-by");
app.set("trust proxy", 1); // derrière le proxy Traefik de Dokploy

app.use(compression());
app.use((req, res, next) => {
  res.set({
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
    "Referrer-Policy": "strict-origin-when-cross-origin",
  });
  next();
});

/* Vérification de vie du conteneur (ne dépend pas de la base). */
app.get("/healthz", (req, res) => res.type("text").send("ok"));

/* État de la connexion à la base. */
app.get("/api/health", async (req, res) => {
  if (!pool) return res.status(503).json({ ok: false, db: "non configurée" });
  try {
    await pool.query("SELECT 1");
    res.json({ ok: true, db: "connectée" });
  } catch {
    res.status(503).json({ ok: false, db: "injoignable" });
  }
});

app.post("/api/contact", express.json({ limit: "20kb" }), async (req, res) => {
  const body = req.body || {};

  // Champ piège anti-robot : on répond « ok » sans rien enregistrer.
  if (body.website) return res.json({ ok: true });

  if (rateLimited(req.ip)) {
    return res.status(429).json({ ok: false, error: "Trop de demandes, réessayez plus tard." });
  }

  const { data, errors } = validateContact(body);
  if (errors.length) return res.status(400).json({ ok: false, error: "Champs invalides.", fields: errors });

  if (!pool || !dbReady) return res.status(503).json({ ok: false, error: "Service indisponible." });

  try {
    await pool.query(
      `INSERT INTO contact_messages (nom, societe, email, telephone, filiale, message)
       VALUES ($1, $2, $3, $4, $5, $6)`,
      [data.nom, data.societe || null, data.email, data.telephone || null, data.filiale, data.message]
    );
    res.status(201).json({ ok: true });
  } catch (err) {
    console.error("[api] enregistrement du message impossible :", err.message);
    res.status(500).json({ ok: false, error: "Erreur serveur." });
  }
});

/* Toute autre route /api inconnue */
app.use("/api", (req, res) => res.status(404).json({ ok: false, error: "Introuvable." }));

/* Pages et ressources statiques ; /btp sert btp.html */
app.use(
  express.static(PUBLIC_DIR, {
    extensions: ["html"],
    setHeaders(res, filePath) {
      if (filePath.endsWith(".html")) res.setHeader("Cache-Control", "no-cache");
      else res.setHeader("Cache-Control", "public, max-age=604800");
    },
  })
);

/* Page 404 */
app.use((req, res) => res.status(404).sendFile(path.join(PUBLIC_DIR, "404.html")));

/* Erreurs (ex. JSON mal formé) */
app.use((err, req, res, next) => {
  if (res.headersSent) return next(err);
  const status = err.status || err.statusCode || 500;
  if (status >= 500) console.error("[app]", err);
  if (req.path.startsWith("/api")) return res.status(status).json({ ok: false, error: "Requête invalide." });
  res.status(status).sendFile(path.join(PUBLIC_DIR, "404.html"));
});

const server = app.listen(PORT, () => {
  console.log(`[app] Maria Group en écoute sur le port ${PORT}`);
  initDb();
});

function shutdown() {
  server.close(() => {
    if (pool) pool.end().finally(() => process.exit(0));
    else process.exit(0);
  });
  setTimeout(() => process.exit(0), 8000).unref();
}
process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);

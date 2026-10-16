-- Schéma de la base Maria Group (exécuté automatiquement au démarrage du serveur).
-- Toutes les instructions sont idempotentes.

-- Messages du formulaire de contact
CREATE TABLE IF NOT EXISTS contact_messages (
  id          BIGSERIAL PRIMARY KEY,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  nom         TEXT NOT NULL,
  societe     TEXT,
  email       TEXT NOT NULL,
  telephone   TEXT,
  filiale     TEXT NOT NULL,
  message     TEXT NOT NULL,
  traite      BOOLEAN NOT NULL DEFAULT false
);

CREATE INDEX IF NOT EXISTS contact_messages_created_at_idx
  ON contact_messages (created_at DESC);

-- Projets (en cours / en préparation) et réalisations (livrées) affichés sur le site
CREATE TABLE IF NOT EXISTS projets (
  id           BIGSERIAL PRIMARY KEY,
  type         TEXT NOT NULL CHECK (type IN ('projet', 'realisation')),
  filiale      TEXT NOT NULL CHECK (filiale IN ('btp', 'gold')),
  categorie    TEXT NOT NULL,             -- ex. Bâtiment, Génie civil, Exploration
  statut       TEXT,                      -- projets : ex. En cours, En préparation
  titre        TEXT NOT NULL,
  description  TEXT NOT NULL,
  lieu         TEXT,
  annee        INTEGER,
  image_url    TEXT,                      -- chemin local, ex. /assets/img/photos/projet-1.jpg
  ordre        INTEGER NOT NULL DEFAULT 0,
  publie       BOOLEAN NOT NULL DEFAULT true,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS projets_type_idx ON projets (type, publie, ordre);

-- Chiffres clés de la page d'accueil
CREATE TABLE IF NOT EXISTS chiffres_cles (
  id       SERIAL PRIMARY KEY,
  valeur   INTEGER NOT NULL,
  suffixe  TEXT NOT NULL DEFAULT '',      -- ex. %, +, /7
  libelle  TEXT NOT NULL,
  ordre    INTEGER NOT NULL DEFAULT 0,
  publie   BOOLEAN NOT NULL DEFAULT true
);

-- Schéma de la base Maria Group (exécuté automatiquement au démarrage du serveur)

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

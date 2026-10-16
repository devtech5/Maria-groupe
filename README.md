# Maria Group — site web

Site de **Maria Group** et de ses filiales **Maria BTP** (bâtiment et travaux publics) et **Maria Gold** (exploration et exploitation aurifère).

## Stack

| Couche | Technologie |
|---|---|
| Interface | React 19 + Next.js 16 (App Router), TypeScript |
| Données | PostgreSQL (bibliothèque `pg`) |
| Hébergement | Docker (Node.js 22) sur Dokploy, HTTPS par Traefik / Let's Encrypt |

## Charte graphique

| Élément | Valeur |
|---|---|
| Couleur primaire | `#162E49` (bleu marine) |
| Couleur secondaire | `#BFA169` (or) |
| Titres | Montserrat (hébergée dans `app/fonts/`) |
| Texte | Open Sans (hébergée dans `app/fonts/`) |

Les couleurs sont des variables CSS en haut de `app/globals.css`.

## Structure

```
app/                     Pages (une route par dossier) et routes API
  layout.tsx             En-tête, pied de page, polices, métadonnées
  page.tsx               Accueil
  groupe/ btp/ gold/ projets/ realisations/ contact/ mentions-legales/
  not-found.tsx          Page 404
  api/contact/route.ts   POST : enregistre un message du formulaire
  api/health/route.ts    GET : état de la connexion à la base
  healthz/route.ts       GET : contrôle de vie du conteneur
  globals.css            Styles du site
components/              Composants React (en-tête, pied de page, blocs, grilles, formulaire, icônes)
lib/
  content.ts             Coordonnées, menu, filiales, contenu par défaut
  data.ts                Lecture des projets / réalisations / chiffres clés dans PostgreSQL
  db.ts                  Connexion PostgreSQL et création des tables
  contact.ts             Validation du formulaire et limite d'envois
db/schema.sql            Tables PostgreSQL (créées automatiquement au démarrage)
proxy.ts                 En-têtes de sécurité (CSP avec nonce, HSTS…)
public/assets/img/       Logos, favicons, photos optionnelles (photos/)
Dockerfile               Image de production
```

## Données affichées depuis PostgreSQL

Le site lit trois types de données. Tant qu'une table est vide (ou si la base est indisponible), le contenu par défaut de `lib/content.ts` s'affiche. Les données sont mises en cache 60 secondes : une modification apparaît sur le site au plus tard une minute après.

| Table | Affichée sur | Champs principaux |
|---|---|---|
| `projets` (type `projet`) | Accueil, Projets, pages Maria BTP / Maria Gold | `filiale` (`btp` ou `gold`), `categorie`, `statut`, `titre`, `description`, `lieu`, `annee`, `image_url`, `ordre`, `publie` |
| `projets` (type `realisation`) | Accueil, Réalisations | mêmes champs |
| `chiffres_cles` | Accueil (4 premiers) | `valeur`, `suffixe`, `libelle`, `ordre`, `publie` |

Exemples (terminal de la base dans Dokploy, ou tout client PostgreSQL) :

```sql
-- Ajouter un projet en cours
INSERT INTO projets (type, filiale, categorie, statut, titre, description, lieu, annee, ordre)
VALUES ('projet', 'gold', 'Exploration', 'En cours', 'Permis aurifère de …', 'Campagne de sondages…', 'Bouaké', 2026, 1);

-- Ajouter une réalisation avec photo (fichier déposé dans public/assets/img/photos/)
INSERT INTO projets (type, filiale, categorie, titre, description, image_url)
VALUES ('realisation', 'btp', 'Génie civil', 'Pont de …', 'Ouvrage livré en …', '/assets/img/photos/pont.jpg');

-- Masquer un élément sans le supprimer
UPDATE projets SET publie = false WHERE id = 3;

-- Chiffres clés de l'accueil
INSERT INTO chiffres_cles (valeur, suffixe, libelle, ordre) VALUES
  (15, '+', 'Années d''expérience', 1),
  (120, '', 'Collaborateurs', 2);
```

Pour des raisons de sécurité, `image_url` n'accepte que des chemins locaux simples (`/assets/…/fichier.jpg|png|webp`).

### Brancher les données d'une autre application

Les lectures sont regroupées dans `lib/data.ts`. Pour afficher les données d'une autre application :

- **même serveur PostgreSQL** : créer un utilisateur en lecture seule limité aux tables ou vues utiles, puis adapter les requêtes de `lib/data.ts` ;
- **API** : remplacer les requêtes SQL de `lib/data.ts` par des appels `fetch` côté serveur, avec la clé de l'API dans une variable d'environnement (jamais préfixée `NEXT_PUBLIC_`).

## Formulaire de contact

Le formulaire envoie les messages à `POST /api/contact`. Le serveur les valide (champs obligatoires, e-mail, anti-robot, 20 Ko max., 5 envois par IP toutes les 10 minutes) puis les enregistre dans la table `contact_messages`.

```sql
SELECT id, created_at, nom, societe, email, telephone, filiale, message
FROM contact_messages WHERE NOT traite ORDER BY created_at DESC;

UPDATE contact_messages SET traite = true WHERE id = 1;
```

## Variables d'environnement

| Variable | Rôle |
|---|---|
| `DATABASE_URL` | Chaîne de connexion PostgreSQL, ex. `postgresql://maria:motdepasse@hote:5432/maria` |
| `SITE_URL` | URL publique du site (métadonnées), défaut `https://maria-groupe.com` |
| `PORT` | Port d'écoute, défaut `3000` |

## Développement local

```bash
npm install
cp .env.example .env.local   # puis adapter DATABASE_URL
npm run dev                  # http://localhost:3000
```

Autres commandes : `npm run typecheck`, `npm run build`, `npm start`.

## Ajouter des photos

Déposez vos photos dans `public/assets/img/photos/` ; elles remplacent automatiquement les illustrations :

| Fichier | Emplacement |
|---|---|
| `hero.jpg` | Grande bannière de l'accueil |
| `btp.jpg`, `gold.jpg` | Cartes des filiales et visuels des pages Maria BTP / Maria Gold |
| `projet-1.jpg` … / `realisation-1.jpg` … | Cartes du contenu par défaut (pour les données en base, utilisez `image_url`) |

Format conseillé : JPG, 1600 px de large maximum, moins de 400 Ko.

## Sécurité

- `Content-Security-Policy` avec nonce unique par requête (seuls les scripts du site s'exécutent, aucune ressource externe), `Strict-Transport-Security` en HTTPS, `Permissions-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Cross-Origin-Opener-Policy`.
- Requêtes SQL paramétrées ; la connexion à la base n'existe que côté serveur.
- Aucune ressource tierce : polices hébergées localement, pas de cookie ni de traceur.
- Conteneur exécuté avec un utilisateur non administrateur.
- Ne publiez pas de port pour l'application dans Dokploy (passez uniquement par **Domains** / Traefik), sinon l'adresse IP utilisée pour la limite d'envois peut être falsifiée.

## Déploiement avec Dokploy (VPS)

### 1. Base PostgreSQL

1. **Create Service → Database → PostgreSQL** : nom `maria-db`, base `maria`, utilisateur `maria`, mot de passe fort.
2. **Deploy**, puis copier l'**Internal Connection URL** (onglet **General**).
3. Ne pas activer d'**External Port**. Activer les **Backups**.

### 2. Application

1. **Create Service → Application**, source **GitHub** : dépôt `devtech5/Maria-groupe`, branche `main`.
2. **Build Type : Dockerfile**.
3. **Environment** : `DATABASE_URL=<Internal Connection URL>`.
4. **Domains** : `maria-groupe.com` et `www.maria-groupe.com`, **Container Port : 3000**, HTTPS Let's Encrypt.
5. **Deploy**, puis vérifier `https://maria-groupe.com/api/health` → `{"ok":true,"db":"connectée"}`.

Les anciennes adresses en `.html` (ex. `/btp.html`) sont redirigées vers les nouvelles (`/btp`).

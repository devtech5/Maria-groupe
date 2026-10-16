# Maria Group — site vitrine

Site internet de **Maria Group** et de ses filiales **Maria BTP** (bâtiment et travaux publics) et **Maria Gold** (exploration et exploitation aurifère).

Pages HTML / CSS / JavaScript servies par un petit serveur Node.js (`server.js`) qui enregistre aussi les messages du formulaire de contact dans **PostgreSQL**.

## Charte graphique

| Élément | Valeur |
|---|---|
| Couleur primaire | `#162E49` (bleu marine) |
| Couleur secondaire | `#BFA169` (or) |
| Titres | Montserrat (hébergée dans `public/assets/fonts/`) |
| Texte | Open Sans (hébergée dans `public/assets/fonts/`) |

Les couleurs sont définies une seule fois, en variables CSS, en haut de `assets/css/style.css`.

## Menu et pages

- **Accueil** — `index.html`
- **Maria Group** (sous-menu)
  - Qui sommes-nous — `groupe.html` (histoire, mission / vision, filiales, valeurs, engagement QHSE)
  - Maria BTP — `btp.html`
  - Maria Gold — `gold.html`
- **Projets** — `projets.html` (projets en cours / en préparation, filtrables par filiale)
- **Réalisations** — `realisations.html` (projets livrés, filtrables par filiale)
- **Contacts** — `contact.html` (coordonnées, WhatsApp, formulaire de demande de devis)

Autres pages : `mentions-legales.html`, `404.html`.

Le menu se modifie dans la liste `NAV` de `tools/build.py`.

## Structure

```
public/              Site publié (pages HTML générées, CSS, JS, images)
  assets/css/        Styles
  assets/js/         Menu, animations, filtres, envoi du formulaire
  assets/img/        Logos, favicons, photos optionnelles (img/photos/)
server.js            Serveur : pages statiques + API du formulaire
db/schema.sql        Tables PostgreSQL (créées automatiquement au démarrage)
tools/build.py       Générateur des pages HTML (dans public/)
tools/icons.py       Icônes et illustrations SVG
Dockerfile           Image de production (Node.js 22)
```

## Modifier le site

Les pages HTML sont générées par `tools/build.py` (en-tête, pied de page et coordonnées partagés).
Pour modifier un texte, les coordonnées ou le menu :

1. Éditer `tools/build.py` (les coordonnées sont regroupées en haut du fichier : téléphone, e-mail, adresse, horaires, réseaux sociaux).
2. Régénérer les pages (écrites dans `public/`) :

   ```bash
   python3 tools/build.py
   ```

Python 3 suffit, aucune bibliothèque n'est nécessaire. Committez ensuite les fichiers de `public/`.

## À compléter avant la mise en ligne

- **Coordonnées** : e-mail, mobile et fixe sont renseignés. Restent à compléter : adresse, horaires, liens réseaux sociaux (en haut de `tools/build.py`).
- **Projets et réalisations** : les cartes actuelles sont des exemples génériques. Les remplacer par vos projets réels (listes `PROJETS` et `REALISATIONS` dans `tools/build.py`).
- **Mentions légales** : forme juridique, RCCM, hébergeur, directeur de publication.

## Ajouter des photos

Le site fonctionne sans photo (illustrations dorées sur fond bleu). Pour ajouter vos propres photos, déposez-les dans `public/assets/img/photos/` avec les noms suivants, puis relancez `python3 tools/build.py` :

| Fichier | Emplacement |
|---|---|
| `hero.jpg` | Grande bannière de l'accueil |
| `btp.jpg`, `gold.jpg` | Cartes des filiales et visuels des pages Maria BTP / Maria Gold |
| `projet-1.jpg` … `projet-6.jpg` | Cartes de la page Projets (ordre de la liste `PROJETS`) |
| `realisation-1.jpg` … `realisation-6.jpg` | Cartes de la page Réalisations (ordre de la liste `REALISATIONS`) |

Un filtre bleu est appliqué automatiquement pour garder la cohérence avec la charte. Format conseillé : JPG, 1600 px de large maximum, moins de 400 Ko.

## Base de données PostgreSQL

Le formulaire de la page Contacts envoie les messages à `POST /api/contact`. Le serveur les valide (champs obligatoires, e-mail, anti-robot, 5 envois max. par IP toutes les 10 minutes) puis les enregistre dans la table `contact_messages` (voir `db/schema.sql`), créée automatiquement au démarrage.

| Variable | Rôle |
|---|---|
| `DATABASE_URL` | Chaîne de connexion PostgreSQL, ex. `postgresql://maria:motdepasse@hote:5432/maria` |
| `PORT` | Port d'écoute du serveur (défaut `3000`) |

Sans `DATABASE_URL`, le site fonctionne mais le formulaire répond « service indisponible ».

Routes utiles :

- `GET /healthz` : le serveur répond (utilisé par le contrôle de santé Docker) ;
- `GET /api/health` : état de la connexion à la base.

Consulter les messages (terminal de la base dans Dokploy, ou tout client PostgreSQL) :

```sql
SELECT id, created_at, nom, societe, email, telephone, filiale, message
FROM contact_messages
WHERE NOT traite
ORDER BY created_at DESC;

-- marquer un message comme traité
UPDATE contact_messages SET traite = true WHERE id = 1;
```

## Sécurité

- Requêtes SQL paramétrées, validation et limite de taille des champs, champ anti-robot, 5 envois max. par IP toutes les 10 minutes (10 000 adresses suivies au maximum).
- En-têtes : `Content-Security-Policy` (aucune ressource externe autorisée), `Strict-Transport-Security` (en HTTPS), `Permissions-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Cross-Origin-Opener-Policy`.
- Aucune ressource tierce : polices hébergées localement, pas de cookie ni de traceur.
- Le conteneur tourne avec un utilisateur non administrateur ; seul `public/` est servi.
- Ne publiez pas de port pour l'application dans Dokploy (passez uniquement par **Domains** / Traefik), sinon l'adresse IP utilisée pour la limite d'envois peut être falsifiée.

## Lancer en local

```bash
npm install
cp .env.example .env          # puis adapter DATABASE_URL
node --env-file=.env server.js
```

puis ouvrir <http://localhost:3000>.

## Déploiement avec Dokploy (VPS)

### 1. Créer la base PostgreSQL

1. Dans votre projet Dokploy : **Create Service → Database → PostgreSQL**.
2. Renseigner un nom (ex. `maria-db`), **Database Name** `maria`, **Database User** `maria` et un mot de passe fort, puis **Create**.
3. **Deploy** la base, puis copier l'**Internal Connection URL** affichée dans l'onglet **General** (de la forme `postgresql://maria:…@maria-db-xxxx:5432/maria`).
4. Ne pas activer d'**External Port** : la base reste accessible uniquement depuis vos services Dokploy.

### 2. Créer l'application

1. **Create Service → Application**, source **GitHub** : dépôt `devtech5/Maria-groupe`, branche `main`.
2. **Build Type : Dockerfile** (chemin `Dockerfile`, contexte `.`), puis **Save**.
3. Onglet **Environment** :

   ```
   DATABASE_URL=postgresql://maria:VOTRE_MOT_DE_PASSE@maria-db-xxxx:5432/maria
   ```

4. Onglet **Domains** : ajouter `maria-groupe.com` et `www.maria-groupe.com`, **Container Port : 3000**, **HTTPS** avec **Let's Encrypt**.
5. Chez Hostinger, enregistrements DNS **A** pour `@` et `www` vers l'adresse IP du VPS.
6. **Deploy**, puis vérifier `https://maria-groupe.com/api/health` : la réponse doit être `{"ok":true,"db":"connectée"}`.

Activez **Auto Deploy** pour redéployer à chaque push sur `main`. Pensez aussi aux sauvegardes de la base (onglet **Backups** de la base PostgreSQL dans Dokploy).

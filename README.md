# Maria Group — site vitrine

Site internet de **Maria Group** et de ses filiales **Maria BTP** (bâtiment et travaux publics) et **Maria Gold** (exploration et exploitation aurifère).

Site statique (HTML / CSS / JavaScript, sans dépendance) : il peut être hébergé tel quel sur GitHub Pages, Netlify, un hébergement mutualisé, etc.

## Charte graphique

| Élément | Valeur |
|---|---|
| Couleur primaire | `#162E49` (bleu marine) |
| Couleur secondaire | `#BFA169` (or) |
| Titres | Montserrat (Google Fonts) |
| Texte | Open Sans (Google Fonts) |

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
assets/
  css/style.css      Styles du site
  js/main.js         Menu mobile, animations, filtres, formulaire
  img/               Logos (versions bleue, blanche, emblème) et favicons
  img/photos/        Photos optionnelles (voir ci-dessous)
tools/
  build.py           Générateur des pages HTML
  icons.py           Icônes et illustrations SVG
```

## Modifier le site

Les pages HTML sont générées par `tools/build.py` (en-tête, pied de page et coordonnées partagés).
Pour modifier un texte, les coordonnées ou le menu :

1. Éditer `tools/build.py` (les coordonnées sont regroupées en haut du fichier : téléphone, e-mail, adresse, horaires, réseaux sociaux).
2. Régénérer les pages :

   ```bash
   python3 tools/build.py
   ```

Python 3 suffit, aucune bibliothèque n'est nécessaire.

## À compléter avant la mise en ligne

- **Coordonnées** : e-mail, mobile et fixe sont renseignés. Restent à compléter : adresse, horaires, liens réseaux sociaux (en haut de `tools/build.py`).
- **Projets et réalisations** : les cartes actuelles sont des exemples génériques. Les remplacer par vos projets réels (listes `PROJETS` et `REALISATIONS` dans `tools/build.py`).
- **Mentions légales** : forme juridique, RCCM, hébergeur, directeur de publication.
- **Formulaire de contact** : par défaut, il ouvre le logiciel de messagerie du visiteur. Pour recevoir les messages directement, créer un formulaire sur un service comme [Formspree](https://formspree.io) puis renseigner son URL dans l'attribut `data-endpoint` du formulaire (`tools/build.py`, section CONTACT).

## Ajouter des photos

Le site fonctionne sans photo (illustrations dorées sur fond bleu). Pour ajouter vos propres photos, déposez-les dans `assets/img/photos/` avec les noms suivants, puis relancez `python3 tools/build.py` :

| Fichier | Emplacement |
|---|---|
| `hero.jpg` | Grande bannière de l'accueil |
| `btp.jpg`, `gold.jpg` | Cartes des filiales et visuels des pages Maria BTP / Maria Gold |
| `projet-1.jpg` … `projet-6.jpg` | Cartes de la page Projets (ordre de la liste `PROJETS`) |
| `realisation-1.jpg` … `realisation-6.jpg` | Cartes de la page Réalisations (ordre de la liste `REALISATIONS`) |

Un filtre bleu est appliqué automatiquement pour garder la cohérence avec la charte. Format conseillé : JPG, 1600 px de large maximum, moins de 400 Ko.

## Aperçu en local

```bash
python3 -m http.server 8000
```

puis ouvrir <http://localhost:8000>.

## Mise en ligne avec GitHub Pages

Dans le dépôt GitHub : **Settings → Pages → Source : Deploy from a branch**, choisir la branche et le dossier `/ (root)`.

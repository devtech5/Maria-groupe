"""Générateur des pages du site Maria Group.

Usage : python3 tools/build.py
Les pages HTML sont écrites dans public/.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from icons import I, ILLUS, PATTERN

# Dossier de sortie : public/ (par défaut)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")

# ---- Coordonnées ----
MOBILE = "+225 07 00 00 00 00"
MOBILE_HREF = "+2250700000000"
FIXE = "+225 27 00 00 00 00"
FIXE_HREF = "+2252700000000"
EMAIL = "hello@maria-groupe.com"
ADDRESS = "Côte d'Ivoire — adresse à compléter"
HOURS = "Lun – Ven : 8h00 – 18h00"
WHATSAPP = "https://wa.me/2250700000000"
FACEBOOK = "#"
LINKEDIN = "#"
INSTAGRAM = "#"


def bg(var, name):
    """Attribut style pour une photo optionnelle (ajoutée seulement si le fichier existe)."""
    rel = f"assets/img/photos/{name}"
    if os.path.exists(os.path.join(OUT, rel)):
        return f' style="--{var}: url(\'{rel}\')"'
    return ""


# ---- Menu ----
# Une entrée est (lien, libellé) ou (libellé, [sous-entrées]).
NAV = [
    ("index.html", "Accueil"),
    ("Maria Group", [
        ("groupe.html", "Qui sommes-nous"),
        ("btp.html", "Maria BTP"),
        ("gold.html", "Maria Gold"),
    ]),
    ("projets.html", "Projets"),
    ("realisations.html", "Réalisations"),
]
CONTACT_LABEL = "Contacts"


def _cur(href, active):
    return ' aria-current="page"' if href == active else ""


def header(active):
    lines = []
    for n, (a, b) in enumerate(NAV):
        if isinstance(b, list):
            sub_id = f"sub-{n}"
            is_active = any(h == active for h, _ in b)
            subs = "\n".join(f'              <li><a href="{h}"{_cur(h, active)}>{t}</a></li>' for h, t in b)
            lines.append(f'''          <li class="has-sub{" is-active" if is_active else ""}">
            <button class="sub-toggle" type="button" aria-expanded="false" aria-controls="{sub_id}">{a}{I["chevron"]}</button>
            <ul class="sub-menu" id="{sub_id}">
{subs}
            </ul>
          </li>''')
        else:
            lines.append(f'          <li><a href="{a}"{_cur(a, active)}>{b}</a></li>')
    items = "\n".join(lines)
    return f'''  <a class="skip-link" href="#contenu">Aller au contenu</a>

  <div class="topbar">
    <div class="container">
      <div class="topbar-info">
        <a href="tel:{MOBILE_HREF}">{I["phone"]}{MOBILE}</a>
        <a class="hide-sm" href="tel:{FIXE_HREF}">{I["phone"]}{FIXE}</a>
        <a href="mailto:{EMAIL}">{I["mail"]}{EMAIL}</a>
        <span class="hide-md">{I["clock"]}{HOURS}</span>
      </div>
      <div class="topbar-social">
        <a href="{FACEBOOK}" aria-label="Facebook">{I["facebook"]}</a>
        <a href="{LINKEDIN}" aria-label="LinkedIn">{I["linkedin"]}</a>
        <a href="{INSTAGRAM}" aria-label="Instagram">{I["instagram"]}</a>
        <a href="{WHATSAPP}" aria-label="WhatsApp">{I["whatsapp"]}</a>
      </div>
    </div>
  </div>

  <header class="site-header">
    <div class="container">
      <a class="brand" href="index.html" aria-label="Maria Group — accueil">
        <img src="assets/img/logo-mark.png" alt="" width="52" height="53">
        <span class="brand-text"><span class="brand-name">MARIA</span><span class="brand-sub">GROUP</span></span>
      </a>
      <nav class="main-nav" id="main-nav" aria-label="Navigation principale">
        <ul>
{items}
          <li class="nav-cta"><a class="btn btn-primary" href="contact.html"{_cur("contact.html", active)}>{CONTACT_LABEL}</a></li>
        </ul>
      </nav>
      <button class="nav-toggle" type="button" aria-controls="main-nav" aria-expanded="false" aria-label="Ouvrir le menu"><span></span></button>
    </div>
  </header>
'''


FOOTER = f'''
  <footer class="site-footer">
    <div class="container footer-main">
      <div class="footer-brand">
        <img src="assets/img/logo-white.png" alt="Maria Group" width="150" height="159">
        <p>Groupe engagé dans le bâtiment, les travaux publics et l'exploitation aurifère. Nous bâtissons et valorisons les ressources avec rigueur, sécurité et responsabilité.</p>
        <div class="footer-social">
          <a href="{FACEBOOK}" aria-label="Facebook">{I["facebook"]}</a>
          <a href="{LINKEDIN}" aria-label="LinkedIn">{I["linkedin"]}</a>
          <a href="{INSTAGRAM}" aria-label="Instagram">{I["instagram"]}</a>
          <a href="{WHATSAPP}" aria-label="WhatsApp">{I["whatsapp"]}</a>
        </div>
      </div>
      <div>
        <h4>Maria Group</h4>
        <ul class="footer-links">
          <li><a href="groupe.html">Qui sommes-nous</a></li>
          <li><a href="btp.html">Maria BTP</a></li>
          <li><a href="gold.html">Maria Gold</a></li>
          <li><a href="groupe.html#hse">Engagement QHSE</a></li>
        </ul>
      </div>
      <div>
        <h4>Navigation</h4>
        <ul class="footer-links">
          <li><a href="index.html">Accueil</a></li>
          <li><a href="projets.html">Projets</a></li>
          <li><a href="realisations.html">Réalisations</a></li>
          <li><a href="contact.html">Contacts</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacts</h4>
        <ul class="footer-contact">
          <li>{I["pin"]}<span>{ADDRESS}</span></li>
          <li>{I["phone"]}<span>Mobile : <a href="tel:{MOBILE_HREF}">{MOBILE}</a></span></li>
          <li>{I["phone"]}<span>Fixe : <a href="tel:{FIXE_HREF}">{FIXE}</a></span></li>
          <li>{I["mail"]}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{I["clock"]}<span>{HOURS}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <span>&copy; <span id="year">2026</span> Maria Group. Tous droits réservés.</span>
        <a href="mentions-legales.html">Mentions légales</a>
      </div>
    </div>
  </footer>

  <button class="to-top" type="button" aria-label="Retour en haut">{I["up"]}</button>
  <script src="assets/js/main.js" defer></script>
'''


def page(filename, title, desc, content, active=None):
    full_title = f"{title} | Maria Group" if filename != "index.html" else "Maria Group — BTP & Mines d'or"
    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#162E49">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Maria Group">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="assets/img/logo.png">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
  <link rel="icon" type="image/png" sizes="512x512" href="assets/img/favicon-512.png">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&amp;family=Open+Sans:wght@400;600&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{header(filename if active is None else active)}
  <main id="contenu">
{content}
  </main>
{FOOTER}</body>
</html>
'''
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit", filename)


def page_hero(eyebrow, title, lead, crumbs):
    """crumbs : liste de libellés ou de (lien, libellé) ; le dernier est la page courante."""
    if isinstance(crumbs, str):
        crumbs = [crumbs]
    items = ['<li><a href="index.html">Accueil</a></li>']
    for c in crumbs[:-1]:
        items.append(f'<li><a href="{c[0]}">{c[1]}</a></li>' if isinstance(c, tuple) else f"<li>{c}</li>")
    items.append(f'<li aria-current="page">{crumbs[-1]}</li>')
    crumb_html = "\n            ".join(items)
    return f'''    <section class="hero page-hero">
      {PATTERN}
      <img class="hero-mark" src="assets/img/logo-mark-white.png" alt="">
      <div class="container">
        <div class="hero-content">
          <ol class="breadcrumb">
            {crumb_html}
          </ol>
          <span class="eyebrow">{eyebrow}</span>
          <h1>{title}</h1>
          <p class="hero-lead">{lead}</p>
        </div>
      </div>
    </section>
'''


def cta(title="Un projet ? Parlons-en.", text="Nos équipes étudient votre besoin et vous proposent une solution adaptée, chiffrée et planifiée."):
    return f'''    <section class="cta-band">
      <div class="container">
        <div class="reveal">
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <a class="btn btn-primary reveal reveal-delay-1" href="contact.html">Nous contacter {I["arrow"]}</a>
      </div>
    </section>
'''


def feature(icon, title, text, gold=False, delay=0):
    d = f" reveal-delay-{delay}" if delay else ""
    return f'''          <article class="feature reveal{d}">
            <div class="icon-box{" gold" if gold else ""}">{I[icon]}</div>
            <h3>{title}</h3>
            <p>{text}</p>
          </article>'''


def service(icon, title, text, bullets, delay=0):
    d = f" reveal-delay-{delay}" if delay else ""
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f'''          <article class="service reveal{d}">
            <div class="icon-box">{I[icon]}</div>
            <h3>{title}</h3>
            <p>{text}</p>
            <ul>{lis}</ul>
          </article>'''


def steps(items):
    out = []
    for n, (t, p) in enumerate(items, 1):
        d = f" reveal-delay-{n - 1}" if n > 1 else ""
        out.append(f'''          <div class="step reveal{d}">
            <div class="step-num">0{n}</div>
            <h3>{t}</h3>
            <p>{p}</p>
          </div>''')
    return "\n".join(out)


def checklist(items):
    return "\n".join(f'            <li>{I["check"]}<span><strong>{t}</strong> — {p}</span></li>' for t, p in items)


def section_head_row(eyebrow, title, btn_href, btn_label, text=""):
    p = f"\n            <p>{text}</p>" if text else ""
    return f'''        <div class="section-head section-head-row reveal">
          <div>
            <span class="eyebrow">{eyebrow}</span>
            <h2>{title}</h2>{p}
          </div>
          <a class="btn btn-outline-dark" href="{btn_href}">{btn_label} {I["arrow"]}</a>
        </div>'''


# ---- Filiales ----
POLES = [
    ("btp", "btp.html", "01", "Maria BTP", "Bâtiment & Travaux Publics",
     "Construction de bâtiments, génie civil, routes et aménagements : nous réalisons vos ouvrages de la conception à la livraison, dans le respect des délais et des normes.",
     ["Bâtiment", "Génie civil", "Routes & VRD"]),
    ("gold", "gold.html", "02", "Maria Gold", "Exploration & exploitation aurifère",
     "Exploration, extraction et traitement du minerai d'or : une expertise minière responsable, sûre et performante au service de la valorisation des ressources aurifères.",
     ["Exploration", "Exploitation", "Traitement"]),
]
CAT_LABEL = {"btp": "Maria BTP", "gold": "Maria Gold"}


def pole_cards():
    out = []
    for i, (key, href, num, name, sub, text, tags) in enumerate(POLES):
        d = f" reveal-delay-{i}" if i else ""
        t = "".join(f"<li>{x}</li>" for x in tags)
        out.append(f'''          <article class="pole-card reveal{d}">
            <a class="pole-visual" href="{href}" aria-label="{name}"{bg("card-img", key + ".jpg")}>
              <span class="pole-num">FILIALE {num}</span>
              {ILLUS[key]}
            </a>
            <div class="pole-body">
              <span class="eyebrow">{sub}</span>
              <h3>{name}</h3>
              <p>{text}</p>
              <ul class="pole-tags">{t}</ul>
              <a class="link-arrow" href="{href}">Découvrir {name} {I["arrow"]}</a>
            </div>
          </article>''')
    return "\n".join(out)


# ---- Réalisations (projets terminés) — à remplacer par vos réalisations réelles ----
# (filiale, type, titre, description)
REALISATIONS = [
    ("btp", "Bâtiment", "Immeuble de bureaux R+5", "Gros œuvre, second œuvre et corps d'état techniques."),
    ("btp", "Travaux publics", "Aménagement de voirie urbaine", "Terrassement, chaussée, assainissement et éclairage."),
    ("btp", "Génie civil", "Ouvrage d'art — pont routier", "Fondations profondes, piles et tablier en béton armé."),
    ("gold", "Exploration", "Campagne de sondages géologiques", "Forages, échantillonnage et analyse des teneurs en or."),
    ("gold", "Exploitation", "Travaux de découverture minière", "Décapage, terrassement de masse et pistes d'accès."),
    ("gold", "Infrastructures", "Plateformes et pistes minières", "Aménagement des zones d'exploitation et de stockage."),
]

# ---- Projets (en cours / en préparation) — à remplacer par vos projets réels ----
# (filiale, statut, titre, description)
PROJETS = [
    ("btp", "En cours", "Ensemble résidentiel", "Construction de logements avec voiries et réseaux divers."),
    ("btp", "En cours", "Réhabilitation de routes", "Reprise de chaussée, drainage et signalisation."),
    ("btp", "En préparation", "Bâtiment administratif", "Études d'exécution et préparation du chantier."),
    ("gold", "En cours", "Programme d'exploration aurifère", "Cartographie géologique et campagnes de sondages."),
    ("gold", "En préparation", "Unité de traitement du minerai", "Études de dimensionnement et choix des procédés."),
    ("gold", "En cours", "Réhabilitation environnementale", "Remise en état et revégétalisation de zones exploitées."),
]


def project_cards(items, prefix, filterable=False, status=False):
    out = []
    for n, (cat, kind, title, text) in enumerate(items, 1):
        data = f' data-category="{cat}"' if filterable else ""
        badge = f'<span class="project-status">{kind}</span>' if status else ""
        kind_html = CAT_LABEL[cat] if status else kind
        out.append(f'''          <article class="project reveal"{data}>
            <div class="project-visual"{bg("card-img", f"{prefix}-{n}.jpg")}>
              {ILLUS[cat]}
              <span class="project-cat">{CAT_LABEL[cat]}</span>{badge}
            </div>
            <div class="project-body">
              <span class="project-kind">{kind_html}</span>
              <h3>{title}</h3>
              <p>{text}</p>
            </div>
          </article>''')
    return "\n".join(out)


def filter_bar(label):
    return f'''        <div class="filter-bar reveal" data-filter-bar role="group" aria-label="{label}">
          <button type="button" class="is-active" data-filter="all" aria-pressed="true">Tous</button>
          <button type="button" data-filter="btp" aria-pressed="false">Maria BTP</button>
          <button type="button" data-filter="gold" aria-pressed="false">Maria Gold</button>
        </div>'''


ABOUT_FRAME = f'''          <div class="frame">
            {PATTERN.replace('class="hero-pattern"', 'class="pattern"')}
            <img src="assets/img/logo-mark-white.png" alt="Emblème Maria Group" width="297" height="302" loading="lazy">
          </div>
          <div class="frame-border"></div>'''


# =========================================================================
# ACCUEIL
# =========================================================================
home = f'''    <section class="hero hero-home"{bg("hero-img", "hero.jpg")}>
      {PATTERN}
      <img class="hero-mark" src="assets/img/logo-mark-white.png" alt="">
      <div class="container">
        <div class="hero-content">
          <span class="eyebrow">BTP · Mines d'or</span>
          <h1>Bâtir et valoriser les ressources : <em>l'excellence</em> au service de vos projets.</h1>
          <p class="hero-lead">Maria Group réunit deux filiales complémentaires, Maria BTP et Maria Gold, pour accompagner les acteurs publics et privés, de la première pierre au premier gramme d'or.</p>
          <div class="hero-actions">
            <a class="btn btn-gold" href="#filiales">Découvrir nos filiales {I["arrow"]}</a>
            <a class="btn btn-outline" href="contact.html">Nous contacter</a>
          </div>
        </div>
      </div>
    </section>

    <div class="hero-poles">
      <div class="container">
        <div class="grid">
          <a class="hero-pole" href="btp.html">
            <div class="icon-box">{I["crane"]}</div>
            <div><h3>Maria BTP</h3><p>Bâtiments, génie civil, routes et aménagements.</p></div>
          </a>
          <a class="hero-pole" href="gold.html">
            <div class="icon-box">{I["ingot"]}</div>
            <div><h3>Maria Gold</h3><p>Exploration, exploitation et traitement de l'or.</p></div>
          </a>
          <a class="hero-pole" href="projets.html">
            <div class="icon-box">{I["clipboard"]}</div>
            <div><h3>Nos projets</h3><p>Les chantiers et programmes que nous menons.</p></div>
          </a>
        </div>
      </div>
    </div>

    <section class="section" id="a-propos">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Qui sommes-nous</span>
          <h2>Un groupe intégré, une seule exigence : la qualité.</h2>
          <p class="lead">Maria Group fédère les savoir-faire du bâtiment, des travaux publics et de l'exploitation minière aurifère.</p>
          <p class="muted">Cette complémentarité nous permet de maîtriser chaque étape de nos projets : infrastructures, terrassements, exploitation et logistique. Résultat : des délais tenus, des coûts optimisés et un interlocuteur unique pour nos clients et partenaires.</p>
          <ul class="check-list">
{checklist([
    ("Interlocuteur unique", "un pilotage centralisé de vos projets."),
    ("Moyens propres", "engins, véhicules et équipes qualifiées."),
    ("Sécurité avant tout", "une culture QHSE appliquée sur chaque site."),
])}
          </ul>
          <a class="btn btn-primary" href="groupe.html">Qui sommes-nous {I["arrow"]}</a>
        </div>
        <div class="about-visual reveal reveal-delay-1">
{ABOUT_FRAME}
          <div class="about-badge"><strong>2</strong><span>filiales d'expertise complémentaires</span></div>
        </div>
      </div>
    </section>

    <section class="section section-soft" id="filiales">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow center">Nos filiales</span>
          <h2>Deux métiers, une vision commune</h2>
          <p>Chaque filiale dispose de ses équipes, de ses équipements et de son savoir-faire, tout en bénéficiant de la force et des synergies du groupe.</p>
        </div>
        <div class="poles-grid cols-2">
{pole_cards()}
        </div>
      </div>
    </section>

    <section class="section section-dark">
      {PATTERN}
      <div class="container">
        <div class="stats">
          <div class="stat reveal"><div class="stat-value" data-count="2">2</div><div class="stat-label">Filiales spécialisées</div></div>
          <div class="stat reveal reveal-delay-1"><div class="stat-value" data-count="360" data-suffix="°">360°</div><div class="stat-label">Solutions intégrées</div></div>
          <div class="stat reveal reveal-delay-2"><div class="stat-value" data-count="24" data-suffix="/7">24/7</div><div class="stat-label">Suivi des opérations</div></div>
          <div class="stat reveal reveal-delay-3"><div class="stat-value" data-count="100" data-suffix="%">100%</div><div class="stat-label">Engagement sécurité</div></div>
        </div>
      </div>
    </section>

    <section class="section" id="valeurs">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow center">Pourquoi nous choisir</span>
          <h2>Des valeurs qui guident chacun de nos chantiers</h2>
        </div>
        <div class="features">
{feature("shield", "Sécurité", "La protection de nos équipes, de nos partenaires et des riverains est notre priorité absolue.")}
{feature("award", "Qualité", "Des ouvrages et des prestations conformes aux normes et aux exigences de nos clients.", delay=1)}
{feature("handshake", "Intégrité", "Transparence, respect des engagements et relations de confiance durables.", delay=2)}
{feature("leaf", "Responsabilité", "Une approche soucieuse de l'environnement et du développement des communautés locales.", delay=3)}
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow center">Notre méthode</span>
          <h2>De l'idée à la livraison</h2>
          <p>Une démarche structurée pour sécuriser chaque étape de votre projet.</p>
        </div>
        <div class="process">
{steps([
    ("Écoute & étude", "Analyse de votre besoin, visite de site et étude de faisabilité."),
    ("Proposition", "Offre technique et financière détaillée, planning prévisionnel."),
    ("Exécution", "Mobilisation des équipes et des moyens, suivi qualité et sécurité."),
    ("Livraison", "Réception des travaux, documentation et suivi après livraison."),
])}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
{section_head_row("Projets", "Nos projets en cours", "projets.html", "Tous nos projets", "Les chantiers et programmes actuellement menés par nos filiales.")}
        <div class="projects">
{project_cards([PROJETS[0], PROJETS[3], PROJETS[1]], "projet", status=True)}
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
{section_head_row("Réalisations", "Nos dernières réalisations", "realisations.html", "Toutes nos réalisations", "Un aperçu des ouvrages et travaux livrés par nos équipes.")}
        <div class="projects">
{project_cards([REALISATIONS[0], REALISATIONS[3], REALISATIONS[2]], "realisation")}
        </div>
      </div>
    </section>

{cta()}'''

page("index.html", "Accueil",
     "Maria Group réunit Maria BTP (bâtiment et travaux publics) et Maria Gold (exploration et exploitation aurifère). Bâtir et valoriser les ressources avec excellence.",
     home)

# =========================================================================
# QUI SOMMES-NOUS
# =========================================================================
groupe = page_hero("Maria Group", "Qui sommes-nous",
                   "Maria Group rassemble deux filiales complémentaires pour offrir à ses clients et partenaires des solutions complètes, fiables et durables.",
                   ["Maria Group", "Qui sommes-nous"]) + f'''
    <section class="section">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Notre histoire</span>
          <h2>Construire l'avenir, ensemble</h2>
          <p class="lead">Né de la volonté de proposer une offre intégrée et de qualité, Maria Group s'est structuré autour de deux filiales : Maria BTP et Maria Gold.</p>
          <p class="muted">Cette organisation nous permet d'intervenir sur des projets d'envergure en mutualisant nos ressources humaines et matérielles. Nos équipes partagent une même culture de l'exigence, de la sécurité et du service client.</p>
          <p class="muted">Le groupe accompagne aussi bien les institutions publiques que les entreprises privées et les acteurs du secteur minier, avec une ambition claire : contribuer durablement au développement des territoires.</p>
        </div>
        <div class="about-visual reveal reveal-delay-1">
{ABOUT_FRAME}
          <div class="about-badge"><strong>1</strong><span>groupe, un interlocuteur unique</span></div>
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="mv-grid">
          <article class="mv-card reveal">
            <div class="icon-box">{I["target"]}</div>
            <h3>Notre mission</h3>
            <p>Concevoir et réaliser des infrastructures durables et valoriser les ressources aurifères avec un haut niveau de qualité et de sécurité.</p>
          </article>
          <article class="mv-card reveal reveal-delay-1">
            <div class="icon-box">{I["eye"]}</div>
            <h3>Notre vision</h3>
            <p>Devenir un groupe de référence, reconnu pour la fiabilité de ses réalisations et sa contribution au développement économique et social.</p>
          </article>
          <article class="mv-card reveal reveal-delay-2">
            <div class="icon-box">{I["users"]}</div>
            <h3>Notre ambition</h3>
            <p>Faire grandir nos talents, investir dans des équipements modernes et nouer des partenariats durables avec nos clients et fournisseurs.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="filiales">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow center">Nos filiales</span>
          <h2>Deux expertises complémentaires</h2>
        </div>
        <div class="poles-grid cols-2">
{pole_cards()}
        </div>
      </div>
    </section>

    <section class="section section-soft" id="valeurs">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow center">Nos valeurs</span>
          <h2>Ce qui nous engage au quotidien</h2>
        </div>
        <div class="features">
{feature("shield", "Sécurité", "Zéro compromis : formation, équipements de protection et procédures strictes sur tous nos sites.")}
{feature("award", "Excellence", "Le souci du travail bien fait, du choix des matériaux jusqu'aux finitions.", delay=1)}
{feature("handshake", "Intégrité", "Une gestion transparente et éthique, dans le respect de nos engagements.", delay=2)}
{feature("bulb", "Innovation", "Des méthodes et des équipements modernes pour gagner en efficacité.", delay=3)}
        </div>
      </div>
    </section>

    <section class="section section-dark" id="hse">
      {PATTERN}
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Engagement QHSE</span>
          <h2>Qualité, Hygiène, Sécurité &amp; Environnement</h2>
          <p>La performance de Maria Group repose sur une démarche QHSE exigeante, appliquée à l'ensemble de nos filiales et de nos sites d'intervention.</p>
          <ul class="check-list">
{checklist([
    ("Prévention", "analyse des risques, plans de prévention et causeries sécurité."),
    ("Formation", "habilitations, conduite d'engins et gestes de premiers secours."),
    ("Environnement", "gestion des déchets et de l'eau, réhabilitation des sites."),
    ("Qualité", "contrôles à chaque étape et traçabilité des matériaux."),
])}
          </ul>
        </div>
        <div class="features cols-2 reveal reveal-delay-1">
{feature("shield", "Sécurité", "Port des EPI et procédures contrôlées.")}
{feature("leaf", "Environnement", "Réduction de notre empreinte.")}
{feature("clipboard", "Qualité", "Contrôles et suivi documenté.")}
{feature("users", "Communautés", "Emploi et sous-traitance locale.")}
        </div>
      </div>
    </section>

{cta("Rejoignez nos partenaires", "Clients, fournisseurs, sous-traitants ou candidats : construisons ensemble les projets de demain.")}'''

page("groupe.html", "Qui sommes-nous",
     "Découvrez Maria Group : histoire, mission, vision, filiales (Maria BTP, Maria Gold), valeurs et engagement QHSE.",
     groupe)


# =========================================================================
# PAGES FILIALES
# =========================================================================
def pole_page(fn, key, name, eyebrow, title, lead, intro_h, intro_p, intro_p2, checks, services_html,
              equip_title, equip, steps_items, cta_t, cta_p, desc):
    content = page_hero(eyebrow, title, lead, [("groupe.html", "Maria Group"), name]) + f'''
    <section class="section">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">{name}</span>
          <h2>{intro_h}</h2>
          <p class="lead">{intro_p}</p>
          <p class="muted">{intro_p2}</p>
          <ul class="check-list">
{checklist(checks)}
          </ul>
          <a class="btn btn-primary" href="contact.html">Demander un devis {I["arrow"]}</a>
        </div>
        <div class="about-visual reveal reveal-delay-1">
          <div class="frame illus-frame"{bg("card-img", key + ".jpg")}>
            {PATTERN.replace('class="hero-pattern"', 'class="pattern"')}
            {ILLUS[key]}
          </div>
          <div class="frame-border"></div>
          <div class="about-badge"><strong>{name.split()[-1]}</strong><span>Une filiale Maria Group</span></div>
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow center">Nos services</span>
          <h2>Ce que nous faisons pour vous</h2>
        </div>
        <div class="services">
{services_html}
        </div>
      </div>
    </section>

    <section class="section section-dark">
      {PATTERN}
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Nos moyens</span>
          <h2>{equip_title}</h2>
          <p>Des équipements entretenus et des équipes qualifiées, mobilisables rapidement sur vos sites.</p>
        </div>
        <ul class="pill-grid reveal reveal-delay-1">
{"".join(f'          <li>{I["check"]}{e}</li>' + chr(10) for e in equip)}        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow center">Notre démarche</span>
          <h2>Un accompagnement de bout en bout</h2>
        </div>
        <div class="process">
{steps(steps_items)}
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
{section_head_row("Projets", f"Projets {name}", "projets.html", "Voir tous les projets")}
        <div class="projects">
{project_cards([p for p in PROJETS if p[0] == key], "projet", status=True)}
        </div>
      </div>
    </section>

{cta(cta_t, cta_p)}'''
    page(fn, name, desc, content)


pole_page(
    "btp.html", "btp", "Maria BTP", "Filiale 01 — Maria BTP",
    "Bâtiment &amp; Travaux Publics",
    "Nous concevons et réalisons des ouvrages solides et durables : bâtiments, infrastructures routières, génie civil et aménagements.",
    "Des ouvrages qui durent",
    "Maria BTP intervient en entreprise générale ou en lots séparés, pour des clients publics comme privés.",
    "Nos moyens propres — engins de terrassement, véhicules de transport et équipes qualifiées — nous permettent de garantir la continuité des chantiers et le respect des plannings, y compris pour les infrastructures des sites miniers de Maria Gold.",
    [("Entreprise générale", "un pilotage complet tous corps d'état."),
     ("Bureau d'études intégré", "plans, métrés et suivi technique."),
     ("Respect des délais", "planification rigoureuse et reporting régulier.")],
    "\n".join([
        service("building", "Construction de bâtiments", "Logements, bureaux, bâtiments industriels et équipements publics.", ["Gros œuvre", "Second œuvre", "Clé en main"]),
        service("road", "Routes &amp; VRD", "Création et réhabilitation de routes, voiries et réseaux divers.", ["Terrassement", "Chaussées & bitumage", "Assainissement"], 1),
        service("bridge", "Génie civil", "Ouvrages d'art et structures en béton armé.", ["Ponts & dalots", "Fondations", "Réservoirs"], 2),
        service("ruler", "Études &amp; ingénierie", "Accompagnement technique en amont et pendant les travaux.", ["Études de faisabilité", "Plans d'exécution", "Métrés & devis"]),
        service("hammer", "Rénovation &amp; réhabilitation", "Remise à neuf, extension et mise aux normes de bâtiments existants.", ["Réhabilitation", "Extensions", "Mise en conformité"], 1),
        service("truck", "Transport &amp; logistique de chantier", "Acheminement des matériaux et des engins sur vos chantiers.", ["Approvisionnement", "Porte-engins", "Location d'engins"], 2),
    ]),
    "Un parc matériel adapté à chaque chantier",
    ["Pelles hydrauliques", "Chargeuses &amp; bulldozers", "Niveleuses", "Compacteurs", "Bétonnières &amp; centrales", "Camions bennes &amp; porte-engins"],
    [("Étude", "Visite de site, relevés et étude technique du projet."),
     ("Chiffrage", "Devis détaillé, choix des matériaux et planning."),
     ("Travaux", "Exécution encadrée, contrôles qualité et sécurité."),
     ("Réception", "Levée des réserves, remise des ouvrages et garantie.")],
    "Votre projet de construction commence ici",
    "Bâtiment, route ou ouvrage d'art : confiez-nous votre projet et recevez une proposition détaillée.",
    "Maria BTP : construction de bâtiments, routes, VRD, génie civil, ouvrages d'art, réhabilitation et logistique de chantier.",
)

pole_page(
    "gold.html", "gold", "Maria Gold", "Filiale 02 — Maria Gold",
    "Exploration &amp; exploitation aurifère",
    "De la prospection à la production, Maria Gold valorise les ressources aurifères de manière sûre, performante et responsable.",
    "L'or, une ressource à valoriser avec responsabilité",
    "Maria Gold est la filiale minière de Maria Group, dédiée à l'exploration et à l'exploitation de gisements aurifères.",
    "Nous mobilisons géologues, ingénieurs et opérateurs expérimentés, appuyés par des équipements adaptés, avec une exigence constante : la sécurité des équipes, le respect de la réglementation minière et la préservation de l'environnement.",
    [("Cycle complet", "de la prospection à la réhabilitation des sites."),
     ("Conformité", "respect du code minier et des normes environnementales."),
     ("Ancrage local", "emploi et développement des communautés riveraines.")],
    "\n".join([
        service("globe", "Exploration &amp; prospection", "Identification et évaluation des gisements aurifères.", ["Géologie & cartographie", "Sondages & forages", "Analyses d'échantillons"]),
        service("pickaxe", "Exploitation minière", "Extraction à ciel ouvert, efficace et sécurisée.", ["Découverture", "Abattage", "Chargement & roulage"], 1),
        service("ingot", "Traitement du minerai", "Valorisation du minerai et récupération de l'or.", ["Concassage & broyage", "Récupération de l'or", "Contrôle des teneurs"], 2),
        service("excavator", "Infrastructures minières", "Aménagement des sites, en synergie avec Maria BTP.", ["Pistes & plateformes", "Bases-vie", "Terrassement de masse"]),
        service("shield", "Sécurité &amp; sûreté", "Protection des équipes, des installations et de la production.", ["Plans de prévention", "Sûreté des sites", "Formation des équipes"], 1),
        service("leaf", "Environnement &amp; communautés", "Une exploitation respectueuse des territoires.", ["Gestion de l'eau", "Réhabilitation", "Projets communautaires"], 2),
    ]),
    "Des équipements robustes pour les sites aurifères",
    ["Pelles hydrauliques", "Dumpers &amp; tombereaux", "Foreuses", "Concasseurs &amp; broyeurs", "Chargeuses", "Équipements de laboratoire"],
    [("Exploration", "Prospection, sondages et analyse des échantillons."),
     ("Évaluation", "Estimation des ressources et étude de faisabilité."),
     ("Exploitation", "Production encadrée et suivi QHSE permanent."),
     ("Réhabilitation", "Remise en état du site et suivi environnemental.")],
    "Un projet aurifère ? Parlons-en.",
    "Titulaire de permis, investisseur ou partenaire : échangeons sur vos projets d'exploration et d'exploitation.",
    "Maria Gold : exploration aurifère, exploitation minière, traitement du minerai d'or, infrastructures minières et réhabilitation des sites.",
)

# =========================================================================
# PROJETS
# =========================================================================
projets = page_hero("Projets", "Nos projets",
                    "Découvrez les chantiers et programmes actuellement menés ou préparés par Maria BTP et Maria Gold.",
                    "Projets") + f'''
    <section class="section">
      <div class="container">
{filter_bar("Filtrer les projets")}
        <div class="projects">
{project_cards(PROJETS, "projet", filterable=True, status=True)}
        </div>
      </div>
    </section>

{cta("Un projet à nous confier ?", "Présentez-nous votre besoin : nous revenons vers vous avec une proposition adaptée.")}'''

page("projets.html", "Projets",
     "Projets en cours et en préparation de Maria Group : bâtiment, travaux publics et exploitation aurifère.",
     projets)

# =========================================================================
# RÉALISATIONS
# =========================================================================
real = page_hero("Réalisations", "Nos réalisations",
                 "Bâtiment, travaux publics et mines d'or : découvrez les ouvrages et travaux livrés par nos équipes.",
                 "Réalisations") + f'''
    <section class="section">
      <div class="container">
{filter_bar("Filtrer les réalisations")}
        <div class="projects">
{project_cards(REALISATIONS, "realisation", filterable=True)}
        </div>
      </div>
    </section>

{cta("Votre projet sera notre prochaine réalisation", "Présentez-nous votre besoin : nous revenons vers vous avec une proposition adaptée.")}'''

page("realisations.html", "Réalisations",
     "Réalisations de Maria Group : bâtiment, travaux publics, génie civil, exploration et exploitation aurifère.",
     real)

# =========================================================================
# CONTACTS
# =========================================================================
contact = page_hero("Contacts", "Parlons de votre projet",
                    "Une question, une demande de devis ou un partenariat ? Notre équipe vous répond dans les meilleurs délais.",
                    "Contacts") + f'''
    <section class="section">
      <div class="container contact-grid">
        <aside class="contact-info reveal">
          <span class="eyebrow">Coordonnées</span>
          <h2>Maria Group</h2>
          <p>Nos équipes sont à votre écoute pour étudier vos projets de BTP et d'exploitation aurifère.</p>
          <ul class="contact-items">
            <li><div class="icon-box">{I["phone"]}</div><div><strong>Mobile</strong><a href="tel:{MOBILE_HREF}">{MOBILE}</a></div></li>
            <li><div class="icon-box">{I["phone"]}</div><div><strong>Fixe</strong><a href="tel:{FIXE_HREF}">{FIXE}</a></div></li>
            <li><div class="icon-box">{I["mail"]}</div><div><strong>E-mail</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
            <li><div class="icon-box">{I["pin"]}</div><div><strong>Adresse</strong>{ADDRESS}</div></li>
            <li><div class="icon-box">{I["clock"]}</div><div><strong>Horaires</strong>{HOURS}</div></li>
          </ul>
          <a class="btn btn-gold contact-wa" href="{WHATSAPP}">{I["whatsapp"]} Écrire sur WhatsApp</a>
        </aside>

        <div class="form-card reveal reveal-delay-1">
          <span class="eyebrow">Formulaire</span>
          <h2 style="font-size:1.6rem">Demande de devis ou d'information</h2>
          <p class="muted">Les champs marqués d'un <span style="color:var(--secondary-600)">*</span> sont obligatoires.</p>
          <!-- Les messages sont envoyés à l'API du serveur (server.js) et enregistrés dans PostgreSQL. -->
          <form id="contact-form" novalidate data-endpoint="/api/contact" data-mailto="{EMAIL}">
            <div class="form-grid">
              <div class="field">
                <label for="nom">Nom &amp; prénom <span class="req">*</span></label>
                <input id="nom" name="nom" type="text" autocomplete="name" required>
                <span class="error-msg">Veuillez indiquer votre nom.</span>
              </div>
              <div class="field">
                <label for="societe">Société</label>
                <input id="societe" name="societe" type="text" autocomplete="organization">
              </div>
              <div class="field">
                <label for="email">E-mail <span class="req">*</span></label>
                <input id="email" name="email" type="email" autocomplete="email" required>
                <span class="error-msg">Veuillez indiquer une adresse e-mail valide.</span>
              </div>
              <div class="field">
                <label for="telephone">Téléphone</label>
                <input id="telephone" name="telephone" type="tel" autocomplete="tel">
              </div>
              <div class="field full">
                <label for="pole">Filiale concernée <span class="req">*</span></label>
                <select id="pole" name="pole" required>
                  <option value="">— Sélectionnez —</option>
                  <option>Maria BTP</option>
                  <option>Maria Gold</option>
                  <option>Maria Group (général)</option>
                </select>
                <span class="error-msg">Veuillez sélectionner une filiale.</span>
              </div>
              <div class="field full">
                <label for="message">Votre message <span class="req">*</span></label>
                <textarea id="message" name="message" required></textarea>
                <span class="error-msg">Veuillez décrire votre demande.</span>
              </div>
              <div class="field full">
                <label class="form-consent" for="consent">
                  <input id="consent" name="consent" type="checkbox" required>
                  <span>J'accepte que mes données soient utilisées pour traiter ma demande. <span class="req">*</span></span>
                </label>
                <span class="error-msg">Votre accord est nécessaire.</span>
              </div>
              <div class="hp-field" aria-hidden="true"><label for="website">Site web</label><input id="website" name="website" type="text" tabindex="-1" autocomplete="off"></div>
              <div class="full">
                <button class="btn btn-primary" type="submit">Envoyer ma demande {I["arrow"]}</button>
              </div>
            </div>
            <div class="form-status" role="status" aria-live="polite"></div>
          </form>
        </div>
      </div>
    </section>
'''

page("contact.html", "Contacts",
     "Contactez Maria Group pour vos projets de BTP et d'exploitation aurifère : demande de devis, information ou partenariat.",
     contact)

# =========================================================================
# MENTIONS LÉGALES
# =========================================================================
legal = page_hero("Informations", "Mentions légales", "Informations légales relatives au site de Maria Group.", "Mentions légales") + f'''
    <section class="section">
      <div class="container prose">
        <h2>Éditeur du site</h2>
        <p>Maria Group<br>{ADDRESS}<br>Mobile : {MOBILE} — Fixe : {FIXE}<br>E-mail : <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>Forme juridique, capital social, numéro d'immatriculation (RCCM) et compte contribuable : à compléter.<br>Directeur de la publication : à compléter.</p>

        <h2>Hébergement</h2>
        <p>Nom, adresse et coordonnées de l'hébergeur du site : à compléter.</p>

        <h2>Propriété intellectuelle</h2>
        <p>L'ensemble des contenus de ce site (textes, logos, images, éléments graphiques) est la propriété exclusive de Maria Group, sauf mention contraire. Toute reproduction, totale ou partielle, sans autorisation préalable écrite est interdite.</p>

        <h2>Données personnelles</h2>
        <p>Les informations transmises via le formulaire de contact sont utilisées uniquement pour répondre à votre demande et ne sont jamais cédées à des tiers. Vous disposez d'un droit d'accès, de rectification et de suppression de vos données en écrivant à <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2>Cookies</h2>
        <p>Ce site n'utilise pas de cookies de suivi publicitaire. Seules des ressources techniques nécessaires à son fonctionnement (polices de caractères) peuvent être chargées.</p>
      </div>
    </section>
'''
page("mentions-legales.html", "Mentions légales", "Mentions légales du site Maria Group.", legal, active="")

# =========================================================================
# 404
# =========================================================================
nf = f'''    <section class="hero page-hero">
      {PATTERN}
      <img class="hero-mark" src="assets/img/logo-mark-white.png" alt="">
      <div class="container">
        <div class="hero-content">
          <span class="eyebrow">Erreur 404</span>
          <h1>Page introuvable</h1>
          <p class="hero-lead">La page que vous recherchez n'existe pas ou a été déplacée.</p>
          <div class="hero-actions">
            <a class="btn btn-gold" href="index.html">Retour à l'accueil {I["arrow"]}</a>
            <a class="btn btn-outline" href="contact.html">Nous contacter</a>
          </div>
        </div>
      </div>
    </section>
'''
page("404.html", "Page introuvable", "Page introuvable.", nf, active="")

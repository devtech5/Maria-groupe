import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from icons import I, ILLUS, PATTERN

# Dossier de sortie : racine du dépôt (par défaut)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- Coordonnées (à personnaliser) ----
PHONE = "+000 00 00 00 00"
PHONE_HREF = "+0000000000"
EMAIL = "contact@mariagroup.com"
ADDRESS = "Siège social — adresse à compléter"
HOURS = "Lun – Ven : 8h00 – 18h00"
WHATSAPP = "https://wa.me/0000000000"
FACEBOOK = "#"
LINKEDIN = "#"
INSTAGRAM = "#"

def bg(var, name):
    """Attribut style pour une photo optionnelle (ajoutée seulement si le fichier existe)."""
    rel = f"assets/img/photos/{name}"
    if os.path.exists(os.path.join(OUT, rel)):
        return f' style="--{var}: url(\'{rel}\')"'
    return ""


NAV = [
    ("index.html", "Accueil"),
    ("groupe.html", "Le Groupe"),
    ("btp.html", "BTP"),
    ("mines.html", "Mines"),
    ("transport.html", "Transport"),
    ("realisations.html", "Réalisations"),
]


def header(active):
    items = "\n".join(
        f'          <li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>'
        for h, t in NAV)
    return f'''  <a class="skip-link" href="#contenu">Aller au contenu</a>

  <div class="topbar">
    <div class="container">
      <div class="topbar-info">
        <a href="tel:{PHONE_HREF}">{I["phone"]}{PHONE}</a>
        <a href="mailto:{EMAIL}">{I["mail"]}{EMAIL}</a>
        <span class="hide-sm">{I["clock"]}{HOURS}</span>
      </div>
      <div class="topbar-social">
        <a href="{FACEBOOK}" aria-label="Facebook">{I["facebook"]}</a>
        <a href="{LINKEDIN}" aria-label="LinkedIn">{I["linkedin"]}</a>
        <a href="{INSTAGRAM}" aria-label="Instagram">{I["instagram"]}</a>
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
          <li class="nav-cta"><a class="btn btn-primary" href="contact.html"{" aria-current=\"page\"" if active == "contact.html" else ""}>Nous contacter</a></li>
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
        <img src="assets/img/logo-white.png" alt="Maria Group" width="150" height="159" loading="lazy">
        <p>Groupe multisectoriel engagé dans le BTP, l'exploitation minière et le transport. Nous bâtissons, extrayons et acheminons avec rigueur, sécurité et responsabilité.</p>
        <div class="footer-social">
          <a href="{FACEBOOK}" aria-label="Facebook">{I["facebook"]}</a>
          <a href="{LINKEDIN}" aria-label="LinkedIn">{I["linkedin"]}</a>
          <a href="{INSTAGRAM}" aria-label="Instagram">{I["instagram"]}</a>
          <a href="{WHATSAPP}" aria-label="WhatsApp">{I["whatsapp"]}</a>
        </div>
      </div>
      <div>
        <h4>Nos pôles</h4>
        <ul class="footer-links">
          <li><a href="btp.html">Maria BTP</a></li>
          <li><a href="mines.html">Maria Mines</a></li>
          <li><a href="transport.html">Maria Transport</a></li>
          <li><a href="realisations.html">Nos réalisations</a></li>
        </ul>
      </div>
      <div>
        <h4>Le groupe</h4>
        <ul class="footer-links">
          <li><a href="groupe.html">Qui sommes-nous</a></li>
          <li><a href="groupe.html#valeurs">Nos valeurs</a></li>
          <li><a href="groupe.html#hse">Engagement QHSE</a></li>
          <li><a href="contact.html">Contact &amp; devis</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul class="footer-contact">
          <li>{I["pin"]}<span>{ADDRESS}</span></li>
          <li>{I["phone"]}<a href="tel:{PHONE_HREF}">{PHONE}</a></li>
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
    full_title = f"{title} | Maria Group" if filename != "index.html" else "Maria Group — BTP, Mines & Transport"
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
{header(active or filename)}
  <main id="contenu">
{content}
  </main>
{FOOTER}</body>
</html>
'''
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit", filename)


def page_hero(eyebrow, title, lead, crumb, img_var=""):
    style = f' style="--hero-img: url(\'{img_var}\')"' if img_var else ""
    return f'''    <section class="hero page-hero"{style}>
      {PATTERN}
      <img class="hero-mark" src="assets/img/logo-mark-white.png" alt="">
      <div class="container">
        <div class="hero-content">
          <ol class="breadcrumb">
            <li><a href="index.html">Accueil</a></li>
            <li aria-current="page">{crumb}</li>
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
        <a class="btn btn-primary reveal reveal-delay-1" href="contact.html">Demander un devis {I["arrow"]}</a>
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
        out.append(f'''          <div class="step reveal reveal-delay-{n - 1 if n > 1 else 0}">
            <div class="step-num">0{n}</div>
            <h3>{t}</h3>
            <p>{p}</p>
          </div>''')
    return "\n".join(out).replace(" reveal-delay-0", "")


def checklist(items):
    return "\n".join(f'            <li>{I["check"]}<span><strong>{t}</strong> — {p}</span></li>' for t, p in items)


POLES = [
    ("btp", "btp.html", "01", "Maria BTP", "Bâtiment & Travaux Publics",
     "Construction de bâtiments, génie civil, routes et aménagements : nous réalisons vos ouvrages de la conception à la livraison, dans le respect des délais et des normes.",
     ["Bâtiment", "Génie civil", "Routes & VRD"]),
    ("mines", "mines.html", "02", "Maria Mines", "Exploitation & services miniers",
     "Exploration, extraction, terrassement et gestion de carrières : une expertise minière responsable, sûre et performante au service de la valorisation des ressources.",
     ["Exploration", "Extraction", "Carrières"]),
    ("transport", "transport.html", "03", "Maria Transport", "Transport & logistique",
     "Transport de marchandises, de matériaux et d'engins lourds, logistique de chantier et location de flotte : nous acheminons vos ressources en toute sécurité.",
     ["Fret routier", "Convoi exceptionnel", "Logistique"]),
]


def pole_cards():
    out = []
    for i, (key, href, num, name, sub, text, tags) in enumerate(POLES):
        d = f" reveal-delay-{i}" if i else ""
        t = "".join(f"<li>{x}</li>" for x in tags)
        out.append(f'''          <article class="pole-card reveal{d}">
            <a class="pole-visual" href="{href}" aria-label="{name}"{bg("card-img", key + ".jpg")}>
              <span class="pole-num">PÔLE {num}</span>
              {ILLUS[key]}
            </a>
            <div class="pole-body">
              <span class="eyebrow">{sub}</span>
              <h3>{name}</h3>
              <p>{text}</p>
              <ul class="pole-tags">{t}</ul>
              <a class="link-arrow" href="{href}">Découvrir le pôle {I["arrow"]}</a>
            </div>
          </article>''')
    return "\n".join(out)


PROJECTS = [
    ("btp", "Bâtiment", "Immeuble de bureaux R+5", "Gros œuvre, second œuvre et corps d'état techniques."),
    ("btp", "Travaux publics", "Aménagement de voirie urbaine", "Terrassement, chaussée, assainissement et éclairage."),
    ("btp", "Génie civil", "Ouvrage d'art — pont routier", "Fondations profondes, piles et tablier béton armé."),
    ("mines", "Carrière", "Exploitation de carrière de granulats", "Abattage, concassage et criblage de matériaux."),
    ("mines", "Mines", "Travaux de découverture minière", "Décapage, terrassement de masse et pistes d'accès."),
    ("mines", "Exploration", "Campagne de sondages géologiques", "Forages, échantillonnage et suivi des données."),
    ("transport", "Logistique", "Approvisionnement de chantier", "Flux de matériaux et planification des rotations."),
    ("transport", "Convoi", "Transport d'engins lourds", "Convoi exceptionnel avec escorte et étude d'itinéraire."),
    ("transport", "Fret", "Transport de minerai", "Rotations de camions bennes entre site et point de stockage."),
]
CAT_LABEL = {"btp": "BTP", "mines": "Mines", "transport": "Transport"}


def project_cards(items, filterable=False):
    out = []
    for n, (cat, kind, title, text) in enumerate(items, 1):
        data = f' data-category="{cat}"' if filterable else ""
        out.append(f'''          <article class="project reveal"{data}>
            <div class="project-visual"{bg("card-img", f"projet-{n}.jpg")}>
              {ILLUS[cat]}
              <span class="project-cat">{CAT_LABEL[cat]}</span>
            </div>
            <div class="project-body">
              <span class="project-kind">{kind}</span>
              <h3>{title}</h3>
              <p>{text}</p>
            </div>
          </article>''')
    return "\n".join(out)


# =========================================================================
# ACCUEIL
# =========================================================================
home = f'''    <section class="hero hero-home"{bg("hero-img", "hero.jpg")}>
      {PATTERN}
      <img class="hero-mark" src="assets/img/logo-mark-white.png" alt="">
      <div class="container">
        <div class="hero-content">
          <span class="eyebrow">BTP · Mines · Transport</span>
          <h1>Bâtir, extraire, transporter : <em>l'excellence</em> au service de vos projets.</h1>
          <p class="hero-lead">Maria Group réunit trois pôles d'expertise complémentaires pour accompagner les acteurs publics et privés, de la première pierre au dernier kilomètre.</p>
          <div class="hero-actions">
            <a class="btn btn-gold" href="#poles">Découvrir nos pôles {I["arrow"]}</a>
            <a class="btn btn-outline" href="contact.html">Demander un devis</a>
          </div>
        </div>
      </div>
    </section>

    <div class="hero-poles">
      <div class="container">
        <div class="grid">
          <a class="hero-pole" href="btp.html">
            <div class="icon-box">{I["crane"]}</div>
            <div><h3>BTP</h3><p>Bâtiments, génie civil, routes et aménagements.</p></div>
          </a>
          <a class="hero-pole" href="mines.html">
            <div class="icon-box">{I["pickaxe"]}</div>
            <div><h3>Mines</h3><p>Exploration, extraction et exploitation de carrières.</p></div>
          </a>
          <a class="hero-pole" href="transport.html">
            <div class="icon-box">{I["truck"]}</div>
            <div><h3>Transport</h3><p>Fret, convois exceptionnels et logistique de chantier.</p></div>
          </a>
        </div>
      </div>
    </div>

    <section class="section" id="a-propos">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Qui sommes-nous</span>
          <h2>Un groupe intégré, une seule exigence : la qualité.</h2>
          <p class="lead">Maria Group est un groupe multisectoriel qui fédère les savoir-faire du bâtiment et des travaux publics, des mines et du transport.</p>
          <p class="muted">Cette intégration nous permet de maîtriser l'ensemble de la chaîne de valeur : extraction des matériaux, acheminement sur site et réalisation des ouvrages. Résultat : des délais tenus, des coûts optimisés et un interlocuteur unique pour nos clients.</p>
          <ul class="check-list">
{checklist([
    ("Interlocuteur unique", "un pilotage centralisé de vos projets multi-métiers."),
    ("Moyens propres", "engins, flotte de véhicules et équipes qualifiées."),
    ("Sécurité avant tout", "une culture QHSE appliquée sur chaque site."),
])}
          </ul>
          <a class="btn btn-primary" href="groupe.html">En savoir plus sur le groupe {I["arrow"]}</a>
        </div>
        <div class="about-visual reveal reveal-delay-1">
          <div class="frame">
            {PATTERN.replace('class="hero-pattern"', 'class="pattern"')}
            <img src="assets/img/logo-mark-white.png" alt="Emblème Maria Group" width="297" height="302" loading="lazy">
          </div>
          <div class="frame-border"></div>
          <div class="about-badge"><strong>3</strong><span>pôles d'expertise complémentaires</span></div>
        </div>
      </div>
    </section>

    <section class="section section-soft" id="poles">
      <div class="container">
        <div class="section-head center reveal">
          <span class="eyebrow center">Nos pôles d'activité</span>
          <h2>Trois métiers, une vision commune</h2>
          <p>Chaque pôle dispose de ses équipes, de ses équipements et de son savoir-faire, tout en bénéficiant de la force et des synergies du groupe.</p>
        </div>
        <div class="poles-grid">
{pole_cards()}
        </div>
      </div>
    </section>

    <section class="section section-dark">
      {PATTERN}
      <div class="container">
        <div class="stats">
          <div class="stat reveal"><div class="stat-value" data-count="3">3</div><div class="stat-label">Pôles d'activité</div></div>
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
    ("Livraison", "Réception des travaux, documentation et service après-livraison."),
])}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;max-width:none">
          <div style="max-width:620px">
            <span class="eyebrow">Réalisations</span>
            <h2>Nos domaines d'intervention</h2>
            <p>Un aperçu des types de projets que nos équipes conduisent au quotidien.</p>
          </div>
          <a class="btn btn-outline-dark" href="realisations.html">Toutes nos réalisations {I["arrow"]}</a>
        </div>
        <div class="projects">
{project_cards([PROJECTS[0], PROJECTS[3], PROJECTS[7]])}
        </div>
      </div>
    </section>

{cta()}'''

page("index.html", "Accueil",
     "Maria Group, groupe multisectoriel spécialisé dans le BTP, l'exploitation minière et le transport. Bâtir, extraire, transporter avec excellence.",
     home)

# =========================================================================
# LE GROUPE
# =========================================================================
groupe = page_hero("Le Groupe", "Une vision, trois expertises",
                   "Maria Group rassemble des métiers complémentaires pour offrir à ses clients des solutions complètes, fiables et durables.",
                   "Le Groupe") + f'''
    <section class="section">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Notre histoire</span>
          <h2>Construire l'avenir, ensemble</h2>
          <p class="lead">Né de la volonté de proposer une offre intégrée et de qualité, Maria Group s'est structuré autour de trois pôles : le BTP, les mines et le transport.</p>
          <p class="muted">Cette organisation nous permet d'intervenir sur des projets d'envergure en mutualisant nos ressources humaines et matérielles. Nos équipes partagent une même culture de l'exigence, de la sécurité et du service client.</p>
          <p class="muted">Aujourd'hui, le groupe accompagne aussi bien les institutions publiques que les entreprises privées et les opérateurs miniers, avec une ambition claire : contribuer durablement au développement des territoires.</p>
        </div>
        <div class="about-visual reveal reveal-delay-1">
          <div class="frame">
            {PATTERN.replace('class="hero-pattern"', 'class="pattern"')}
            <img src="assets/img/logo-mark-white.png" alt="Emblème Maria Group" width="297" height="302" loading="lazy">
          </div>
          <div class="frame-border"></div>
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
            <p>Concevoir, réaliser et opérer des projets d'infrastructures, d'exploitation minière et de logistique avec un haut niveau de qualité et de sécurité.</p>
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

    <section class="section" id="valeurs">
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
          <p>La performance de Maria Group repose sur une démarche QHSE exigeante, appliquée à l'ensemble de nos pôles et de nos sites d'intervention.</p>
          <ul class="check-list">
{checklist([
    ("Prévention", "analyse des risques, plans de prévention et causeries sécurité."),
    ("Formation", "habilitations, conduite d'engins et gestes de premiers secours."),
    ("Environnement", "gestion des déchets, maîtrise des poussières et réhabilitation des sites."),
    ("Qualité", "contrôles à chaque étape et traçabilité des matériaux."),
])}
          </ul>
        </div>
        <div class="features cols-3 reveal reveal-delay-1" style="grid-template-columns:1fr 1fr">
{feature("shield", "Sécurité", "Port des EPI et procédures contrôlées.")}
{feature("leaf", "Environnement", "Réduction de notre empreinte.")}
{feature("clipboard", "Qualité", "Contrôles et suivi documenté.")}
{feature("users", "Communautés", "Emploi et sous-traitance locale.")}
        </div>
      </div>
    </section>

{cta("Rejoignez nos partenaires", "Clients, fournisseurs, sous-traitants ou candidats : construisons ensemble les projets de demain.")}'''

page("groupe.html", "Le Groupe",
     "Découvrez Maria Group : histoire, mission, vision, valeurs et engagement QHSE d'un groupe actif dans le BTP, les mines et le transport.",
     groupe)

# =========================================================================
# PAGES PÔLES
# =========================================================================
def pole_page(fn, key, crumb, eyebrow, title, lead, intro_h, intro_p, intro_p2, checks, services_html, equip_title, equip, steps_items, cta_t, cta_p, desc):
    content = page_hero(eyebrow, title, lead, crumb) + f'''
    <section class="section">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">{crumb}</span>
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
          <div class="about-badge"><strong>{crumb}</strong><span>Un pôle Maria Group</span></div>
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
        <div class="section-head reveal" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;max-width:none">
          <div style="max-width:620px">
            <span class="eyebrow">Réalisations</span>
            <h2>Exemples de projets {crumb}</h2>
          </div>
          <a class="btn btn-outline-dark" href="realisations.html">Voir toutes les réalisations {I["arrow"]}</a>
        </div>
        <div class="projects">
{project_cards([p for p in PROJECTS if p[0] == key])}
        </div>
      </div>
    </section>

{cta(cta_t, cta_p)}'''
    page(fn, crumb, desc, content)


pole_page(
    "btp.html", "btp", "BTP", "Pôle 01 — Maria BTP",
    "Bâtiment &amp; Travaux Publics",
    "Nous concevons et réalisons des ouvrages solides et durables : bâtiments, infrastructures routières, génie civil et aménagements.",
    "Des ouvrages qui durent",
    "Le pôle BTP de Maria Group intervient en entreprise générale ou en lots séparés, pour des clients publics comme privés.",
    "Notre maîtrise des matériaux — en synergie avec notre pôle Mines — et de leur acheminement — grâce à notre pôle Transport — nous permet de garantir la continuité des chantiers et le respect des plannings.",
    [("Entreprise générale", "un pilotage complet tous corps d'état."),
     ("Bureau d'études intégré", "plans, métrés et suivi technique."),
     ("Respect des délais", "planification rigoureuse et reporting régulier.")],
    "\n".join([
        service("building", "Construction de bâtiments", "Logements, bureaux, bâtiments industriels et équipements publics.", ["Gros œuvre", "Second œuvre", "Clé en main"]),
        service("road", "Routes &amp; VRD", "Création et réhabilitation de routes, voiries et réseaux divers.", ["Terrassement", "Chaussées & bitumage", "Assainissement"], 1),
        service("bridge", "Génie civil", "Ouvrages d'art et structures en béton armé.", ["Ponts & dalots", "Fondations", "Réservoirs"], 2),
        service("ruler", "Études &amp; ingénierie", "Accompagnement technique en amont et pendant les travaux.", ["Études de faisabilité", "Plans d'exécution", "Métrés & devis"]),
        service("hammer", "Rénovation &amp; réhabilitation", "Remise à neuf, extension et mise aux normes de bâtiments existants.", ["Réhabilitation", "Extensions", "Mise en conformité"], 1),
        service("layers", "Aménagements extérieurs", "Mise en valeur des espaces et des sites.", ["Clôtures & portails", "Pavage", "Espaces verts"], 2),
    ]),
    "Un parc matériel adapté à chaque chantier",
    ["Pelles hydrauliques", "Chargeuses &amp; bulldozers", "Niveleuses", "Compacteurs", "Bétonnières &amp; centrales", "Grues &amp; échafaudages"],
    [("Étude", "Visite de site, relevés et étude technique du projet."),
     ("Chiffrage", "Devis détaillé, choix des matériaux et planning."),
     ("Travaux", "Exécution encadrée, contrôles qualité et sécurité."),
     ("Réception", "Levée des réserves, remise des ouvrages et garantie.")],
    "Votre projet de construction commence ici",
    "Bâtiment, route ou ouvrage d'art : confiez-nous votre projet et recevez une proposition détaillée.",
    "Maria BTP : construction de bâtiments, routes, VRD, génie civil, ouvrages d'art et réhabilitation.",
)

pole_page(
    "mines.html", "mines", "Mines", "Pôle 02 — Maria Mines",
    "Exploitation &amp; services miniers",
    "De l'exploration à l'extraction, nous valorisons les ressources du sous-sol de manière sûre, performante et responsable.",
    "Une expertise minière responsable",
    "Le pôle Mines de Maria Group accompagne les titulaires de permis et les opérateurs miniers sur l'ensemble du cycle d'exploitation.",
    "Nous mettons à disposition des équipes expérimentées et des engins adaptés aux conditions les plus exigeantes, avec une attention particulière portée à la sécurité des opérations et à la réhabilitation des sites.",
    [("Cycle complet", "de la prospection à la réhabilitation."),
     ("Production maîtrisée", "suivi des volumes et des rendements."),
     ("Respect de l'environnement", "plans de gestion et remise en état.")],
    "\n".join([
        service("globe", "Exploration &amp; prospection", "Identification et évaluation des gisements.", ["Études géologiques", "Sondages & forages", "Échantillonnage"]),
        service("pickaxe", "Extraction minière", "Exploitation à ciel ouvert, efficace et sécurisée.", ["Découverture", "Abattage", "Chargement & roulage"], 1),
        service("mountain", "Carrières &amp; granulats", "Production de matériaux pour le BTP.", ["Concassage", "Criblage", "Stockage"], 2),
        service("excavator", "Terrassement de masse", "Mouvements de terre de grands volumes.", ["Décapage", "Pistes d'accès", "Plateformes"]),
        service("flask", "Traitement &amp; contrôle", "Suivi de la qualité des matériaux extraits.", ["Analyses", "Contrôle qualité", "Traçabilité"], 1),
        service("leaf", "Réhabilitation des sites", "Remise en état et revalorisation après exploitation.", ["Remblaiement", "Revégétalisation", "Suivi environnemental"], 2),
    ]),
    "Des équipements robustes pour les sites miniers",
    ["Pelles minières", "Dumpers &amp; tombereaux", "Foreuses", "Concasseurs mobiles", "Cribles", "Bulldozers"],
    [("Évaluation", "Analyse du gisement, des contraintes et des objectifs."),
     ("Planification", "Plan d'exploitation, moyens et planning de production."),
     ("Exploitation", "Production encadrée et suivi QHSE permanent."),
     ("Réhabilitation", "Remise en état du site et suivi environnemental.")],
    "Valorisons ensemble vos ressources",
    "Exploration, extraction ou carrière : nos équipes étudient votre projet minier.",
    "Maria Mines : exploration, extraction minière, carrières, granulats, terrassement de masse et réhabilitation de sites.",
)

pole_page(
    "transport.html", "transport", "Transport", "Pôle 03 — Maria Transport",
    "Transport &amp; logistique",
    "Fret routier, convois exceptionnels et logistique de chantier : nous acheminons vos marchandises et vos équipements en toute sécurité.",
    "Vos ressources, au bon endroit, au bon moment",
    "Le pôle Transport de Maria Group dispose d'une flotte de véhicules adaptée au transport de marchandises, de matériaux de construction, de minerais et d'engins lourds.",
    "Nos chauffeurs expérimentés et notre suivi des opérations garantissent des livraisons ponctuelles et sécurisées, sur courtes comme sur longues distances.",
    [("Flotte entretenue", "véhicules contrôlés et maintenance préventive."),
     ("Suivi des livraisons", "information en temps réel sur vos expéditions."),
     ("Chauffeurs qualifiés", "formation à la conduite sécurisée.")],
    "\n".join([
        service("truck", "Transport de marchandises", "Fret routier national et sous-régional.", ["Charges complètes", "Groupage", "Distribution"]),
        service("container", "Transport de matériaux", "Approvisionnement des chantiers et des sites miniers.", ["Granulats & sable", "Ciment & fer", "Minerais"], 1),
        service("excavator", "Convois exceptionnels", "Transport d'engins et de charges hors gabarit.", ["Porte-engins", "Étude d'itinéraire", "Escorte"], 2),
        service("warehouse", "Logistique &amp; entreposage", "Gestion des flux et des stocks.", ["Stockage", "Gestion de stock", "Préparation"]),
        service("route", "Logistique de chantier", "Organisation des rotations et des flux sur site.", ["Planification", "Rotations", "Coordination"], 1),
        service("gauge", "Location de véhicules", "Mise à disposition de camions et d'engins.", ["Avec chauffeur", "Courte & longue durée", "Maintenance incluse"], 2),
    ]),
    "Une flotte polyvalente",
    ["Camions bennes", "Semi-remorques plateau", "Porte-engins", "Porte-conteneurs", "Citernes", "Véhicules légers de liaison"],
    [("Besoin", "Analyse des volumes, des délais et des contraintes."),
     ("Organisation", "Choix des véhicules, itinéraire et planning."),
     ("Acheminement", "Transport sécurisé et suivi en temps réel."),
     ("Livraison", "Remise conforme et bon de livraison signé.")],
    "Besoin d'acheminer vos marchandises ?",
    "Demandez une cotation : nous vous proposons la solution de transport la plus adaptée.",
    "Maria Transport : fret routier, transport de matériaux et de minerais, convois exceptionnels, logistique et location de véhicules.",
)

# =========================================================================
# RÉALISATIONS
# =========================================================================
real = page_hero("Réalisations", "Nos domaines d'intervention",
                 "Bâtiment, travaux publics, mines et transport : découvrez les types de projets portés par nos équipes.",
                 "Réalisations") + f'''
    <section class="section">
      <div class="container">
        <div class="filter-bar reveal" data-filter-bar role="group" aria-label="Filtrer les réalisations">
          <button type="button" class="is-active" data-filter="all" aria-pressed="true">Tous</button>
          <button type="button" data-filter="btp" aria-pressed="false">BTP</button>
          <button type="button" data-filter="mines" aria-pressed="false">Mines</button>
          <button type="button" data-filter="transport" aria-pressed="false">Transport</button>
        </div>
        <div class="projects">
{project_cards(PROJECTS, filterable=True)}
        </div>
      </div>
    </section>

{cta("Votre projet sera notre prochaine réalisation", "Présentez-nous votre besoin : nous revenons vers vous avec une proposition adaptée.")}'''

page("realisations.html", "Réalisations",
     "Réalisations de Maria Group : projets de bâtiment, travaux publics, exploitation minière, carrières et transport.",
     real)

# =========================================================================
# CONTACT
# =========================================================================
contact = page_hero("Contact", "Parlons de votre projet",
                    "Une question, une demande de devis ou un partenariat ? Notre équipe vous répond dans les meilleurs délais.",
                    "Contact") + f'''
    <section class="section">
      <div class="container contact-grid">
        <aside class="contact-info reveal">
          <span class="eyebrow">Coordonnées</span>
          <h2>Maria Group</h2>
          <p>Nos équipes sont à votre écoute pour étudier vos projets BTP, miniers et de transport.</p>
          <ul class="contact-items">
            <li><div class="icon-box">{I["pin"]}</div><div><strong>Adresse</strong>{ADDRESS}</div></li>
            <li><div class="icon-box">{I["phone"]}</div><div><strong>Téléphone</strong><a href="tel:{PHONE_HREF}">{PHONE}</a></div></li>
            <li><div class="icon-box">{I["mail"]}</div><div><strong>E-mail</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
            <li><div class="icon-box">{I["clock"]}</div><div><strong>Horaires</strong>{HOURS}</div></li>
          </ul>
        </aside>

        <div class="form-card reveal reveal-delay-1">
          <span class="eyebrow">Formulaire</span>
          <h2 style="font-size:1.6rem">Demande de devis ou d'information</h2>
          <p class="muted">Les champs marqués d'un <span style="color:var(--secondary-600)">*</span> sont obligatoires.</p>
          <!-- Pour recevoir les messages sans logiciel de messagerie, renseignez data-endpoint (ex. https://formspree.io/f/XXXX) -->
          <form id="contact-form" novalidate data-endpoint="" data-mailto="{EMAIL}">
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
                <label for="pole">Pôle concerné <span class="req">*</span></label>
                <select id="pole" name="pole" required>
                  <option value="">— Sélectionnez —</option>
                  <option>BTP</option>
                  <option>Mines</option>
                  <option>Transport</option>
                  <option>Autre / Plusieurs pôles</option>
                </select>
                <span class="error-msg">Veuillez sélectionner un pôle.</span>
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

page("contact.html", "Contact",
     "Contactez Maria Group pour vos projets de BTP, mines et transport : demande de devis, information ou partenariat.",
     contact)

# =========================================================================
# MENTIONS LÉGALES
# =========================================================================
legal = page_hero("Informations", "Mentions légales", "Informations légales relatives au site de Maria Group.", "Mentions légales") + f'''
    <section class="section">
      <div class="container prose">
        <h2>Éditeur du site</h2>
        <p>Maria Group<br>{ADDRESS}<br>Téléphone : {PHONE}<br>E-mail : <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>Forme juridique, capital social, numéro d'immatriculation (RCCM) et identifiant fiscal : à compléter.<br>Directeur de la publication : à compléter.</p>

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

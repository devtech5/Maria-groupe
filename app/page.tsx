import Link from "next/link";
import { AboutFrame, bgStyle, CheckList, Cta, Feature, PoleCards, SectionHead, SectionHeadRow, Steps } from "@/components/blocks";
import { Icon, Pattern } from "@/components/icons";
import { ProjectGrid } from "@/components/ProjectGrid";
import { apercu, getChiffresCles, getProjets } from "@/lib/data";
import { photo } from "@/lib/photos";

export const metadata = {
  title: { absolute: "Maria Group — BTP & Mines d'or" },
  description:
    "Maria Group réunit Maria BTP (bâtiment et travaux publics) et Maria Gold (exploration et exploitation aurifère). Bâtir et valoriser les ressources avec excellence.",
};

export default async function HomePage() {
  const [projets, realisations, chiffres] = await Promise.all([
    getProjets("projet"),
    getProjets("realisation"),
    getChiffresCles(),
  ]);

  return (
    <>
      <section className="hero hero-home" style={bgStyle("--hero-img", photo("hero.jpg"))}>
        <Pattern />
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img className="hero-mark" src="/assets/img/logo-mark-white.png" alt="" />
        <div className="container">
          <div className="hero-content">
            <span className="eyebrow">BTP · Mines d&apos;or</span>
            <h1>
              Bâtir et valoriser les ressources : <em>l&apos;excellence</em> au service de vos projets.
            </h1>
            <p className="hero-lead">
              Maria Group réunit deux filiales complémentaires, Maria BTP et Maria Gold, pour accompagner les acteurs
              publics et privés, de la première pierre au premier gramme d&apos;or.
            </p>
            <div className="hero-actions">
              <a className="btn btn-gold" href="#filiales">
                Découvrir nos filiales <Icon name="arrow" />
              </a>
              <Link className="btn btn-outline" href="/contact">
                Nous contacter
              </Link>
            </div>
          </div>
        </div>
      </section>

      <div className="hero-poles">
        <div className="container">
          <div className="grid">
            <Link className="hero-pole" href="/btp">
              <div className="icon-box"><Icon name="crane" /></div>
              <div>
                <h3>Maria BTP</h3>
                <p>Bâtiments, génie civil, routes et aménagements.</p>
              </div>
            </Link>
            <Link className="hero-pole" href="/gold">
              <div className="icon-box"><Icon name="ingot" /></div>
              <div>
                <h3>Maria Gold</h3>
                <p>Exploration, exploitation et traitement de l&apos;or.</p>
              </div>
            </Link>
            <Link className="hero-pole" href="/projets">
              <div className="icon-box"><Icon name="clipboard" /></div>
              <div>
                <h3>Nos projets</h3>
                <p>Les chantiers et programmes que nous menons.</p>
              </div>
            </Link>
          </div>
        </div>
      </div>

      <section className="section" id="a-propos">
        <div className="container split">
          <div className="reveal">
            <span className="eyebrow">Qui sommes-nous</span>
            <h2>Un groupe intégré, une seule exigence : la qualité.</h2>
            <p className="lead">
              Maria Group fédère les savoir-faire du bâtiment, des travaux publics et de l&apos;exploitation minière
              aurifère.
            </p>
            <p className="muted">
              Cette complémentarité nous permet de maîtriser chaque étape de nos projets : infrastructures,
              terrassements, exploitation et logistique. Résultat : des délais tenus, des coûts optimisés et un
              interlocuteur unique pour nos clients et partenaires.
            </p>
            <CheckList
              items={[
                ["Interlocuteur unique", "un pilotage centralisé de vos projets."],
                ["Moyens propres", "engins, véhicules et équipes qualifiées."],
                ["Sécurité avant tout", "une culture QHSE appliquée sur chaque site."],
              ]}
            />
            <Link className="btn btn-primary" href="/groupe">
              Qui sommes-nous <Icon name="arrow" />
            </Link>
          </div>
          <AboutFrame
            badge={
              <>
                <strong>2</strong>
                <span>filiales d&apos;expertise complémentaires</span>
              </>
            }
          />
        </div>
      </section>

      <section className="section section-soft" id="filiales">
        <div className="container">
          <SectionHead
            eyebrow="Nos filiales"
            title="Deux métiers, une vision commune"
            text="Chaque filiale dispose de ses équipes, de ses équipements et de son savoir-faire, tout en bénéficiant de la force et des synergies du groupe."
          />
          <PoleCards photos={{ btp: photo("btp.jpg"), gold: photo("gold.jpg") }} />
        </div>
      </section>

      <section className="section section-dark">
        <Pattern />
        <div className="container">
          <div className="stats">
            {chiffres.map((c, i) => (
              <div key={c.libelle} className={`stat reveal${i ? ` reveal-delay-${i}` : ""}`}>
                <div className="stat-value" data-count={c.valeur} data-suffix={c.suffixe}>
                  {c.valeur}
                  {c.suffixe}
                </div>
                <div className="stat-label">{c.libelle}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section" id="valeurs">
        <div className="container">
          <SectionHead eyebrow="Pourquoi nous choisir" title="Des valeurs qui guident chacun de nos chantiers" />
          <div className="features">
            <Feature icon="shield" title="Sécurité" text="La protection de nos équipes, de nos partenaires et des riverains est notre priorité absolue." />
            <Feature icon="award" title="Qualité" text="Des ouvrages et des prestations conformes aux normes et aux exigences de nos clients." d={1} />
            <Feature icon="handshake" title="Intégrité" text="Transparence, respect des engagements et relations de confiance durables." d={2} />
            <Feature icon="leaf" title="Responsabilité" text="Une approche soucieuse de l'environnement et du développement des communautés locales." d={3} />
          </div>
        </div>
      </section>

      <section className="section section-soft">
        <div className="container">
          <SectionHead
            eyebrow="Notre méthode"
            title="De l'idée à la livraison"
            text="Une démarche structurée pour sécuriser chaque étape de votre projet."
          />
          <Steps
            items={[
              ["Écoute & étude", "Analyse de votre besoin, visite de site et étude de faisabilité."],
              ["Proposition", "Offre technique et financière détaillée, planning prévisionnel."],
              ["Exécution", "Mobilisation des équipes et des moyens, suivi qualité et sécurité."],
              ["Livraison", "Réception des travaux, documentation et suivi après livraison."],
            ]}
          />
        </div>
      </section>

      <section className="section">
        <div className="container">
          <SectionHeadRow
            eyebrow="Projets"
            title="Nos projets en cours"
            href="/projets"
            label="Tous nos projets"
            text="Les chantiers et programmes actuellement menés par nos filiales."
          />
          <ProjectGrid projets={apercu(projets)} />
        </div>
      </section>

      <section className="section section-soft">
        <div className="container">
          <SectionHeadRow
            eyebrow="Réalisations"
            title="Nos dernières réalisations"
            href="/realisations"
            label="Toutes nos réalisations"
            text="Un aperçu des ouvrages et travaux livrés par nos équipes."
          />
          <ProjectGrid projets={apercu(realisations)} />
        </div>
      </section>

      <Cta />
    </>
  );
}

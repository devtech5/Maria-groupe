import { AboutFrame, CheckList, Cta, Feature, PageHero, PoleCards, SectionHead } from "@/components/blocks";
import { Icon, Pattern } from "@/components/icons";
import { photo } from "@/lib/photos";

export const metadata = {
  title: "Qui sommes-nous",
  description:
    "Découvrez Maria Group : histoire, mission, vision, filiales (Maria BTP, Maria Gold), valeurs et engagement QHSE.",
};

export default function GroupePage() {
  return (
    <>
      <PageHero
        eyebrow="Maria Group"
        title="Qui sommes-nous"
        lead="Maria Group rassemble deux filiales complémentaires pour offrir à ses clients et partenaires des solutions complètes, fiables et durables."
        crumbs={["Maria Group", "Qui sommes-nous"]}
      />

      <section className="section">
        <div className="container split">
          <div className="reveal">
            <span className="eyebrow">Notre histoire</span>
            <h2>Construire l&apos;avenir, ensemble</h2>
            <p className="lead">
              Né de la volonté de proposer une offre intégrée et de qualité, Maria Group s&apos;est structuré autour de
              deux filiales : Maria BTP et Maria Gold.
            </p>
            <p className="muted">
              Cette organisation nous permet d&apos;intervenir sur des projets d&apos;envergure en mutualisant nos
              ressources humaines et matérielles. Nos équipes partagent une même culture de l&apos;exigence, de la
              sécurité et du service client.
            </p>
            <p className="muted">
              Le groupe accompagne aussi bien les institutions publiques que les entreprises privées et les acteurs du
              secteur minier, avec une ambition claire : contribuer durablement au développement des territoires.
            </p>
          </div>
          <AboutFrame
            badge={
              <>
                <strong>1</strong>
                <span>groupe, un interlocuteur unique</span>
              </>
            }
          />
        </div>
      </section>

      <section className="section section-soft">
        <div className="container">
          <div className="mv-grid">
            <article className="mv-card reveal">
              <div className="icon-box"><Icon name="target" /></div>
              <h3>Notre mission</h3>
              <p>
                Concevoir et réaliser des infrastructures durables et valoriser les ressources aurifères avec un haut
                niveau de qualité et de sécurité.
              </p>
            </article>
            <article className="mv-card reveal reveal-delay-1">
              <div className="icon-box"><Icon name="eye" /></div>
              <h3>Notre vision</h3>
              <p>
                Devenir un groupe de référence, reconnu pour la fiabilité de ses réalisations et sa contribution au
                développement économique et social.
              </p>
            </article>
            <article className="mv-card reveal reveal-delay-2">
              <div className="icon-box"><Icon name="users" /></div>
              <h3>Notre ambition</h3>
              <p>
                Faire grandir nos talents, investir dans des équipements modernes et nouer des partenariats durables
                avec nos clients et fournisseurs.
              </p>
            </article>
          </div>
        </div>
      </section>

      <section className="section" id="filiales">
        <div className="container">
          <SectionHead eyebrow="Nos filiales" title="Deux expertises complémentaires" />
          <PoleCards photos={{ btp: photo("btp.jpg"), gold: photo("gold.jpg") }} />
        </div>
      </section>

      <section className="section section-soft" id="valeurs">
        <div className="container">
          <SectionHead eyebrow="Nos valeurs" title="Ce qui nous engage au quotidien" />
          <div className="features">
            <Feature icon="shield" title="Sécurité" text="Zéro compromis : formation, équipements de protection et procédures strictes sur tous nos sites." />
            <Feature icon="award" title="Excellence" text="Le souci du travail bien fait, du choix des matériaux jusqu'aux finitions." d={1} />
            <Feature icon="handshake" title="Intégrité" text="Une gestion transparente et éthique, dans le respect de nos engagements." d={2} />
            <Feature icon="bulb" title="Innovation" text="Des méthodes et des équipements modernes pour gagner en efficacité." d={3} />
          </div>
        </div>
      </section>

      <section className="section section-dark" id="hse">
        <Pattern />
        <div className="container split">
          <div className="reveal">
            <span className="eyebrow">Engagement QHSE</span>
            <h2>Qualité, Hygiène, Sécurité &amp; Environnement</h2>
            <p>
              La performance de Maria Group repose sur une démarche QHSE exigeante, appliquée à l&apos;ensemble de nos
              filiales et de nos sites d&apos;intervention.
            </p>
            <CheckList
              items={[
                ["Prévention", "analyse des risques, plans de prévention et causeries sécurité."],
                ["Formation", "habilitations, conduite d'engins et gestes de premiers secours."],
                ["Environnement", "gestion des déchets et de l'eau, réhabilitation des sites."],
                ["Qualité", "contrôles à chaque étape et traçabilité des matériaux."],
              ]}
            />
          </div>
          <div className="features cols-2 reveal reveal-delay-1">
            <Feature icon="shield" title="Sécurité" text="Port des EPI et procédures contrôlées." />
            <Feature icon="leaf" title="Environnement" text="Réduction de notre empreinte." />
            <Feature icon="clipboard" title="Qualité" text="Contrôles et suivi documenté." />
            <Feature icon="users" title="Communautés" text="Emploi et sous-traitance locale." />
          </div>
        </div>
      </section>

      <Cta
        title="Rejoignez nos partenaires"
        text="Clients, fournisseurs, sous-traitants ou candidats : construisons ensemble les projets de demain."
      />
    </>
  );
}

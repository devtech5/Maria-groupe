import Link from "next/link";
import { AboutFrame, bgStyle, CheckList, Cta, PageHero, SectionHead, SectionHeadRow, Services, Steps, type ServiceDef } from "@/components/blocks";
import { Icon, Illustration, Pattern, type Filiale } from "@/components/icons";
import { ProjectGrid } from "@/components/ProjectGrid";
import { getProjets } from "@/lib/data";
import { photo } from "@/lib/photos";

export type FilialeContent = {
  key: Filiale;
  name: string;
  short: string;
  eyebrow: string;
  title: string;
  lead: string;
  introTitle: string;
  intro: string;
  intro2: string;
  checks: [string, string][];
  services: ServiceDef[];
  equipTitle: string;
  equipment: string[];
  steps: [string, string][];
  ctaTitle: string;
  ctaText: string;
};

/** Gabarit commun des pages Maria BTP et Maria Gold. */
export async function FilialePage({ c }: { c: FilialeContent }) {
  const projets = (await getProjets("projet")).filter((p) => p.filiale === c.key);

  return (
    <>
      <PageHero eyebrow={c.eyebrow} title={c.title} lead={c.lead} crumbs={[{ href: "/groupe", label: "Maria Group" }, c.name]} />

      <section className="section">
        <div className="container split">
          <div className="reveal">
            <span className="eyebrow">{c.name}</span>
            <h2>{c.introTitle}</h2>
            <p className="lead">{c.intro}</p>
            <p className="muted">{c.intro2}</p>
            <CheckList items={c.checks} />
            <Link className="btn btn-primary" href="/contact">
              Demander un devis <Icon name="arrow" />
            </Link>
          </div>
          <AboutFrame
            badge={
              <>
                <strong>{c.short}</strong>
                <span>Une filiale Maria Group</span>
              </>
            }
          >
            <div className="frame illus-frame" style={bgStyle("--card-img", photo(`${c.key}.jpg`))}>
              <Pattern className="pattern" />
              <Illustration filiale={c.key} />
            </div>
          </AboutFrame>
        </div>
      </section>

      <section className="section section-soft">
        <div className="container">
          <SectionHead eyebrow="Nos services" title="Ce que nous faisons pour vous" />
          <Services items={c.services} />
        </div>
      </section>

      <section className="section section-dark">
        <Pattern />
        <div className="container split">
          <div className="reveal">
            <span className="eyebrow">Nos moyens</span>
            <h2>{c.equipTitle}</h2>
            <p>Des équipements entretenus et des équipes qualifiées, mobilisables rapidement sur vos sites.</p>
          </div>
          <ul className="pill-grid reveal reveal-delay-1">
            {c.equipment.map((e) => (
              <li key={e}>
                <Icon name="check" />
                {e}
              </li>
            ))}
          </ul>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <SectionHead eyebrow="Notre démarche" title="Un accompagnement de bout en bout" />
          <Steps items={c.steps} />
        </div>
      </section>

      {projets.length > 0 && (
        <section className="section section-soft">
          <div className="container">
            <SectionHeadRow eyebrow="Projets" title={`Projets ${c.name}`} href="/projets" label="Voir tous les projets" />
            <ProjectGrid projets={projets.slice(0, 6)} />
          </div>
        </section>
      )}

      <Cta title={c.ctaTitle} text={c.ctaText} />
    </>
  );
}

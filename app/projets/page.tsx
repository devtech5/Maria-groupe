import { Cta, PageHero } from "@/components/blocks";
import { ProjectGrid } from "@/components/ProjectGrid";
import { getProjets } from "@/lib/data";

export const metadata = {
  title: "Projets",
  description: "Projets en cours et en préparation de Maria Group : bâtiment, travaux publics et exploitation aurifère.",
};

export default async function ProjetsPage() {
  const projets = await getProjets("projet");
  return (
    <>
      <PageHero
        eyebrow="Projets"
        title="Nos projets"
        lead="Découvrez les chantiers et programmes actuellement menés ou préparés par Maria BTP et Maria Gold."
        crumbs={["Projets"]}
      />
      <section className="section">
        <div className="container">
          <ProjectGrid projets={projets} filterable label="Filtrer les projets" />
        </div>
      </section>
      <Cta title="Un projet à nous confier ?" text="Présentez-nous votre besoin : nous revenons vers vous avec une proposition adaptée." />
    </>
  );
}

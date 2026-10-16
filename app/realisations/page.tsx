import { Cta, PageHero } from "@/components/blocks";
import { ProjectGrid } from "@/components/ProjectGrid";
import { getProjets } from "@/lib/data";

export const metadata = {
  title: "Réalisations",
  description: "Réalisations de Maria Group : bâtiment, travaux publics, génie civil, exploration et exploitation aurifère.",
};

export default async function RealisationsPage() {
  const realisations = await getProjets("realisation");
  return (
    <>
      <PageHero
        eyebrow="Réalisations"
        title="Nos réalisations"
        lead="Bâtiment, travaux publics et mines d'or : découvrez les ouvrages et travaux livrés par nos équipes."
        crumbs={["Réalisations"]}
      />
      <section className="section">
        <div className="container">
          <ProjectGrid projets={realisations} filterable label="Filtrer les réalisations" />
        </div>
      </section>
      <Cta
        title="Votre projet sera notre prochaine réalisation"
        text="Présentez-nous votre besoin : nous revenons vers vous avec une proposition adaptée."
      />
    </>
  );
}

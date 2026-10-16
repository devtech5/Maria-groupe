"use client";

import { useState } from "react";
import { Illustration, type Filiale } from "@/components/icons";
import { FILIALE_LABEL, type Projet } from "@/lib/content";
import { bgStyle } from "@/components/blocks";

export function ProjectCard({ projet, hidden = false }: { projet: Projet; hidden?: boolean }) {
  const isProjet = projet.type === "projet";
  const meta = [projet.lieu, projet.annee].filter(Boolean).join(" · ");
  return (
    <article className="project reveal" hidden={hidden}>
      <div className="project-visual" style={bgStyle("--card-img", projet.imageUrl)}>
        <Illustration filiale={projet.filiale} />
        <span className="project-cat">{FILIALE_LABEL[projet.filiale]}</span>
        {isProjet && projet.statut && <span className="project-status">{projet.statut}</span>}
      </div>
      <div className="project-body">
        <span className="project-kind">{projet.categorie}</span>
        <h3>{projet.titre}</h3>
        <p>{projet.description}</p>
        {meta && <p className="project-meta">{meta}</p>}
      </div>
    </article>
  );
}

type Filter = "all" | Filiale;

const FILTERS: { value: Filter; label: string }[] = [
  { value: "all", label: "Tous" },
  { value: "btp", label: "Maria BTP" },
  { value: "gold", label: "Maria Gold" },
];

/** Grille de projets, avec filtre par filiale si `filterable`. */
export function ProjectGrid({ projets, filterable = false, label }: { projets: Projet[]; filterable?: boolean; label?: string }) {
  const [filter, setFilter] = useState<Filter>("all");
  const shown = (p: Projet) => filter === "all" || p.filiale === filter;

  return (
    <>
      {filterable && (
        <div className="filter-bar reveal" role="group" aria-label={label}>
          {FILTERS.map((f) => (
            <button
              key={f.value}
              type="button"
              className={filter === f.value ? "is-active" : undefined}
              aria-pressed={filter === f.value}
              onClick={() => setFilter(f.value)}
            >
              {f.label}
            </button>
          ))}
        </div>
      )}
      <div className="projects">
        {/* Toutes les cartes restent dans la page (animations d'apparition) ; le filtre les masque. */}
        {projets.map((p) => (
          <ProjectCard key={p.id} projet={p} hidden={!shown(p)} />
        ))}
      </div>
      {!projets.some(shown) && <p className="muted empty-state">Aucun élément pour le moment.</p>}
    </>
  );
}

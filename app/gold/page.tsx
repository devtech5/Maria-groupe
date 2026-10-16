import { FilialePage, type FilialeContent } from "@/components/FilialePage";

export const metadata = {
  title: "Maria Gold",
  description:
    "Maria Gold : exploration aurifère, exploitation minière, traitement du minerai d'or, infrastructures minières et réhabilitation des sites.",
};

const GOLD: FilialeContent = {
  key: "gold",
  name: "Maria Gold",
  short: "Gold",
  eyebrow: "Filiale 02 — Maria Gold",
  title: "Exploration & exploitation aurifère",
  lead: "De la prospection à la production, Maria Gold valorise les ressources aurifères de manière sûre, performante et responsable.",
  introTitle: "L'or, une ressource à valoriser avec responsabilité",
  intro: "Maria Gold est la filiale minière de Maria Group, dédiée à l'exploration et à l'exploitation de gisements aurifères.",
  intro2:
    "Nous mobilisons géologues, ingénieurs et opérateurs expérimentés, appuyés par des équipements adaptés, avec une exigence constante : la sécurité des équipes, le respect de la réglementation minière et la préservation de l'environnement.",
  checks: [
    ["Cycle complet", "de la prospection à la réhabilitation des sites."],
    ["Conformité", "respect du code minier et des normes environnementales."],
    ["Ancrage local", "emploi et développement des communautés riveraines."],
  ],
  services: [
    { icon: "globe", title: "Exploration & prospection", text: "Identification et évaluation des gisements aurifères.", bullets: ["Géologie & cartographie", "Sondages & forages", "Analyses d'échantillons"] },
    { icon: "pickaxe", title: "Exploitation minière", text: "Extraction à ciel ouvert, efficace et sécurisée.", bullets: ["Découverture", "Abattage", "Chargement & roulage"] },
    { icon: "ingot", title: "Traitement du minerai", text: "Valorisation du minerai et récupération de l'or.", bullets: ["Concassage & broyage", "Récupération de l'or", "Contrôle des teneurs"] },
    { icon: "excavator", title: "Infrastructures minières", text: "Aménagement des sites, en synergie avec Maria BTP.", bullets: ["Pistes & plateformes", "Bases-vie", "Terrassement de masse"] },
    { icon: "shield", title: "Sécurité & sûreté", text: "Protection des équipes, des installations et de la production.", bullets: ["Plans de prévention", "Sûreté des sites", "Formation des équipes"] },
    { icon: "leaf", title: "Environnement & communautés", text: "Une exploitation respectueuse des territoires.", bullets: ["Gestion de l'eau", "Réhabilitation", "Projets communautaires"] },
  ],
  equipTitle: "Des équipements robustes pour les sites aurifères",
  equipment: ["Pelles hydrauliques", "Dumpers & tombereaux", "Foreuses", "Concasseurs & broyeurs", "Chargeuses", "Équipements de laboratoire"],
  steps: [
    ["Exploration", "Prospection, sondages et analyse des échantillons."],
    ["Évaluation", "Estimation des ressources et étude de faisabilité."],
    ["Exploitation", "Production encadrée et suivi QHSE permanent."],
    ["Réhabilitation", "Remise en état du site et suivi environnemental."],
  ],
  ctaTitle: "Un projet aurifère ? Parlons-en.",
  ctaText: "Titulaire de permis, investisseur ou partenaire : échangeons sur vos projets d'exploration et d'exploitation.",
};

export default function GoldPage() {
  return <FilialePage c={GOLD} />;
}

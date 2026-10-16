/*
 * Contenu éditorial du site : coordonnées, menu, filiales,
 * et données par défaut (affichées tant que la base PostgreSQL est vide ou indisponible).
 */
import type { Filiale } from "@/components/icons";

export const CONTACT = {
  mobile: "+225 07 00 00 00 00",
  mobileHref: "+2250700000000",
  fixe: "+225 27 00 00 00 00",
  fixeHref: "+2252700000000",
  email: "hello@maria-groupe.com",
  address: "Côte d'Ivoire — adresse à compléter",
  hours: "Lun – Ven : 8h00 – 18h00",
  whatsapp: "https://wa.me/2250700000000",
  facebook: "#",
  linkedin: "#",
  instagram: "#",
};

export type NavLink = { href: string; label: string };
export type NavItem = NavLink | { label: string; children: NavLink[] };

export const NAV: NavItem[] = [
  { href: "/", label: "Accueil" },
  {
    label: "Maria Group",
    children: [
      { href: "/groupe", label: "Qui sommes-nous" },
      { href: "/btp", label: "Maria BTP" },
      { href: "/gold", label: "Maria Gold" },
    ],
  },
  { href: "/projets", label: "Projets" },
  { href: "/realisations", label: "Réalisations" },
];

export const FILIALE_LABEL: Record<Filiale, string> = { btp: "Maria BTP", gold: "Maria Gold" };

export type Pole = {
  key: Filiale;
  href: string;
  num: string;
  name: string;
  sub: string;
  text: string;
  tags: string[];
};

export const POLES: Pole[] = [
  {
    key: "btp",
    href: "/btp",
    num: "01",
    name: "Maria BTP",
    sub: "Bâtiment & Travaux Publics",
    text: "Construction de bâtiments, génie civil, routes et aménagements : nous réalisons vos ouvrages de la conception à la livraison, dans le respect des délais et des normes.",
    tags: ["Bâtiment", "Génie civil", "Routes & VRD"],
  },
  {
    key: "gold",
    href: "/gold",
    num: "02",
    name: "Maria Gold",
    sub: "Exploration & exploitation aurifère",
    text: "Exploration, extraction et traitement du minerai d'or : une expertise minière responsable, sûre et performante au service de la valorisation des ressources aurifères.",
    tags: ["Exploration", "Exploitation", "Traitement"],
  },
];

/* ---- Données dynamiques (types partagés avec lib/data.ts) ---- */

export type ProjetType = "projet" | "realisation";

export type Projet = {
  id: string;
  type: ProjetType;
  filiale: Filiale;
  categorie: string;
  statut: string | null;
  titre: string;
  description: string;
  lieu: string | null;
  annee: number | null;
  imageUrl: string | null;
};

export type ChiffreCle = { valeur: number; suffixe: string; libelle: string };

function defaut(
  type: ProjetType,
  n: number,
  filiale: Filiale,
  categorie: string,
  statut: string | null,
  titre: string,
  description: string
): Projet {
  return { id: `defaut-${type}-${n}`, type, filiale, categorie, statut, titre, description, lieu: null, annee: null, imageUrl: null };
}

/** Exemples génériques, remplacés dès que la table `projets` contient des lignes publiées. */
export const DEFAULT_PROJETS: Projet[] = [
  defaut("projet", 1, "btp", "Bâtiment", "En cours", "Ensemble résidentiel", "Construction de logements avec voiries et réseaux divers."),
  defaut("projet", 2, "btp", "Travaux publics", "En cours", "Réhabilitation de routes", "Reprise de chaussée, drainage et signalisation."),
  defaut("projet", 3, "btp", "Bâtiment", "En préparation", "Bâtiment administratif", "Études d'exécution et préparation du chantier."),
  defaut("projet", 4, "gold", "Exploration", "En cours", "Programme d'exploration aurifère", "Cartographie géologique et campagnes de sondages."),
  defaut("projet", 5, "gold", "Traitement", "En préparation", "Unité de traitement du minerai", "Études de dimensionnement et choix des procédés."),
  defaut("projet", 6, "gold", "Environnement", "En cours", "Réhabilitation environnementale", "Remise en état et revégétalisation de zones exploitées."),
];

export const DEFAULT_REALISATIONS: Projet[] = [
  defaut("realisation", 1, "btp", "Bâtiment", null, "Immeuble de bureaux R+5", "Gros œuvre, second œuvre et corps d'état techniques."),
  defaut("realisation", 2, "btp", "Travaux publics", null, "Aménagement de voirie urbaine", "Terrassement, chaussée, assainissement et éclairage."),
  defaut("realisation", 3, "btp", "Génie civil", null, "Ouvrage d'art — pont routier", "Fondations profondes, piles et tablier en béton armé."),
  defaut("realisation", 4, "gold", "Exploration", null, "Campagne de sondages géologiques", "Forages, échantillonnage et analyse des teneurs en or."),
  defaut("realisation", 5, "gold", "Exploitation", null, "Travaux de découverture minière", "Décapage, terrassement de masse et pistes d'accès."),
  defaut("realisation", 6, "gold", "Infrastructures", null, "Plateformes et pistes minières", "Aménagement des zones d'exploitation et de stockage."),
];

/** Valeurs génériques, remplacées dès que la table `chiffres_cles` contient des lignes publiées. */
export const DEFAULT_CHIFFRES: ChiffreCle[] = [
  { valeur: 2, suffixe: "", libelle: "Filiales spécialisées" },
  { valeur: 360, suffixe: "°", libelle: "Solutions intégrées" },
  { valeur: 24, suffixe: "/7", libelle: "Suivi des opérations" },
  { valeur: 100, suffixe: "%", libelle: "Engagement sécurité" },
];

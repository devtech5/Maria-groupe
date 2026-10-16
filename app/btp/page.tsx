import { FilialePage, type FilialeContent } from "@/components/FilialePage";

export const metadata = {
  title: "Maria BTP",
  description:
    "Maria BTP : construction de bâtiments, routes, VRD, génie civil, ouvrages d'art, réhabilitation et logistique de chantier.",
};

const BTP: FilialeContent = {
  key: "btp",
  name: "Maria BTP",
  short: "BTP",
  eyebrow: "Filiale 01 — Maria BTP",
  title: "Bâtiment & Travaux Publics",
  lead: "Nous concevons et réalisons des ouvrages solides et durables : bâtiments, infrastructures routières, génie civil et aménagements.",
  introTitle: "Des ouvrages qui durent",
  intro: "Maria BTP intervient en entreprise générale ou en lots séparés, pour des clients publics comme privés.",
  intro2:
    "Nos moyens propres — engins de terrassement, véhicules de transport et équipes qualifiées — nous permettent de garantir la continuité des chantiers et le respect des plannings, y compris pour les infrastructures des sites miniers de Maria Gold.",
  checks: [
    ["Entreprise générale", "un pilotage complet tous corps d'état."],
    ["Bureau d'études intégré", "plans, métrés et suivi technique."],
    ["Respect des délais", "planification rigoureuse et reporting régulier."],
  ],
  services: [
    { icon: "building", title: "Construction de bâtiments", text: "Logements, bureaux, bâtiments industriels et équipements publics.", bullets: ["Gros œuvre", "Second œuvre", "Clé en main"] },
    { icon: "road", title: "Routes & VRD", text: "Création et réhabilitation de routes, voiries et réseaux divers.", bullets: ["Terrassement", "Chaussées & bitumage", "Assainissement"] },
    { icon: "bridge", title: "Génie civil", text: "Ouvrages d'art et structures en béton armé.", bullets: ["Ponts & dalots", "Fondations", "Réservoirs"] },
    { icon: "ruler", title: "Études & ingénierie", text: "Accompagnement technique en amont et pendant les travaux.", bullets: ["Études de faisabilité", "Plans d'exécution", "Métrés & devis"] },
    { icon: "hammer", title: "Rénovation & réhabilitation", text: "Remise à neuf, extension et mise aux normes de bâtiments existants.", bullets: ["Réhabilitation", "Extensions", "Mise en conformité"] },
    { icon: "truck", title: "Transport & logistique de chantier", text: "Acheminement des matériaux et des engins sur vos chantiers.", bullets: ["Approvisionnement", "Porte-engins", "Location d'engins"] },
  ],
  equipTitle: "Un parc matériel adapté à chaque chantier",
  equipment: ["Pelles hydrauliques", "Chargeuses & bulldozers", "Niveleuses", "Compacteurs", "Bétonnières & centrales", "Camions bennes & porte-engins"],
  steps: [
    ["Étude", "Visite de site, relevés et étude technique du projet."],
    ["Chiffrage", "Devis détaillé, choix des matériaux et planning."],
    ["Travaux", "Exécution encadrée, contrôles qualité et sécurité."],
    ["Réception", "Levée des réserves, remise des ouvrages et garantie."],
  ],
  ctaTitle: "Votre projet de construction commence ici",
  ctaText: "Bâtiment, route ou ouvrage d'art : confiez-nous votre projet et recevez une proposition détaillée.",
};

export default function BtpPage() {
  return <FilialePage c={BTP} />;
}

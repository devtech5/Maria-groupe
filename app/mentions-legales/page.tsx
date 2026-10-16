import { PageHero } from "@/components/blocks";
import { CONTACT } from "@/lib/content";

export const metadata = { title: "Mentions légales", description: "Mentions légales du site Maria Group." };

export default function MentionsLegalesPage() {
  return (
    <>
      <PageHero eyebrow="Informations" title="Mentions légales" lead="Informations légales relatives au site de Maria Group." crumbs={["Mentions légales"]} />
      <section className="section">
        <div className="container prose">
          <h2>Éditeur du site</h2>
          <p>
            Maria Group<br />
            {CONTACT.address}<br />
            Mobile : {CONTACT.mobile} — Fixe : {CONTACT.fixe}<br />
            E-mail : <a href={`mailto:${CONTACT.email}`}>{CONTACT.email}</a>
          </p>
          <p>
            Forme juridique, capital social, numéro d&apos;immatriculation (RCCM) et compte contribuable : à compléter.
            <br />
            Directeur de la publication : à compléter.
          </p>

          <h2>Hébergement</h2>
          <p>Nom, adresse et coordonnées de l&apos;hébergeur du site : à compléter.</p>

          <h2>Propriété intellectuelle</h2>
          <p>
            L&apos;ensemble des contenus de ce site (textes, logos, images, éléments graphiques) est la propriété
            exclusive de Maria Group, sauf mention contraire. Toute reproduction, totale ou partielle, sans autorisation
            préalable écrite est interdite.
          </p>

          <h2>Données personnelles</h2>
          <p>
            Les informations transmises via le formulaire de contact sont enregistrées dans notre base de données,
            utilisées uniquement pour répondre à votre demande et ne sont jamais cédées à des tiers. Vous disposez
            d&apos;un droit d&apos;accès, de rectification et de suppression de vos données en écrivant à{" "}
            <a href={`mailto:${CONTACT.email}`}>{CONTACT.email}</a>.
          </p>

          <h2>Cookies</h2>
          <p>
            Ce site n&apos;utilise aucun cookie et ne fait appel à aucun service tiers de suivi : toutes ses ressources,
            y compris les polices de caractères, sont hébergées sur nos serveurs.
          </p>
        </div>
      </section>
    </>
  );
}

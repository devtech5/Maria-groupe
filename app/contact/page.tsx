import { PageHero } from "@/components/blocks";
import { ContactForm } from "@/components/ContactForm";
import { Icon } from "@/components/icons";
import { CONTACT } from "@/lib/content";

export const metadata = {
  title: "Contacts",
  description:
    "Contactez Maria Group pour vos projets de BTP et d'exploitation aurifère : demande de devis, information ou partenariat.",
};

export default function ContactPage() {
  return (
    <>
      <PageHero
        eyebrow="Contacts"
        title="Parlons de votre projet"
        lead="Une question, une demande de devis ou un partenariat ? Notre équipe vous répond dans les meilleurs délais."
        crumbs={["Contacts"]}
      />
      <section className="section">
        <div className="container contact-grid">
          <aside className="contact-info reveal">
            <span className="eyebrow">Coordonnées</span>
            <h2>Maria Group</h2>
            <p>Nos équipes sont à votre écoute pour étudier vos projets de BTP et d&apos;exploitation aurifère.</p>
            <ul className="contact-items">
              <li>
                <div className="icon-box"><Icon name="phone" /></div>
                <div><strong>Mobile</strong><a href={`tel:${CONTACT.mobileHref}`}>{CONTACT.mobile}</a></div>
              </li>
              <li>
                <div className="icon-box"><Icon name="phone" /></div>
                <div><strong>Fixe</strong><a href={`tel:${CONTACT.fixeHref}`}>{CONTACT.fixe}</a></div>
              </li>
              <li>
                <div className="icon-box"><Icon name="mail" /></div>
                <div><strong>E-mail</strong><a href={`mailto:${CONTACT.email}`}>{CONTACT.email}</a></div>
              </li>
              <li>
                <div className="icon-box"><Icon name="pin" /></div>
                <div><strong>Adresse</strong>{CONTACT.address}</div>
              </li>
              <li>
                <div className="icon-box"><Icon name="clock" /></div>
                <div><strong>Horaires</strong>{CONTACT.hours}</div>
              </li>
            </ul>
            <a className="btn btn-gold contact-wa" href={CONTACT.whatsapp}>
              <Icon name="whatsapp" /> Écrire sur WhatsApp
            </a>
          </aside>

          <div className="form-card reveal reveal-delay-1">
            <span className="eyebrow">Formulaire</span>
            <h2 className="form-title">Demande de devis ou d&apos;information</h2>
            <p className="muted">Les champs marqués d&apos;un <span className="req">*</span> sont obligatoires.</p>
            <ContactForm />
          </div>
        </div>
      </section>
    </>
  );
}

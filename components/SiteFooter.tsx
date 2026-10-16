import Link from "next/link";
import { Icon } from "@/components/icons";
import { CONTACT } from "@/lib/content";

export function SiteFooter() {
  return (
    <footer className="site-footer">
      <div className="container footer-main">
        <div className="footer-brand">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/assets/img/logo-white.png" alt="Maria Group" width={150} height={159} />
          <p>
            Groupe engagé dans le bâtiment, les travaux publics et l&apos;exploitation aurifère. Nous bâtissons et
            valorisons les ressources avec rigueur, sécurité et responsabilité.
          </p>
          <div className="footer-social">
            <a href={CONTACT.facebook} aria-label="Facebook">
              <Icon name="facebook" />
            </a>
            <a href={CONTACT.linkedin} aria-label="LinkedIn">
              <Icon name="linkedin" />
            </a>
            <a href={CONTACT.instagram} aria-label="Instagram">
              <Icon name="instagram" />
            </a>
            <a href={CONTACT.whatsapp} aria-label="WhatsApp">
              <Icon name="whatsapp" />
            </a>
          </div>
        </div>
        <div>
          <h4>Maria Group</h4>
          <ul className="footer-links">
            <li><Link href="/groupe">Qui sommes-nous</Link></li>
            <li><Link href="/btp">Maria BTP</Link></li>
            <li><Link href="/gold">Maria Gold</Link></li>
            <li><Link href="/groupe#hse">Engagement QHSE</Link></li>
          </ul>
        </div>
        <div>
          <h4>Navigation</h4>
          <ul className="footer-links">
            <li><Link href="/">Accueil</Link></li>
            <li><Link href="/projets">Projets</Link></li>
            <li><Link href="/realisations">Réalisations</Link></li>
            <li><Link href="/contact">Contacts</Link></li>
          </ul>
        </div>
        <div>
          <h4>Contacts</h4>
          <ul className="footer-contact">
            <li><Icon name="pin" /><span>{CONTACT.address}</span></li>
            <li><Icon name="phone" /><span>Mobile : <a href={`tel:${CONTACT.mobileHref}`}>{CONTACT.mobile}</a></span></li>
            <li><Icon name="phone" /><span>Fixe : <a href={`tel:${CONTACT.fixeHref}`}>{CONTACT.fixe}</a></span></li>
            <li><Icon name="mail" /><a href={`mailto:${CONTACT.email}`}>{CONTACT.email}</a></li>
            <li><Icon name="clock" /><span>{CONTACT.hours}</span></li>
          </ul>
        </div>
      </div>
      <div className="footer-bottom">
        <div className="container">
          <span>&copy; {new Date().getFullYear()} Maria Group. Tous droits réservés.</span>
          <Link href="/mentions-legales">Mentions légales</Link>
        </div>
      </div>
    </footer>
  );
}

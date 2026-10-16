import Link from "next/link";
import { Icon, Pattern } from "@/components/icons";

export const metadata = { title: "Page introuvable" };

export default function NotFound() {
  return (
    <section className="hero page-hero">
      <Pattern />
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img className="hero-mark" src="/assets/img/logo-mark-white.png" alt="" />
      <div className="container">
        <div className="hero-content">
          <span className="eyebrow">Erreur 404</span>
          <h1>Page introuvable</h1>
          <p className="hero-lead">La page que vous recherchez n&apos;existe pas ou a été déplacée.</p>
          <div className="hero-actions">
            <Link className="btn btn-gold" href="/">
              Retour à l&apos;accueil <Icon name="arrow" />
            </Link>
            <Link className="btn btn-outline" href="/contact">
              Nous contacter
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

/* Blocs de mise en page réutilisés par les pages. */
import Link from "next/link";
import type { CSSProperties, ReactNode } from "react";
import { Icon, Illustration, Pattern, type IconName } from "@/components/icons";
import { POLES } from "@/lib/content";

function delay(n: number) {
  return n ? ` reveal-delay-${n}` : "";
}

/** Style d'une photo de fond facultative (URL déjà validée côté serveur). */
export function bgStyle(variable: "--card-img" | "--hero-img", url: string | null | undefined): CSSProperties | undefined {
  return url ? ({ [variable]: `url('${url}')` } as CSSProperties) : undefined;
}

type Crumb = string | { href: string; label: string };

export function PageHero({ eyebrow, title, lead, crumbs }: { eyebrow: string; title: string; lead: string; crumbs: Crumb[] }) {
  const last = crumbs[crumbs.length - 1];
  return (
    <section className="hero page-hero">
      <Pattern />
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img className="hero-mark" src="/assets/img/logo-mark-white.png" alt="" />
      <div className="container">
        <div className="hero-content">
          <ol className="breadcrumb">
            <li><Link href="/">Accueil</Link></li>
            {crumbs.slice(0, -1).map((c) =>
              typeof c === "string" ? (
                <li key={c}>{c}</li>
              ) : (
                <li key={c.href}><Link href={c.href}>{c.label}</Link></li>
              )
            )}
            <li aria-current="page">{typeof last === "string" ? last : last.label}</li>
          </ol>
          <span className="eyebrow">{eyebrow}</span>
          <h1>{title}</h1>
          <p className="hero-lead">{lead}</p>
        </div>
      </div>
    </section>
  );
}

export function Cta({
  title = "Un projet ? Parlons-en.",
  text = "Nos équipes étudient votre besoin et vous proposent une solution adaptée, chiffrée et planifiée.",
}: {
  title?: string;
  text?: string;
}) {
  return (
    <section className="cta-band">
      <div className="container">
        <div className="reveal">
          <h2>{title}</h2>
          <p>{text}</p>
        </div>
        <Link className="btn btn-primary reveal reveal-delay-1" href="/contact">
          Nous contacter <Icon name="arrow" />
        </Link>
      </div>
    </section>
  );
}

export function Feature({ icon, title, text, d = 0 }: { icon: IconName; title: string; text: string; d?: number }) {
  return (
    <article className={`feature reveal${delay(d)}`}>
      <div className="icon-box"><Icon name={icon} /></div>
      <h3>{title}</h3>
      <p>{text}</p>
    </article>
  );
}

export type ServiceDef = { icon: IconName; title: string; text: string; bullets: string[] };

export function Services({ items }: { items: ServiceDef[] }) {
  return (
    <div className="services">
      {items.map((s, i) => (
        <article key={s.title} className={`service reveal${delay(i % 3)}`}>
          <div className="icon-box"><Icon name={s.icon} /></div>
          <h3>{s.title}</h3>
          <p>{s.text}</p>
          <ul>
            {s.bullets.map((b) => (
              <li key={b}>{b}</li>
            ))}
          </ul>
        </article>
      ))}
    </div>
  );
}

export function Steps({ items }: { items: [string, string][] }) {
  return (
    <div className="process">
      {items.map(([t, p], i) => (
        <div key={t} className={`step reveal${delay(i)}`}>
          <div className="step-num">0{i + 1}</div>
          <h3>{t}</h3>
          <p>{p}</p>
        </div>
      ))}
    </div>
  );
}

export function CheckList({ items }: { items: [string, string][] }) {
  return (
    <ul className="check-list">
      {items.map(([t, p]) => (
        <li key={t}>
          <Icon name="check" />
          <span>
            <strong>{t}</strong> — {p}
          </span>
        </li>
      ))}
    </ul>
  );
}

export function SectionHead({ eyebrow, title, text }: { eyebrow: string; title: string; text?: string }) {
  return (
    <div className="section-head center reveal">
      <span className="eyebrow center">{eyebrow}</span>
      <h2>{title}</h2>
      {text && <p>{text}</p>}
    </div>
  );
}

export function SectionHeadRow({
  eyebrow,
  title,
  href,
  label,
  text,
}: {
  eyebrow: string;
  title: string;
  href: string;
  label: string;
  text?: string;
}) {
  return (
    <div className="section-head section-head-row reveal">
      <div>
        <span className="eyebrow">{eyebrow}</span>
        <h2>{title}</h2>
        {text && <p>{text}</p>}
      </div>
      <Link className="btn btn-outline-dark" href={href}>
        {label} <Icon name="arrow" />
      </Link>
    </div>
  );
}

export function PoleCards({ photos }: { photos: Partial<Record<string, string | null>> }) {
  return (
    <div className="poles-grid cols-2">
      {POLES.map((p, i) => (
        <article key={p.key} className={`pole-card reveal${delay(i)}`}>
          <Link className="pole-visual" href={p.href} aria-label={p.name} style={bgStyle("--card-img", photos[p.key])}>
            <span className="pole-num">FILIALE {p.num}</span>
            <Illustration filiale={p.key} />
          </Link>
          <div className="pole-body">
            <span className="eyebrow">{p.sub}</span>
            <h3>{p.name}</h3>
            <p>{p.text}</p>
            <ul className="pole-tags">
              {p.tags.map((t) => (
                <li key={t}>{t}</li>
              ))}
            </ul>
            <Link className="link-arrow" href={p.href}>
              Découvrir {p.name} <Icon name="arrow" />
            </Link>
          </div>
        </article>
      ))}
    </div>
  );
}

export function AboutFrame({ badge, children }: { badge: ReactNode; children?: ReactNode }) {
  return (
    <div className="about-visual reveal reveal-delay-1">
      {children ?? (
        <div className="frame">
          <Pattern className="pattern" />
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/assets/img/logo-mark-white.png" alt="Emblème Maria Group" width={297} height={302} loading="lazy" />
        </div>
      )}
      <div className="frame-border" />
      <div className="about-badge">{badge}</div>
    </div>
  );
}

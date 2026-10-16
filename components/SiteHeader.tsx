"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { Icon } from "@/components/icons";
import { CONTACT, NAV } from "@/lib/content";

const subId = (label: string) => `sub-${label.toLowerCase().replace(/\s+/g, "-")}`;

export function SiteHeader() {
  const pathname = usePathname();
  const [navOpen, setNavOpen] = useState(false);
  const [openSub, setOpenSub] = useState<string | null>(null);
  const [scrolled, setScrolled] = useState(false);
  const headerRef = useRef<HTMLElement>(null);

  // Ferme les menus à chaque changement de page.
  useEffect(() => {
    setNavOpen(false);
    setOpenSub(null);
  }, [pathname]);

  useEffect(() => {
    document.body.classList.toggle("nav-open", navOpen);
    if (navOpen && headerRef.current) {
      const top = headerRef.current.getBoundingClientRect().top;
      document.documentElement.style.setProperty("--topbar-offset", `${Math.max(0, top)}px`);
    }
  }, [navOpen]);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 10);
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setNavOpen(false);
        setOpenSub(null);
      }
    };
    const onClick = (e: MouseEvent) => {
      if (!(e.target as Element).closest(".has-sub")) setOpenSub(null);
    };
    const onResize = () => {
      if (window.innerWidth > 960) setNavOpen(false);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onResize);
    document.addEventListener("keydown", onKey);
    document.addEventListener("click", onClick);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onResize);
      document.removeEventListener("keydown", onKey);
      document.removeEventListener("click", onClick);
    };
  }, []);

  const current = (href: string) => (pathname === href ? "page" : undefined);

  return (
    <>
      <a className="skip-link" href="#contenu">
        Aller au contenu
      </a>

      <div className="topbar">
        <div className="container">
          <div className="topbar-info">
            <a href={`tel:${CONTACT.mobileHref}`}>
              <Icon name="phone" />
              {CONTACT.mobile}
            </a>
            <a className="hide-sm" href={`tel:${CONTACT.fixeHref}`}>
              <Icon name="phone" />
              {CONTACT.fixe}
            </a>
            <a href={`mailto:${CONTACT.email}`}>
              <Icon name="mail" />
              {CONTACT.email}
            </a>
            <span className="hide-md">
              <Icon name="clock" />
              {CONTACT.hours}
            </span>
          </div>
          <div className="topbar-social">
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
      </div>

      <header ref={headerRef} className={`site-header${scrolled ? " is-scrolled" : ""}`}>
        <div className="container">
          <Link className="brand" href="/" aria-label="Maria Group — accueil">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src="/assets/img/logo-mark.png" alt="" width={52} height={53} />
            <span className="brand-text">
              <span className="brand-name">MARIA</span>
              <span className="brand-sub">GROUP</span>
            </span>
          </Link>

          <nav className="main-nav" id="main-nav" aria-label="Navigation principale">
            <ul>
              {NAV.map((item) =>
                "children" in item ? (
                  <li
                    key={item.label}
                    className={[
                      "has-sub",
                      item.children.some((c) => c.href === pathname) ? "is-active" : "",
                      openSub === item.label ? "is-open" : "",
                    ]
                      .filter(Boolean)
                      .join(" ")}
                  >
                    <button
                      className="sub-toggle"
                      type="button"
                      aria-expanded={openSub === item.label}
                      aria-controls={subId(item.label)}
                      onClick={(e) => {
                        e.stopPropagation();
                        setOpenSub(openSub === item.label ? null : item.label);
                      }}
                    >
                      {item.label}
                      <Icon name="chevron" />
                    </button>
                    <ul className="sub-menu" id={subId(item.label)}>
                      {item.children.map((c) => (
                        <li key={c.href}>
                          <Link href={c.href} aria-current={current(c.href)}>
                            {c.label}
                          </Link>
                        </li>
                      ))}
                    </ul>
                  </li>
                ) : (
                  <li key={item.href}>
                    <Link href={item.href} aria-current={current(item.href)}>
                      {item.label}
                    </Link>
                  </li>
                )
              )}
              <li className="nav-cta">
                <Link className="btn btn-primary" href="/contact" aria-current={current("/contact")}>
                  Contacts
                </Link>
              </li>
            </ul>
          </nav>

          <button
            className="nav-toggle"
            type="button"
            aria-controls="main-nav"
            aria-expanded={navOpen}
            aria-label={navOpen ? "Fermer le menu" : "Ouvrir le menu"}
            onClick={() => setNavOpen(!navOpen)}
          >
            <span />
          </button>
        </div>
      </header>
    </>
  );
}

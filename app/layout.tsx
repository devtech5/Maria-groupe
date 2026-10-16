import type { Metadata, Viewport } from "next";
import localFont from "next/font/local";
import { connection } from "next/server";
import type { ReactNode } from "react";
import { Effects } from "@/components/Effects";
import { SiteFooter } from "@/components/SiteFooter";
import { SiteHeader } from "@/components/SiteHeader";
import "./globals.css";

// Polices hébergées avec le site (SIL Open Font License, voir app/fonts/).
const montserrat = localFont({
  src: "./fonts/montserrat-latin.woff2",
  weight: "100 900",
  display: "swap",
  variable: "--font-montserrat",
});
const openSans = localFont({
  src: "./fonts/open-sans-latin.woff2",
  weight: "300 800",
  display: "swap",
  variable: "--font-open-sans",
});

const SITE_URL = process.env.SITE_URL ?? "https://maria-groupe.com";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: { default: "Maria Group — BTP & Mines d'or", template: "%s | Maria Group" },
  description:
    "Maria Group réunit Maria BTP (bâtiment et travaux publics) et Maria Gold (exploration et exploitation aurifère).",
  icons: {
    icon: [
      { url: "/assets/img/favicon-32.png", sizes: "32x32", type: "image/png" },
      { url: "/assets/img/favicon-512.png", sizes: "512x512", type: "image/png" },
    ],
    apple: "/assets/img/apple-touch-icon.png",
  },
  openGraph: { type: "website", siteName: "Maria Group", locale: "fr_FR", images: ["/assets/img/logo.png"] },
};

export const viewport: Viewport = { themeColor: "#162E49" };

export default async function RootLayout({ children }: { children: ReactNode }) {
  // Rendu à chaque requête : nécessaire au nonce de la Content-Security-Policy (voir proxy.ts).
  await connection();
  return (
    <html lang="fr" className={`${montserrat.variable} ${openSans.variable}`}>
      <body>
        <SiteHeader />
        <main id="contenu">{children}</main>
        <SiteFooter />
        <Effects />
      </body>
    </html>
  );
}

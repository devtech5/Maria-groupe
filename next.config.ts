import type { NextConfig } from "next";

// Anciennes adresses du site statique (.html) redirigées vers les nouvelles routes.
const LEGACY_PAGES = ["groupe", "btp", "gold", "projets", "realisations", "contact", "mentions-legales"];

const nextConfig: NextConfig = {
  output: "standalone",
  poweredByHeader: false,
  async redirects() {
    return [
      { source: "/index.html", destination: "/", permanent: true },
      ...LEGACY_PAGES.map((page) => ({ source: `/${page}.html`, destination: `/${page}`, permanent: true })),
    ];
  },
  async headers() {
    return [
      {
        source: "/assets/:path*",
        headers: [{ key: "Cache-Control", value: "public, max-age=604800" }],
      },
    ];
  },
};

export default nextConfig;

import fs from "node:fs";
import path from "node:path";

/**
 * Photo optionnelle déposée dans public/assets/img/photos/.
 * Renvoie son URL si le fichier existe, sinon null (l'illustration par défaut s'affiche).
 */
export function photo(name: string): string | null {
  const file = path.join(process.cwd(), "public", "assets", "img", "photos", name);
  return fs.existsSync(file) ? `/assets/img/photos/${name}` : null;
}

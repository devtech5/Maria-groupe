import { NextResponse } from "next/server";
import { getPool } from "@/lib/db";

export const dynamic = "force-dynamic";

/* État de la connexion à la base. */
export async function GET() {
  const pool = getPool();
  if (!pool) return NextResponse.json({ ok: false, db: "non configurée" }, { status: 503 });
  try {
    await pool.query("SELECT 1");
    return NextResponse.json({ ok: true, db: "connectée" });
  } catch {
    return NextResponse.json({ ok: false, db: "injoignable" }, { status: 503 });
  }
}

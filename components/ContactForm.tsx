"use client";

import { useRef, useState, type FormEvent } from "react";
import { Icon } from "@/components/icons";
import { FILIALES_CONTACT } from "@/lib/contact";

type Field = "nom" | "email" | "pole" | "message" | "consent";
type Status = { kind: "success" | "error"; text: string } | null;

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function findErrors(form: HTMLFormElement): Set<Field> {
  const v = (name: string) => ((form.elements.namedItem(name) as HTMLInputElement | null)?.value ?? "").trim();
  const errors = new Set<Field>();
  if (!v("nom")) errors.add("nom");
  if (!EMAIL_RE.test(v("email"))) errors.add("email");
  if (!v("pole")) errors.add("pole");
  if (v("message").length < 5) errors.add("message");
  if (!(form.elements.namedItem("consent") as HTMLInputElement).checked) errors.add("consent");
  return errors;
}

export function ContactForm() {
  const formRef = useRef<HTMLFormElement>(null);
  const [errors, setErrors] = useState<Set<Field>>(new Set());
  const [status, setStatus] = useState<Status>(null);
  const [sending, setSending] = useState(false);

  const fieldClass = (name: Field, extra = "") => `field${extra}${errors.has(name) ? " has-error" : ""}`;
  const invalid = (name: Field) => (errors.has(name) ? true : undefined);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const form = e.currentTarget;
    setStatus(null);

    const found = findErrors(form);
    setErrors(found);
    if (found.size) {
      setStatus({ kind: "error", text: "Merci de compléter correctement les champs obligatoires." });
      const first = form.querySelector<HTMLElement>(`[name="${[...found][0]}"]`);
      first?.focus();
      return;
    }

    const payload: Record<string, unknown> = Object.fromEntries(new FormData(form).entries());
    payload.consent = true;

    setSending(true);
    try {
      const res = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(payload),
      });
      if (res.status === 429) throw new Error("Trop de demandes envoyées. Merci de réessayer dans quelques minutes.");
      if (!res.ok) throw new Error();
      form.reset();
      setStatus({ kind: "success", text: "Merci ! Votre message a bien été envoyé. Nous vous répondrons rapidement." });
    } catch (err) {
      setStatus({
        kind: "error",
        text:
          (err as Error).message ||
          "Une erreur est survenue. Veuillez réessayer ou nous écrire directement par e-mail.",
      });
    } finally {
      setSending(false);
    }
  }

  function onBlur(name: Field) {
    if (!formRef.current) return;
    const found = findErrors(formRef.current);
    setErrors((prev) => {
      const next = new Set(prev);
      if (found.has(name)) next.add(name);
      else next.delete(name);
      return next;
    });
  }

  return (
    <form ref={formRef} id="contact-form" noValidate onSubmit={onSubmit}>
      <div className="form-grid">
        <div className={fieldClass("nom")}>
          <label htmlFor="nom">Nom &amp; prénom <span className="req">*</span></label>
          <input id="nom" name="nom" type="text" autoComplete="name" maxLength={120} required aria-invalid={invalid("nom")} onBlur={() => onBlur("nom")} />
          <span className="error-msg">Veuillez indiquer votre nom.</span>
        </div>
        <div className="field">
          <label htmlFor="societe">Société</label>
          <input id="societe" name="societe" type="text" autoComplete="organization" maxLength={160} />
        </div>
        <div className={fieldClass("email")}>
          <label htmlFor="email">E-mail <span className="req">*</span></label>
          <input id="email" name="email" type="email" autoComplete="email" maxLength={200} required aria-invalid={invalid("email")} onBlur={() => onBlur("email")} />
          <span className="error-msg">Veuillez indiquer une adresse e-mail valide.</span>
        </div>
        <div className="field">
          <label htmlFor="telephone">Téléphone</label>
          <input id="telephone" name="telephone" type="tel" autoComplete="tel" maxLength={40} />
        </div>
        <div className={fieldClass("pole", " full")}>
          <label htmlFor="pole">Filiale concernée <span className="req">*</span></label>
          <select id="pole" name="pole" required defaultValue="" aria-invalid={invalid("pole")} onBlur={() => onBlur("pole")}>
            <option value="">— Sélectionnez —</option>
            {FILIALES_CONTACT.map((f) => (
              <option key={f}>{f}</option>
            ))}
          </select>
          <span className="error-msg">Veuillez sélectionner une filiale.</span>
        </div>
        <div className={fieldClass("message", " full")}>
          <label htmlFor="message">Votre message <span className="req">*</span></label>
          <textarea id="message" name="message" maxLength={5000} required aria-invalid={invalid("message")} onBlur={() => onBlur("message")} />
          <span className="error-msg">Veuillez décrire votre demande.</span>
        </div>
        <div className={fieldClass("consent", " full")}>
          <label className="form-consent" htmlFor="consent">
            <input id="consent" name="consent" type="checkbox" required aria-invalid={invalid("consent")} />
            <span>J&apos;accepte que mes données soient utilisées pour traiter ma demande. <span className="req">*</span></span>
          </label>
          <span className="error-msg">Votre accord est nécessaire.</span>
        </div>
        <div className="hp-field" aria-hidden="true">
          <label htmlFor="website">Site web</label>
          <input id="website" name="website" type="text" tabIndex={-1} autoComplete="off" />
        </div>
        <div className="full">
          <button className="btn btn-primary" type="submit" disabled={sending}>
            {sending ? "Envoi en cours…" : "Envoyer ma demande"} <Icon name="arrow" />
          </button>
        </div>
      </div>
      <div className={`form-status${status ? ` is-${status.kind}` : ""}`} role="status" aria-live="polite">
        {status?.text}
      </div>
    </form>
  );
}

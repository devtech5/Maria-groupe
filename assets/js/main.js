/* MARIA GROUP — scripts du site */
(function () {
  "use strict";

  var body = document.body;
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("main-nav");
  var toTop = document.querySelector(".to-top");

  /* ---- Menu mobile ---- */
  function closeNav() {
    body.classList.remove("nav-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
  }
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      if (open) {
        var top = header.getBoundingClientRect().top;
        document.documentElement.style.setProperty("--topbar-offset", Math.max(0, top) + "px");
      }
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeNav();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 960) closeNav();
    });
  }

  /* ---- En-tête au défilement + bouton retour en haut ---- */
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle("is-scrolled", y > 10);
    if (toTop) toTop.classList.toggle("is-visible", y > 600);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (toTop) {
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---- Apparition au défilement ---- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---- Compteurs animés ---- */
  var counters = document.querySelectorAll("[data-count]");
  function animateCounter(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    var duration = 1600;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if (counters.length && "IntersectionObserver" in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          co.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { co.observe(el); });
  }

  /* ---- Filtre des réalisations ---- */
  var filterBar = document.querySelector("[data-filter-bar]");
  if (filterBar) {
    var items = document.querySelectorAll("[data-category]");
    filterBar.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-filter]");
      if (!btn) return;
      var f = btn.getAttribute("data-filter");
      filterBar.querySelectorAll("button").forEach(function (b) {
        b.classList.toggle("is-active", b === btn);
        b.setAttribute("aria-pressed", b === btn ? "true" : "false");
      });
      items.forEach(function (item) {
        var show = f === "all" || item.getAttribute("data-category") === f;
        item.hidden = !show;
      });
    });
  }

  /* ---- Formulaire de contact ---- */
  var form = document.getElementById("contact-form");
  if (form) {
    var status = form.querySelector(".form-status");
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    function validateField(field) {
      var input = field.querySelector("input, select, textarea");
      if (!input) return true;
      var val = (input.value || "").trim();
      var ok = true;
      if (input.required && !val) ok = false;
      if (ok && input.type === "email" && val && !emailRe.test(val)) ok = false;
      if (input.type === "checkbox" && input.required) ok = input.checked;
      field.classList.toggle("has-error", !ok);
      input.setAttribute("aria-invalid", ok ? "false" : "true");
      return ok;
    }

    form.querySelectorAll(".field").forEach(function (field) {
      var input = field.querySelector("input, select, textarea");
      if (input) input.addEventListener("blur", function () { validateField(field); });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "form-status";
      status.textContent = "";

      var valid = true;
      form.querySelectorAll(".field").forEach(function (field) {
        if (!validateField(field)) valid = false;
      });
      var consent = form.querySelector("#consent");
      if (consent && !consent.checked) valid = false;

      if (!valid) {
        status.classList.add("is-error");
        status.textContent = "Merci de compléter correctement les champs obligatoires.";
        var firstErr = form.querySelector(".has-error input, .has-error select, .has-error textarea");
        if (firstErr) firstErr.focus();
        return;
      }
      if (form.querySelector(".hp-field input").value) return; // anti-spam

      var data = new FormData(form);
      var endpoint = form.getAttribute("data-endpoint");

      if (endpoint) {
        /* Envoi via un service de formulaire (ex. Formspree) */
        var btn = form.querySelector("button[type=submit]");
        btn.disabled = true;
        fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } })
          .then(function (r) {
            if (!r.ok) throw new Error();
            form.reset();
            status.classList.add("is-success");
            status.textContent = "Merci ! Votre message a bien été envoyé. Nous vous répondrons rapidement.";
          })
          .catch(function () {
            status.classList.add("is-error");
            status.textContent = "Une erreur est survenue. Veuillez réessayer ou nous écrire directement par e-mail.";
          })
          .finally(function () { btn.disabled = false; });
      } else {
        /* Repli : ouverture du client e-mail */
        var to = form.getAttribute("data-mailto");
        var subject = "[Site web] " + (data.get("pole") || "Demande") + " — " + data.get("nom");
        var lines = [
          "Nom : " + data.get("nom"),
          "Société : " + (data.get("societe") || "-"),
          "E-mail : " + data.get("email"),
          "Téléphone : " + (data.get("telephone") || "-"),
          "Pôle concerné : " + data.get("pole"),
          "",
          data.get("message")
        ];
        window.location.href = "mailto:" + to + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
        status.classList.add("is-success");
        status.textContent = "Votre logiciel de messagerie va s'ouvrir pour finaliser l'envoi.";
      }
    });
  }

  /* ---- Année du copyright ---- */
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();

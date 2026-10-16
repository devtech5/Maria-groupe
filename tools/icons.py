"""Icônes SVG (trait 24x24, couleur héritée)."""

def _svg(inner, vb="0 0 24 24"):
    return (f'<svg viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg>')

I = {
    "chevron": _svg('<path d="M6 9l6 6 6-6"/>'),
    "ingot": _svg('<path d="M2 20l2.5-5h7L14 20zM10 20l2.5-5h7L22 20zM6 15l2.5-5h7L18 15"/><path d="M19 3v3M17.5 4.5h3"/>'),
    "arrow": _svg('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    "up": _svg('<path d="M12 19V5M6 11l6-6 6 6"/>'),
    "check": _svg('<path d="M5 12.5l4.5 4.5L19 7.5"/>'),
    "phone": _svg('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>'),
    "mail": _svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'),
    "pin": _svg('<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'),
    "clock": _svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    "building": _svg('<path d="M4 21V6l8-3v18M12 21V9l8 3v9M2 21h20"/><path d="M7 8v.01M7 11v.01M7 14v.01M7 17v.01M16 14v.01M16 17v.01"/>'),
    "crane": _svg('<path d="M6 21V4M6 4h14M6 4l-3 3M9 4l-3 4M20 4v5M18 9h4v3h-4zM3 21h7M6 7h3"/><path d="M14 4L6 10"/>'),
    "pickaxe": _svg('<path d="M14.5 9.5L4 20M3 8.5C7 3 15 2 21 7M15.5 3C21 7 22 15 16.5 21"/><path d="M12 5l7 7"/>'),
    "mountain": _svg('<path d="M2 20l7-12 4 6 3-4 6 10z"/><path d="M7.5 10.5L9 12l1.5-1.5"/>'),
    "gem": _svg('<path d="M6 3h12l4 6-10 12L2 9z"/><path d="M2 9h20M9 3l3 18M15 3l-3 18"/>'),
    "truck": _svg('<path d="M2 6h12v10H2zM14 9h4l4 4v3h-8"/><circle cx="6.5" cy="17.5" r="2"/><circle cx="17.5" cy="17.5" r="2"/>'),
    "route": _svg('<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8a3 3 0 0 0 0-6H8a3 3 0 0 1 0-6h8"/>'),
    "warehouse": _svg('<path d="M3 21V9l9-5 9 5v12"/><path d="M7 21v-8h10v8M7 17h10"/>'),
    "container": _svg('<rect x="2" y="7" width="20" height="11" rx="1"/><path d="M6 7v11M10 7v11M14 7v11M18 7v11"/>'),
    "road": _svg('<path d="M8 3L4 21M16 3l4 18M12 4v2M12 10v3M12 17v3"/>'),
    "bridge": _svg('<path d="M2 17h20M4 17v4M20 17v4M2 13c4 0 6-6 10-6s6 6 10 6M8 9.5V17M16 9.5V17M12 7v10"/>'),
    "hammer": _svg('<path d="M14 6l4 4M3 21l9-9M13 5l2-2 6 6-2 2-2-1-2 2-4-4 2-2z"/>'),
    "ruler": _svg('<path d="M3 17L17 3l4 4L7 21z"/><path d="M7 13l2 2M10 10l2 2M13 7l2 2"/>'),
    "drill": _svg('<path d="M12 2v4M8 6h8l-1 6H9zM10 12l2 10 2-10"/>'),
    "flask": _svg('<path d="M9 3h6M10 3v6L4.5 19a1.5 1.5 0 0 0 1.3 2h12.4a1.5 1.5 0 0 0 1.3-2L14 9V3"/><path d="M7 15h10"/>'),
    "shield": _svg('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>'),
    "award": _svg('<circle cx="12" cy="9" r="6"/><path d="M8.5 13.5L7 22l5-3 5 3-1.5-8.5"/>'),
    "handshake": _svg('<path d="M2 11l4-4 4 2 3-2 4 1 5 3M2 11l6 6a2 2 0 0 0 3 0l1-1M22 10l-5 5-3-3"/><path d="M11 16l2 2a2 2 0 0 0 3-3"/>'),
    "bulb": _svg('<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.8.8 1 1.5 1 2.5h6c0-1 .2-1.7 1-2.5A6 6 0 0 0 12 3z"/>'),
    "leaf": _svg('<path d="M5 19C5 10 10 4 20 4c0 10-6 15-15 15z"/><path d="M5 19l8-8"/>'),
    "users": _svg('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.5a5 5 0 0 1 5.5 5"/>'),
    "target": _svg('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>'),
    "eye": _svg('<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>'),
    "globe": _svg('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>'),
    "gauge": _svg('<path d="M4 18a9 9 0 1 1 16 0"/><path d="M12 14l4-5"/><circle cx="12" cy="14" r="1.2"/>'),
    "clipboard": _svg('<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 11h6M9 15h4"/>'),
    "layers": _svg('<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>'),
    "excavator": _svg('<path d="M2 18h11v-5H6l-2 2v3M8 13V9h4l1 4"/><path d="M13 11l4-6 4 3-2 4"/><path d="M19 12l2 3h-3"/><circle cx="5" cy="19.5" r="1"/><circle cx="10" cy="19.5" r="1"/>'),
    "facebook": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8.5V6.8c0-.8.5-1 1-1h2.2V2.1L14.2 2C11 2 10.3 4.4 10.3 5.9v2.6H8v3.8h2.3V22H14v-9.7h2.9l.4-3.8z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.5 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM3 8.8h3V21H3zM8.6 8.8h2.9v1.7c.5-.9 1.7-2 3.6-2 3.8 0 4.5 2.5 4.5 5.8V21h-3v-6c0-1.4 0-3.3-2-3.3s-2.3 1.6-2.3 3.2V21h-3z"/></svg>',
    "instagram": _svg('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/>'),
    "whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/></svg>',
}

# Grandes illustrations (traits dorés) pour les visuels des pôles
ILLUS = {
    "btp": '''<svg class="pole-illus" viewBox="0 0 200 160" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M10 150h180"/>
  <path d="M40 150V60h46v90M86 150V90h44v60M130 150V40h40v110"/>
  <path d="M52 74h8M68 74h8M52 92h8M68 92h8M52 110h8M68 110h8M52 128h8M68 128h8"/>
  <path d="M98 104h8M112 104h8M98 122h8M112 122h8"/>
  <path d="M140 54h8M154 54h8M140 72h8M154 72h8M140 90h8M154 90h8M140 108h8M154 108h8M140 126h8M154 126h8"/>
  <path d="M22 150V14M22 14h110M22 14l-12 12M22 32l18-18M40 14l-18 18M58 14L40 32M76 14L58 32"/>
  <path d="M110 14v26M104 40h12v10h-12z" opacity=".8"/>
</svg>''',
    "gold": '''<svg class="pole-illus" viewBox="0 0 200 160" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path d="M6 150h188"/>
  <path d="M10 150l46-84 28 40 20-26 40 70"/>
  <path d="M46 84l10-18 10 14"/>
  <path d="M58 150v-22a16 16 0 0 1 32 0v22"/>
  <path d="M146 150l4-12h16l4 12zM172 150l4-12h16l4 12zM159 138l4-12h16l4 12z"/>
  <path d="M188 104v12M182 110h12M140 112v8M136 116h8" opacity=".8"/>
  <path d="M152 34L124 62M130 26c10-4 24-2 32 8M160 56c4-10 2-24-8-32"/>
</svg>''',
}

# Motif de lignes (inspiré des traits du logo) pour les fonds sombres
PATTERN = '''<svg class="hero-pattern" viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice" fill="none" aria-hidden="true">
  <g stroke="#BFA169" stroke-width="1" opacity=".35">
    <path d="M760 760L1060 -60M800 760L1100 -60M840 760L1140 -60"/>
    <path d="M980 760L1280 -60M1020 760L1320 -60"/>
  </g>
  <circle cx="1020" cy="350" r="300" stroke="#BFA169" stroke-width="1.2" opacity=".28"/>
  <circle cx="1020" cy="350" r="230" stroke="#ffffff" stroke-width="1" opacity=".08"/>
</svg>'''

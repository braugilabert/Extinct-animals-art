"""Une papel, paisaje, rama y especie en una única lámina SVG (4:5, formato
de Instagram)."""
from __future__ import annotations

import hashlib
import random
from xml.sax.saxutils import escape

from .brush import darken, deckle_rect, lighten, paper_grain, speckle_field, sun_glow
from .landscapes import LANDSCAPES
from .palettes import PALETTES
from .scene import blooms, perch
from .species import SPECIES

CANVAS_W, CANVAS_H = 400, 500          # 4:5 -> 1080x1350 px a width=1080
CARD = (20, 20, 340, 450)              # zona pintada (x, y, ancho, alto)
OFFSET = (10, 0)                       # centra la zona pintada sobre el papel
FONT = "Georgia, 'Times New Roman', serif"


def rng_factory(seed):
    """Un generador aleatorio independiente por capa, estable para una semilla."""
    def rng_for(name: str) -> random.Random:
        return random.Random(f"{seed}:{name}")
    return rng_for


def _choose_landscape(meta, explicit: str | None, seed: int) -> str:
    """Elige un fondo reproducible cuando la ficha solo dice ``generic``."""
    if explicit:
        return explicit
    preferred = meta.get("landscape", "generic")
    if preferred != "generic":
        return preferred
    # La ficha ya contiene el contexto ecológico; úsalo antes de recurrir a
    # una elección aleatoria. Así una especie marina no acaba siempre en el
    # mismo paisaje montañoso que un mamífero de bosque.
    context = " ".join(str(meta.get(k, "")) for k in ("habitat", "distribution", "description", "visual_notes")).lower()
    if any(word in context for word in ("marino", "marina", "costa", "isla de bering", "atlántico", "playa", "oceán")):
        return "costa"
    if any(word in context for word in ("humedal", "marisma", "laguna", "pantano", "ribera", "río", "limícola", "garza", "pato", "oca")):
        return "humedal"
    if any(word in context for word in ("bosque", "selva", "monte húmedo", "vegetación densa", "forestal")):
        return "bosque"
    # Las especies antiguas se benefician de un fondo variado, pero la misma
    # semilla sigue produciendo siempre el mismo resultado.
    options = ("generic", "humedal", "costa", "bosque")
    token = f'{meta.get("slug", "species")}:{seed}'.encode("utf-8")
    index = int(hashlib.sha256(token).hexdigest()[:8], 16) % len(options)
    return options[index]


def build_svg(species: str = "ara_gossei", palette: str = "acuarela_antigua",
              landscape: str | None = None, seed: int = 7, caption: bool = True,
              grain: bool = True, flower: bool = True) -> str:
    if species not in SPECIES:
        raise KeyError(f"Especie desconocida: {species}. Disponibles: {', '.join(SPECIES)}")
    if palette not in PALETTES:
        raise KeyError(f"Paleta desconocida: {palette}. Disponibles: {', '.join(PALETTES)}")

    module = SPECIES[species]
    meta = module.META
    pal = PALETTES[palette]
    land_key = _choose_landscape(meta, landscape, seed)
    if land_key not in LANDSCAPES:
        raise KeyError(f"Paisaje desconocido: {land_key}. Disponibles: {', '.join(LANDSCAPES)}")
    land = LANDSCAPES[land_key]
    rng_for = rng_factory(seed)

    x, y, w, h = CARD
    paint_edge = deckle_rect(x, y, w, h, rng_for("deckle"))
    title = f'{meta["scientific_name"]} ({meta["common_name"]})'
    research_desc = " ".join(
        f"{label}: {meta[key]}."
        for key, label in (
            ("status", "Estado"),
            ("distribution", "Distribución"),
            ("habitat", "Hábitat"),
            ("visual_notes", "Rasgos visuales"),
            ("drawing_notes", "Guia de dibujo"),
            ("reference_taxa", "Comparaciones prudentes"),
            ("reference_images", "Referencias visuales locales"),
        )
        if meta.get(key)
    )
    accessible_desc = meta.get("description", f"Ilustración tipo acuarela de {title}.")
    if research_desc:
        accessible_desc = f"{accessible_desc} {research_desc}"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CANVAS_W} {CANVAS_H}" '
        f'width="{CANVAS_W * 2}" height="{CANVAS_H * 2}" role="img">',
        f"<title>{escape(title)}</title>",
        f"<desc>{escape(accessible_desc)}</desc>",
        "<defs>",
        f'<clipPath id="paint"><path d="{paint_edge}"/></clipPath>',
        '<radialGradient id="paperglow" cx="0.5" cy="0.45" r="0.75">'
        f'<stop offset="0" stop-color="{lighten(pal["paper"], 0.5)}" stop-opacity="0.55"/>'
        f'<stop offset="1" stop-color="{darken(pal["paper"], 0.25)}" stop-opacity="0.25"/>'
        "</radialGradient>",
        "</defs>",
        f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="{pal["paper"]}"/>',
        f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="url(#paperglow)"/>',
        f'<g transform="translate({OFFSET[0]} {OFFSET[1]})">',
        '<g clip-path="url(#paint)">',
        land["backdrop"](pal, rng_for),
        sun_glow(300, 74, 18, pal["mist"], rng_for("ambient-glow")),
        speckle_field(25, 30, 330, 330, pal["bloom_a"], rng_for("ambient-speckles"),
                      count=18, opacity=(.025, .07), radius=(.3, 1.2)),
        blooms(pal, rng_for),
        land["foliage"](pal, rng_for),
        perch(pal, rng_for, flower=flower),
        module.draw(rng_for),
        "</g>",
        f'<path d="{paint_edge}" fill="none" stroke="{darken(pal["paper"], 0.35)}" '
        'stroke-width="0.8" stroke-opacity="0.35" stroke-linejoin="round"/>',
        "</g>",
    ]
    if grain:
        parts.append(paper_grain(CANVAS_W, CANVAS_H, pal["paper"], rng_for("grain")))
    if caption:
        text = f'{meta["scientific_name"]} · {land["label"]}'
        parts.append(
            f'<text x="{CANVAS_W / 2}" y="489" text-anchor="middle" font-size="12" '
            f'font-style="italic" font-family="{FONT}" fill="{pal["caption"]}">'
            f"{escape(text)}</text>"
        )
    parts.append("</svg>")
    return "\n".join(parts)

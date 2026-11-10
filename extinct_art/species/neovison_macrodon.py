"""Ficha visual de Neovison macrodon — Visón marino."""
from .base import draw_taxon

META = {
    "slug": "neovison_macrodon",
    "scientific_name": "Neovison macrodon",
    "common_name": "Visón marino",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; finales XIX o comienzos XX",
    "description": "Interpretación artística de Neovison macrodon, Visón marino. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/neovison_macrodon.md",
    "source_url": "https://www.gbif.org/species/search?q=Neovison%20macrodon",
    "distribution": "costa de Maine a Nuevo Brunswick",
    "habitat": "costa rocosa",
    "visual_notes": "mustélido grande, unos 91 cm, pelaje pardo rojizo oscuro",
    "extinction_notes": "caza por piel; especie discutida frente a N. vison",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.86}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)


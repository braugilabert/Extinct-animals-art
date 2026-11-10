"""Ficha visual de Pinguinus impennis — Alca gigante."""
from .base import draw_taxon

META = {
    "slug": "pinguinus_impennis",
    "scientific_name": "Pinguinus impennis",
    "common_name": "Alca gigante",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; 1844",
    "description": "Interpretación artística de Pinguinus impennis, Alca gigante. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pinguinus_impennis.md",
    "source_url": "https://www.gbif.org/species/search?q=Pinguinus%20impennis",
    "distribution": "Atlántico norte",
    "habitat": "costa rocosa e islas de cría",
    "visual_notes": "álcido grande negro y blanco, pico alto y alas reducidas",
    "extinction_notes": "caza por carne, huevos y pieles",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.08,"long_beak":True,"white_body":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)


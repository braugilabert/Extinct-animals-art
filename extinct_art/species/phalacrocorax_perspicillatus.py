"""Ficha visual de Phalacrocorax perspicillatus — Cormorán de Pallas."""
from .base import draw_taxon

META = {
    "slug": "phalacrocorax_perspicillatus",
    "scientific_name": "Phalacrocorax perspicillatus",
    "common_name": "Cormorán de Pallas",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; 1852",
    "description": "Interpretación artística de Phalacrocorax perspicillatus, Cormorán de Pallas. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/phalacrocorax_perspicillatus.md",
    "source_url": "https://www.gbif.org/species/search?q=Phalacrocorax%20perspicillatus",
    "distribution": "isla de Bering",
    "habitat": "costa subártica",
    "visual_notes": "cormorán gigante de vuelo limitado",
    "extinction_notes": "caza por carne y huevos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


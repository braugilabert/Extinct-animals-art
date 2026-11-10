"""Ficha visual de Dromaius novaehollandiae minor — Emú de la isla Kangaroo."""
from .base import draw_taxon

META = {
    "slug": "dromaius_novaehollandiae_minor",
    "scientific_name": "Dromaius novaehollandiae minor",
    "common_name": "Emú de la isla Kangaroo",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Dromaius novaehollandiae minor, Emú de la isla Kangaroo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dromaius_novaehollandiae_minor.md",
    "source_url": "https://www.gbif.org/species/search?q=Dromaius%20novaehollandiae%20minor",
    "distribution": "isla King",
    "habitat": "matorral y bosque",
    "visual_notes": "emú insular aproximadamente de mitad de tamaño",
    "extinction_notes": "caza, incendios y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.3,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)


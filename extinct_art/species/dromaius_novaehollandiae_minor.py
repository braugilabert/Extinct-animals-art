"""Ficha visual de Dromaius novaehollandiae minor — Emú de la isla Kangaroo."""
from .base import draw_taxon

META = {
    "slug": "dromaius_novaehollandiae_minor",
    "scientific_name": "Dromaius novaehollandiae minor",
    "common_name": "Emú de la isla Kangaroo",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Dromaius novaehollandiae minor, Emú de la isla Kangaroo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dromaius_novaehollandiae_minor.md",
    "source_url": "https://www.gbif.org/species/search?q=Dromaius%20novaehollandiae%20minor",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


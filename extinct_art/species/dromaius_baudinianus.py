"""Ficha visual de Dromaius baudinianus — Emú de la isla King."""
from .base import draw_taxon

META = {
    "slug": "dromaius_baudinianus",
    "scientific_name": "Dromaius baudinianus",
    "common_name": "Emú de la isla King",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; sin registros desde 1819",
    "description": "Interpretación artística de Dromaius baudinianus, Emú de la isla King. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dromaius_baudinianus.md",
    "source_url": "https://www.gbif.org/species/search?q=Dromaius%20baudinianus",
    "distribution": "isla Kangaroo",
    "habitat": "matorral y bosque",
    "visual_notes": "emú insular robusto",
    "extinction_notes": "caza y fuegos frecuentes",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


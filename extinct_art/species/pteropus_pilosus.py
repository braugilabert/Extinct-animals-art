"""Ficha visual de Pteropus pilosus — Zorro volador de Guam."""
from .base import draw_taxon

META = {
    "slug": "pteropus_pilosus",
    "scientific_name": "Pteropus pilosus",
    "common_name": "Zorro volador de Guam",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Pteropus pilosus, Zorro volador de Guam. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pteropus_pilosus.md",
    "source_url": "https://www.gbif.org/species/search?q=Pteropus%20pilosus",
    "distribution": "Guam",
    "habitat": "bosque tropical",
    "visual_notes": "zorro volador grande",
    "extinction_notes": "caza y pérdida de bosque; validez por revisar",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


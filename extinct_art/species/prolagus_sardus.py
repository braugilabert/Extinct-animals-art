"""Ficha visual de Prolagus sardus — Pika sarda."""
from .base import draw_taxon

META = {
    "slug": "prolagus_sardus",
    "scientific_name": "Prolagus sardus",
    "common_name": "Pika sarda",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; fecha incierta",
    "description": "Interpretación artística de Prolagus sardus, Pika sarda. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/prolagus_sardus.md",
    "source_url": "https://www.gbif.org/species/search?q=Prolagus%20sardus",
    "distribution": "Cerdeña y Córcega",
    "habitat": "matorral mediterráneo",
    "visual_notes": "lagomorfo robusto de orejas cortas",
    "extinction_notes": "caza, competencia e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)


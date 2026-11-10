"""Ficha visual de Prolagus sardus — Pika sarda."""
from .base import draw_taxon

META = {
    "slug": "prolagus_sardus",
    "scientific_name": "Prolagus sardus",
    "common_name": "Pika sarda",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Prolagus sardus, Pika sarda. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/prolagus_sardus.md",
    "source_url": "https://www.gbif.org/species/search?q=Prolagus%20sardus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


"""Ficha visual de Bos primigenius primigenius — Uro."""
from .base import draw_taxon

META = {
    "slug": "bos_primigenius_primigenius",
    "scientific_name": "Bos primigenius primigenius",
    "common_name": "Uro",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Bos primigenius primigenius, Uro. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/bos_primigenius_primigenius.md",
    "source_url": "https://www.gbif.org/species/search?q=Bos%20primigenius%20primigenius",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


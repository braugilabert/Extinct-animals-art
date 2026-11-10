"""Ficha visual de Nycticorax mauritianus — Garza nocturna de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "nycticorax_mauritianus",
    "scientific_name": "Nycticorax mauritianus",
    "common_name": "Garza nocturna de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Nycticorax mauritianus, Garza nocturna de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/nycticorax_mauritianus.md",
    "source_url": "https://www.gbif.org/species/search?q=Nycticorax%20mauritianus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


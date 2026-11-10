"""Ficha visual de Necropsittacus rodricanus — Loro de Rodrigues."""
from .base import draw_taxon

META = {
    "slug": "necropsittacus_rodricanus",
    "scientific_name": "Necropsittacus rodricanus",
    "common_name": "Loro de Rodrigues",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Necropsittacus rodricanus, Loro de Rodrigues. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/necropsittacus_rodricanus.md",
    "source_url": "https://www.gbif.org/species/search?q=Necropsittacus%20rodricanus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


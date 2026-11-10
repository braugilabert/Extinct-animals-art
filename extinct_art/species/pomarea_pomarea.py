"""Ficha visual de Pomarea pomarea — Monarca de Maupiti."""
from .base import draw_taxon

META = {
    "slug": "pomarea_pomarea",
    "scientific_name": "Pomarea pomarea",
    "common_name": "Monarca de Maupiti",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Pomarea pomarea, Monarca de Maupiti. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pomarea_pomarea.md",
    "source_url": "https://www.gbif.org/species/search?q=Pomarea%20pomarea",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


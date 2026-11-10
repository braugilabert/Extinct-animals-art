"""Ficha visual de Mascarenotus grucheti — Autillo de Reunión."""
from .base import draw_taxon

META = {
    "slug": "mascarenotus_grucheti",
    "scientific_name": "Mascarenotus grucheti",
    "common_name": "Autillo de Reunión",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Mascarenotus grucheti, Autillo de Reunión. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/mascarenotus_grucheti.md",
    "source_url": "https://www.gbif.org/species/search?q=Mascarenotus%20grucheti",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


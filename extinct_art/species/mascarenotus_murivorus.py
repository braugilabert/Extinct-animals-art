"""Ficha visual de Mascarenotus murivorus — Autillo de Rodrigues."""
from .base import draw_taxon

META = {
    "slug": "mascarenotus_murivorus",
    "scientific_name": "Mascarenotus murivorus",
    "common_name": "Autillo de Rodrigues",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Mascarenotus murivorus, Autillo de Rodrigues. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/mascarenotus_murivorus.md",
    "source_url": "https://www.gbif.org/species/search?q=Mascarenotus%20murivorus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


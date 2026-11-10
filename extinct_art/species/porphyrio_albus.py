"""Ficha visual de Porphyrio albus — Calamón blanco."""
from .base import draw_taxon

META = {
    "slug": "porphyrio_albus",
    "scientific_name": "Porphyrio albus",
    "common_name": "Calamón blanco",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Porphyrio albus, Calamón blanco. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/porphyrio_albus.md",
    "source_url": "https://www.gbif.org/species/search?q=Porphyrio%20albus",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


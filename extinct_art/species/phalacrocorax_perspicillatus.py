"""Ficha visual de Phalacrocorax perspicillatus — Cormorán de Pallas."""
from .base import draw_taxon

META = {
    "slug": "phalacrocorax_perspicillatus",
    "scientific_name": "Phalacrocorax perspicillatus",
    "common_name": "Cormorán de Pallas",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Phalacrocorax perspicillatus, Cormorán de Pallas. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/phalacrocorax_perspicillatus.md",
    "source_url": "https://www.gbif.org/species/search?q=Phalacrocorax%20perspicillatus",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


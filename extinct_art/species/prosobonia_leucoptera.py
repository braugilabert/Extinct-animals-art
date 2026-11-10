"""Ficha visual de Prosobonia leucoptera — Correlimos de Tahití."""
from .base import draw_taxon

META = {
    "slug": "prosobonia_leucoptera",
    "scientific_name": "Prosobonia leucoptera",
    "common_name": "Correlimos de Tahití",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Prosobonia leucoptera, Correlimos de Tahití. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/prosobonia_leucoptera.md",
    "source_url": "https://www.gbif.org/species/search?q=Prosobonia%20leucoptera",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


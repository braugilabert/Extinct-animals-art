"""Ficha visual de Dusicyon australis — Zorro/lobo de las Malvinas."""
from .base import draw_taxon

META = {
    "slug": "dusicyon_australis",
    "scientific_name": "Dusicyon australis",
    "common_name": "Zorro/lobo de las Malvinas",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Dusicyon australis, Zorro/lobo de las Malvinas. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dusicyon_australis.md",
    "source_url": "https://www.gbif.org/species/search?q=Dusicyon%20australis",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


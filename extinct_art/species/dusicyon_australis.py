"""Ficha visual de Dusicyon australis — Zorro/lobo de las Malvinas."""
from .base import draw_taxon

META = {
    "slug": "dusicyon_australis",
    "scientific_name": "Dusicyon australis",
    "common_name": "Zorro/lobo de las Malvinas",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; 1876",
    "description": "Interpretación artística de Dusicyon australis, Zorro/lobo de las Malvinas. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dusicyon_australis.md",
    "source_url": "https://www.gbif.org/species/search?q=Dusicyon%20australis",
    "distribution": "islas Malvinas",
    "habitat": "turbera, playa, llanura y roquedo",
    "visual_notes": "cánido mediano; pelaje pardo y punta de cola blanca",
    "extinction_notes": "caza por piel y protección del ganado",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


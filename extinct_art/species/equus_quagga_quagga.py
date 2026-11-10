"""Ficha visual de Equus quagga quagga — Quagga."""
from .base import draw_taxon

META = {
    "slug": "equus_quagga_quagga",
    "scientific_name": "Equus quagga quagga",
    "common_name": "Quagga",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; 1883 en cautividad",
    "description": "Interpretación artística de Equus quagga quagga, Quagga. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/equus_quagga_quagga.md",
    "source_url": "https://www.gbif.org/species/search?q=Equus%20quagga%20quagga",
    "distribution": "Sudáfrica",
    "habitat": "pradera y matorral",
    "visual_notes": "cebra rayada delante y parda detrás",
    "extinction_notes": "caza comercial y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


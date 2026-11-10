"""Ficha visual de Zosterops semiflavus — Ojiblanco de Marianne."""
from .base import draw_taxon

META = {
    "slug": "zosterops_semiflavus",
    "scientific_name": "Zosterops semiflavus",
    "common_name": "Ojiblanco de Marianne",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; finales XIX o comienzos XX",
    "description": "Interpretación artística de Zosterops semiflavus, Ojiblanco de Marianne. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/zosterops_semiflavus.md",
    "source_url": "https://www.gbif.org/species/search?q=Zosterops%20semiflavus",
    "distribution": "isla Marianne, Seychelles",
    "habitat": "bosque insular",
    "visual_notes": "ojiblanco con anillo ocular y tonos amarillos",
    "extinction_notes": "pérdida de bosque y depredadores",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


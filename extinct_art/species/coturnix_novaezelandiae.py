"""Ficha visual de Coturnix novaezelandiae — Codorniz de Nueva Zelanda / koreke."""
from .base import draw_taxon

META = {
    "slug": "coturnix_novaezelandiae",
    "scientific_name": "Coturnix novaezelandiae",
    "common_name": "Codorniz de Nueva Zelanda / koreke",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Coturnix novaezelandiae, Codorniz de Nueva Zelanda / koreke. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/coturnix_novaezelandiae.md",
    "source_url": "https://www.gbif.org/species/search?q=Coturnix%20novaezelandiae",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


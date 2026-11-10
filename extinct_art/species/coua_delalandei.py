"""Ficha visual de Coua delalandei — Coua de Delalande."""
from .base import draw_taxon

META = {
    "slug": "coua_delalandei",
    "scientific_name": "Coua delalandei",
    "common_name": "Coua de Delalande",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; 1834",
    "description": "Interpretación artística de Coua delalandei, Coua de Delalande. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/coua_delalandei.md",
    "source_url": "https://www.gbif.org/species/search?q=Coua%20delalandei",
    "distribution": "Nosy Boraha, Madagascar",
    "habitat": "selva litoral",
    "visual_notes": "cucúlido grande; asociado a caracoles",
    "extinction_notes": "captura, deforestación, ratas y gatos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)


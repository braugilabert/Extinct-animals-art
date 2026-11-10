"""Ficha visual de Capra pyrenaica lusitanica — Cabra montés portuguesa."""
from .base import draw_taxon

META = {
    "slug": "capra_pyrenaica_lusitanica",
    "scientific_name": "Capra pyrenaica lusitanica",
    "common_name": "Cabra montés portuguesa",
    "kind": "mammal",
    "landscape": "generic",
    "status": "subespecie extinta; siglo XIX",
    "description": "Interpretación artística de Capra pyrenaica lusitanica, Cabra montés portuguesa. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/capra_pyrenaica_lusitanica.md",
    "source_url": "https://www.gbif.org/species/search?q=Capra%20pyrenaica%20lusitanica",
    "distribution": "Portugal y noroeste ibérico",
    "habitat": "montaña rocosa",
    "visual_notes": "cabra montés y cuernos curvados",
    "extinction_notes": "caza y pérdida de refugios",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.08,"horns":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)


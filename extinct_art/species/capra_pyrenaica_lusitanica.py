"""Ficha visual de Capra pyrenaica lusitanica — Cabra montés portuguesa."""
from .base import draw_taxon

META = {
    "slug": "capra_pyrenaica_lusitanica",
    "scientific_name": "Capra pyrenaica lusitanica",
    "common_name": "Cabra montés portuguesa",
    "kind": "mammal",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Capra pyrenaica lusitanica, Cabra montés portuguesa. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/capra_pyrenaica_lusitanica.md",
    "source_url": "https://www.gbif.org/species/search?q=Capra%20pyrenaica%20lusitanica",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


"""Ficha visual de Aepyornis spp. — Ave elefante de Madagascar."""
from .base import draw_taxon

META = {
    "slug": "aepyornis",
    "scientific_name": "Aepyornis spp.",
    "common_name": "Ave elefante de Madagascar",
    "kind": "bird",
    "landscape": "generic",
    "status": "por verificar con la ficha de referencia",
    "description": "Interpretación artística de Aepyornis spp., Ave elefante de Madagascar. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/aepyornis.md",
    "source_url": "https://www.gbif.org/species/search?q=Aepyornis%20spp.",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS)


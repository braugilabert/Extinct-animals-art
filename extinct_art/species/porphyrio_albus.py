"""Ficha visual de Porphyrio albus — Calamón blanco."""
from .base import draw_taxon

META = {
    "slug": "porphyrio_albus",
    "scientific_name": "Porphyrio albus",
    "common_name": "Calamón blanco",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Porphyrio albus, Calamón blanco. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/porphyrio_albus.md",
    "source_url": "https://www.gbif.org/species/search?q=Porphyrio%20albus",
    "distribution": "Lord Howe",
    "habitat": "humedal y bosque",
    "visual_notes": "calamón descrito como blanco",
    "extinction_notes": "caza y depredadores introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1,"long_beak":True,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)


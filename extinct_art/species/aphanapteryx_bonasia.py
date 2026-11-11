"""Ficha visual de Aphanapteryx bonasia — Rascón rojo de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "aphanapteryx_bonasia",
    "scientific_name": "Aphanapteryx bonasia",
    "common_name": "Rascón rojo de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVII",
    "description": "Interpretación artística de Aphanapteryx bonasia, Rascón rojo de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/aphanapteryx_bonasia/aphanapteryx_bonasia.md",
    "source_url": "https://www.gbif.org/species/search?q=Aphanapteryx%20bonasia",
    "distribution": "Mauricio",
    "habitat": "suelo forestal y humedal",
    "visual_notes": "rascón no volador, patas fuertes y pico curvado",
    "extinction_notes": "caza y depredadores introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.12,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Rascón no volador de Mauricio, descrito como grande, de cuerpo alargado, patas robustas y pico curvado. Las fuentes históricas apuntan a tonos rojizos o castaños, pero el patrón exacto es incierto.', 'visual_notes': 'Rascón terrestre grande; patas fuertes, alas reducidas y pico curvado; pardo rojizo hipotético.', 'drawing_notes': 'Silueta baja y corredora, con cuello adelantado y dedos visibles; evitar la forma de gallina.', 'reference_taxa': 'Rascón de Rodrigues Aphanapteryx y otros rails insulares actuales.', 'profile': {'body_scale': 1.13, 'flightless': True, 'long_beak': True, 'long_legs': True}}
RESEARCH_SOURCES = []

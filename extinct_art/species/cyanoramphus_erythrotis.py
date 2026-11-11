"""Ficha visual de Cyanoramphus erythrotis — Perico de la isla Macquarie."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_erythrotis",
    "scientific_name": "Cyanoramphus erythrotis",
    "common_name": "Perico de la isla Macquarie",
    "kind": "bird",
    "landscape": "generic",
    "status": "subespecie extinta; 1890-1891",
    "description": "Interpretación artística de Cyanoramphus erythrotis, Perico de la isla Macquarie. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_erythrotis/cyanoramphus_erythrotis.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20erythrotis",
    "distribution": "Macquarie",
    "habitat": "matorral subantártico y tussock",
    "visual_notes": "perico verde; anidaba en tussock",
    "extinction_notes": "gatos, perros y cambios de la isla",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Perico de Macquarie, subespecie insular del kākāriki de frente roja. El género suele ser verde, con frente o corona roja y azul en alas; representarlo pequeño, de cola puntiaguda y pico claro.', 'visual_notes': 'Perico verde de cola larga; corona o frente rojiza y azul en el ala como patrón de Cyanoramphus.', 'drawing_notes': 'La comparación con el kākāriki actual es razonable para la forma, pero no prueba cada marca de esta subespecie.', 'reference_taxa': 'Cyanoramphus novaezelandiae y C. hochstetteri.', 'profile': {'body_scale': 0.78, 'parrot': True, 'long_tail': True, 'red_head': True}, 'colors': {'body': '#5C8A52', 'body_hi': '#A2B76D', 'dark': '#31533B', 'accent': '#B0443D'}}
RESEARCH_SOURCES = []

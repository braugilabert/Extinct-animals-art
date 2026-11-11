"""Ficha visual de Psittacula bensoni — Periquito gris de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "psittacula_bensoni",
    "scientific_name": "Psittacula bensoni",
    "common_name": "Periquito gris de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVIII",
    "description": "Interpretación artística de Psittacula bensoni, Periquito gris de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/psittacula_bensoni/psittacula_bensoni.md",
    "source_url": "https://www.gbif.org/species/search?q=Psittacula%20bensoni",
    "distribution": "Mauricio y quizá Reunión",
    "habitat": "bosque insular",
    "visual_notes": "periquito gris; dibujo histórico disponible",
    "extinction_notes": "caza, captura e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Periquito gris de Mauricio, conocido por dibujos históricos. Representar un periquito de cola larga, pico curvado y plumaje gris o gris verdoso; el dibujo histórico es más útil que una comparación genérica con loros verdes.', 'visual_notes': 'Periquito de tamaño medio; plumaje gris, pico robusto y cola larga.', 'drawing_notes': 'Mantener el gris como rasgo principal y no convertirlo automáticamente en verde.', 'reference_taxa': 'Psittacula exsul y dibujos históricos de Psittacula bensoni.', 'profile': {'body_scale': 0.92, 'parrot': True, 'long_tail': True, 'large_bill': True}, 'colors': {'body': '#717A78', 'body_hi': '#AAB0A4', 'dark': '#3D4847', 'accent': '#9B5445'}}
RESEARCH_SOURCES = []

"""Ficha visual de Prosobonia ellisi — Correlimos de Moorea."""
from .base import draw_taxon

META = {
    "slug": "prosobonia_ellisi",
    "scientific_name": "Prosobonia ellisi",
    "common_name": "Correlimos de Moorea",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; hacia 1777",
    "description": "Interpretación artística de Prosobonia ellisi, Correlimos de Moorea. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/prosobonia_ellisi/prosobonia_ellisi.md",
    "source_url": "https://www.gbif.org/species/search?q=Prosobonia%20ellisi",
    "distribution": "Moorea",
    "habitat": "playa, marisma y humedal",
    "visual_notes": "limícola pequeño",
    "extinction_notes": "caza y depredadores introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1,"long_beak":True,"flightless":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Correlimos de Moorea, limícola pequeño de costa y humedal. Usar patas finas, cuerpo compacto y pico recto de longitud media; el plumaje pardo y blanco es una aproximación de Prosobonia.', 'visual_notes': 'Limícola pequeño; patas finas, pico recto y plumaje pardo grisáceo con vientre claro.', 'drawing_notes': 'Mantener la escala pequeña y las patas visibles; no usar la silueta de una garza.', 'reference_taxa': 'Prosobonia parvirostris y otros correlimos polinesios.', 'profile': {'body_scale': 0.62, 'wader': True, 'long_legs': True, 'long_beak': True}}
RESEARCH_SOURCES = []

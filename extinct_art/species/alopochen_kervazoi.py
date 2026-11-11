"""Ficha visual de Alopochen kervazoi — Ganso de Reunión / oca de Kervazo."""
from .base import draw_taxon

META = {
    "slug": "alopochen_kervazoi",
    "scientific_name": "Alopochen kervazoi",
    "common_name": "Ganso de Reunión / oca de Kervazo",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVII",
    "description": "Interpretación artística de Alopochen kervazoi, Ganso de Reunión / oca de Kervazo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/alopochen_kervazoi/alopochen_kervazoi.md",
    "source_url": "https://www.gbif.org/species/search?q=Alopochen%20kervazoi",
    "distribution": "Reunión",
    "habitat": "humedales y costa",
    "visual_notes": "oca insular robusta; plumaje incierto",
    "extinction_notes": "caza y especies introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Oca robusta de Reunión. La anatomía exacta y el plumaje son inciertos; dibujar un ganso terrestre de cuello medio, cuerpo ancho y patas relativamente fuertes, con tonos pardos y grises discretos.', 'visual_notes': 'Oca insular robusta; cabeza y pico de anátida; plumaje pardo grisáceo hipotético.', 'drawing_notes': 'No usar un cisne ni un pato pequeño; mantener proporciones de oca del género Alopochen.', 'reference_taxa': 'Alopochen aegyptiaca y otras ocas del género Alopochen.', 'profile': {'body_scale': 1.05, 'waterbird': True, 'large_bill': True}}
RESEARCH_SOURCES = []

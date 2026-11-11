"""Ficha visual de Lophopsittacus mauritianus — Loro de pico ancho de Mauricio."""
from .base import draw_taxon

META = {
    "slug": "lophopsittacus_mauritianus",
    "scientific_name": "Lophopsittacus mauritianus",
    "common_name": "Loro de pico ancho de Mauricio",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVII",
    "description": "Interpretación artística de Lophopsittacus mauritianus, Loro de pico ancho de Mauricio. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/lophopsittacus_mauritianus/lophopsittacus_mauritianus.md",
    "source_url": "https://www.gbif.org/species/search?q=Lophopsittacus%20mauritianus",
    "distribution": "Mauricio",
    "habitat": "bosque y humedal",
    "visual_notes": "loro grande de pico ancho",
    "extinction_notes": "caza, deforestación e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Loro de pico ancho de Mauricio, probablemente grande y de cabeza voluminosa. La anatomía se conoce sobre todo por restos; usar pico ancho, cola relativamente corta y plumaje verde grisáceo o pardo como hipótesis.', 'visual_notes': 'Loro grande de cabeza y pico anchos; cola no extremadamente larga; coloración incierta.', 'drawing_notes': 'Distinguirlo de Ara: más compacto y de cola más corta, con pico ancho.', 'reference_taxa': 'Restos de Lophopsittacus y loros de pico robusto actuales.', 'profile': {'body_scale': 1.08, 'parrot': True, 'short_tail': True, 'large_bill': True}}
RESEARCH_SOURCES = []

"""Ficha visual de Necropsittacus rodricanus — Loro de Rodrigues."""
from .base import draw_taxon

META = {
    "slug": "necropsittacus_rodricanus",
    "scientific_name": "Necropsittacus rodricanus",
    "common_name": "Loro de Rodrigues",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XVIII",
    "description": "Interpretación artística de Necropsittacus rodricanus, Loro de Rodrigues. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/necropsittacus_rodricanus/necropsittacus_rodricanus.md",
    "source_url": "https://www.gbif.org/species/search?q=Necropsittacus%20rodricanus",
    "distribution": "Rodrigues",
    "habitat": "bosque insular",
    "visual_notes": "loro grande; plumaje hipotético",
    "extinction_notes": "caza, captura e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Loro de Rodrigues de cabeza y mandíbulas proporcionalmente grandes, cola larga y cuerpo robusto. Las fuentes históricas describen verdes, azules y rojo en alas o pico con variación; presentar una versión verde azulada y marcarla como reconstrucción.', 'visual_notes': 'Loro grande, cabeza y pico muy robustos, cola larga; verde azulado con posible rojo alar.', 'drawing_notes': 'La cabeza grande y la cola larga son rasgos importantes; no reducirlo a un periquito común.', 'reference_taxa': 'Descripción histórica de Tafforet y comparaciones con Nestor/Tanygnathus.', 'profile': {'body_scale': 1.12, 'parrot': True, 'long_tail': True, 'large_bill': True}}
RESEARCH_SOURCES = []

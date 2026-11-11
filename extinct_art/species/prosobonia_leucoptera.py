"""Ficha visual de Prosobonia leucoptera — Correlimos de Tahití."""
from .base import draw_taxon

META = {
    "slug": "prosobonia_leucoptera",
    "scientific_name": "Prosobonia leucoptera",
    "common_name": "Correlimos de Tahití",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; fecha incierta",
    "description": "Interpretación artística de Prosobonia leucoptera, Correlimos de Tahití. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/prosobonia_leucoptera/prosobonia_leucoptera.md",
    "source_url": "https://www.gbif.org/species/search?q=Prosobonia%20leucoptera",
    "distribution": "Tahití",
    "habitat": "costa y humedal",
    "visual_notes": "limícola; alas blancas sugeridas por el nombre",
    "extinction_notes": "caza y pérdida de humedal; validez discutida",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1,"long_beak":True,"flightless":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Correlimos de Tahití, conocido por observaciones históricas y con validez discutida. El epíteto sugiere alas blancas, pero no debe inventarse un patrón completo; usar limícola pequeño, pardo y blanco.', 'visual_notes': 'Limícola pequeño; patas finas, pico recto y posible blanco en alas; patrón general incierto.', 'drawing_notes': 'Marcar el blanco alar como sugerencia nominal, no como dato seguro.', 'reference_taxa': 'Prosobonia parvirostris.', 'profile': {'body_scale': 0.62, 'wader': True, 'long_legs': True, 'long_beak': True, 'white_body': True}}
RESEARCH_SOURCES = []

"""Ficha visual de Panthera leo melanochaitus — León del Cabo."""
from .base import draw_taxon

META = {
    "slug": "panthera_leo_melanochaitus",
    "scientific_name": "Panthera leo melanochaitus",
    "common_name": "León del Cabo",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta en libertad; hacia 1858",
    "description": "Interpretación artística de Panthera leo melanochaitus, León del Cabo. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/panthera_leo_melanochaitus/panthera_leo_melanochaitus.md",
    "source_url": "https://www.gbif.org/species/search?q=Panthera%20leo%20melanochaitus",
    "distribution": "región del Cabo",
    "habitat": "sabana y matorral",
    "visual_notes": "león grande; melena oscura discutida",
    "extinction_notes": "caza, conflicto ganadero y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.18,"mane":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'León del Cabo, población o subespecie histórica de Sudáfrica. Usar león grande de cuerpo musculoso; la melena oscura y extendida aparece en relatos pero no debe darse por segura para todos los machos.', 'visual_notes': 'León robusto de sabana; pelaje leonado y posible melena oscura, especialmente en machos.', 'drawing_notes': 'Mantener anatomía de león, no de tigre; la melena oscura es una variante documentada/discutida.', 'reference_taxa': 'Panthera leo; registros históricos del león del Cabo.', 'profile': {'body_scale': 1.18, 'mane': True, 'cat': True}, 'colors': {'body': '#876746', 'body_hi': '#B09268', 'dark': '#48352B', 'accent': '#604033'}}
RESEARCH_SOURCES = []

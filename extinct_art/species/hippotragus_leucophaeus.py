"""Ficha visual de Hippotragus leucophaeus — Antílope azul."""
from .base import draw_taxon

META = {
    "slug": "hippotragus_leucophaeus",
    "scientific_name": "Hippotragus leucophaeus",
    "common_name": "Antílope azul",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; hacia 1800",
    "description": "Interpretación artística de Hippotragus leucophaeus, Antílope azul. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/hippotragus_leucophaeus/hippotragus_leucophaeus.md",
    "source_url": "https://www.gbif.org/species/search?q=Hippotragus%20leucophaeus",
    "distribution": "región del Cabo",
    "habitat": "pradera y matorral",
    "visual_notes": "antílope con cuernos; tono azulado debatido",
    "extinction_notes": "caza y transformación de pastizales",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.08,"horns":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Antílope azul del Cabo; antílope de tamaño medio-grande, cuerpo esbelto, cuernos anillados y pelaje descrito como gris azulado o azul pálido, aunque el tono fue debatido y pudo ser gris pardo.', 'visual_notes': 'Antílope robusto de pelaje gris azulado hipotético, vientre claro y cuernos curvados hacia atrás.', 'drawing_notes': 'El azul debe ser desaturado; conservar una silueta de Hippotragus y cuernos, no de ciervo.', 'reference_taxa': 'Hippotragus equinus y Hippotragus niger.', 'profile': {'body_scale': 1.08, 'horns': True, 'antelope': True}, 'colors': {'body': '#667477', 'body_hi': '#A2AC9F', 'dark': '#384343', 'accent': '#8B5C4A'}}
RESEARCH_SOURCES = []

"""Ficha visual de Ursus arctos crowtheri — Oso del Atlas."""
from .base import draw_taxon

META = {
    "slug": "ursus_arctos_crowtheri",
    "scientific_name": "Ursus arctos crowtheri",
    "common_name": "Oso del Atlas",
    "kind": "mammal",
    "landscape": "generic",
    "status": "subespecie extinta; siglo XIX",
    "description": "Interpretación artística de Ursus arctos crowtheri, Oso del Atlas. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/ursus_arctos_crowtheri/ursus_arctos_crowtheri.md",
    "source_url": "https://www.gbif.org/species/search?q=Ursus%20arctos%20crowtheri",
    "distribution": "montes Atlas",
    "habitat": "bosque montano y matorral",
    "visual_notes": "oso pardo oscuro; tamaño incierto",
    "extinction_notes": "caza y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.2}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Oso del Atlas, población histórica del oso pardo del norte de África. Representar oso pardo de tamaño moderado, cuerpo robusto, hombros fuertes y pelaje pardo oscuro; el tamaño exacto de la subespecie es discutido.', 'visual_notes': 'Oso pardo compacto; hocico corto, orejas redondeadas y pelaje oscuro; hábitat montano mediterráneo.', 'drawing_notes': 'No exagerar el tamaño como oso polar o grizzly; conservar la silueta de oso pardo.', 'reference_taxa': 'Ursus arctos actuales y registros históricos del Atlas.', 'profile': {'body_scale': 1.12, 'bear': True, 'round_body': True}, 'colors': {'body': '#544139', 'body_hi': '#8B6951', 'dark': '#2E2521', 'accent': '#704437'}}
RESEARCH_SOURCES = []

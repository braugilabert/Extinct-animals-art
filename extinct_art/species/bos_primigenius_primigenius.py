"""Ficha visual de Bos primigenius primigenius — Uro."""
from .base import draw_taxon

META = {
    "slug": "bos_primigenius_primigenius",
    "scientific_name": "Bos primigenius primigenius",
    "common_name": "Uro",
    "kind": "mammal",
    "landscape": "generic",
    "status": "subespecie extinta; 1627",
    "description": "Interpretación artística de Bos primigenius primigenius, Uro. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/bos_primigenius_primigenius/bos_primigenius_primigenius.md",
    "source_url": "https://www.gbif.org/species/search?q=Bos%20primigenius%20primigenius",
    "distribution": "Europa, Asia occidental y norte de África",
    "habitat": "pradera, bosque abierto y humedal",
    "visual_notes": "bovino enorme, hombros altos y cuernos largos",
    "extinction_notes": "caza, domesticación y pérdida de hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.08,"horns":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Uro europeo: toro salvaje enorme, de patas relativamente largas, lomo con cruz alta y cuernos largos que salen lateralmente y se curvan hacia delante y arriba. Los toros septentrionales eran negros o negruzcos; vacas más pardas y terneros rojizos.', 'visual_notes': 'Bovino muy grande; hombros altos, vientre relativamente recogido, cuernos largos hacia delante; toro negro pardo.', 'drawing_notes': 'La cruz alta, las patas largas y los cuernos son más diagnósticos que una simple vaca doméstica.', 'reference_taxa': 'Bos primigenius; ganado doméstico solo como comparación anatómica parcial.', 'profile': {'body_scale': 1.3, 'horns': True, 'ungulate': True, 'high_shoulder': True}, 'colors': {'body': '#342D28', 'body_hi': '#685348', 'dark': '#1E1917', 'accent': '#8A5A45'}}
RESEARCH_SOURCES = ['https://portals.iucn.org/library/efiles/documents/RD-1962-001-En.pdf']

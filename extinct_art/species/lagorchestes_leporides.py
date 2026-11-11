"""Ficha visual de Lagorchestes leporides — Canguro rata de la isla de Bernier."""
from .base import draw_taxon

META = {
    "slug": "lagorchestes_leporides",
    "scientific_name": "Lagorchestes leporides",
    "common_name": "Canguro rata de la isla de Bernier",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Lagorchestes leporides, Canguro rata de la isla de Bernier. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/lagorchestes_leporides/lagorchestes_leporides.md",
    "source_url": "https://www.gbif.org/species/search?q=Lagorchestes%20leporides",
    "distribution": "sudeste de Australia",
    "habitat": "matorral y pradera",
    "visual_notes": "hare-wallaby pardo de cola larga",
    "extinction_notes": "depredadores y alteración del hábitat",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.86}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Canguro liebre oriental; macrópodo pequeño de orejas largas, patas posteriores desarrolladas y cola larga. Las fuentes describen tonos rojizos o pardos, con vientre más claro.', 'visual_notes': 'Wallaby liebre; cuerpo compacto, patas posteriores largas, orejas grandes, cola larga y pelaje pardo rojizo.', 'drawing_notes': 'Usar una silueta saltadora y esbelta, no la de un canguro gigante.', 'reference_taxa': 'Lagorchestes hirsutus.', 'profile': {'body_scale': 0.84, 'marsupial': True, 'long_tail': True, 'long_legs': True}, 'colors': {'body': '#956449', 'body_hi': '#C09268', 'dark': '#4B352B', 'accent': '#8E4939'}}
RESEARCH_SOURCES = []

"""Ficha visual de Prolagus sardus — Pika sarda."""
from .base import draw_taxon

META = {
    "slug": "prolagus_sardus",
    "scientific_name": "Prolagus sardus",
    "common_name": "Pika sarda",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; fecha incierta",
    "description": "Interpretación artística de Prolagus sardus, Pika sarda. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/prolagus_sardus/prolagus_sardus.md",
    "source_url": "https://www.gbif.org/species/search?q=Prolagus%20sardus",
    "distribution": "Cerdeña y Córcega",
    "habitat": "matorral mediterráneo",
    "visual_notes": "lagomorfo robusto de orejas cortas",
    "extinction_notes": "caza, competencia e introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Pika sarda o prolagus, lagomorfo insular robusto de Cerdeña y Córcega conocido por restos. Tenía cuerpo compacto, orejas relativamente cortas y patas traseras desarrolladas; el pelaje es inferido en tonos pardo grisáceos.', 'visual_notes': 'Lagomorfo robusto, orejas cortas, cuerpo bajo y patas traseras fuertes; pardo grisáceo hipotético.', 'drawing_notes': 'No dibujarlo como conejo de orejas largas: el rasgo útil es la forma compacta de pika insular.', 'reference_taxa': 'Prolagus sardus; comparación funcional con pikas actuales (Ochotona), no identidad.', 'profile': {'body_scale': 0.88, 'rodent': True, 'round_body': True, 'short_tail': True, 'short_ears': True}}
RESEARCH_SOURCES = []

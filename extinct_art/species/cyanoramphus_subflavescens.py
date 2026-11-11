"""Ficha visual de Cyanoramphus subflavescens — Perico de Lord Howe."""
from .base import draw_taxon

META = {
    "slug": "cyanoramphus_subflavescens",
    "scientific_name": "Cyanoramphus subflavescens",
    "common_name": "Perico de Lord Howe",
    "kind": "bird",
    "landscape": "generic",
    "status": "subespecie extinta; siglo XIX",
    "description": "Interpretación artística de Cyanoramphus subflavescens, Perico de Lord Howe. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/cyanoramphus_subflavescens/cyanoramphus_subflavescens.md",
    "source_url": "https://www.gbif.org/species/search?q=Cyanoramphus%20subflavescens",
    "distribution": "Lord Howe",
    "habitat": "bosque y matorral",
    "visual_notes": "perico insular; descripción limitada",
    "extinction_notes": "caza y depredadores introducidos",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Perico de Lord Howe, forma insular del complejo de kākāriki. Usar perico verde pequeño-mediano, cola larga y manchas de corona discretas; los detalles subespecíficos son limitados.', 'visual_notes': 'Perico verde amarillento, cola puntiaguda y cuerpo ligero; patrón rojo reducido o incierto.', 'drawing_notes': 'No hacerlo tan robusto como un loro grande ni tan pálido como un periquito doméstico.', 'reference_taxa': 'Cyanoramphus novaezelandiae; comparación con kākāriki actuales.', 'profile': {'body_scale': 0.8, 'parrot': True, 'long_tail': True}, 'colors': {'body': '#6F9850', 'body_hi': '#B0BF78', 'dark': '#3C5B38', 'accent': '#A55240'}}
RESEARCH_SOURCES = []

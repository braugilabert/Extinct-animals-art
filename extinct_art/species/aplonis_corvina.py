"""Ficha visual de Aplonis corvina — Estornino de Kosrae."""
from .base import draw_taxon

META = {
    "slug": "aplonis_corvina",
    "scientific_name": "Aplonis corvina",
    "common_name": "Estornino de Kosrae",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; siglo XIX",
    "description": "Interpretación artística de Aplonis corvina, Estornino de Kosrae. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/aplonis_corvina/aplonis_corvina.md",
    "source_url": "https://www.gbif.org/species/search?q=Aplonis%20corvina",
    "distribution": "Kosrae, Carolinas",
    "habitat": "bosque tropical",
    "visual_notes": "estornino insular; coloración escasa",
    "extinction_notes": "pérdida de bosque y especies introducidas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Estornino de Kosrae, probablemente un paseriforme de bosque de tamaño medio. La especie se conoce mal; usar cuerpo compacto, pico recto y plumaje oscuro con brillo metálico moderado como hipótesis.', 'visual_notes': 'Estornino insular; cuerpo compacto, cola media y plumaje negro o pardo oscuro posiblemente brillante.', 'drawing_notes': 'Mantener la forma de estornino, no de cuervo: pico más corto y cuerpo menor.', 'reference_taxa': 'Aplonis tabuensis y Aplonis atrifusca como referencias de género.', 'profile': {'body_scale': 0.9, 'dark_body': True, 'songbird': True}, 'colors': {'body': '#3D4B4C', 'body_hi': '#718486', 'dark': '#202B31', 'accent': '#8D5A45'}}
RESEARCH_SOURCES = []

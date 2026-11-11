"""Ficha visual de Aepyornis spp. — Ave elefante de Madagascar."""
from .base import draw_taxon

META = {
    "slug": "aepyornis",
    "scientific_name": "Aepyornis spp.",
    "common_name": "Ave elefante de Madagascar",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinto; género con varias especies",
    "description": "Interpretación artística de Aepyornis spp., Ave elefante de Madagascar. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/aepyornis/aepyornis.md",
    "source_url": "https://www.gbif.org/species/search?q=Aepyornis%20spp.",
    "distribution": "Madagascar",
    "habitat": "bosque, humedal y zonas abiertas",
    "visual_notes": "ratite gigante y huevos enormes; elegir especie antes de dibujar",
    "extinction_notes": "caza y transformación del hábitat; cronología variable",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":1.3,"flightless":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Ratita gigante de Madagascar; representar un ave terrestre de cuerpo enorme, cuello largo, cabeza relativamente pequeña y alas reducidas. El color del plumaje no está establecido con seguridad: usar marrón grisáceo como hipótesis prudente.', 'visual_notes': 'Ave elefante ratita gigante; huevos excepcionalmente grandes; cuello largo y alas reducidas; plumaje marrón grisáceo hipotético.', 'drawing_notes': 'Documentado: ratita gigante, no voladora y de Madagascar. Hipótesis visual: silueta pesada, patas largas y plumaje pardo apagado; no dibujar un avestruz exacto ni afirmar un color concreto.', 'reference_taxa': 'Aepyornis; comparación funcional prudente con avestruz y casuario actuales, no como copia.', 'profile': {'body_scale': 1.34, 'flightless': True, 'long_legs': True, 'long_neck': True, 'giant': True, 'ratite': True}}
RESEARCH_SOURCES = ['https://www.nhm.ac.uk/our-science/services/collections/palaeontology/fossil-birds.html']

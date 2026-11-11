"""Ficha visual de Dusicyon australis — Zorro/lobo de las Malvinas."""
from .base import draw_taxon

META = {
    "slug": "dusicyon_australis",
    "scientific_name": "Dusicyon australis",
    "common_name": "Zorro/lobo de las Malvinas",
    "kind": "mammal",
    "landscape": "generic",
    "status": "extinta; 1876",
    "description": "Interpretación artística de Dusicyon australis, Zorro/lobo de las Malvinas. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/dusicyon_australis/dusicyon_australis.md",
    "source_url": "https://www.gbif.org/species/search?q=Dusicyon%20australis",
    "distribution": "islas Malvinas",
    "habitat": "turbera, playa, llanura y roquedo",
    "visual_notes": "cánido mediano; pelaje pardo y punta de cola blanca",
    "extinction_notes": "caza por piel y protección del ganado",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.86}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Warrah o lobo de las Malvinas: cánido mediano y robusto, de unos 97 cm de cabeza-cuerpo y unos 38 cm a la cruz. Tenía patas cortas, orejas pequeñas, cola tupida con punta blanca y manto dorsal mezclado de leonado, pardo y negro, más claro por debajo.', 'visual_notes': 'Cánido compacto tipo zorro grande; patas cortas, orejas pequeñas, dorso pardo-leonado mezclado y punta de cola blanca.', 'drawing_notes': 'La cola blanca y la baja altura son rasgos muy útiles; no dibujarlo como lobo continental alto.', 'reference_taxa': 'Dusicyon australis; Animal Diversity Web y comparación con Chrysocyon brachyurus.', 'profile': {'body_scale': 0.98, 'wolf': True, 'short_legs': True, 'bushy_tail': True, 'white_tail_tip': True}, 'colors': {'body': '#80624C', 'body_hi': '#B08C67', 'dark': '#44352D', 'light': '#D0B18A', 'accent': '#F0E3C6'}}
RESEARCH_SOURCES = ['https://animaldiversity.org/accounts/Dusicyon_australis/']

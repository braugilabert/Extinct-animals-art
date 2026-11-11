"""Ficha visual de Psittacula exsul — Periquito de Newton."""
from .base import draw_taxon

META = {
    "slug": "psittacula_exsul",
    "scientific_name": "Psittacula exsul",
    "common_name": "Periquito de Newton",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; hacia 1875",
    "description": "Interpretación artística de Psittacula exsul, Periquito de Newton. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/psittacula_exsul/psittacula_exsul.md",
    "source_url": "https://www.gbif.org/species/search?q=Psittacula%20exsul",
    "distribution": "Rodrigues",
    "habitat": "bosque y matorral",
    "visual_notes": "periquito insular con ejemplares conservados",
    "extinction_notes": "caza, captura y depredadores",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":False}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Periquito de Newton de Rodrigues, de unos 40 cm según World Parrot Trust. Descripciones históricas mencionan morfos verdes o azul verdosos, cabeza más oscura, alas con rojo y pico superior rojo e inferior negro; separar estas variantes.', 'visual_notes': 'Periquito grande de cola larga; verde o azul verdoso, cabeza oscura, posible rojo alar y pico bicolor.', 'drawing_notes': 'La ficha permite una versión verde y otra azulada, pero no mezclarlas sin indicarlo como morfo histórico.', 'reference_taxa': 'Psittacula exsul; descripción histórica de Tafforet y World Parrot Trust.', 'profile': {'body_scale': 1.05, 'parrot': True, 'long_tail': True, 'large_bill': True}, 'colors': {'body': '#617F78', 'body_hi': '#8EAAA0', 'dark': '#263C3B', 'accent': '#B4473F'}}
RESEARCH_SOURCES = ['https://parrots.org/encyclopedia/newtons-parakeet/', 'https://boc-online.org/bulletins/downloads/BBOC1343-Hume.pdf']

"""Ficha visual de Ara erythrocephala — Guacamayo de cabeza roja."""
from .base import draw_taxon

META = {
    "slug": "ara_erythrocephala",
    "scientific_name": "Ara erythrocephala",
    "common_name": "Guacamayo de cabeza roja",
    "kind": "bird",
    "landscape": "generic",
    "status": "taxón histórico discutido",
    "description": "Interpretación artística de Ara erythrocephala, Guacamayo de cabeza roja. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/ara_erythrocephala.md",
    "source_url": "https://www.gbif.org/species/search?q=Ara%20erythrocephala",
    "distribution": "Caribe",
    "habitat": "bosque tropical",
    "visual_notes": "guacamayo de cabeza roja según el nombre; resto hipotético",
    "extinction_notes": "caza y pérdida de hábitat hipotéticas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.94,"crest":True}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)


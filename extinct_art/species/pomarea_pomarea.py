"""Ficha visual de Pomarea pomarea — Monarca de Maupiti."""
from .base import draw_taxon

META = {
    "slug": "pomarea_pomarea",
    "scientific_name": "Pomarea pomarea",
    "common_name": "Monarca de Maupiti",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta; mediados del XIX",
    "description": "Interpretación artística de Pomarea pomarea, Monarca de Maupiti. Consultar la ficha de references/species antes de publicar.",
    "reference_file": "references/species/pomarea_pomarea/pomarea_pomarea.md",
    "source_url": "https://www.gbif.org/species/search?q=Pomarea%20pomarea",
    "distribution": "Maupiti",
    "habitat": "bosque tropical",
    "visual_notes": "monarca pequeño; plumaje poco documentado",
    "extinction_notes": "pérdida de bosque y ratas",
    "research_status": "investigación inicial: revisar la fuente enlazada y la ficha Markdown antes de publicar",
    "research_limitations": "la anatomía completa, el color y la cronología pueden estar incompletos o discutidos",
}

# Colores iniciales: hipótesis visual, no reconstrucción definitiva.
PROFILE = {"body_scale":0.95}

COLORS = {}

def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)



# Datos visuales investigados y usados por draw().
DRAWING_DATA = {'description': 'Monarca de Tahití, pequeño paseriforme arborícola conocido por pocos ejemplares. Usar cuerpo compacto, pico fino y cola media; el plumaje oscuro con zonas claras es una hipótesis basada en monarcas polinesios.', 'visual_notes': 'Monarca pequeño; cuerpo compacto, pico fino y tonos oscuros o grisáceos hipotéticos.', 'drawing_notes': 'No darle la forma de un estornino grande: es un paseriforme ligero de bosque.', 'reference_taxa': 'Pomarea nigra y otras Pomarea polinesias.', 'profile': {'body_scale': 0.7, 'songbird': True, 'thin_bill': True}}
RESEARCH_SOURCES = []

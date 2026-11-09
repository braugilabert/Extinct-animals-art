"""Registro de especies. Para añadir una: crea species/<nombre>.py con META y
draw(rng_for), importa el módulo aquí y regístralo en SPECIES."""
from . import ara_gossei

SPECIES = {
    "ara_gossei": ara_gossei,
}

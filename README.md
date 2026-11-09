# Extinct Animals Art

Generador, gratuito y en local, de láminas tipo acuarela antigua de especies
extintas, en formato 4:5 para Instagram (1080x1350 px). Es un homenaje a las
especies que ya no están en la Tierra.

Todo es Python más SVG: no usa APIs ni servicios de pago. Con la misma semilla
sale siempre la misma imagen.

![Ara gossei, acuarela antigua](img/ara_gossei_acuarela_antigua_s7.png)

*Ejemplo: `python generate.py` (Ara gossei, paleta `acuarela_antigua`, semilla 7).*

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt  # solo cairosvg, para exportar a PNG
```

El PNG es opcional: el SVG se genera sin ninguna dependencia. Si `cairosvg`
no funciona en tu sistema (en Windows necesita las librerías de Cairo), el
exportador prueba con `rsvg-convert` e Inkscape, y si no hay ninguno puedes
usar `--no-png`.

## Uso

```bash
python generate.py                        # Ara gossei, paleta por defecto
python generate.py ara_gossei --seed 12   # otra variación de la pincelada
python generate.py --palette sepia
python generate.py --all-palettes         # una imagen por paleta
python generate.py --no-png               # solo SVG
python generate.py --width 2160           # PNG más grande
python generate.py --list                 # especies, paletas y paisajes
```

Los resultados se guardan en `output/` (no se suben a Git; se regeneran).
Otras opciones: `--no-caption`, `--no-grain`, `--no-flower`, `--landscape`.

## Estructura

| Ruta | Qué contiene |
| --- | --- |
| `generate.py` | Línea de comandos |
| `extinct_art/compose.py` | Une papel, paisaje, rama y especie en la lámina |
| `extinct_art/palettes.py` | Paletas de la escena (papel, paisaje, rama, flor) |
| `extinct_art/landscapes.py` | Paisajes de fondo |
| `extinct_art/species/` | Una especie por archivo, con sus colores y su dibujo |
| `extinct_art/brush.py` | Utilidades de pincelada: manchas, bordes irregulares, granulado |
| `extinct_art/render.py` | Exportación SVG a PNG |

## Cómo añadir cosas

- **Paleta nueva:** copia una de `palettes.py`, cambia los colores y
  regístrala en `PALETTES`.
- **Paisaje nuevo:** escribe dos funciones (telón y follaje) como las de
  `landscapes.py` y regístralas en `LANDSCAPES`.
- **Especie nueva:** crea `species/<nombre>.py` con `META` y
  `draw(rng_for)`, e impórtala en `species/__init__.py`.

Cada especie necesita su propio dibujo base, porque la anatomía cambia
(un dodo no se dibuja como un guacamayo). Lo que se reutiliza entre especies
es el papel, las paletas, los paisajes y el pincel.

## Sobre las especies

Las láminas son interpretaciones a partir de descripciones y láminas
históricas, no reconstrucciones exactas. El *Ara gossei*, por ejemplo, es una
especie hipotética: se conoce solo por una descripción de Gosse (1847) y una
lámina de Rothschild (1907), y es posible que fuera el guacamayo cubano
(*Ara tricolor*). Conviene indicarlo en el pie de cada publicación.

## Tests

```bash
python -m unittest discover
```

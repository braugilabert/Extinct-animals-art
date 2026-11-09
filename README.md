# Extinct Animals Art

Generador local de láminas 4:5 con aspecto de acuarela antigua para especies extintas o desaparecidas. El proyecto combina SVG procedural, paletas de color, paisajes y un dibujo específico para cada especie. No necesita API ni servicios de pago y, usando la misma semilla, vuelve a producir la misma ilustración.

![Ara gossei, acuarela antigua](img/ara_gossei_acuarela_antigua_s7.png)

La imagen anterior es el resultado de:

```bash
python generate.py ara_gossei --palette acuarela_antigua --seed 7
```

## Qué se puede hacer ahora

- Elegir una especie registrada por su identificador (`ara_gossei`).
- Guardar el nombre científico y el nombre común en la ficha de la especie.
- Añadir una descripción histórica o artística a esa ficha. La descripción queda incluida en el `<desc>` del SVG, además de servir como documentación.
- Elegir paleta, paisaje, semilla y tamaño de salida.
- Generar SVG, PNG o ambos.
- Quitar el rótulo, el granulado del papel o la flor de la composición.
- Trabajar con bocetos y referencias guardándolos en `references/<identificador>/`. Sirven para estudiar anatomía, postura, color y fuentes; el dibujo final se implementa en el módulo Python de la especie.

El programa no convierte todavía automáticamente un texto o un boceto en una especie dibujada. La geometría debe escribirse a mano porque cada animal tiene una anatomía diferente. Sí queda preparado un flujo claro para introducir el nombre, la investigación, las fuentes, los bocetos y después traducirlos a formas SVG.

## Instalación

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

`cairosvg` se usa para exportar a PNG. El SVG puede generarse sin esa dependencia. Si Cairo no funciona en Windows, instala Inkscape o `rsvg-convert`, o usa `--no-png`.

## Crear una ilustración de una especie

### 1. Preparar la ficha de investigación

Copia [`docs/plantilla-especie.md`](docs/plantilla-especie.md) y guárdala como `references/<identificador>/<identificador>.md`. El identificador debe ser simple, en minúsculas y con guiones bajos: `dodo`, `pinguinus_impennis` o `capra_pyrenaica_lusitanica`.

Incluye nombre científico y nombres históricos o comunes, fecha y lugar aproximados de desaparición, descripción anatómica, hábitat, grado de certeza, fuentes, decisiones visuales y advertencias para no presentar una hipótesis como un hecho.

Los bocetos pueden guardarse junto a la ficha:

```text
references/
└── pinguinus_impennis/
    ├── pinguinus_impennis.md
    ├── boceto_postura.jpg
    └── referencia_historica.png
```

### 2. Crear el módulo de dibujo

Copia `extinct_art/species/ara_gossei.py` como `extinct_art/species/<identificador>.py`. Cambia al menos `META`, `COLORS` y la función `draw(rng_for)`. `META` debe contener:

```python
META = {
    "scientific_name": "Pinguinus impennis",
    "common_name": "Alca gigante",
    "landscape": "jamaica",  # sustituir por un paisaje disponible
    "status": "extinta",
    "description": "Ave marina no voladora del Atlántico norte.",
}
```

La función `draw` devuelve fragmentos SVG. Se pueden reutilizar `wash`, `stroke`, `blob` y `scale_marks` desde `extinct_art/brush.py`; así se conserva el acabado de acuarela. No hace falta redibujar el papel, el grano, el paisaje ni la rama: `compose.py` los añade automáticamente.

### 3. Registrar la especie

Edita `extinct_art/species/__init__.py`:

```python
from . import ara_gossei, pinguinus_impennis

SPECIES = {
    "ara_gossei": ara_gossei,
    "pinguinus_impennis": pinguinus_impennis,
}
```

### 4. Generar y revisar

```bash
python generate.py --list
python generate.py pinguinus_impennis --seed 7
python generate.py pinguinus_impennis --palette sepia --no-png
python generate.py pinguinus_impennis --all-palettes --width 2160
```

Los archivos aparecen en `output/`. Esa carpeta se puede borrar y regenerar; las fuentes, fichas y bocetos deben conservarse en `references/`.

## Opciones de generación

```text
--palette NOMBRE       acuarela_antigua, sepia o amanecer
--all-palettes          genera una versión por paleta
--landscape NOMBRE      fuerza el paisaje de fondo
--seed NÚMERO           controla la variación de la pincelada
--width PÍXELES         ancho del PNG; la altura mantiene la proporción 4:5
--out CARPETA           carpeta de salida
--no-png                solo SVG
--no-caption            elimina el rótulo inferior
--no-grain              elimina el granulado del papel
--no-flower             elimina el hibisco de la rama
--list                  muestra especies, paletas y paisajes disponibles
```

## Estructura

| Ruta | Contenido |
| --- | --- |
| `generate.py` | Interfaz de línea de comandos |
| `extinct_art/compose.py` | Composición de papel, paisaje, rama y especie |
| `extinct_art/species/` | Una ficha visual Python por especie |
| `extinct_art/brush.py` | Manchas, pinceladas, bordes y textura |
| `extinct_art/palettes.py` | Paletas de la lámina |
| `extinct_art/landscapes.py` | Paisajes disponibles |
| `references/` | Fichas, fuentes y bocetos de trabajo |
| `docs/plantilla-especie.md` | Plantilla para investigar una especie |
| `docs/especies-notas.md` | Anotaciones recibidas para futuras ilustraciones |
| `output/` | SVG y PNG generados |

## Criterios de documentación y rigor

Estas láminas son interpretaciones artísticas, no reconstrucciones exactas. Cuando una especie solo se conoce por relatos, restos o una lámina posterior, esa incertidumbre debe aparecer en `META`, en la ficha y, si procede, en la publicación final. Conviene distinguir entre nombre científico moderno, nombres usados históricamente y nombres populares.

La lista de animales de `docs/especies-notas.md` es un punto de partida, no una verificación taxonómica definitiva. Antes de dibujar o publicar una especie, comprueba su estado, sinonimias, fecha de extinción y fuentes primarias o institucionales.

## Tests

```bash
python -m unittest discover
```

Los tests comprueban que todas las especies y paletas producen XML válido y que la semilla mantiene la reproducibilidad.

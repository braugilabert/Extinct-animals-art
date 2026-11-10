# Crear una especie desde cero

Esta guía explica cómo añadir una especie nueva sin modificar `generate.py` ni
registrarla manualmente en una lista.

## Flujo general

```text
investigar → ficha Markdown → módulo Python → drawing_data.py
→ perfil anatómico → validar → generar con generate.py
```

## 1. Crear los archivos iniciales

Desde la carpeta principal del proyecto:

```powershell
python new_species.py
```

El asistente pedirá nombre científico, nombre común, grupo animal,
distribución, hábitat y estado. Creará:

```text
extinct_art/species/nueva_especie.py
references/species/nueva_especie.md
```

Usa minúsculas, guiones bajos y ningún acento en el nombre del archivo:

```text
Raphus cucullatus → raphus_cucullatus
```

## 2. Completar la ficha Markdown

Abre `references/species/nueva_especie.md` y completa especialmente
**Descripción útil para el dibujo**. Incluye, cuando existan fuentes fiables:

- tamaño, peso y proporciones;
- forma de cabeza, pico, hocico, dientes o cuernos;
- alas, cola, patas y postura;
- colores, patrones y dimorfismo sexual;
- hábitat, distribución y paisaje;
- nivel de incertidumbre de cada dato;
- fuentes consultadas y referencias visuales.

Es mejor escribir que un color es hipotético que presentarlo como un hecho.

## 3. Completar el módulo Python

Abre `extinct_art/species/nueva_especie.py`. La estructura mínima es:

```python
from .base import draw_taxon

META = {
    "slug": "nueva_especie",
    "scientific_name": "Nombre scientificus",
    "common_name": "Nombre común",
    "kind": "bird",
    "landscape": "generic",
    "status": "extinta",
    "description": "Descripción breve.",
    "reference_file": "references/species/nueva_especie.md",
    "source_url": "https://www.gbif.org/",
    "distribution": "región o isla documentada",
    "habitat": "hábitat documentado",
    "visual_notes": "rasgos visuales principales",
    "extinction_notes": "causas o hipótesis",
    "research_status": "fuentes revisadas",
    "research_limitations": "datos todavía inciertos",
}

PROFILE = {"body_scale": 1.0}
COLORS = {}


def draw(rng_for) -> str:
    return draw_taxon(rng_for, META, COLORS, PROFILE)
```

`draw()` es la función que dibuja el animal. Normalmente basta con llamar a
`draw_taxon()`. Para una anatomía excepcional puedes crear una función propia.

## 4. Completar los datos visuales de la especie

Para una especie nueva creada con `new_species.py`, los datos visuales se
guardan dentro de su propio módulo Python, en `DRAWING_DATA`. Así no tienes
que editar otro archivo central para cada especie:

```python
DRAWING_DATA = {
    "description": "Descripción útil para construir la silueta.",
    "visual_notes": "Rasgos que deben verse.",
    "drawing_notes": "Datos documentados e hipótesis.",
    "reference_taxa": "Especies actuales usadas solo como comparación.",
}

RESEARCH_SOURCES = [
    "https://enlace-a-la-fuente.org",
]
```

El asistente ya incluye estas variables en el nuevo módulo.

### Especies antiguas del proyecto

Las especies que ya existían siguen usando `drawing_data.py` como catálogo
central. Es intencionado: evita duplicar y mantener dos versiones de los datos
de 58 especies. El cargador acepta ambos sistemas y da prioridad a los datos
locales si una especie nueva los tiene.

Si prefieres completar una especie antigua dentro de su módulo, puedes copiar
allí `DRAWING_DATA` y `RESEARCH_SOURCES`; no es necesario migrar todas las
demás especies.

## 5. Completar `drawing_data.py`

Añade en `extinct_art/species/drawing_data.py` una entrada con la misma clave
que el `slug`:

```python
"nueva_especie": {
    "description": "Descripción útil para construir la silueta.",
    "visual_notes": "Rasgos que deben verse.",
    "drawing_notes": "Datos documentados e hipótesis.",
    "reference_taxa": "Especies actuales usadas solo como comparación.",
    "profile": {
        "body_scale": 1.0,
        "parrot": True,
    },
    "colors": {
        "body": "#607052",
        "body_hi": "#A4B17C",
        "dark": "#303A2A",
        "light": "#E8DDB5",
        "accent": "#A8503E",
    },
},
```

La ficha Markdown es la documentación completa; `drawing_data.py` contiene la
versión estructurada que necesita el dibujo. Al cargar el catálogo,
`species/__init__.py` combina automáticamente esos datos con `META` y
`PROFILE` del módulo Python.

## 6. Elegir el perfil anatómico

Usa únicamente perfiles compatibles con la descripción:

| Perfil | Uso |
|---|---|
| `parrot` | loros y guacamayos |
| `ratite` | emús, avestruces y aves elefante |
| `owl` | búhos y autillos |
| `waterbird` | aves acuáticas |
| `wader` | limícolas, ibis y aves de patas largas |
| `ground_bird` | aves terrestres y rascones |
| `songbird` | paseriformes pequeños |
| `pigeon` | palomas |
| `ungulate`, `horse`, `goat`, `antelope` | ungulados |
| `cat` | felinos |
| `wolf`, `bear`, `rodent`, `marsupial`, `mustelid` | mamíferos |
| `bat` | murciélagos |
| `snake_head` | serpientes |
| `gecko` | geckos |

También existen rasgos complementarios:

```python
{
    "body_scale": 1.15,
    "long_tail": True,
    "long_legs": True,
    "large_bill": True,
    "white_body": True,
    "stripes": True,
    "horns": True,
    "mane": True,
}
```

No actives un rasgo solo porque produzca una imagen más llamativa: debe estar
respaldado por una fuente o marcado como hipótesis.

## 7. Añadir referencias visuales

Si existen ilustraciones o fotografías con licencia adecuada:

```powershell
python tools/download_reference_images.py --species nueva_especie --limit 3
```

Se guardarán en:

```text
references/species/nueva_especie_images/
```

Las referencias sirven para documentar rasgos y extraer una paleta orientativa.
No se copian automáticamente dentro del animal: la anatomía sigue dependiendo
de la ficha y del perfil.

## 8. Validar

```powershell
python generate.py --validate
python generate.py nueva_especie --describe
```

La validación comprueba módulos, fichas, metadatos obligatorios, URLs y que los
datos visuales cargados también aparecen en la ficha Markdown.

## 9. Generar

```powershell
python generate.py nueva_especie
```

Variantes útiles:

```powershell
python generate.py nueva_especie --seed 12
python generate.py nueva_especie --no-png
python generate.py nueva_especie --landscape bosque
```

La misma semilla produce la misma versión reproducible.

## 10. Revisar el resultado

Comprueba si:

- la silueta pertenece al grupo correcto;
- las proporciones son razonables;
- se ven los rasgos diagnósticos;
- los colores están documentados o marcados como hipótesis;
- el paisaje coincide con la distribución;
- el pie muestra la ubicación correcta;
- no se han añadido detalles sin respaldo.

Si parece genérica, corrige primero `profile`, `visual_notes` y
`drawing_notes` en `drawing_data.py`. Si el perfil no basta, modifica o crea
una función anatómica específica en `base.py` o en el módulo de la especie.

## 11. Qué archivos se ejecutan

En el uso normal solo necesitas:

```powershell
python generate.py nueva_especie
```

El flujo interno es:

```text
generate.py → compose.py → species/__init__.py
→ módulo de especie + drawing_data.py → base.py o draw() propio
→ paisajes, pinceles y paletas → SVG y PNG en output/
```

No tienes que ejecutar directamente `__init__.py`, `base.py`, `compose.py` ni
el módulo individual de la especie.

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
- Consultar las 58 fichas individuales de `references/species/`, preparadas a partir de la lista de `docs/especies-notas.md` y con enlaces para completar la investigación.
- Crear una especie nueva automáticamente con `new_species.py`, sin copiar archivos a mano.
- Validar que el catálogo, los paisajes y las fichas de referencia están conectados correctamente.

El programa no convierte todavía automáticamente un texto o un boceto en una especie dibujada. La geometría debe escribirse a mano porque cada animal tiene una anatomía diferente. Sí queda preparado un flujo claro para introducir el nombre, la investigación, las fuentes, los bocetos y después traducirlos a formas SVG.

## Diferencia entre las fichas Markdown y los módulos Python

Cada especie tiene dos archivos relacionados, pero cumplen funciones distintas:

| Archivo | Para qué sirve |
| --- | --- |
| `references/species/<especie>.md` | Es la ficha de investigación y planificación. Guarda lo que sabemos, las fuentes, la distribución, el hábitat, los rasgos anatómicos, los colores posibles, las dudas y los bocetos. No genera imágenes. |
| `extinct_art/species/<especie>.py` | Es la ficha técnica del generador. Contiene los metadatos que usa el programa y la función `draw(rng_for)`, que devuelve las formas SVG del animal. Sí participa en la generación de imágenes. |

La relación es esta:

```text
fuentes y bocetos
        ↓
ficha Markdown: qué sabemos y qué podemos representar
        ↓ revisión y traducción manual
módulo Python: cómo se dibuja mediante SVG
        ↓
generate.py → lámina SVG → PNG opcional
```

Por ejemplo, en la ficha Markdown de `pinguinus_impennis` se documenta que el
alca gigante era un ave marina grande, no voladora, de costas del Atlántico
norte. Después esa información se traduce al módulo Python: se elige el grupo
`bird`, una silueta, colores, postura y paisaje. El programa no lee todavía el
texto Markdown para dibujar automáticamente; la persona que investiga realiza
esa traducción de forma consciente.

La ficha Markdown es, por tanto, la fuente de conocimiento y memoria del
proyecto. El módulo Python es la implementación visual. Si cambias solo la
ficha Markdown, la imagen no cambiará hasta que actualices también el módulo
Python. Si cambias solo el módulo Python, la imagen cambiará, pero la decisión
visual quedará mal documentada.

## Qué debe contener cada uno

### Ficha Markdown

Úsala para guardar:

- nombres científicos, comunes e históricos;
- distribución, hábitat y cronología;
- tamaño, anatomía, plumaje, pelaje o escamas;
- alimentación y comportamiento cuando se conozcan;
- causas de extinción y nivel de certeza;
- enlaces, libros, museos, ejemplares y licencias de imágenes;
- decisiones artísticas y rasgos que son hipótesis.

### Módulo Python

Úsalo para guardar:

- `META`: nombres, grupo, paisaje, descripción y datos de investigación;
- `COLORS`: colores utilizados en la ilustración;
- `draw(rng_for)`: geometría SVG del animal;
- llamadas a `wash`, `stroke`, `blob` y `scale_marks` para el acabado de acuarela.

No pegues una investigación larga dentro del módulo Python. Enlaza la ficha
Markdown con `reference_file` y deja en `META` solo el resumen que necesita el
generador.

## Instalación

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

`cairosvg` se usa para exportar a PNG, pero en Windows necesita además la biblioteca nativa Cairo. Instalar solamente `cairosvg` puede producir un error como `no library called "cairo-2" was found`. La solución recomendada en Windows es instalar [Inkscape](https://inkscape.org/release/) y volver a ejecutar el comando; el exportador busca también las rutas habituales de Inkscape aunque no estén en `PATH`. Como alternativa, instala `rsvg-convert`/librsvg. Si solo necesitas la ilustración vectorial, usa `--no-png`.

### Windows: Cairo e Inkscape

`requirements.txt` contiene las dependencias de Python, pero no puede instalar
Inkscape ni las DLL nativas de Cairo. En Windows se ha configurado Inkscape
1.4.4 y se ha añadido esta carpeta al PATH de usuario:

```text
C:\Program Files\Inkscape\bin
```

Esa carpeta contiene `libcairo-2.dll`. Si instalas Inkscape en otro equipo,
añade su carpeta `bin` al PATH o deja que el exportador la encuentre en la
ubicación habitual. Después de modificar el PATH, cierra y vuelve a abrir
PowerShell o VS Code.

Para comprobar la instalación:

```bash
inkscape --version
```

Si aparece un error de Cairo, puedes seguir trabajando con SVG mientras
instalas Inkscape:

```bash
# Siempre funciona sin Cairo: conserva el SVG
python generate.py aepyornis --no-png

# Después de instalar Inkscape, genera SVG y PNG
python generate.py aepyornis
```

## Crear una ilustración de una especie, paso a paso

Este es el flujo recomendado para pasar de una idea o una especie de tus notas a una lámina terminada.

### Paso 1: elegir y nombrar la especie

Escoge una especie de `docs/especies-notas.md` o añade una nueva. Define un identificador simple, en minúsculas y con guiones bajos: `dodo`, `pinguinus_impennis` o `capra_pyrenaica_lusitanica`. Ese identificador se utilizará en los nombres de archivos y en el comando de generación.

Para crear automáticamente los dos archivos iniciales:

```bash
python new_species.py dodo "Raphus cucullatus" "Dodo" --kind bird --landscape generic
```

El comando crea el módulo Python y la ficha Markdown, y nunca sobrescribe una especie existente. El módulo incluye también los campos `distribution`, `habitat`, `visual_notes` y `extinction_notes`; hay que rellenarlos con la investigación antes de dibujar la versión definitiva.

### Paso 2: crear la carpeta de trabajo

Dentro de `references/species/`, utiliza la ficha Markdown del identificador:

```text
references/
└── species/
    ├── pinguinus_impennis.md
    └── pinguinus_impennis_bocetos/
        ├── boceto_postura.jpg
        └── referencia_historica.png
```

### Paso 3: completar la investigación

Copia [`docs/plantilla-especie.md`](docs/plantilla-especie.md) y guárdala como `references/species/<identificador>.md`. Incluye nombre científico y nombres históricos o comunes, fecha y lugar aproximados de desaparición, descripción anatómica, hábitat, grado de certeza, fuentes, decisiones visuales y advertencias para no presentar una hipótesis como un hecho.

Los bocetos pueden guardarse en `references/species/<identificador>_bocetos/`. Anota para cada imagen su autoría, licencia y enlace de origen. Un boceto puede orientar la postura, el tamaño, la silueta o los colores, pero no se incorpora automáticamente al SVG.

### Paso 4: crear el módulo de dibujo

Copia uno de los módulos de `extinct_art/species/` como `extinct_art/species/<identificador>.py`, o parte de una ficha ya preparada. Cada módulo contiene `META`, `COLORS` y `draw(rng_for)`. `META` debe contener:

```python
META = {
    "scientific_name": "Pinguinus impennis",
    "common_name": "Alca gigante",
    "slug": "pinguinus_impennis",
    "kind": "bird",           # bird, mammal o reptile
    "landscape": "generic",   # sustituir por un paisaje disponible
    "status": "extinta",
    "description": "Ave marina no voladora del Atlántico norte.",
}
```

La función `draw` devuelve fragmentos SVG. Las fichas nuevas reutilizan `draw_taxon` de `extinct_art/species/base.py`, que ofrece perfiles iniciales de ave, mamífero o reptil. El perfil se deriva del identificador de la especie, de modo que especies distintas no parten exactamente de la misma silueta, proporción, cola, pico, orejas o tono. Para una ilustración fiel hay que sustituir esa silueta inicial por geometría específica usando `wash`, `stroke`, `blob` y `scale_marks` desde `extinct_art/brush.py`. El papel, el grano, el paisaje y la rama los añade `compose.py` automáticamente. Los campos `distribution`, `habitat`, `visual_notes` y `extinction_notes` se conservan en `META` y se incluyen en la descripción accesible del SVG.

### Paso 5: registrar la especie

No hace falta editar manualmente `extinct_art/species/__init__.py`. El proyecto descubre automáticamente todos los módulos `.py` de esa carpeta que tengan `META` y `draw`. Comprueba el registro con:

```python
python generate.py --validate
python generate.py --list
python generate.py pinguinus_impennis --describe
```

### Paso 6: generar una primera versión

```bash
python generate.py --list
python generate.py pinguinus_impennis --seed 7
python generate.py pinguinus_impennis --palette sepia --no-png
python generate.py pinguinus_impennis --all-palettes --width 2160
python generate.py --all-species --no-png
```

`--validate` comprueba los campos obligatorios, el grupo animal, las URLs y la existencia de cada ficha Markdown. `--describe` muestra los metadatos que utilizará el generador.

Los archivos aparecen en `output/`. Esa carpeta se puede borrar y regenerar; las fuentes, fichas y bocetos deben conservarse en `references/`.

### Paso 7: revisar la ilustración

Abre el SVG o PNG y comprueba la silueta, la postura, los colores, el paisaje, el rótulo y el grado de fidelidad de cada rasgo. Si algo no está respaldado por una fuente, indícalo como interpretación en la ficha. Ajusta `COLORS`, las formas SVG y `META["description"]`, y vuelve a generar con la misma semilla para comparar cambios.

### Paso 8: conservar una versión reproducible

Apunta en la ficha el comando utilizado, por ejemplo:

```text
python generate.py pinguinus_impennis --palette sepia --seed 7 --width 2160
```

Conserva la ficha, las fuentes y los bocetos. El contenido de `output/` no es necesario para reconstruir la imagen, porque el proyecto lo genera de nuevo.

## Mejoras posibles del proyecto

### Mejoras ya aplicadas

- Se han creado módulos Python para los 58 taxones de las anotaciones.
- El registro de especies es automático: añadir un `.py` con `META` y `draw` basta.
- Se puede validar el catálogo con `python generate.py --validate`.
- Se pueden generar todas las especies con `python generate.py --all-species`.
- Las siluetas iniciales se reutilizan por grupo animal mediante `species/base.py`.
- Las fichas y los módulos guardan el enlace de referencia usado para investigar cada taxón.
- Se ha añadido un paisaje `generic` para evitar asignar Jamaica a especies que no corresponden a ese lugar.
- `new_species.py` crea una ficha y un módulo nuevos sin sobrescribir archivos existentes.
- La validación comprueba también las URLs y la existencia de las fichas Markdown.
- `--describe` permite revisar los metadatos antes de generar una lámina.
- Los tests comprueban la integridad del catálogo completo.

Las fichas nuevas son una base visual inicial: los módulos funcionan y generan SVG, y ahora contienen un resumen de investigación para orientar el dibujo. Una reconstrucción anatómica rigurosa requiere sustituir la silueta genérica de cada especie por geometría específica después de revisar sus restos, ejemplares, láminas y descripciones. Las fechas, sinonimias y colores deben volver a comprobarse antes de publicar.

Estas son las mejoras que considero más útiles, ordenadas aproximadamente por prioridad:

1. **Separar los datos del dibujo.** Mover `META` y las referencias a JSON o YAML para que una futura interfaz edite fichas sin tocar Python.
2. **Generar una composición de estudio.** Incluir nombre, descripción, estado, fecha y fuentes en una lámina documental.
3. **Añadir un modo de boceto.** Mostrar una imagen de referencia junto al resultado, conservando autoría y licencia.
4. **Incorporar más perfiles reutilizables.** Añadir peces, anfibios, plantas, aves marinas, mamíferos con cuernos y animales no voladores.
5. **Crear una galería de previsualización.** Generar una cuadrícula HTML o contacto PNG con todas las especies y paletas.
6. **Mejorar la salida editorial.** Añadir formatos de impresión, márgenes, tipografías y exportación para redes sociales.
7. **Refinar la anatomía especie por especie.** Sustituir las siluetas genéricas por geometría basada en ejemplares, restos y láminas históricas.
8. **Revisar taxonomía y licencias.** Mantener fuentes, sinonimias, fechas y permisos en cada ficha de referencia.

La mejora más valiosa para el uso diario sería la primera: permitiría cambiar nombres, descripciones, fuentes y notas sin tocar el código que dibuja la anatomía. La generación automática a partir de un boceto podría añadirse más adelante, pero debería mantener una revisión humana porque muchas especies extintas solo se conocen de forma incompleta.

## Opciones de generación

```text
new_species.py SLUG "Nombre científico" "Nombre común" --kind bird|mammal|reptile
--describe              muestra los metadatos de la especie elegida
--validate              valida especies y fichas
--all-species            genera una imagen por cada especie
--palette NOMBRE       acuarela_antigua, sepia, amanecer, verde_humedal,
                       ocaso_rojizo o niebla_azul
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
| `generate.py` | Interfaz de línea de comandos y generación por lotes |
| `new_species.py` | Crea el módulo y la ficha de una especie nueva |
| `extinct_art/compose.py` | Composición de papel, paisaje, rama y especie |
| `extinct_art/species/` | Una ficha visual Python por especie |
| `extinct_art/species/base.py` | Siluetas y primitivas reutilizables por grupo animal |
| `extinct_art/species/__init__.py` | Descubrimiento y validación automática de módulos |
| `extinct_art/brush.py` | Manchas, pinceladas, bordes y textura |
| `extinct_art/palettes.py` | Paletas de la lámina |
| `extinct_art/landscapes.py` | Paisajes disponibles |
| `references/species/` | Una ficha Markdown por cada taxón de las anotaciones |
| `references/` | Fuentes, bocetos y material de trabajo |
| `docs/plantilla-especie.md` | Plantilla para investigar una especie |
| `docs/especies-notas.md` | Anotaciones recibidas para futuras ilustraciones |
| `output/` | SVG y PNG generados |

## Criterios de documentación y rigor

Estas láminas son interpretaciones artísticas, no reconstrucciones exactas. Cuando una especie solo se conoce por relatos, restos o una lámina posterior, esa incertidumbre debe aparecer en `META`, en la ficha y, si procede, en la publicación final. Conviene distinguir entre nombre científico moderno, nombres usados históricamente y nombres populares.

La lista de animales de `docs/especies-notas.md` es un punto de partida, no una verificación taxonómica definitiva. Antes de dibujar o publicar una especie, comprueba su estado, sinonimias, fecha de extinción y fuentes primarias o institucionales.

## Variedad visual

Ademas de las paletas originales, se pueden usar `verde_humedal`, `ocaso_rojizo`
y `niebla_azul`. Los paisajes disponibles son `jamaica`, `generic`, `humedal`,
`costa` y `bosque`.

Si la especie usa `generic` y no se indica `--landscape`, `compose.py` elige un
paisaje de forma automatica y reproducible segun la especie y la semilla. Para
fijar una combinacion concreta:

```bash
python generate.py pinguinus_impennis --palette verde_humedal --landscape humedal
```

`brush.py` incluye ahora salpicaduras, pincel seco, veladuras de luz y ondas de
agua. Estas herramientas se combinan con las siluetas de `species/base.py` para
que las especies tengan diferencias de textura, color y ambiente.

## Datos visuales investigados y perfiles anatómicos

Cada especie tiene ahora una capa de información visual en
`extinct_art/species/drawing_data.py`. Esta capa se carga automáticamente al
iniciar el catálogo y amplía `META` con:

- `description`: descripción práctica para construir la ilustración;
- `visual_notes`: rasgos que deben verse en la silueta;
- `drawing_notes`: qué está respaldado y qué debe tratarse como hipótesis;
- `reference_taxa`: especies actuales usadas únicamente como comparación
  funcional;
- `profile`: rasgos que puede dibujar `species/base.py`;
- `research_sources`: enlaces externos usados cuando hay información anatómica
  especialmente detallada.

Las fichas Markdown de `references/species/` contienen la misma información en
la sección **Descripción útil para el dibujo**. La guía general está en
[`references/species/drawing-data.md`](references/species/drawing-data.md).

### Cómo se usan las especies actuales

Una especie viva no se copia automáticamente. Solo se utiliza para resolver
una estructura cuando existe una relación taxonómica o funcional razonable:

```text
fuentes, restos y descripciones históricas
                    ↓
rasgos confirmados de la especie extinta
                    ↓
especie actual comparable, solo como referencia anatómica
                    ↓
perfil específico de base.py + colores documentados o marcados como hipótesis
```

Por ejemplo, un *Psittacula exsul* puede tomar de otros *Psittacula* la
proporción general del pico y la cola, pero conserva los colores históricos
descritos para esa especie y no se convierte en una copia de un periquito vivo.
En taxones conocidos solo por relatos o restos fragmentarios se usa una
silueta prudente y se evita inventar patrones detallados.

### Perfiles disponibles en `base.py`

Además de los perfiles generales de ave, mamífero y reptil, se contemplan
ratites y aves no voladoras, loros, palomas, búhos, garzas, limícolas,
fringílidos, cánidos, felinos, osos, ungulados con cuernos, caballos, cebras,
roedores, marsupiales, murciélagos, mustélidos, geckos y serpientes. Cada
especie activa solo los rasgos compatibles con su descripción.

Para revisar los datos que utilizará el programa:

```bash
python generate.py pinguinus_impennis --describe
python generate.py dusicyon_australis --describe
python generate.py --validate
```

Al añadir una especie nueva, completa también su entrada en
`drawing_data.py`, actualiza la sección de descripción de su ficha Markdown y
marca claramente cualquier color, tamaño o conducta que sea una inferencia.

### Mejora reciente: las especies ya no comparten una silueta unica

La version anterior dibujaba casi todas las aves con el mismo cuerpo ovalado
y resolvia la diferencia mediante colores y pequenos detalles. Eso producia
imagenes reconocibles como acuarelas, pero no como animales diferentes. Ahora
`base.py` selecciona una anatomia por familia y por rasgos de la ficha:

- ratites y aves corredoras: torso vertical, cuello, patas largas y alas
  reducidas;
- loros y guacamayos: cabeza grande, pico curvado y cola diferenciada;
- dodos, palomas terrestres y rascones: cuerpo horizontal pesado y patas
  visibles;
- buhos: disco facial y ojos frontales;
- garzas, cormoranes y limicolas: cuello, pico y patas de ave acuatica;
- paseriformes: cuerpo pequeno, pico fino y cola proporcionada;
- ungulados: cuello, cuernos, crin y patas de mamifero con pezuñas;
- felinos, canidos, osos, roedores, marsupiales, mustelidos y murcielagos:
  siluetas cuadrupedas o membranas propias;
- serpientes y geckos: cuerpo reptiliano, cabeza y textura escamosa propias.

La prioridad de cada generacion es: anatomia documentada, proporcion,
postura, rasgos diagnosticos, color y por ultimo textura artistica. El color
de una referencia visual nunca puede convertir un dodo en un loro ni una
serpiente en un lagarto.

La informacion se organiza a partir de fuentes de museos, organizaciones
zoologicas y literatura especializada. Para el dodo se mantiene la cautela de
las reconstrucciones modernas: hay huesos abundantes, pero el tejido blando y
el color exacto siguen siendo inciertos. Para *Dusicyon australis* se usan las
medidas, patas cortas, orejas pequenas, pelaje mezclado y punta blanca de la
cola documentados por fuentes zoologicas. Para *Psittacula exsul* se conservan
los morfos verdes y azulados, las manchas rojas alares y el pico bicolor
descritos en fuentes especializadas. Los enlaces concretos estan en
`drawing_data.py` y en las fichas individuales.

Esto mejora la fidelidad, pero no convierte una reconstruccion en una
fotografia: cuando una especie solo se conoce por relatos, huesos o una
ilustracion antigua, la ficha mantiene la incertidumbre y separa hechos de
hipotesis.

Para comprobar rapidamente la diferencia entre perfiles:

```powershell
python generate.py aepyornis --no-png --out output/comparativa
python generate.py raphus_cucullatus --no-png --out output/comparativa
python generate.py dusicyon_australis --no-png --out output/comparativa
python generate.py hoplodactylus_delcourti --no-png --out output/comparativa
```

Si una especie nueva vuelve a parecer generica, no hay que tocar
`generate.py`: se corrigen su `profile`, `description`, `visual_notes` y
`drawing_notes` en `drawing_data.py`, se refleja la decision en su ficha
Markdown y se ejecuta `python generate.py --validate`.

## Referencias visuales descargadas

El script [`tools/download_reference_images.py`](tools/download_reference_images.py)
busca referencias en Wikimedia Commons y crea una carpeta por especie:

```text
references/species/
└── pinguinus_impennis_images/
    ├── 01_referencia.jpg
    ├── references.json
    └── README.md
```

`references.json` conserva la URL de Commons, la autoría y la licencia. Las
imágenes sirven para estudiar anatomía, color, postura y ambiente; no se
incrustan automáticamente en el SVG ni se presentan como una reconstrucción
de la especie. El programa incorpora sus rutas en `META["reference_images"]`
y las menciona en la descripción accesible del SVG.

Cuando existe al menos una imagen local, `extinct_art/reference.py` la analiza
con Pillow y obtiene una paleta media de referencia. `species/base.py` mezcla
esa paleta de forma muy suave con los colores de `COLORS` y del perfil de la
especie. Así las ilustraciones tienen en cuenta las láminas y bocetos usados,
pero una imagen con un fondo o un mapa no puede cambiar por sí sola la
anatomía: la forma sigue dependiendo de `META`, `PROFILE`, `drawing_data.py` y
la investigación Markdown.

Si no hay imagen descargada o Pillow no está instalado, la generación continúa
con los datos científicos y la paleta del módulo. Instala las dependencias con
`pip install -r requirements.txt`.

Para descargar una especie concreta:

```bash
python tools/download_reference_images.py --species ara_gossei --limit 3
```

Para el catálogo completo conviene respetar el límite de Wikimedia Commons:

```bash
python tools/download_reference_images.py --limit 1 --delay 5 --offset 0 --count 10
python tools/download_reference_images.py --limit 1 --delay 5 --offset 10 --count 10
python tools/download_reference_images.py --limit 1 --delay 5 --offset 20 --count 10
python tools/download_reference_images.py --limit 1 --delay 5 --offset 30 --count 10
python tools/download_reference_images.py --limit 1 --delay 5 --offset 40 --count 10
python tools/download_reference_images.py --limit 1 --delay 5 --offset 50 --count 10
```

Los lotes actualizan `reference-images-index.json` sin borrar los resultados
anteriores. Si Commons responde con `HTTP 429`, espera unos minutos y repite
solo el lote que estaba ejecutándose. No hay que borrar las carpetas ya
creadas. Una especie sin una imagen fiable queda documentada sin referencias,
en lugar de rellenarse con una imagen parecida pero engañosa.

El proceso completo no significa que todas las especies tengan tres imágenes:
los taxones discutidos o conocidos solo por textos pueden no tener una imagen
fiable en Commons. El objetivo es descargar todas las referencias abiertas que
se puedan verificar, no recopilar imágenes con copyright dudoso.

## Archivos nuevos para referencias

- `tools/download_reference_images.py`: descarga referencias abiertas por
  lotes y conserva sus licencias.
- `extinct_art/reference.py`: extrae una paleta cromática de las imágenes
  locales sin intentar sustituir la reconstrucción anatómica.
- `references/species/reference-images-index.json`: índice acumulado de las
  referencias encontradas.
- `requirements.txt`: incluye Pillow para leer PNG y JPEG locales.

## Uso normal: solo necesitas `generate.py`

Para crear una especie nueva desde cero, consulta la guía detallada:

[`docs/crear_especie_desde_cero.md`](docs/crear_especie_desde_cero.md)

Las especies nuevas creadas con `new_species.py` pueden guardar sus datos
visuales en `DRAWING_DATA` y sus fuentes en `RESEARCH_SOURCES` dentro de su
propio módulo. `drawing_data.py` se conserva como catálogo central de las
especies existentes para evitar duplicar información.

Después de instalar las dependencias, el flujo habitual es muy sencillo:

```powershell
python generate.py --list
python generate.py ara_gossei
python generate.py pinguinus_impennis --seed 12
```

El comando principal carga automáticamente las fichas Markdown, los datos de
`drawing_data.py`, los perfiles de `species/base.py`, las paletas, los
paisajes, las referencias visuales locales y las texturas. No tienes que
ejecutar `compose.py`, `base.py`, `reference.py` ni los módulos individuales
de `species/` directamente.

Los demás archivos cumplen funciones internas:

- `extinct_art/species/*.py`: instrucciones visuales de cada especie;
- `references/species/*.md`: investigación y decisiones de dibujo;
- `drawing_data.py`: datos visuales ampliados que conectan investigación y
  generación;
- `compose.py`, `base.py`, `brush.py`, `palettes.py` y `landscapes.py`:
  componentes reutilizables cargados por `generate.py`;
- `tools/download_reference_images.py`: herramienta opcional para actualizar
  referencias de Internet; no hace falta ejecutarla para generar una imagen.

Solo necesitarás editar archivos internos cuando quieras añadir una especie,
corregir una fuente o mejorar su anatomía. Para el uso diario, el punto de
entrada es siempre `generate.py`.

## Comprobacion de fichas Markdown y modulos Python

La informacion no se mantiene duplicada manualmente en 58 archivos Python.
Cada modulo contiene la identidad basica, la distribucion, el habitat y la
funcion `draw()`. Al cargar el catalogo, `extinct_art/species/__init__.py`
incorpora automaticamente a ese modulo los campos investigados de
`drawing_data.py`: descripcion, rasgos visuales, guia de dibujo,
comparaciones prudentes, perfil anatomico, colores y fuentes.

Esto significa que, durante una ejecucion normal, el modulo Python si recibe
la informacion relevante de su ficha Markdown, pero existe una unica fuente
de datos ampliados para evitar que la ficha y el codigo se separen. El comando
`--validate` comprueba ahora que cada valor visual cargado tambien aparece en
`references/species/<slug>.md`. Si falta algo, la validacion lo indica antes
de generar imagenes.

## Ubicacion geografica en la lamina

Cada especie obtiene `META["location_label"]` a partir de la distribucion ya
documentada en su ficha. Esa etiqueta aparece junto al nombre cientifico en
el pie de la ilustracion, por ejemplo:

```text
Raphus cucullatus · Mauricio (isla)
```

La misma ubicacion selecciona un fondo regional cuando es razonable. Las
especies de Mauricio, Rodrigues, Reunión, Madagascar, Lord Howe, Macquarie,
Chatham, Tahití, Raiatea, Moorea, las Malvinas y otras islas usan un horizonte
oceánico con relieve insular. `Ara gossei` conserva específicamente
`Blue Mountains, Jamaica`. Las especies continentales o de localidad dudosa
mantienen un fondo ecológico más prudente. La ubicación no inventa una
localidad exacta: si la fuente solo dice una isla o región, eso es lo que se
muestra.

## Tests

```bash
python -m unittest discover
```

Los tests comprueban que todas las especies y paletas producen XML válido y que la semilla mantiene la reproducibilidad.

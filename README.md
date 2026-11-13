# Extinct Animals Art

Generador local de láminas ilustradas sobre especies extintas o desaparecidas.
Combina investigación, bocetos SVG reproducibles, paisajes regionales y
texturas de acuarela sin depender de modelos de IA ni servicios externos.

La entrada principal es siempre:

```powershell
python generate.py <especie>
```

Ejemplos:

```powershell
python generate.py ara_gossei
python generate.py raphus_cucullatus --seed 12
```

## Qué genera

El modo normal crea una lámina SVG y, si existe un
renderizador, también un PNG. Incluye el animal, un paisaje compatible con su
distribución, papel, rama, textura, nombre científico, nombre común, ubicación
probable y una descripción accesible de la ficha.


## Generación sin modelo

### SVG: rápido y reproducible

```powershell
python generate.py ara_gossei
```

Funciona sin modelos de IA. La misma especie y semilla producen el mismo
boceto y permiten revisar anatomía, composición, metadatos y paisaje.

## Instalación

Desde la carpeta del proyecto:

```powershell
python -m pip install -r requirements.txt
```

`cairosvg` y `Pillow` son dependencias Python. En Windows, CairoSVG puede
necesitar Cairo nativo; Inkscape sirve como alternativa para convertir SVG a
PNG. El programa avisa si no encuentra ningún motor de renderizado.


## Comandos importantes

```powershell
python generate.py --list
python generate.py pinguinus_impennis --describe
python generate.py --validate
python generate.py ara_gossei --no-png
python generate.py ara_gossei --landscape jamaica --palette sepia --seed 19
python generate.py --all-species --no-png
```

## Organización de una especie

Cada taxón tiene dos fuentes coordinadas:

```text
extinct_art/species/raphus_cucullatus.py
references/species/raphus_cucullatus/raphus_cucullatus.md
references/species/raphus_cucullatus/references.json
references/species/raphus_cucullatus/01_referencia.jpg
```

El módulo Python contiene lo que el programa necesita para dibujar:

- `META`: identidad, distribución, hábitat, estado y descripción breve;
- `PROFILE`: rasgos anatómicos que activan las formas de `base.py`;
- `COLORS`: colores documentados o marcados como hipótesis;
- `DRAWING_DATA`: descripción útil para el dibujo y límites de la evidencia;
- `RESEARCH_SOURCES`: fuentes utilizadas;
- `draw(rng_for)`: devuelve las formas SVG del animal.

La ficha Markdown contiene la investigación extensa, fuentes, decisiones
visuales e incertidumbres. El Markdown no dibuja por sí solo. Si se modifica la
ficha, hay que trasladar al módulo Python cualquier cambio que deba afectar a
la imagen.

No existe un `drawing_data.py` central. Los datos visuales de cada especie
viven junto a su módulo para que no haya que perseguir información por varios
catálogos.

## Flujo visual

```text
ficha Markdown
    ↓
META + DRAWING_DATA + PROFILE + COLORS
    ↓
base.py o draw() específico
    ↓
boceto SVG del animal
    ↓
compose.py añade paisaje, papel, rama y rótulo
    ↓
lámina SVG/PNG final
```

`base.py` ya no usa solamente `kind`. Primero aplica el perfil de la especie y
después activa una anatomía compatible:

- ratitas: torso vertical, cuello y patas largos;
- dodo y palomas terrestres: cuerpo pesado, alas reducidas y pico propio;
- loros: cabeza grande, pico curvado y cola larga;
- aves marinas: postura erguida, alas cortas y pico especializado;
- garzas y limícolas: cuello y patas largos;
- ungulados y caballos: cuello, patas y pezuñas;
- felinos, cánidos, osos, roedores y mustélidos: siluetas de mamífero;
- murciélagos: membranas alares;
- serpientes y geckos: cuerpo reptiliano y textura escamosa.

Las especies con más evidencia o importancia visual pueden tener una función
anatómica dedicada. `Ara gossei` es el ejemplo más detallado: sus formas están
dibujadas en su propio módulo porque es un taxón hipotético y no debe
presentarse como una reconstrucción segura.

`Aepyornis` también tiene ahora una composición específica: cuerpo enorme,
cuello robusto, cabeza relativamente pequeña, alas reducidas, patas visibles y
huevo de referencia. Su escala se ajusta al marco para que no se corten la
cabeza ni los pies. Las ratitas de tipo `Dromaius` usan además una escala
limitada para permanecer dentro del cuadro.

## Referencias visuales

Las imágenes se guardan dentro de la carpeta de cada especie. Sirven para
documentar postura, color, proporciones y comparaciones. El programa extrae de
ellas una paleta orientativa cuando es posible, pero no copia automáticamente
su anatomía: una lámina histórica puede ser artística o científicamente
incorrecta.

Las referencias se usan para decidir la anatomía, la postura y la paleta del
módulo Python. No se copian automáticamente: una lámina histórica puede ser
artística o científicamente incorrecta.

## Calidad y límites científicos

La prioridad de cada generación es:

1. anatomía documentada;
2. proporciones y postura;
3. rasgos diagnósticos;
4. color respaldado por fuentes o marcado como hipótesis;
5. ambiente y ubicación;
6. textura artística.

Cuando un rasgo no está documentado se debe escribir como hipótesis en
`DRAWING_DATA` y en la ficha Markdown. Una especie actual solo sirve como
comparación funcional, no convierte a la especie extinta en una copia de ella.

El modo híbrido mejora el acabado, pero no verifica por sí mismo la verdad
científica. Hay que revisar cada resultado y descartar deformaciones, rasgos
modernos o colores no respaldados.

## Crear una especie nueva

```powershell
python new_species.py --slug nombre_especie --scientific-name "Nombre especie" --common-name "Nombre común"
```

Después:

1. Completa la investigación en `references/species/<slug>/<slug>.md`.
2. Añade fuentes y referencias visuales en esa misma carpeta.
3. Completa `META`, `DRAWING_DATA`, `PROFILE` y `COLORS` en el módulo Python.
4. Escoge solo rasgos anatómicos compatibles con la evidencia.
5. Ejecuta `python generate.py <slug> --describe`.
6. Ejecuta `python generate.py --validate`.
7. Genera el boceto con `python generate.py <slug>`.
8. Revisa la ilustración y anota qué es seguro y qué es interpretativo.

No hay que editar `__init__.py`, `compose.py` ni `generate.py` para registrar
una especie normal: el catálogo descubre automáticamente los módulos que
contienen `META` y `draw()`.

## Archivos principales

| Archivo | Función |
|---|---|
| `generate.py` | Único punto de entrada para generar y validar |
| `extinct_art/compose.py` | Une animal, paisaje, papel y rótulo |
| `extinct_art/species/<slug>.py` | Datos y dibujo de cada especie |
| `extinct_art/species/base.py` | Anatomías reutilizables y perfiles específicos |
| `extinct_art/brush.py` | Lavados, pinceladas y textura |
| `extinct_art/landscapes.py` | Fondos regionales |
| `extinct_art/palettes.py` | Paletas de la lámina |
| `extinct_art/reference.py` | Manifiestos y paletas de referencias |
| `references/species/` | Fichas Markdown, fuentes e imágenes |
| `output/` | Resultados generados; se puede regenerar |

## Verificación

```powershell
python generate.py --validate
python -m unittest discover -s tests -q
python generate.py ara_gossei --seed 7
python generate.py raphus_cucullatus --seed 7
python generate.py aepyornis --seed 7
```

Los tres comandos deben producir láminas válidas y reproducibles.

## Próximas mejoras

- Crear funciones anatómicas dedicadas para las especies restantes con
  suficiente evidencia.
- Detectar automáticamente animales recortados, duplicados o deformados.
- Mantener licencias, autores y URLs de cada referencia.
- Añadir una galería comparativa de SVG, boceto y resultado híbrido.

El modo SVG no necesita modelos, funciona sin conexión, es reproducible y
mantiene el control total del dibujo. La calidad se consigue traduciendo la
investigación de cada ficha a geometría anatómica específica.

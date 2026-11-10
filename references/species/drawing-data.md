# Datos visuales ampliados

Los módulos Python cargan los datos de `extinct_art/species/drawing_data.py` al
iniciarse. Esa capa amplía cada ficha con:

- `description`: resumen que orienta la imagen.
- `visual_notes`: rasgos visibles que se pueden representar.
- `drawing_notes`: separación entre rasgos documentados e hipótesis.
- `reference_taxa`: especies actuales usadas solo como comparación funcional.
- `profile`: rasgos que `species/base.py` sabe dibujar.

Las comparaciones actuales no sustituyen a la especie extinta. Sirven para
resolver una forma anatómica solo cuando la descripción, los restos o las
afinidades taxonómicas lo permiten. Por ejemplo, `Psittacula exsul` puede usar
un periquito del género Psittacula como referencia de proporciones, pero no se
le asigna automáticamente el plumaje de una especie viva concreta.

## Fuentes de detalle anatómico

Las entradas con información especialmente útil conservan sus enlaces en
`META["research_sources"]` y se pueden consultar con:

```bash
python generate.py pinguinus_impennis --describe
```

Entre ellas están el Natural History Museum para el alca gigante, el dodo y
los restos de aves ratites; Animal Diversity Web para el warrah; el informe
histórico de IUCN para el uro y la cabra montés portuguesa; World Parrot Trust
para el periquito de Newton; y Birds New Zealand para el grupo Cyanoramphus.

## Criterio de reconstrucción

1. Se conserva como hecho la anatomía respaldada por ejemplares, restos o
   descripciones históricas.
2. Se marca como hipótesis todo color, patrón o proporción que no esté fijado.
3. Una especie viva se usa únicamente para completar una estructura ausente,
   nunca para convertir la especie extinta en una copia de ella.
4. En los taxones discutidos o conocidos solo por relatos se prioriza una
   silueta prudente y una paleta desaturada.

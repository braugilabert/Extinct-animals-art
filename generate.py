#!/usr/bin/env python3
"""Genera ilustraciones de especies extintas (SVG + PNG) en local y gratis.

Ejemplos:
    python generate.py                          # Ara gossei con la paleta por defecto
    python generate.py ara_gossei --seed 12     # otra variación del "pincel"
    python generate.py --palette sepia
    python generate.py --all-palettes           # una imagen por paleta
    python generate.py --no-png                 # solo SVG
    python generate.py --list
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from extinct_art.compose import build_svg
from extinct_art.landscapes import LANDSCAPES
from extinct_art.palettes import PALETTES
from extinct_art.render import RenderError, svg_to_png
from extinct_art.species import SPECIES, validate_species


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("species", nargs="?", default="ara_gossei", help="especie a dibujar")
    p.add_argument("--all-species", action="store_true", help="genera una imagen de cada especie registrada")
    p.add_argument("--palette", default="acuarela_antigua", help="paleta de la escena")
    p.add_argument("--all-palettes", action="store_true", help="genera una imagen por cada paleta")
    p.add_argument("--landscape", default=None, help="paisaje de fondo (por defecto, el de la especie)")
    p.add_argument("--seed", type=int, default=7, help="semilla del pincel (misma semilla = misma imagen)")
    p.add_argument("--width", type=int, default=1080, help="ancho del PNG en píxeles (4:5 -> alto = ancho x 1.25)")
    p.add_argument("--out", default="output", help="carpeta de salida")
    p.add_argument("--no-png", action="store_true", help="no exportar PNG")
    p.add_argument("--no-caption", action="store_true", help="sin rótulo inferior")
    p.add_argument("--no-grain", action="store_true", help="sin granulado de papel")
    p.add_argument("--no-flower", action="store_true", help="sin hibisco en la rama")
    p.add_argument("--list", action="store_true", help="muestra especies, paletas y paisajes")
    p.add_argument("--validate", action="store_true", help="valida los metadatos de las especies")
    p.add_argument("--describe", action="store_true", help="muestra los metadatos de la especie elegida")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if args.validate:
        errors = validate_species(Path.cwd())
        if errors:
            print("Errores de metadatos:")
            print("\n".join(f"- {error}" for error in errors))
            return 1
        print(f"Metadatos válidos: {len(SPECIES)} especies")
        return 0

    if args.list:
        print(f"Especies ({len(SPECIES)}):", ", ".join(SPECIES))
        print("Paletas: ", ", ".join(PALETTES))
        print("Paisajes:", ", ".join(LANDSCAPES))
        return 0

    if args.describe:
        if args.species not in SPECIES:
            print(f"Error: especie desconocida: {args.species}", file=sys.stderr)
            return 1
        for key, value in SPECIES[args.species].META.items():
            print(f"{key}: {value}")
        return 0

    if args.all_species and args.species != "ara_gossei":
        print("Aviso: --all-species ignora la especie posicional.", file=sys.stderr)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    species_names = list(SPECIES) if args.all_species else [args.species]
    palettes = list(PALETTES) if args.all_palettes else [args.palette]

    for species_name in species_names:
        for palette in palettes:
            try:
                svg = build_svg(
                    species=species_name, palette=palette, landscape=args.landscape,
                    seed=args.seed, caption=not args.no_caption,
                    grain=not args.no_grain, flower=not args.no_flower,
                )
            except KeyError as exc:
                print(f"Error: {exc.args[0]}", file=sys.stderr)
                return 1

            stem = f"{species_name}_{palette}_s{args.seed}"
            svg_path = out_dir / f"{stem}.svg"
            svg_path.write_text(svg, encoding="utf-8")
            print(f"SVG: {svg_path}")

            if not args.no_png:
                png_path = out_dir / f"{stem}.png"
                try:
                    engine = svg_to_png(svg_path, png_path, width=args.width)
                except RenderError as exc:
                    print(f"Aviso: {exc}", file=sys.stderr)
                    return 2
                print(f"PNG: {png_path}  (motor: {engine})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

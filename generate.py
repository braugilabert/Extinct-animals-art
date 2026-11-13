#!/usr/bin/env python3
"""Genera ilustraciones de especies extintas en local y gratis."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from extinct_art.compose import build_svg
from extinct_art.comfyui import DEFAULT_URL as COMFYUI_DEFAULT_URL, generate as comfy_generate
from extinct_art.landscapes import LANDSCAPES
from extinct_art.ollama_support import (
    DEFAULT_MODEL,
    DEFAULT_URL,
    analyze_species,
    apply_svg_guidance,
    write_analysis,
)
from extinct_art.palettes import PALETTES
from extinct_art.render import RenderError, svg_to_png
from extinct_art.species import SPECIES, validate_species


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("species", nargs="?", default="ara_gossei", help="especie a dibujar")
    p.add_argument("--all-species", action="store_true", help="genera una imagen de cada especie")
    p.add_argument("--palette", default="acuarela_antigua", help="paleta de la escena")
    p.add_argument("--all-palettes", action="store_true", help="genera una imagen por cada paleta")
    p.add_argument("--landscape", default=None, help="paisaje de fondo")
    p.add_argument("--seed", type=int, default=7, help="semilla reproducible del pincel")
    p.add_argument("--width", type=int, default=1080, help="ancho del PNG en píxeles")
    p.add_argument("--out", default="output", help="carpeta de salida")
    p.add_argument("--no-png", action="store_true", help="no exportar PNG")
    p.add_argument("--no-caption", action="store_true", help="sin rótulo inferior")
    p.add_argument("--no-grain", action="store_true", help="sin granulado de papel")
    p.add_argument("--no-flower", action="store_true", help="sin hibisco en la rama")
    p.add_argument("--ollama", action="store_true", help="analiza fichas y referencias con Ollama")
    p.add_argument("--ollama-model", default=DEFAULT_MODEL,
                   help=f"modelo de visión, por defecto {DEFAULT_MODEL}")
    p.add_argument("--ollama-url", default=DEFAULT_URL, help="URL local de Ollama")
    p.add_argument("--ollama-images", type=int, default=5,
                   help="máximo de imágenes de referencia enviadas a Ollama")
    p.add_argument("--comfyui", action="store_true",
                   help="envía el boceto a ComfyUI mediante su API local")
    p.add_argument("--comfyui-url", default=COMFYUI_DEFAULT_URL,
                   help="URL local de ComfyUI")
    p.add_argument("--checkpoint", default=None,
                   help="nombre del checkpoint instalado en ComfyUI")
    p.add_argument("--comfyui-steps", type=int, default=24,
                   help="pasos del workflow de ComfyUI")
    p.add_argument("--comfyui-denoise", type=float, default=.55,
                   help="fuerza img2img de ComfyUI, entre 0 y 1")
    p.add_argument("--list", action="store_true", help="muestra especies, paletas y paisajes")
    p.add_argument("--validate", action="store_true", help="valida los metadatos")
    p.add_argument("--describe", action="store_true", help="muestra los metadatos de la especie")
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
        print("Paletas:", ", ".join(PALETTES))
        print("Paisajes:", ", ".join(LANDSCAPES))
        return 0
    if args.describe:
        if args.species not in SPECIES:
            print(f"Error: especie desconocida: {args.species}", file=sys.stderr)
            return 1
        for key, value in SPECIES[args.species].META.items():
            print(f"{key}: {value}")
        return 0
    if args.species not in SPECIES and not args.all_species:
        print(f"Error: especie desconocida: {args.species}", file=sys.stderr)
        return 1

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    species_names = list(SPECIES) if args.all_species else [args.species]
    palettes = list(PALETTES) if args.all_palettes else [args.palette]

    for species_name in species_names:
        module = SPECIES[species_name]
        analysis = None
        ollama_error = None
        if args.ollama:
            try:
                analysis = analyze_species(
                    Path.cwd(), module, model=args.ollama_model,
                    base_url=args.ollama_url, max_images=args.ollama_images,
                )
                changes = apply_svg_guidance(module, analysis)
                if changes:
                    print(f"Cambios visuales de Ollama para {species_name}: {', '.join(changes)}")
                else:
                    print(f"Ollama analizó {species_name}, pero no propuso cambios SVG aplicables.")
            except RuntimeError as exc:
                ollama_error = exc
                print(f"Aviso de Ollama: {exc}", file=sys.stderr)

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

            sketch_path = out_dir / f"{stem}_comfy_sketch.png"
            if not args.no_png:
                png_path = out_dir / f"{stem}.png"
                try:
                    engine = svg_to_png(svg_path, png_path, width=args.width)
                except RenderError as exc:
                    print(f"Aviso: {exc}", file=sys.stderr)
                    return 2
                print(f"PNG: {png_path}  (motor: {engine})")

            if args.comfyui:
                if args.no_png:
                    try:
                        svg_to_png(svg_path, sketch_path, width=args.width)
                    except RenderError as exc:
                        print(f"Aviso: no se pudo crear el boceto para ComfyUI: {exc}", file=sys.stderr)
                        return 2
                else:
                    sketch_path = png_path
                comfy_path = out_dir / f"{stem}_comfy.png"
                try:
                    comfy_generate(
                        module, sketch_path, comfy_path, args.comfyui_url,
                        args.checkpoint, args.seed, steps=args.comfyui_steps,
                        denoise=args.comfyui_denoise,
                    )
                except Exception as exc:
                    print(f"Error de ComfyUI: {exc}", file=sys.stderr)
                    return 3
                print(f"ComfyUI: {comfy_path}")

            if analysis is not None:
                analysis_path = write_analysis(out_dir, stem, module, analysis)
                print(f"Análisis Ollama: {analysis_path}")

        if ollama_error is not None:
            return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())

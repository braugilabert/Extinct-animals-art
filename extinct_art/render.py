"""Exportar SVG -> PNG con herramientas gratuitas y locales.

Orden de preferencia: cairosvg (pip) -> rsvg-convert -> Inkscape.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class RenderError(RuntimeError):
    pass


def svg_to_png(svg_path, png_path, width: int = 1080) -> str:
    """Convierte un SVG en PNG de `width` px de ancho. Devuelve qué motor se usó."""
    svg_path, png_path = Path(svg_path), Path(png_path)
    errors: list[str] = []

    try:
        import cairosvg  # type: ignore
    except (ImportError, OSError) as exc:  # OSError: falta la librería Cairo del sistema
        errors.append(f"cairosvg no disponible ({exc})")
    else:
        try:
            cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=width)
            return "cairosvg"
        except Exception as exc:  # noqa: BLE001
            errors.append(f"cairosvg falló ({exc})")

    exe = shutil.which("rsvg-convert")
    if exe:
        subprocess.run([exe, "-w", str(width), "-o", str(png_path), str(svg_path)], check=True)
        return "rsvg-convert"

    exe = shutil.which("inkscape")
    if exe:
        subprocess.run(
            [exe, str(svg_path), "--export-type=png",
             f"--export-filename={png_path}", f"--export-width={width}"],
            check=True,
        )
        return "inkscape"

    raise RenderError(
        "No se pudo crear el PNG. Instala cairosvg (pip install cairosvg), "
        "librsvg (rsvg-convert) o Inkscape. Detalle: " + "; ".join(errors)
    )

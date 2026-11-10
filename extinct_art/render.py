"""Exportar SVG -> PNG con herramientas gratuitas y locales.

Orden de preferencia: cairosvg (pip) -> rsvg-convert -> Inkscape.
"""
from __future__ import annotations

import shutil
import subprocess
import os
import sys
from pathlib import Path


class RenderError(RuntimeError):
    pass


_DLL_HANDLES = []


def _windows_tool(name: str) -> str | None:
    """Encuentra ejecutables instalados pero no incluidos en PATH."""
    found = shutil.which(name)
    if found or sys.platform != "win32":
        return found
    candidates = [
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Inkscape" / "bin" / f"{name}.exe",
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "GTK3-Runtime Win64" / "bin" / f"{name}.exe",
        Path(r"C:\msys64\mingw64\bin") / f"{name}.exe",
    ]
    return next((str(path) for path in candidates if path.exists()), None)


def _prepare_cairo_dll_search() -> None:
    """Añade rutas habituales de DLL antes de importar CairoSVG en Windows."""
    if sys.platform != "win32" or not hasattr(os, "add_dll_directory"):
        return
    roots = [
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Inkscape" / "bin",
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "GTK3-Runtime Win64" / "bin",
        Path(r"C:\msys64\mingw64\bin"),
    ]
    for root in roots:
        if root.exists():
            _DLL_HANDLES.append(os.add_dll_directory(str(root)))


def svg_to_png(svg_path, png_path, width: int = 1080) -> str:
    """Convierte un SVG en PNG de `width` px de ancho. Devuelve qué motor se usó."""
    svg_path, png_path = Path(svg_path), Path(png_path)
    errors: list[str] = []

    try:
        _prepare_cairo_dll_search()
        import cairosvg  # type: ignore
    except (ImportError, OSError) as exc:  # OSError: falta la librería Cairo del sistema
        errors.append(f"cairosvg no disponible ({exc})")
    else:
        try:
            cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=width)
            return "cairosvg"
        except Exception as exc:  # noqa: BLE001
            errors.append(f"cairosvg falló ({exc})")

    exe = _windows_tool("rsvg-convert")
    if exe:
        subprocess.run([exe, "-w", str(width), "-o", str(png_path), str(svg_path)], check=True)
        return "rsvg-convert"

    exe = _windows_tool("inkscape")
    if exe:
        subprocess.run(
            [exe, str(svg_path), "--export-type=png",
             f"--export-filename={png_path}", f"--export-width={width}"],
            check=True,
        )
        return "inkscape"

    raise RenderError(
        "No se pudo crear el PNG, aunque el SVG sí se ha generado. En Windows "
        "la opción más sencilla es instalar Inkscape y volver a ejecutar el comando. "
        "También puedes usar --no-png para conservar solo el SVG. Detalle: " + "; ".join(errors)
    )

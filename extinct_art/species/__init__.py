"""Registro automático de módulos de especies."""
from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path

from ..reference import palette_from_references


def _location_for(meta):
    """Convierte la distribucion de la ficha en una etiqueta y un escenario.

    No intenta inventar una localidad exacta: solo normaliza lugares que ya
    aparecen en META. La etiqueta se imprime en la lamina y ``landscape`` se
    usa para escoger un fondo regional.
    """
    raw = str(meta.get("distribution", "")).strip()
    text = raw.casefold()
    rules = (
        (("jamaica",), "Blue Mountains, Jamaica", "jamaica"),
        (("mauricio", "mauritius"), "Mauricio (isla)", "island"),
        (("rodrigues",), "Rodrigues (isla)", "island"),
        (("reunion", "reunión", "reuni"), "Reunión (isla)", "island"),
        (("madagascar",), "Madagascar", "island"),
        (("malvinas", "falkland"), "Islas Malvinas", "island"),
        (("lord howe",), "Isla Lord Howe", "island"),
        (("macquarie",), "Isla Macquarie", "island"),
        (("chatham",), "Islas Chatham", "island"),
        (("guadalupe",), "Guadalupe", "island"),
        (("tahiti",), "Tahití", "island"),
        (("raiatea",), "Raiatea", "island"),
        (("moorea",), "Moorea", "island"),
        (("kosrae",), "Kosrae", "island"),
        (("santa cruz",), "Santa Cruz, Antillas", "island"),
        (("bonin",), "Islas Bonin", "island"),
        (("seychelles",), "Seychelles", "island"),
        (("nueva zelanda", "new zealand"), "Nueva Zelanda", "island"),
        (("kangaroo",), "Isla Kangaroo, Australia", "island"),
        (("bering",), "Isla de Bering", "island"),
        (("atlántico norte", "atlantic"), "Atlántico norte", "costa"),
        (("cabo", "sudáfrica", "south africa"), "Sudáfrica", "generic"),
        (("caspio", "caspian"), "Mar Caspio", "costa"),
        (("europa", "euroasia", "euroasi"), "Europa y Eurasia", "generic"),
        (("cerdeña", "córcega", "sardinia"), "Cerdeña y Córcega", "island"),
    )
    for needles, label, landscape in rules:
        if any(needle in text for needle in needles):
            return label, landscape
    return raw or "localidad no precisada", meta.get("landscape", "generic")


def _load_species():
    found = {}
    for module_info in pkgutil.iter_modules(__path__):
        if module_info.name.startswith("_") or module_info.name == "base":
            continue
        module = importlib.import_module(f"{__name__}.{module_info.name}")
        meta = getattr(module, "META", None)
        draw = getattr(module, "draw", None)
        if isinstance(meta, dict) and callable(draw):
            location_label, inferred_landscape = _location_for(meta)
            meta["location_label"] = location_label
            meta["location_landscape"] = inferred_landscape
            if meta.get("landscape") == "generic" and inferred_landscape != "generic":
                meta["landscape"] = inferred_landscape
            # Cada módulo contiene sus propios datos visuales: la ficha Python
            # es la única fuente de datos ejecutable de esa especie.
            extra = getattr(module, "DRAWING_DATA", {})
            for key in ("description", "visual_notes", "drawing_notes", "reference_taxa"):
                if extra.get(key):
                    meta[key] = extra[key]
            slug_sources = getattr(module, "RESEARCH_SOURCES", None)
            if slug_sources:
                meta["research_sources"] = slug_sources
            slug = meta.get("slug", module_info.name)
            image_manifest = Path(__file__).resolve().parents[2] / "references" / "species" / slug / "references.json"
            if image_manifest.exists():
                try:
                    import json
                    manifest = json.loads(image_manifest.read_text(encoding="utf-8"))
                    meta["reference_images"] = [item["local_file"] for item in manifest.get("references", [])]
                except (OSError, ValueError, KeyError):
                    meta["reference_images"] = []
            reference_palette = palette_from_references(Path(__file__).resolve().parents[2], slug)
            if reference_palette:
                meta["reference_palette"] = reference_palette
            if extra.get("profile") and hasattr(module, "PROFILE"):
                module.PROFILE.update(extra["profile"])
            if extra.get("colors") and hasattr(module, "COLORS"):
                module.COLORS.update(extra["colors"])
            found[meta.get("slug", module_info.name)] = module
    return dict(sorted(found.items()))


SPECIES = _load_species()


def validate_species(project_root=None):
    """Devuelve errores de metadatos, paisajes y fichas de referencia."""
    required = {"scientific_name", "common_name", "landscape", "description", "kind"}
    errors = []
    for slug, module in SPECIES.items():
        missing = required - set(module.META)
        if missing:
            errors.append(f"{slug}: faltan META: {', '.join(sorted(missing))}")
        drawing_data = getattr(module, "DRAWING_DATA", None)
        if not isinstance(drawing_data, dict):
            errors.append(f"{slug}: falta DRAWING_DATA en el mÃ³dulo Python")
        else:
            missing_visual = {"description", "visual_notes", "drawing_notes", "reference_taxa"} - set(drawing_data)
            if missing_visual:
                errors.append(f"{slug}: faltan DRAWING_DATA: {', '.join(sorted(missing_visual))}")
        if module.META.get("kind") not in {"bird", "mammal", "reptile"}:
            errors.append(f"{slug}: kind debe ser bird, mammal o reptile")
        if not str(module.META.get("source_url", "")).startswith(("http://", "https://")):
            errors.append(f"{slug}: source_url no es una URL")
        if project_root and module.META.get("reference_file"):
            ref = Path(project_root) / module.META["reference_file"]
            if not ref.exists():
                errors.append(f"{slug}: no existe {module.META['reference_file']}")
            else:
                try:
                    markdown = ref.read_text(encoding="utf-8")
                    for key in ("description", "visual_notes", "drawing_notes", "reference_taxa"):
                        value = module.META.get(key)
                        if value and value not in markdown:
                            errors.append(f"{slug}: META['{key}'] no coincide con la ficha Markdown")
                except OSError as exc:
                    errors.append(f"{slug}: no se pudo leer la ficha Markdown: {exc}")
    return errors

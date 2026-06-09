"""Validate import boundaries for a future terrain/bathymetry helper.

This checker is static. It parses Python source with ast and never imports or
executes the candidate module.
"""

from __future__ import annotations

import argparse
import ast
import fnmatch
import json
from pathlib import Path


SCHEMA = "rrkal_displaytools.terrain_bathymetry_import_boundary.v1"
DEFAULT_TARGET = Path("render_core/terrain_bathymetry_boundary.py")

FORBIDDEN_IMPORT_PREFIXES = (
    "taichi_global_bathymetry",
    "taichi",
    "PyQt6",
    "PySide6",
    "vispy",
    "numpy",
    "xarray",
    "netCDF4",
    "requests",
    "urllib",
    "pymysql",
    "sqlalchemy",
    "websocket",
    "render_core.render_plan",
    "render_core.preview",
    "render_core.metadata",
)

FORBIDDEN_NAMES = {
    "QtHybridWindow",
    "VisPyHybridViewer",
    "TaichiGlobeRenderer",
    "HybridRenderController",
    "load_topography",
    "synthetic_topography",
    "download",
    "fetch",
    "GEBCO",
    "ETOPO",
    "NOAA",
    "cache_hit",
    "cache_miss",
    "topography_cache",
    "sample_lon",
    "sample_lat",
    "bump",
    "normal",
    "raymarch",
    "height_lookup",
    "flip_longitude",
    "flip_latitude",
    "compute_sun_direction",
    "light_dir",
    "dot_l",
    "twilight",
    "projection",
    "mask_overlay_to_globe",
    "alpha_compose",
    "alpha_blend_compose",
    "alpha_compose_transparent",
    "build_layer_render_plan_apply_path",
    "apply_layer_render_plan_composition",
    "write_preview_frame_png",
    "build_renderer_output_metadata_payload",
    "sidecar_writer",
    "artifact_writer",
    "state_writer",
    "png_writer",
    "runtime_json_writer",
    "AISStream",
    "ADSBStream",
    "ADSBLive",
}

FORBIDDEN_NAME_PATTERNS = (
    "*metadata*writer*",
    "*artifact*writer*",
    "*state*writer*",
    "*png*writer*",
    "*runtime*json*writer*",
    "*provider*cache*",
    "*terrain*sampling*",
    "*sphere*intersection*",
    "*height*lookup*",
    "*gui*event*loop*",
    "*websocket*",
    "*sql*",
    "*adsb*",
    "*ais*live*",
)

FORBIDDEN_MODULE_KEYWORDS = (
    "provider_cache",
    "topography_cache",
    "gebco",
    "etopo",
    "noaa",
    "download",
    "fetch",
    "terrain_sampling",
    "raymarch",
    "sphere_intersection",
    "height_lookup",
    "metadata_sidecar",
    "artifact_writer",
    "state_writer",
    "png_writer",
    "runtime_json",
    "sql",
    "websocket",
    "ais",
    "adsb",
)

FORBIDDEN_FAMILIES = {
    "monolith": ["taichi_global_bathymetry"],
    "runtime_ui_gpu": [
        "taichi",
        "PyQt6",
        "PySide6",
        "vispy",
        "QtHybridWindow",
        "VisPyHybridViewer",
        "TaichiGlobeRenderer",
    ],
    "data_provider_cache_execution": [
        "numpy",
        "xarray",
        "netCDF4",
        "requests",
        "urllib",
        "download",
        "fetch",
        "load_topography",
        "synthetic_topography",
        "GEBCO",
        "ETOPO",
        "NOAA",
        "cache_hit",
        "cache_miss",
        "topography_cache",
        "provider cache",
    ],
    "shader_sampling_bump": [
        "sample_lon",
        "sample_lat",
        "terrain sampling",
        "bump",
        "normal",
        "raymarch",
        "sphere intersection",
        "height lookup",
    ],
    "projection_flip_lighting": [
        "flip_longitude",
        "flip_latitude",
        "compute_sun_direction",
        "light_dir",
        "dot_l",
        "twilight",
        "projection",
        "mask_overlay_to_globe",
    ],
    "runtime_controller": ["HybridRenderController", "reload mutation", "GUI/event loop"],
    "hot_path": [
        "alpha_compose",
        "alpha_blend_compose",
        "alpha_compose_transparent",
        "build_layer_render_plan_apply_path",
        "apply_layer_render_plan_composition",
    ],
    "artifact_metadata": [
        "metadata sidecar writer",
        "artifact writer",
        "state writer",
        "PNG writer",
        "runtime JSON writer",
    ],
    "live_source_paths": ["SQL", "WebSocket", "AIS", "ADS-B"],
}


def _family_for_token(token: str) -> str:
    lowered = token.lower().replace("_", " ")
    for family, tokens in FORBIDDEN_FAMILIES.items():
        for item in tokens:
            item_lower = item.lower().replace("_", " ")
            if item_lower in lowered or lowered in item_lower:
                return family
    if any(word in lowered for word in ("metadata", "artifact", "state writer", "png", "runtime json")):
        return "artifact_metadata"
    if any(word in lowered for word in ("sql", "websocket", "ais", "adsb")):
        return "live_source_paths"
    if any(word in lowered for word in ("cache", "provider", "download", "fetch", "gebco", "etopo", "noaa")):
        return "data_provider_cache_execution"
    if any(word in lowered for word in ("sample", "bump", "normal", "raymarch", "height lookup", "sphere")):
        return "shader_sampling_bump"
    if any(word in lowered for word in ("flip", "light", "twilight", "projection", "mask")):
        return "projection_flip_lighting"
    return "forbidden_name"


def _name_is_forbidden(name: str) -> tuple[bool, str, str]:
    if name in FORBIDDEN_NAMES:
        family = _family_for_token(name)
        return True, family, f"forbidden_name:{name}"
    for pattern in FORBIDDEN_NAME_PATTERNS:
        if fnmatch.fnmatch(name, pattern):
            family = _family_for_token(name)
            return True, family, f"forbidden_name_pattern:{pattern}"
    return False, "", ""


def _module_is_forbidden(module: str) -> tuple[bool, str, str]:
    clean = module.strip()
    for prefix in FORBIDDEN_IMPORT_PREFIXES:
        if clean == prefix or clean.startswith(prefix + "."):
            family = _family_for_token(prefix)
            return True, family, f"forbidden_module_prefix:{prefix}"
    lowered = clean.lower()
    for keyword in FORBIDDEN_MODULE_KEYWORDS:
        if keyword in lowered:
            family = _family_for_token(keyword)
            return True, family, f"forbidden_module_keyword:{keyword}"
    return False, "", ""


def _iter_imported_names(node: ast.ImportFrom):
    for alias in node.names:
        yield alias.name
        if alias.asname:
            yield alias.asname


def _base_packet(source_name: str) -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "target": source_name,
        "candidate_exists": True,
        "status": "pass",
        "boundary_passed": True,
        "violations": [],
        "checked_imports": [],
        "checked_names": [],
        "forbidden_families": FORBIDDEN_FAMILIES,
        "string_labels_allowed_as_data": True,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "boundary": "Static AST import-boundary check only; does not import or execute the target module.",
    }


def _append_name_violation(violations: list[dict[str, object]], node: ast.AST, kind: str, name: str) -> None:
    forbidden, family, reason = _name_is_forbidden(name)
    if forbidden:
        violations.append(
            {
                "line": getattr(node, "lineno", 0),
                "kind": kind,
                "module": "",
                "name": name,
                "forbidden_family": family,
                "reason": reason,
            }
        )


def _call_target_name(func: ast.AST) -> str:
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


def validate_source(source: str, source_name: str = "<memory>") -> dict[str, object]:
    packet = _base_packet(source_name)
    violations: list[dict[str, object]] = []
    checked_imports: list[str] = []
    checked_names: list[str] = []

    try:
        tree = ast.parse(source, filename=source_name)
    except SyntaxError as exc:
        packet.update(
            {
                "status": "syntax_error",
                "boundary_passed": False,
                "violations": [
                    {
                        "line": exc.lineno or 0,
                        "kind": "syntax_error",
                        "module": "",
                        "name": "",
                        "forbidden_family": "syntax_error",
                        "reason": "syntax_error",
                        "message": exc.msg,
                    }
                ],
            }
        )
        return packet

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                checked_imports.append(alias.name)
                forbidden, family, reason = _module_is_forbidden(alias.name)
                if forbidden:
                    violations.append(
                        {
                            "line": node.lineno,
                            "kind": "import",
                            "module": alias.name,
                            "name": alias.asname or "",
                            "forbidden_family": family,
                            "reason": reason,
                        }
                    )
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            checked_imports.append(module)
            forbidden, family, reason = _module_is_forbidden(module)
            imported_names = list(_iter_imported_names(node))
            checked_names.extend(imported_names)
            name_hits = []
            name_families = []
            for name in imported_names:
                name_forbidden, name_family, name_reason = _name_is_forbidden(name)
                if name_forbidden:
                    name_hits.append({"name": name, "forbidden_family": name_family, "reason": name_reason})
                    name_families.append(name_family)
            if forbidden or name_hits:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "from_import",
                        "module": module,
                        "names": name_hits,
                        "forbidden_family": family or sorted(set(name_families))[0],
                        "reason": reason or "forbidden_imported_name",
                    }
                )
        elif isinstance(node, ast.Name):
            checked_names.append(node.id)
            _append_name_violation(violations, node, "name_reference", node.id)
        elif isinstance(node, ast.Attribute):
            checked_names.append(node.attr)
            _append_name_violation(violations, node, "attribute_reference", node.attr)
        elif isinstance(node, ast.Call):
            name = _call_target_name(node.func)
            if name:
                checked_names.append(name)
                _append_name_violation(violations, node, "call_target", name)
        elif isinstance(node, ast.FunctionDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "function_definition", node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "async_function_definition", node.name)
        elif isinstance(node, ast.ClassDef):
            checked_names.append(node.name)
            _append_name_violation(violations, node, "class_definition", node.name)

    packet.update(
        {
            "status": "fail" if violations else "pass",
            "boundary_passed": not violations,
            "violations": violations,
            "checked_imports": sorted(set(checked_imports)),
            "checked_names": sorted(set(checked_names)),
        }
    )
    return packet


def validate_target(path: Path) -> dict[str, object]:
    if not path.exists():
        packet = _base_packet(str(path))
        packet.update(
            {
                "candidate_exists": False,
                "status": "not_applicable_candidate_missing",
                "boundary_passed": True,
                "violations": [],
                "checked_imports": [],
                "checked_names": [],
                "boundary": "Candidate terrain/bathymetry helper module is not present yet; no target module was imported or executed.",
            }
        )
        return packet
    return validate_source(path.read_text(encoding="utf-8"), str(path))


def run_negative_self_test() -> dict[str, object]:
    snippets = {
        "monolith": "import taichi_global_bathymetry\n",
        "taichi": "import taichi as ti\n",
        "pyqt": "from PyQt6 import QtWidgets\n",
        "vispy": "import vispy\n",
        "numpy": "import numpy as np\n",
        "xarray": "import xarray as xr\n",
        "netcdf4": "import netCDF4\n",
        "requests": "import requests\n",
        "urllib": "import urllib.request\n",
        "load_topography_import": "from terrain_loader import load_topography\n",
        "synthetic_topography_name": "def f():\n    return synthetic_topography\n",
        "gebco_name": "def f():\n    return GEBCO\n",
        "cache_hit_def": "def cache_hit():\n    return True\n",
        "sample_lon_name": "def f():\n    return sample_lon\n",
        "bump_call": "def f():\n    return bump()\n",
        "normal_attr": "def f(obj):\n    return obj.normal\n",
        "raymarch_def": "def raymarch():\n    return None\n",
        "flip_longitude_name": "def f():\n    return flip_longitude\n",
        "compute_sun_direction_call": "def f():\n    return compute_sun_direction()\n",
        "light_attr": "def f(obj):\n    return obj.light_dir\n",
        "controller": "def f():\n    return HybridRenderController\n",
        "renderer_class_def": "class TaichiGlobeRenderer:\n    pass\n",
        "alpha": "from render_core.render_plan import alpha_compose\n",
        "apply_path": "def f():\n    return build_layer_render_plan_apply_path\n",
        "metadata": "from render_core.metadata import build_renderer_output_metadata_payload\n",
        "artifact_writer": "def f():\n    return runtime_json_writer\n",
        "websocket": "import websocket\n",
        "ais": "def f():\n    return AISStream\n",
    }
    results = {}
    for name, source in snippets.items():
        packet = validate_source(source, f"<self-test:{name}>")
        results[name] = {"detected": not packet["boundary_passed"], "violations": packet["violations"]}
    all_detected = all(result["detected"] for result in results.values())
    return {
        "schema": SCHEMA,
        "target": "<negative-self-test>",
        "candidate_exists": True,
        "status": "pass" if all_detected else "fail",
        "boundary_passed": all_detected,
        "negative_self_test_passed": all_detected,
        "all_forbidden_snippets_detected": all_detected,
        "violations": [] if all_detected else results,
        "checked_imports": [],
        "checked_names": [],
        "forbidden_families": FORBIDDEN_FAMILIES,
        "string_labels_allowed_as_data": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", nargs="?", default=str(DEFAULT_TARGET))
    parser.add_argument("--self-test-negative", action="store_true")
    args = parser.parse_args()

    packet = run_negative_self_test() if args.self_test_negative else validate_target(Path(args.target))
    print(json.dumps(packet, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if packet.get("boundary_passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())

"""Validate import boundaries for a future compose queue helper module.

This checker is static. It parses Python source with ast and never imports or
executes the candidate module.
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
from typing import Iterable


SCHEMA = "rrkal_displaytools.layer_render_plan_compose_queue_import_boundary.v1"
DEFAULT_TARGET = Path("render_core/layer_render_plan_compose_queue.py")

FORBIDDEN_IMPORT_PREFIXES = (
    "taichi_global_bathymetry",
    "taichi",
    "PyQt6",
    "PySide6",
    "vispy",
    "numpy",
    "pandas",
    "datashader",
    "render_core.render_plan",
    "render_core.preview",
    "render_core.metadata",
    "render_core.dataframe_normalizers",
    "cursor_geodesy",
    "closed_loop_status",
    "renderer_config_gateway",
)

FORBIDDEN_NAME_IMPORTS = {
    "HybridRenderController",
    "TaichiGlobeRenderer",
    "QtHybridWindow",
    "VisPyHybridViewer",
    "alpha_compose",
    "alpha_blend_compose",
    "alpha_compose_transparent",
    "merge_alpha_compose_overlay_run",
    "apply_layer_render_plan_composition",
    "apply_layer_render_plan_merged_candidate_composition",
    "write_preview_frame_png",
    "build_renderer_output_metadata_payload",
    "write_compose_parity_artifacts",
    "normalize_ais_frame",
    "normalize_aircraft_frame",
    "dataframe_from_text",
    "dataframe_from_json",
    "dataframe_from_jsonl",
    "dataframe_from_geojson",
    "dataframe_from_nmea",
    "PointOverlayBudgetPolicy",
    "DatashaderSamplingPolicy",
    "LayerRenderBudgetPolicy",
    "AdaptiveRenderQualityPolicy",
}

FORBIDDEN_NAME_REFERENCES = FORBIDDEN_NAME_IMPORTS

FORBIDDEN_MODULE_KEYWORDS = (
    "provider",
    "source_loader",
    "source_loading",
    "loader",
    "fetch",
    "download",
    "cache",
    "artifact_writer",
    "sidecar_writer",
)


def _module_is_forbidden(module: str) -> tuple[bool, str]:
    clean = module.strip()
    for prefix in FORBIDDEN_IMPORT_PREFIXES:
        if clean == prefix or clean.startswith(prefix + "."):
            return True, f"forbidden_module_prefix:{prefix}"
    lowered = clean.lower()
    for keyword in FORBIDDEN_MODULE_KEYWORDS:
        if keyword in lowered:
            return True, f"forbidden_module_keyword:{keyword}"
    return False, ""


def _imported_names(node: ast.ImportFrom) -> Iterable[str]:
    for alias in node.names:
        yield alias.name
        if alias.asname:
            yield alias.asname


def validate_source(source: str, source_name: str = "<memory>") -> dict[str, object]:
    tree = ast.parse(source, filename=source_name)
    violations: list[dict[str, object]] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                forbidden, reason = _module_is_forbidden(alias.name)
                if forbidden:
                    violations.append(
                        {
                            "line": node.lineno,
                            "kind": "import",
                            "module": alias.name,
                            "name": alias.asname or "",
                            "reason": reason,
                        }
                    )
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            forbidden, reason = _module_is_forbidden(module)
            names = list(_imported_names(node))
            name_hits = sorted(set(names).intersection(FORBIDDEN_NAME_IMPORTS))
            if forbidden or name_hits:
                violations.append(
                    {
                        "line": node.lineno,
                        "kind": "from_import",
                        "module": module,
                        "names": name_hits,
                        "reason": reason or "forbidden_imported_name",
                    }
                )
        elif isinstance(node, ast.Name) and node.id in FORBIDDEN_NAME_REFERENCES:
            violations.append(
                {
                    "line": node.lineno,
                    "kind": "name_reference",
                    "module": "",
                    "name": node.id,
                    "reason": "forbidden_name_reference",
                }
            )

    return {
        "schema": SCHEMA,
        "source": source_name,
        "status": "fail" if violations else "pass",
        "candidate_exists": True,
        "boundary_passed": not violations,
        "contract_only": True,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "violations": violations,
        "allowed_future_helper_behavior": "pure_dict_list_helpers_only",
        "boundary": "Static AST import-boundary check only; does not import or execute the target module.",
    }


def validate_target(path: Path) -> dict[str, object]:
    if not path.exists():
        return {
            "schema": SCHEMA,
            "source": str(path),
            "status": "not_applicable_candidate_missing",
            "candidate_exists": False,
            "boundary_passed": True,
            "contract_only": True,
            "runtime_render_invoked": False,
            "runtime_merge_enabled": False,
            "violations": [],
            "boundary": "Candidate compose queue helper module is not present yet; no target module was imported or executed.",
        }
    source = path.read_text(encoding="utf-8")
    return validate_source(source, str(path))


def run_negative_self_test() -> dict[str, object]:
    snippets = {
        "monolith": "import taichi_global_bathymetry\n",
        "controller": "from taichi_global_bathymetry import HybridRenderController\n",
        "taichi": "import taichi as ti\n",
        "pyqt": "from PyQt6 import QtWidgets\n",
        "vispy": "import vispy\n",
        "numpy": "import numpy as np\n",
        "pandas": "import pandas as pd\n",
        "datashader": "import datashader as ds\n",
        "render_plan_module": "from render_core.render_plan import build_layer_render_plan_compose_runs\n",
        "alpha_helper": "from render_core.render_plan import alpha_compose\n",
        "alpha_name": "def f():\n    return alpha_blend_compose\n",
        "metadata_writer": "from render_core.metadata import build_renderer_output_metadata_payload\n",
        "artifact_writer": "from render_core.preview import write_preview_frame_png\n",
        "normalizer": "from render_core.dataframe_normalizers import normalize_ais_frame\n",
        "parser": "from taichi_global_bathymetry import dataframe_from_text\n",
        "provider": "from provider_loader import load_provider\n",
        "sibling_policy": "from render_core.point_overlay_budget_policy import PointOverlayBudgetPolicy\n",
    }
    results: dict[str, bool] = {}
    for name, source in snippets.items():
        packet = validate_source(source, f"<self-test:{name}>")
        results[name] = bool(packet["violations"])

    passed = all(results.values())
    return {
        "schema": f"{SCHEMA}.self_test",
        "status": "pass" if passed else "fail",
        "contract_only": True,
        "negative_self_test_passed": passed,
        "all_forbidden_snippets_detected": passed,
        "results": results,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "boundary": "In-memory negative self-test only; no file writes and no target module execution.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate compose queue helper import boundaries.")
    parser.add_argument("target", nargs="?", default=str(DEFAULT_TARGET))
    parser.add_argument("--self-test-negative", action="store_true")
    args = parser.parse_args()

    packet = run_negative_self_test() if args.self_test_negative else validate_target(Path(args.target))
    print(json.dumps(packet, ensure_ascii=False, indent=2))
    return 0 if packet.get("boundary_passed", packet.get("negative_self_test_passed", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())

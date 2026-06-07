"""Validate import boundaries for a future adaptive render quality policy helper.

This checker is static. It parses Python source with ast and never imports or
executes the candidate module.
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
from typing import Iterable


FORBIDDEN_IMPORT_PREFIXES = (
    "taichi",
    "PyQt6",
    "PySide6",
    "vispy",
    "pyais",
    "pandas",
    "numpy",
    "datashader",
    "taichi_global_bathymetry",
    "rrkal_displaytools_qt_panel",
    "render_core.preview",
    "render_core.metadata",
    "render_core.dataframe_normalizers",
    "render_core.point_overlay_budget_policy",
    "render_core.datashader_sampling_policy",
    "render_core.layer_render_budget_policy",
    "cursor_geodesy",
    "closed_loop_status",
    "renderer_config_gateway",
)

FORBIDDEN_NAME_IMPORTS = {
    "HybridRenderController",
    "TaichiGlobeRenderer",
    "QtHybridWindow",
    "VisPyHybridViewer",
    "write_preview_frame_png",
    "build_renderer_output_metadata_payload",
    "dataframe_from_text",
    "dataframe_from_json",
    "dataframe_from_jsonl",
    "dataframe_from_geojson",
    "dataframe_from_nmea",
    "normalize_ais_frame",
    "normalize_aircraft_frame",
    "find_column",
    "normalize_name",
    "PointOverlayBudgetPolicy",
    "DatashaderSamplingPolicy",
    "LayerRenderBudgetPolicy",
    "LAYER_RENDER_COSTS",
}

FORBIDDEN_MODULE_KEYWORDS = (
    "provider",
    "source",
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

    return {
        "schema": "rrkal_displaytools.adaptive_render_quality_policy_import_boundary.v1",
        "source": source_name,
        "status": "fail" if violations else "pass",
        "candidate_exists": True,
        "boundary_passed": not violations,
        "contract_only": True,
        "runtime_render_invoked": False,
        "runtime_merge_enabled": False,
        "violations": violations,
        "boundary": "Static AST import-boundary check only; does not import or execute the target module.",
    }


def validate_target(path: Path) -> dict[str, object]:
    if not path.exists():
        return {
            "schema": "rrkal_displaytools.adaptive_render_quality_policy_import_boundary.v1",
            "source": str(path),
            "status": "not_applicable_candidate_missing",
            "candidate_exists": False,
            "boundary_passed": True,
            "contract_only": True,
            "runtime_render_invoked": False,
            "runtime_merge_enabled": False,
            "violations": [],
            "boundary": "Candidate adaptive render quality policy helper module is not present yet; no target module was imported or executed.",
        }
    source = path.read_text(encoding="utf-8")
    return validate_source(source, str(path))


def run_negative_self_test() -> dict[str, object]:
    snippets = {
        "taichi": "import taichi as ti\n",
        "pyqt": "from PyQt6 import QtWidgets\n",
        "vispy": "import vispy\n",
        "pyais": "import pyais\n",
        "pandas": "import pandas as pd\n",
        "numpy": "import numpy as np\n",
        "datashader": "import datashader as ds\n",
        "monolith": "import taichi_global_bathymetry as tgb\n",
        "controller": "from taichi_global_bathymetry import HybridRenderController\n",
        "artifact_writer": "from render_core.preview import write_preview_frame_png\n",
        "metadata_writer": "from render_core.metadata import build_renderer_output_metadata_payload\n",
        "provider_loader": "from ocean_condition_provider import OceanConditionProvider\n",
        "source_fetch": "from source_fetcher import fetch_records\n",
        "download_cache": "import download_cache\n",
        "parser": "from taichi_global_bathymetry import dataframe_from_text\n",
        "normalizer": "from render_core.dataframe_normalizers import normalize_ais_frame\n",
        "point_policy": "from render_core.point_overlay_budget_policy import PointOverlayBudgetPolicy\n",
        "datashader_policy": "from render_core.datashader_sampling_policy import DatashaderSamplingPolicy\n",
        "layer_policy": "from render_core.layer_render_budget_policy import LayerRenderBudgetPolicy\n",
        "layer_costs": "from render_core.layer_render_budget_policy import LAYER_RENDER_COSTS\n",
    }
    results = {}
    for name, source in snippets.items():
        packet = validate_source(source, f"<self-test:{name}>")
        results[name] = bool(packet["violations"])

    passed = all(results.values())
    return {
        "schema": "rrkal_displaytools.adaptive_render_quality_policy_import_boundary.self_test.v1",
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
    parser = argparse.ArgumentParser(description="Validate adaptive render quality policy helper import boundaries.")
    parser.add_argument("target", nargs="?", default="render_core/adaptive_render_quality_policy.py")
    parser.add_argument("--self-test-negative", action="store_true")
    args = parser.parse_args()

    packet = run_negative_self_test() if args.self_test_negative else validate_target(Path(args.target))
    print(json.dumps(packet, ensure_ascii=False, indent=2))
    return 0 if packet.get("boundary_passed", packet.get("negative_self_test_passed", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())

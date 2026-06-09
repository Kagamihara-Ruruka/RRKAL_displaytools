# Dynamic Point Cutout Cartography Gate

## Gate scope

本 gate 只建立 dynamic point 已切除區塊的靜態測繪圖。它量化目前已抽出的 descriptor / policy / ledger helper、checker 覆蓋、helper tests、gate 文件與剩餘候選表面，不建立新 helper，不移動 source，不修改 monolith、checker 或 `render_core` helper。

## Evidence read

- Required startup HEAD: `453995b refactor: extract dynamic point selection render policy descriptors`
- Required evidence scan: `rg -n "dynamic_point|AIS|ADS-B|selection|render_policy|source_lineage" taichi_global_bathymetry.py render_core tests docs scripts`
- Static count mapping over `taichi_global_bathymetry.py`, `render_core`, `tests`, `docs`, and `scripts`

The evidence scan found dynamic point surfaces across helper modules, checker scripts, tests, docs, and older runtime-adjacent scripts. This gate records those hits as cartography evidence only; it does not execute runtime paths.

## Cutout map summary

| Cutout | Helper | Checker | Helper test | Boundary |
| --- | --- | --- | --- | --- |
| Aggregate boundary descriptors | `render_core/dynamic_point_boundary.py` | `scripts/validate_displaytools_dynamic_point_import_boundary.py` | `tests/test_displaytools_dynamic_point_boundary_helpers.py` | descriptor / policy / ledger shell |
| Source/lineage boundary descriptors | `render_core/dynamic_point_source_lineage_boundary.py` | `scripts/validate_displaytools_dynamic_point_source_lineage_import_boundary.py` | `tests/test_displaytools_dynamic_point_source_lineage_boundary_helpers.py` | descriptor / policy / ledger shell |
| Selection/render policy boundary descriptors | `render_core/dynamic_point_selection_render_policy_boundary.py` | `scripts/validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py` | `tests/test_displaytools_dynamic_point_selection_render_policy_boundary_helpers.py` | descriptor / policy / ledger shell |

## Quantification summary

Static line/count mapping for this gate:

- `taichi_global_bathymetry.py` total lines: 21072
- aggregate helper line count: 196
- source/lineage helper line count: 183
- selection/render policy helper line count: 194
- extracted helper total line count: 573
- dynamic point checker count: 3
- dynamic point helper test count: 3
- dynamic point gate doc count before this new gate: 16
- dynamic point gate test count before this new gate: 13

Current monolith delta from these extractions is not directly measurable from the current static snapshot without replaying the pre-extraction baseline diffs. This gate therefore records helper shell size and remaining monolith size rather than claiming a precise removed-line delta.

## Extracted helper inventory

The three extracted helpers are static descriptor shells. They do not import the monolith, do not read AIS or ADS-B data, do not connect SQL or WebSocket, do not import pandas, Datashader, NumPy, Qt, VisPy, or Taichi, and do not move projection, picker, controller, or renderer behavior.

## Checker inventory

Current dynamic point checker coverage includes:

- aggregate dynamic point import-boundary checker
- source/lineage import-boundary checker
- selection/render policy import-boundary checker

Each checker is AST-only and separates string labels from executable references. This cartography gate does not modify checker scripts.

## Remaining dynamic point surfaces

| Surface | Status | Blocked by | Recommended mapping |
| --- | --- | --- | --- |
| payload / coordinate quality deeper boundary | mapping candidate | projection formula, dataframe runtime | `dynamic_point_payload_coordinate_quality_boundary_fixture_gate` |
| replay / live lineage deeper boundary | mapping candidate | SQL replay runtime, WebSocket live runtime, cache/database IO | `dynamic_point_replay_live_lineage_deeper_boundary_fixture_gate` |
| render cap / adaptive sampling deeper boundary | mapping candidate | Datashader runtime, renderer count runtime | `dynamic_point_render_policy_deeper_boundary_fixture_gate` |
| controller/runtime/datashader/projection/SQL/live blocked surfaces | blocked runtime only | controller, picker, projection, SQL/live, renderer host | `stop_for_o1_or_runtime_mapping_review` |

## Recommended next gate

`dynamic_point_payload_coordinate_quality_boundary_fixture_gate`

Reason: source/lineage and selection/render policy descriptor shells are now mapped and extracted. The payload/coordinate quality surface is the next narrow mapping candidate, but it must remain label-only until projection, dataframe, and runtime dependencies are separately blocked.

## Explicit exclusions

This gate does not:

- create helper modules
- move source
- modify `taichi_global_bathymetry.py`
- modify any `render_core/*.py`
- modify checker scripts
- execute renderer, Taichi, Qt, or VisPy
- read real AIS, ADS-B, cache, or database data
- execute SQL, WebSocket, or live-source paths
- execute pandas, Datashader, or NumPy runtime
- change projection, flip, mask, controller, picker, hit-test, or render behavior
- claim readiness, safe-to-extract, bug fix, visual parity, performance, or live-data restoration

## Boundary statement

Docs/test-only dynamic point cutout cartography gate. No helper module creation, no source movement, no production source change, no checker change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
# Dynamic Point Payload / Coordinate Quality Craton Ablation Matrix Gate

## Gate scope

本 gate 建立 dynamic point payload / coordinate quality 的卡秋莎矩陣與確定格填入。此 slice 只新增 docs/test-only matrix，不建立 helper module，不建立 checker script，不移動 source，不修改 `render_core`、checker 或 `taichi_global_bathymetry.py`。

## Evidence read

- Required startup HEAD: `4714f01 test: add dynamic point payload coordinate quality gate`
- Required evidence scan: `rg -n "payload|coordinate|timestamp|source_id|speed|heading|missing|invalid|stale|quality|dynamic_point" tests docs render_core taichi_global_bathymetry.py scripts`
- Prior payload / coordinate quality boundary fixture gate
- Existing dynamic point helper, checker, cartography, matrix, planning, and extraction docs/tests

Evidence shows payload fields, timestamp handling, speed/heading fields, coordinate quality labels, and dynamic point descriptor shells. This gate records those surfaces as descriptor-only matrix evidence and does not execute runtime paths.

## Phase A matrix summary

| Pin | Dependency classification | Fixture status | Boundary |
| --- | --- | --- | --- |
| `payload_shape_pin` | descriptor / policy / ledger | `pinned` | payload field shape labels only |
| `coordinate_quality_pin` | descriptor / policy / ledger | `unresolved_static_only` | missing, invalid, out-of-range, zero, and anti-meridian labels only |
| `timestamp_quality_pin` | descriptor / policy / ledger | `unresolved_static_only` | missing, stale, future, and timezone ambiguity labels only |
| `source_id_quality_pin` | descriptor / policy / ledger | `unresolved_static_only` | missing, synthetic, AIS, and ADS-B id labels only |
| `speed_heading_quality_pin` | descriptor / policy / ledger | `pinned` | speed and heading labels only |
| `point_vector_sync_fault_pin` | descriptor / policy / ledger | `unresolved_static_only` | sync fault ledger only |
| `projection_dependency_stop_pin` | blocked runtime dependency | `blocked_runtime_only` | projection / flip / mask formulas remain blocked |
| `live_source_dependency_stop_pin` | blocked runtime dependency | `blocked_runtime_only` | SQL / WebSocket / live / cache / database runtime remains blocked |
| `controller_selection_dependency_stop_pin` | blocked runtime dependency | `blocked_runtime_only` | controller / picker / hit-test runtime remains blocked |
| `renderer_runtime_dependency_stop_pin` | blocked runtime dependency | `blocked_runtime_only` | renderer / Qt / VisPy / Taichi / Datashader runtime remains blocked |

All pins carry `null_mode`, `tripwire_mode`, `trace_mode`, and `substitute_mode` as descriptor-only ablation modes.

## Phase B deterministic boundary fill

- `future_helper_target = render_core\dynamic_point_payload_coordinate_quality_boundary.py`
- `new_checker_required = true`
- `existing_checker_reusable = false`
- `payload_coordinate_quality_planning_candidate = true`
- `payload_coordinate_quality_extraction_candidate = false`
- `helper_module_creation_authorized = false`
- `source_movement_authorized = false`

Reason: payload / coordinate quality has distinct stop lines around projection formula, live source, dataframe runtime, controller selection, and renderer runtime. A dedicated checker is required before extraction planning or source movement.

## Candidate families assessment

Planning-only candidate families:

- `build_dynamic_point_payload_shape_descriptor`
- `build_dynamic_point_coordinate_quality_descriptor`
- `build_dynamic_point_timestamp_quality_descriptor`
- `build_dynamic_point_source_id_quality_descriptor`
- `build_dynamic_point_speed_heading_quality_descriptor`
- `build_dynamic_point_payload_coordinate_quality_known_fault_ledger`
- `dynamic_point_payload_coordinate_quality_boundary_descriptor`
- `dynamic_point_payload_coordinate_quality_planning_bundle`

These are not created in this gate.

## Blocked surfaces

- projection / flip / mask formula
- SQL / WebSocket / live source
- real AIS / ADS-B / cache / database reads
- pandas / Datashader / NumPy runtime
- controller selection / picker / hit-test runtime
- renderer / Qt / VisPy / Taichi runtime
- metadata / artifact writer
- alpha / apply / composition hot path

## Phase C recommended next gate

`dynamic_point_payload_coordinate_quality_import_boundary_checker_gate`

Reason: the matrix has enough deterministic boundary cells to define a dedicated checker target and forbidden families before any planning or extraction gate.

## Explicit exclusions

This gate does not:

- create `render_core\dynamic_point_payload_coordinate_quality_boundary.py`
- create checker scripts
- move source
- modify `render_core/*.py`
- modify `taichi_global_bathymetry.py`
- execute the monolith
- read real AIS, ADS-B, cache, or database data
- execute SQL, WebSocket, or live-source paths
- import pandas, Datashader, or NumPy runtime
- change projection, flip, mask, controller, picker, hit-test, renderer, Qt, VisPy, or Taichi behavior
- claim readiness, safe-to-extract, bug fix, visual parity, performance, or live-data readiness

## Boundary statement

Docs/test-only dynamic point payload/coordinate quality craton ablation capability matrix and deterministic boundary fill gate. No helper module creation, no source movement, no production source change, no import-boundary checker creation, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
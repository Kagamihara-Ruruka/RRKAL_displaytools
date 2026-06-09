# Dynamic Point Payload / Coordinate Quality Import Boundary Checker Gate

## Gate scope

本 gate 新增 dynamic point payload / coordinate quality 專屬 AST import-boundary checker。Checker 預設 target 是 `render_core\dynamic_point_payload_coordinate_quality_boundary.py`，但本 gate 不建立該 helper，不移動 source，不修改 `render_core` 或 `taichi_global_bathymetry.py`。

## Checker behavior

Checker script: `scripts\validate_displaytools_dynamic_point_payload_coordinate_quality_import_boundary.py`

Default target: `render_core\dynamic_point_payload_coordinate_quality_boundary.py`

Behavior pinned by tests:

- static AST-only parse
- no target import
- no target execution
- missing target returns JSON pass with `candidate_exists=false`, `status=not_applicable_candidate_missing`, and `boundary_passed=true`
- syntax error returns JSON with `status=syntax_error` and nonzero CLI exit
- forbidden executable imports, names, attributes, call targets, and declarations fail
- string labels remain allowed as descriptor data
- `--self-test-negative` detects all forbidden snippets

## Missing candidate behavior

The future helper target is intentionally absent in this slice. Missing candidate is a pass condition because this gate installs the checker before helper creation.

Pinned missing candidate fields:

- `candidate_exists=false`
- `status=not_applicable_candidate_missing`
- `boundary_passed=true`
- `violations=[]`

## Forbidden family coverage

| Family | Examples |
| --- | --- |
| `monolith` | `taichi_global_bathymetry` |
| `live_source` | `pymysql`, `sqlalchemy`, `websocket`, `AISStream`, `ADSBStream`, live AIS, live ADS-B |
| `cache_database_io` | cache read/write/load/save, DB URL, replay query, database read |
| `runtime_dataframe` | `pandas`, `datashader`, `numpy` |
| `projection_formula` | projection formula, flip formula, mask formula, `project_point`, `lon_lat_to_screen` |
| `controller_selection` | selected vehicle runtime, picker, hit-test, controller mutation |
| `renderer_host` | `TaichiGlobeRenderer`, `QtHybridWindow`, `VisPyHybridViewer`, `taichi`, `PyQt6`, `PySide6`, `vispy` |
| `hot_path` | alpha helpers, apply path, composition apply |
| `artifact_metadata` | metadata sidecar writer, artifact writer, state writer, PNG writer, runtime JSON writer |

## Allowed string-label distinction

These labels are allowed only as data strings:

- `payload_shape`
- `coordinate_quality`
- `timestamp_quality`
- `source_id_quality`
- `speed_heading_quality`
- `missing`
- `invalid`
- `stale`
- `unknown`
- `anti_meridian_candidate`
- `timezone_ambiguity`
- `point_vector_sync_fault`
- `projection_dependency`
- `live_source_dependency`
- `controller_selection_dependency`
- `renderer_runtime_dependency`

If those concepts appear as imports, executable names, attributes, calls, or declarations that match forbidden families, the checker fails them.

## Validation shape

The checker tests cover:

- missing target pass
- clean temporary descriptor candidate pass
- forbidden import fail
- forbidden from-import fail
- forbidden name reference fail
- forbidden attribute reference fail
- forbidden call target fail
- forbidden class definition fail
- forbidden function definition fail
- forbidden async function definition fail
- syntax error JSON fail
- allowed string labels pass
- negative self-test pass
- stable CLI JSON shape

## Explicit exclusions

This gate does not:

- create `render_core\dynamic_point_payload_coordinate_quality_boundary.py`
- move source
- modify `render_core/*.py`
- modify `taichi_global_bathymetry.py`
- import or execute the monolith
- read real AIS, ADS-B, cache, or database data
- execute SQL, WebSocket, or live-source paths
- import pandas, Datashader, or NumPy runtime
- change projection, flip, mask, controller, picker, hit-test, renderer, Qt, VisPy, or Taichi behavior
- claim readiness, safe-to-extract, bug fix, visual parity, performance, or live-data readiness

## Boundary statement

Tooling/docs-only dynamic point payload/coordinate quality import-boundary checker gate. No helper module creation, no source movement, no production helper target creation, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
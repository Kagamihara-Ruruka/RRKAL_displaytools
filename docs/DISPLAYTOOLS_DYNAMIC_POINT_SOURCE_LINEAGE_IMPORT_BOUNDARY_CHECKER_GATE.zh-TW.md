# Displaytools Dynamic Point Source / Lineage Import-Boundary Checker Gate

## Scope

本文件定義 dynamic point source/lineage 專屬 AST import-boundary checker gate。此 slice 只新增 checker、checker tests 與 gate doc，不建立 `render_core\dynamic_point_source_lineage_boundary.py`，不修改 `render_core\dynamic_point_boundary.py`，不修改或 import `taichi_global_bathymetry.py`。

Checker 目標是替未來第二層 source/lineage descriptor helper 預先建立安檢門，確保 candidate 只能保留 descriptor、policy、ledger 資料形狀，不能把 SQL、WebSocket、cache/database IO、dataframe/projection runtime、controller selection 或 renderer host 依賴帶進 helper。

## Evidence read

- `scripts\validate_displaytools_dynamic_point_import_boundary.py`
- `tests\test_displaytools_dynamic_point_import_boundary.py`
- `tests\test_displaytools_dynamic_point_source_lineage_craton_ablation_matrix.py`
- `docs\DISPLAYTOOLS_DYNAMIC_POINT_SOURCE_LINEAGE_CRATON_ABLATION_MATRIX_GATE.zh-TW.md`
- `render_core\dynamic_point_boundary.py`
- current `taichi_global_bathymetry.py` remains read-only and is not imported or executed

## Checker behavior

Checker script: `scripts\validate_displaytools_dynamic_point_source_lineage_import_boundary.py`

Default target: `render_core\dynamic_point_source_lineage_boundary.py`

Required behavior:

- static AST parse only
- target module is never imported
- target module is never executed
- CLI output is JSON
- missing candidate returns pass JSON with `candidate_exists=false`, `status=not_applicable_candidate_missing`, and `boundary_passed=true`
- forbidden executable reference returns nonzero with `boundary_passed=false` and non-empty `violations`
- syntax error returns nonzero JSON with `status=syntax_error`
- negative self-test uses in-memory snippets only and writes no product target file

## Missing candidate behavior

`render_core\dynamic_point_source_lineage_boundary.py` is intentionally absent in this slice. Missing target is not a failure because this gate installs the checker before helper creation.

Pinned missing candidate packet fields:

- `candidate_exists=false`
- `status=not_applicable_candidate_missing`
- `boundary_passed=true`
- `violations=[]`

## Forbidden family coverage

Forbidden families pinned by this gate:

| family | examples |
| --- | --- |
| `monolith` | `taichi_global_bathymetry` |
| `sql_replay_database` | `pymysql`, `sqlalchemy`, `mysql`, `DB URL`, `replay query` |
| `live_stream` | `websocket`, `AISStream`, `ADSBStream`, `live AIS`, `live ADS-B` |
| `cache_database_io` | cache read, cache write, database read, provider cache |
| `runtime_dataframe_projection` | `pandas`, `datashader`, `numpy`, projection formula, flip formula, mask formula |
| `controller_selection` | selected vehicle runtime, picker, hit-test, controller mutation |
| `renderer_host` | `TaichiGlobeRenderer`, `QtHybridWindow`, `VisPyHybridViewer`, `taichi`, `PyQt6`, `PySide6`, `vispy` |
| `hot_path` | alpha helpers, apply path, composition apply |
| `artifact_metadata` | metadata sidecar writer, artifact writer, state writer, PNG writer, runtime JSON writer |

## AST coverage

The checker inspects:

- `ast.Import`
- `ast.ImportFrom`
- `ast.Name`
- `ast.Attribute`
- `ast.Call`
- `ast.FunctionDef.name`
- `ast.AsyncFunctionDef.name`
- `ast.ClassDef.name`

Declaration-name coverage is required so a future candidate cannot re-declare forbidden source, stream, cache, controller, renderer, or writer names as local functions or classes.

## Allowed string-label distinction

The following labels are allowed only as data strings:

- `ais_source`
- `adsb_source`
- `sql_replay_lineage`
- `websocket_live_lineage`
- `synthetic_source`
- `unavailable_source`
- `timestamp_quality`
- `coordinate_payload_quality`
- `source_id`
- `lineage_status`
- `cache_read_blocked_surface`
- `database_blocked_surface`
- `live_stream_blocked_surface`

If similar names appear as imports, from-imports, executable name references, attribute references, call targets, function definitions, async function definitions, or class definitions, they are checked against forbidden families and may fail.

## Negative self-test result expectation

`--self-test-negative` must detect snippets from every forbidden family, including forbidden declaration names. The self-test is in-memory only and does not create `render_core\dynamic_point_source_lineage_boundary.py`.

Expected self-test packet fields:

- `negative_self_test_passed=true`
- `all_forbidden_snippets_detected=true`
- `boundary_passed=true`

## Relationship to prior matrix gate

The source/lineage craton ablation matrix filled these deterministic cells:

- `future_helper_target = render_core\dynamic_point_source_lineage_boundary.py`
- `new_checker_required = true`
- `source_lineage_planning_candidate = true`
- `source_lineage_extraction_candidate = false`
- `helper_module_creation_authorized = false`
- `source_movement_authorized = false`

This checker gate implements only the checker cell. It does not authorize the future helper module or source movement.

## Explicit exclusions

This gate excludes:

- creating `render_core\dynamic_point_source_lineage_boundary.py`
- modifying `render_core\dynamic_point_boundary.py`
- modifying `taichi_global_bathymetry.py`
- modifying the aggregate dynamic point checker
- importing or executing monolith
- importing or executing SQL, WebSocket, cache, live, dataframe, or runtime dependencies
- reading real AIS, ADS-B, cache, or database data
- changing projection, controller, or render behavior
- authorizing source movement
- declaring extraction candidate status
- live-data, readiness, bug-fix, visual parity, or performance claims

## Boundary statement

Tooling/docs-only dynamic point source/lineage import-boundary checker gate. No helper module creation, no source movement, no production helper target creation, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix claim.

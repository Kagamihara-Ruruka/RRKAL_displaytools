# Displaytools AIS / Aircraft Dynamic Point Import Boundary Checker Gate

## Scope

本文件定義 AIS / aircraft dynamic point descriptor helper 的 tooling/docs-only import boundary checker gate。未來假想目標是 `render_core\dynamic_point_boundary.py`，本輪不建立 helper module、不移動 source、不修改 production code。

此 gate 只建立 AST-only checker、checker tests 與文件索引。checker 不 import 目標 module、不 execute 目標 module，missing candidate 必須回傳 JSON pass，表示目前尚無 candidate 可檢查。

## Checker behavior

| field | pinned value |
| --- | --- |
| `schema` | `rrkal_displaytools.dynamic_point_import_boundary.v1` |
| `default_target` | `render_core\dynamic_point_boundary.py` |
| `candidate_missing_status` | `not_applicable_candidate_missing` |
| `candidate_missing_boundary_passed` | `true` |
| `syntax_error_status` | `syntax_error` |
| `string_labels_allowed_as_data` | `true` |
| `runtime_render_invoked` | `false` |
| `runtime_merge_enabled` | `false` |

Checker inspection scope:

- `ast.Import`
- `ast.ImportFrom`
- `ast.Name`
- `ast.Attribute`
- `ast.Call` target names
- `ast.FunctionDef.name`
- `ast.AsyncFunctionDef.name`
- `ast.ClassDef.name`

## Missing candidate behavior

`render_core\dynamic_point_boundary.py` is not created in this slice. The checker must report:

- `candidate_exists = false`
- `status = not_applicable_candidate_missing`
- `boundary_passed = true`
- `violations = []`

This missing-candidate pass is not an extraction claim. It only proves the checker can run before the future helper exists.

## Forbidden family coverage

The checker blocks executable imports, direct name references, attribute references, call targets, and declaration names for these families:

| family | blocked examples |
| --- | --- |
| monolith | `taichi_global_bathymetry` |
| SQL replay database | `pymysql`, `sqlalchemy`, `mysql`, `DB_URL`, `replay_query` |
| live stream | `websocket`, `AISStream`, `ADSBStream`, live AIS labels as executable names |
| runtime dataframe projection | `pandas`, `datashader`, `numpy`, projection formula, flip formula, mask formula |
| controller selection | selected vehicle runtime, picker, hit-test, controller mutation |
| renderer host | `TaichiGlobeRenderer`, `QtHybridWindow`, `VisPyHybridViewer`, `taichi`, `PyQt6`, `PySide6`, `vispy` |
| hot path | alpha helpers, apply path, composition apply |
| artifact metadata | metadata sidecar writer, artifact writer, state writer, PNG writer, runtime JSON writer |

## Allowed string-label distinction

The checker intentionally allows harmless string labels when they are packet data only:

- `AIS`
- `ADS-B`
- `replay`
- `synthetic`
- `unavailable`
- `live_lineage_unresolved`
- `timestamp_staleness`
- `selected_vehicle`
- `projection_label`
- `datashader_blocked`
- `sql_blocked`
- `websocket_blocked`
- `cache_unavailable`

These labels remain forbidden when used as executable imports, declarations, call targets, direct references, attribute references, or runtime dependencies.

## Negative self-test

`--self-test-negative` uses in-memory snippets only. It does not write product files and does not create `render_core\dynamic_point_boundary.py`.

The negative self-test must prove that forbidden snippets covering monolith, SQL replay, live stream, dataframe runtime, projection or mask formula names, controller selection, renderer host, hot path, and artifact writer references are detected.

## Stop lines

This gate does not authorize:

- helper module creation
- source movement
- production source modification
- monolith import
- SQL, WebSocket, or live-source execution
- real AIS, ADS-B, cache, or database reads
- pandas, datashader, or numpy runtime
- projection, flip, or mask formula changes
- controller selection runtime changes
- renderer, Qt, VisPy, or Taichi runtime execution
- metadata or output schema changes
- runtime merge enablement
- live-data, readiness, visual parity, performance, or bug-fix claims

## Recommended next gate

If this checker gate passes, the next step remains review-driven. A future extraction slice may only be considered after `o_1` review and any required macro observer review. The future helper candidate must remain descriptor, policy, and ledger only.

## Boundary statement

Tooling/docs-only AIS/aircraft dynamic point import-boundary checker gate. No helper module creation, no source movement, no production source change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection runtime change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/bug-fix claim.

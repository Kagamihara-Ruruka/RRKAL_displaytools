# Displaytools Dynamic Point Source / Lineage Source-Surface Movement Preimplementation Gate

## Scope

本文件定義 AIS / aircraft dynamic point source/lineage 的 docs/test-only source-surface movement preimplementation gate。此 slice 只分類 source/lineage surfaces，不建立 helper module，不移動 source，不修改 `render_core\dynamic_point_boundary.py`，不修改或 import `taichi_global_bathymetry.py`。

Provider/lineage fixture gate 已指出下一步應先看 source/lineage，而不是 selection/render-policy。本 gate 將 source/lineage 分成 descriptor-only candidate 與 runtime stop-line surfaces，避免下一刀碰到 SQL、WebSocket、live source、cache、database、dataframe runtime、projection、controller 或 renderer host。

## Evidence read

- `tests\test_displaytools_dynamic_point_provider_lineage_boundary.py`
- `docs\DISPLAYTOOLS_DYNAMIC_POINT_PROVIDER_LINEAGE_BOUNDARY_FIXTURE_GATE.zh-TW.md`
- `render_core\dynamic_point_boundary.py`
- `tests\test_displaytools_dynamic_point_boundary_helpers.py`
- `tests\test_displaytools_dynamic_point_craton_ablation_matrix.py`
- `tests\test_displaytools_dynamic_point_boundary_minimal_extraction_planning.py`
- `scripts\validate_displaytools_dynamic_point_import_boundary.py`
- current `taichi_global_bathymetry.py` remains read-only and is not imported or executed

## Source-surface category matrix

| category | planning candidate | extraction candidate | blocked reason |
| --- | --- | --- | --- |
| `category_a_source_lineage_descriptor_policy_ledger` | `true` | `false` | descriptor labels and ledgers only |
| `category_b_sql_replay_runtime` | `false` | `false` | SQL replay is executable database runtime |
| `category_c_live_websocket_runtime` | `false` | `false` | WebSocket and live streams are network runtime |
| `category_d_cache_database_io` | `false` | `false` | real AIS, ADS-B, cache, and database reads are IO behavior |
| `category_e_dataframe_projection_runtime` | `false` | `false` | pandas, datashader, numpy, projection, flip, and mask are runtime or formula surfaces |
| `category_f_controller_selection_runtime` | `false` | `false` | selected vehicle, picker, hit-test, and controller mutation are runtime behavior |
| `category_g_renderer_host_runtime` | `false` | `false` | renderer, Qt, VisPy, Taichi, and GUI host are runtime behavior |

Only category A can be a future descriptor planning candidate. No category is an extraction candidate in this slice.

## Candidate summary

| field | value |
| --- | --- |
| `source_lineage_planning_candidate` | `true` |
| `source_lineage_extraction_candidate` | `false` |
| `source_movement_authorized` | `false` |
| `helper_module_creation_authorized` | `false` |
| `import_boundary_checker_required_before_extraction` | `true` |
| `existing_checker` | `scripts\validate_displaytools_dynamic_point_import_boundary.py` |
| `future_helper_target` | `render_core\dynamic_point_source_lineage_boundary.py` |

Target decision: this gate chooses `render_core\dynamic_point_source_lineage_boundary.py` instead of reusing `render_core\dynamic_point_boundary.py`, because source/lineage is a second-layer candidate narrower than the existing aggregate dynamic point boundary helper. This is a planning target only. The file must not be created in this slice.

## Future descriptor candidate families

Future descriptor-only candidate families:

- `build_dynamic_point_source_lineage_descriptor`
- `build_dynamic_point_replay_lineage_label_descriptor`
- `build_dynamic_point_live_lineage_label_descriptor`
- `build_dynamic_point_source_availability_descriptor`
- `build_dynamic_point_timestamp_quality_descriptor`
- `build_dynamic_point_coordinate_payload_quality_descriptor`
- `build_dynamic_point_source_lineage_known_fault_ledger`
- `dynamic_point_source_lineage_boundary_descriptor`
- `dynamic_point_source_lineage_planning_bundle`

Each candidate is limited to dict/list/scalar descriptor builder or policy/ledger table content. Runtime dependencies are not allowed. Candidate planning is true; candidate extraction remains false.

## Blocked surfaces

Blocked surfaces:

- SQL / MySQL / pymysql / sqlalchemy / DB URL / replay query execution
- WebSocket / live AIS / live ADS-B stream execution
- real AIS / ADS-B / cache / database read
- pandas / datashader / numpy runtime
- projection / flip / mask formula
- controller selection / picker / hit-test mutation
- renderer / Qt / VisPy / Taichi runtime
- metadata / artifact writer
- alpha / apply / composition hot path
- readiness / performance / visual parity / bug-fix / live-data claims

These surfaces remain outside descriptor planning and must not be pulled into a future helper candidate.

## Decision output

| field | value |
| --- | --- |
| `source_lineage_source_surface_gate_passed` | `true` |
| `source_lineage_planning_candidate` | `true` |
| `source_lineage_extraction_candidate` | `false` |
| `source_movement_authorized` | `false` |
| `helper_module_creation_authorized` | `false` |
| `recommended_next_gate` | `dynamic_point_source_lineage_craton_ablation_matrix_gate` |

The next gate should use a craton ablation matrix to sharpen dependency footprints before any import-boundary checker or extraction planning for the source/lineage second layer.

## Explicit exclusions

This gate excludes:

- modifying `render_core\dynamic_point_boundary.py`
- creating `render_core\dynamic_point_source_lineage_boundary.py`
- modifying or importing `taichi_global_bathymetry.py`
- SQL, WebSocket, live source, cache, database, dataframe, or runtime imports
- projection, flip, mask, controller, renderer, Qt, VisPy, or Taichi behavior changes
- helper module creation
- source movement
- extraction authorization
- live-data, readiness, bug-fix, visual parity, or performance claims

## Boundary statement

Docs/test-only dynamic point source/lineage source-surface movement preimplementation gate. No helper module creation, no source movement, no production source change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix claim.

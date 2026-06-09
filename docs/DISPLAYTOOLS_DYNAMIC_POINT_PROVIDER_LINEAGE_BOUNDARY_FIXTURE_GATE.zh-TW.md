# Displaytools Dynamic Point Provider / Lineage Boundary Fixture Gate

## Scope

本文件定義 AIS / aircraft dynamic point provider / lineage boundary fixture gate。此 slice 只新增測試與文件，用純 descriptor 釐清 AIS、ADS-B、SQL replay label、WebSocket live label、synthetic、unavailable、timestamp、lat/lon、source id、lineage status 與 blocked provider surfaces 的邊界。

本 gate 不修改 `render_core\dynamic_point_boundary.py`，不建立 helper module，不修改 `taichi_global_bathymetry.py`，不 import monolith，不執行 SQL、WebSocket、live source、cache、database、pandas、datashader、numpy、projection、controller、renderer、Qt、VisPy 或 Taichi runtime。

## Evidence read

- `render_core\dynamic_point_boundary.py`
- `tests\test_displaytools_dynamic_point_boundary_helpers.py`
- `tests\test_displaytools_dynamic_point_craton_ablation_matrix.py`
- `tests\test_displaytools_dynamic_point_boundary_minimal_extraction_planning.py`
- `scripts\validate_displaytools_dynamic_point_import_boundary.py`
- current `taichi_global_bathymetry.py` remains read-only and is not imported or executed

## Provider / lineage fixture matrix

| surface | source kind | lineage kind | fixture status | forbidden next action |
| --- | --- | --- | --- | --- |
| `ais_source` | `AIS` | source label only | `pinned` | do not execute AIS provider or database source |
| `adsb_source` | `ADS-B` | source label only | `pinned` | do not execute ADS-B provider or live source |
| `sql_replay_lineage` | `replay` | SQL replay label only | `blocked_runtime_only` | do not execute SQL, MySQL, pymysql, sqlalchemy, or replay query |
| `websocket_live_lineage` | `live_lineage_unresolved` | WebSocket live label only | `blocked_runtime_only` | do not open WebSocket, live AIS, or live ADS-B |
| `synthetic_source` | `synthetic` | synthetic label only | `pinned` | do not generate runtime points or render buffers |
| `unavailable_source` | `unavailable` | unavailable label only | `pinned` | do not probe real provider or cache |
| `stale_timestamp` | `AIS` | timestamp staleness label only | `unresolved_static_only` | do not execute real clock or replay clock |
| `missing_timestamp` | `AIS` | timestamp missing label only | `unresolved_static_only` | do not parse real payload or query database |
| `missing_lat_lon` | `AIS` | coordinate missing label only | `unresolved_static_only` | do not invoke projection or mask formula |
| `invalid_lat_lon` | `ADS-B` | coordinate invalid label only | `unresolved_static_only` | do not normalize real coordinates or invoke projection |
| `source_id_label` | `AIS` | source id label only | `pinned` | do not resolve real source identity or database handle |
| `lineage_status_label` | `AIS` | lineage status label only | `pinned` | do not convert lineage label into runtime source |
| `provider_blocked_surface` | `unavailable` | provider blocked label only | `blocked_runtime_only` | do not execute provider loader or source runtime |
| `database_blocked_surface` | `replay` | database blocked label only | `blocked_runtime_only` | do not open database or create DB handle |
| `live_stream_blocked_surface` | `live_lineage_unresolved` | live stream blocked label only | `blocked_runtime_only` | do not open socket or live stream |
| `cache_read_blocked_surface` | `unavailable` | cache read blocked label only | `blocked_runtime_only` | do not read real AIS, ADS-B, cache, or database |

Every fixture descriptor is limited to dict/list/scalar packet data. Runtime object, callable, module, DB handle, dataframe, socket, and render buffer values remain forbidden.

## Decision output

| field | value |
| --- | --- |
| `provider_lineage_fixture_gate_passed` | `true` |
| `source_lineage_planning_candidate` | `true` |
| `selection_render_policy_planning_candidate` | `false` |
| `source_lineage_extraction_candidate` | `false` |
| `selection_render_policy_extraction_candidate` | `false` |
| `helper_module_creation_authorized` | `false` |
| `source_movement_authorized` | `false` |
| `recommended_next_gate` | `dynamic_point_source_lineage_source_surface_movement_preimplementation_gate` |

The matrix points the next planning gate toward source/lineage because provider and lineage stop lines are now sharper than selection/render-policy stop lines. This does not authorize extraction.

## Explicit exclusions

This gate excludes:

- helper module creation
- production source movement
- `render_core\dynamic_point_boundary.py` modification
- `taichi_global_bathymetry.py` modification or import
- SQL / MySQL / pymysql / sqlalchemy / replay query
- WebSocket / live AIS / live ADS-B
- real AIS / ADS-B / cache / database read
- pandas / datashader / numpy runtime import
- projection / flip / mask formula
- controller selection / picker / hit-test mutation
- renderer / Qt / VisPy / Taichi runtime
- metadata / artifact writers
- alpha / apply / composition hot path
- runtime merge enablement
- readiness, performance, visual parity, bug-fix, or live-data claim

## Recommended next gate

Recommended next gate: `dynamic_point_source_lineage_source_surface_movement_preimplementation_gate`.

The next gate should classify whether source/lineage descriptors can be further planned without touching SQL, WebSocket, live source, real cache, database, dataframe runtime, projection, or controller behavior.

## Boundary statement

Test/docs-only dynamic point provider/lineage boundary fixture gate. No helper module creation, no source movement, no production source change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix claim.

# Displaytools Dynamic Point Source / Lineage Craton Ablation Matrix Gate

## Scope

本文件定義 dynamic point source/lineage 的 docs/test-only craton ablation capability matrix 與 deterministic boundary fill gate。此 slice 不建立 `render_core\dynamic_point_source_lineage_boundary.py`，不修改 `render_core\dynamic_point_boundary.py`，不修改 import-boundary checker，不修改或 import `taichi_global_bathymetry.py`。

此 gate 根據 source/lineage source-surface movement gate 的結論，將 source/lineage pins 做 descriptor-only ablation matrix，並直接填出下一刀的 target、descriptor candidate families、blocked runtime surfaces、checker need 與 next gate。

## Evidence read

- `tests\test_displaytools_dynamic_point_source_lineage_source_surface_movement.py`
- `docs\DISPLAYTOOLS_DYNAMIC_POINT_SOURCE_LINEAGE_SOURCE_SURFACE_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md`
- `tests\test_displaytools_dynamic_point_provider_lineage_boundary.py`
- `render_core\dynamic_point_boundary.py`
- `tests\test_displaytools_dynamic_point_boundary_helpers.py`
- `tests\test_displaytools_dynamic_point_craton_ablation_matrix.py`
- `scripts\validate_displaytools_dynamic_point_import_boundary.py`
- current `taichi_global_bathymetry.py` remains read-only and is not imported or executed

## Phase A: Source / Lineage Ablation Matrix

Every pin carries:

- `pin_name`
- `ablation_modes`
- `consumer_expectation`
- `rollback_method`
- `dependency_classification`
- `fixture_status`
- `forbidden_next_action`

Ablation modes are pinned for every row:

- `null_mode`
- `tripwire_mode`
- `trace_mode`
- `substitute_mode`

| pin | dependency classification | fixture status | consumer expectation |
| --- | --- | --- | --- |
| `ais_source_label` | descriptor policy ledger | `pinned` | descriptor consumers degrade to unavailable source label only |
| `adsb_source_label` | descriptor policy ledger | `pinned` | descriptor consumers degrade to unavailable source label only |
| `sql_replay_lineage_label` | descriptor label with blocked runtime peer | `pinned` | tripwire marks SQL replay as blocked runtime dependency |
| `websocket_live_lineage_label` | descriptor label with blocked runtime peer | `pinned` | tripwire marks live lineage as blocked runtime dependency |
| `synthetic_source_label` | descriptor policy ledger | `pinned` | substitute descriptor remains local fixture data |
| `unavailable_source_label` | descriptor policy ledger | `pinned` | null mode keeps provider unavailable branch deterministic |
| `timestamp_quality_label` | descriptor policy ledger | `unresolved_static_only` | trace mode records stale and missing timestamp labels only |
| `coordinate_payload_quality_label` | descriptor policy ledger | `unresolved_static_only` | trace mode records missing and invalid lat/lon labels only |
| `source_id_label` | descriptor policy ledger | `pinned` | substitute mode keeps source id as scalar label |
| `lineage_status_label` | descriptor policy ledger | `pinned` | null mode keeps lineage status label unresolved without runtime source |
| `provider_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if provider execution is required |
| `database_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if database runtime is required |
| `live_stream_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if live stream runtime is required |
| `cache_io_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if cache IO is required |
| `dataframe_projection_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if dataframe or projection runtime is required |

The matrix excludes runtime patching. Rollback is either restoration of a test-local descriptor label or not applicable because no runtime patch is used.

## Phase B: Deterministic Boundary Fill

| filled cell | value |
| --- | --- |
| `future_helper_target` | `render_core\dynamic_point_source_lineage_boundary.py` |
| `import_boundary_checker_needed` | `true` |
| `existing_checker_reusable` | `false` |
| `new_checker_required` | `true` |
| `source_lineage_planning_candidate` | `true` |
| `source_lineage_extraction_candidate` | `false` |
| `helper_module_creation_authorized` | `false` |
| `source_movement_authorized` | `false` |

The existing aggregate dynamic point checker is not modified in this slice. Because the future target is a narrower second-layer helper, a dedicated source-lineage checker is required before extraction planning can advance.

## Candidate families assessment

Descriptor-only candidate families:

- `build_dynamic_point_source_lineage_descriptor`
- `build_dynamic_point_replay_lineage_label_descriptor`
- `build_dynamic_point_live_lineage_label_descriptor`
- `build_dynamic_point_source_availability_descriptor`
- `build_dynamic_point_timestamp_quality_descriptor`
- `build_dynamic_point_coordinate_payload_quality_descriptor`
- `build_dynamic_point_source_lineage_known_fault_ledger`
- `dynamic_point_source_lineage_boundary_descriptor`
- `dynamic_point_source_lineage_planning_bundle`

Assessment: these are planning candidates only. They are not extraction candidates in this slice.

## Blocked runtime surfaces

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

These surfaces remain blocked and must not appear in a future descriptor helper.

## Phase C: Next-gate decision

Recommended next gate: `dynamic_point_source_lineage_import_boundary_checker_gate`.

Reason: the future target `render_core\dynamic_point_source_lineage_boundary.py` is distinct from the existing aggregate `render_core\dynamic_point_boundary.py`. A dedicated checker is the clean next step before any minimal extraction planning for the second-layer source/lineage helper.

## Explicit exclusions

This gate excludes:

- creating `render_core\dynamic_point_source_lineage_boundary.py`
- modifying `render_core\dynamic_point_boundary.py`
- modifying `taichi_global_bathymetry.py`
- creating or modifying import-boundary checker scripts
- importing or executing monolith
- importing or executing SQL, WebSocket, cache, live, dataframe, or runtime dependencies
- changing projection, controller, or render behavior
- authorizing source movement
- declaring extraction candidate status
- live-data, readiness, bug-fix, visual parity, or performance claims

## Boundary statement

Docs/test-only dynamic point source/lineage craton ablation capability matrix and deterministic boundary fill gate. No helper module creation, no source movement, no production source change, no import-boundary checker change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix claim.

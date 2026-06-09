# Displaytools AIS / Aircraft Dynamic Point Craton Ablation Capability Matrix Gate

## Scope

本文件定義 AIS / aircraft dynamic point 的 docs/test-only 克拉通消融能力矩陣與確定格填入法試點。此 gate 不建立 `render_core\dynamic_point_boundary.py`，不修改 production source，不 import monolith，不執行 SQL、WebSocket、live source、database、datashader、renderer、Qt、VisPy 或 Taichi runtime。

此 gate 的目的，是用矩陣化 descriptor 描述 dynamic point 各表面被暫時遮斷、替換或追蹤時，可能影響哪些 consumer。接著把 Phase A 能確定推出的 descriptor、stop-line、checker、planning 邊界直接填入 Phase B，減少下一刀前的不確定格。

## Phase A: Craton Ablation Capability Matrix

Matrix dimensions:

- `craton_surface`
- `ablation_mode`
- `consumer_surface`
- `expected_effect`
- `risk_level`
- `rollback_method`
- `evidence_level`
- `forbidden_next_action`

Ablation modes:

- `null_mode`
- `tripwire_mode`
- `trace_mode`
- `substitute_mode`

Required matrix cases:

| craton surface | ablation mode | consumer surface | expected effect | risk level | rollback method | evidence level |
| --- | --- | --- | --- | --- | --- | --- |
| source descriptor | null mode | descriptor bundle | degraded descriptor | low | remove fake descriptor | historically grounded |
| payload shape descriptor | substitute mode | future helper candidate | no effect | low | restore descriptor bundle | structurally inferred |
| replay/live lineage descriptor | tripwire mode | safety checker | hidden dependency discovered | medium | reset test-local recorder | historically grounded |
| selection descriptor | trace mode | selection panel | hidden dependency discovered | medium | reset test-local recorder | structurally inferred |
| render policy descriptor | null mode | render policy consumer | degraded descriptor | medium | restore descriptor bundle | structurally inferred |
| safety ledger | tripwire mode | safety checker | extraction stop condition | blocked | reset test-local recorder | historically grounded |
| known fault ledger | substitute mode | planning bundle | degraded descriptor | low | restore descriptor bundle | exploratory |
| projection peer sync candidate | trace mode | projection peer | hidden dependency discovered | high | reset test-local recorder | structurally inferred |
| selection panel dependency | trace mode | selection panel | hidden dependency discovered | high | reset test-local recorder | structurally inferred |
| render policy consumer dependency | null mode | render policy consumer | degraded descriptor | medium | restore descriptor bundle | structurally inferred |
| SQL/WebSocket/datashader runtime dependency | tripwire mode | safety checker | blocked runtime dependency | blocked | not applicable because no runtime patch | historically grounded |
| runtime dependency required stop condition | tripwire mode | future helper candidate | extraction stop condition | blocked | not applicable because no runtime patch | structurally inferred |

Every row is descriptor-only. It does not patch production objects and does not invoke runtime behavior.

## Phase B: Deterministic Boundary Fill

The matrix fills these deterministic cells directly:

| filled cell | value |
| --- | --- |
| `future_helper_target` | `render_core\dynamic_point_boundary.py` |
| `candidate_scope` | `descriptor_policy_ledger_only` |
| `source_movement_authorized` | `false` |
| `helper_module_creation_authorized` | `false` |
| `dynamic_point_extraction_candidate` | `false` |
| `dynamic_point_planning_candidate` | `true` |
| `a1_macro_observer_required_before_source_movement` | `true` |
| `import_boundary_checker_already_available` | `true` |
| `checker_script` | `scripts\validate_displaytools_dynamic_point_import_boundary.py` |
| `runtime_dependency_allowed` | `false` |
| `sql_replay_database_surface` | `blocked` |
| `live_stream_surface` | `blocked` |
| `dataframe_projection_runtime_surface` | `blocked` |
| `controller_selection_runtime_surface` | `blocked` |
| `renderer_host_surface` | `blocked` |
| `metadata_artifact_writer_surface` | `blocked` |

This fill does not authorize extraction. It only records cells that are already determined by fixture gates, planning gates, and the import-boundary checker.

## Phase C: Next-slice refinement

Decision output:

| field | value |
| --- | --- |
| `ablation_matrix_methodology_trial` | `true` |
| `production_monkey_patch_used` | `false` |
| `runtime_import_used` | `false` |
| `source_movement_authorized` | `false` |
| `dynamic_point_extraction_candidate` | `false` |
| `matrix_improves_next_gate_precision` | `true` |
| `matrix_precision_reason` | matrix fills deterministic descriptor stop lines before source movement |
| `recommended_next_gate` | `dynamic_point_boundary_minimal_extraction_gate_after_a1_macro_review` |

The matrix is useful because it narrows the next gate to descriptor, policy, and ledger only while preserving runtime stop lines. It does not claim the helper is safe to extract.

## Explicit stop lines

This gate forbids:

- creating `render_core\dynamic_point_boundary.py`
- modifying production source
- importing `taichi_global_bathymetry.py`
- monkey patching production objects
- executing SQL, WebSocket, live source, replay database, or cache reads
- importing pandas, datashader, or numpy runtime
- changing projection, flip, or mask formulas
- changing controller selection runtime
- executing renderer, Qt, VisPy, or Taichi runtime
- changing metadata or output schema
- enabling runtime merge
- claiming live data restoration, readiness, bug fix, visual parity, performance, or safe extraction

## Recommended next gate

If `o_1` accepts this methodology trial and `a_1` macro observer supports the boundary, the next gate can be `dynamic_point_boundary_minimal_extraction_gate_after_a1_macro_review`. That next gate would still need explicit authorization and must not be inferred from this document alone.

## Boundary statement

Docs/test-only dynamic point craton ablation capability matrix and deterministic boundary fill methodology trial. No production monkey patch, no production source change, no helper module creation, no source movement, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection runtime change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/bug-fix/safe-to-extract claim.

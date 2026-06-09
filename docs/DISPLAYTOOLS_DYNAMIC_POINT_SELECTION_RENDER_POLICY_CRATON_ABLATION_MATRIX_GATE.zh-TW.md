# Displaytools Dynamic Point Selection / Render Policy Craton Ablation Matrix Gate

## Scope

本文件定義 dynamic point selection / render policy 的 docs/test-only craton ablation capability matrix 與 deterministic boundary fill gate。此 slice 不建立 `render_core\dynamic_point_selection_render_policy_boundary.py`，不修改 `render_core\dynamic_point_boundary.py`，不修改 `render_core\dynamic_point_source_lineage_boundary.py`，不修改 checker，不修改或 import `taichi_global_bathymetry.py`。

目的只是在 source/lineage 已完成第二層 descriptor helper 後，測繪 selected vehicle、selected layer、hit state、picker status、visible/rendered count、render cap 與 adaptive sampling 這些 surface 是否能維持 descriptor / policy / ledger-only 邊界。

## Evidence read

- `render_core\dynamic_point_boundary.py`
- `render_core\dynamic_point_source_lineage_boundary.py`
- `tests\test_displaytools_dynamic_point_source_lineage_boundary_helpers.py`
- `tests\test_displaytools_dynamic_point_source_lineage_craton_ablation_matrix.py`
- `tests\test_displaytools_dynamic_point_craton_ablation_matrix.py`
- current `taichi_global_bathymetry.py` remains read-only and is not imported or executed

## Phase A: Selection / Render Policy Ablation Matrix

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
| `selected_vehicle_label` | descriptor policy ledger | `pinned` | descriptor consumers degrade to no selected vehicle label only |
| `selected_layer_label` | descriptor policy ledger | `pinned` | descriptor consumers degrade to no selected layer label only |
| `hit_state_label` | descriptor policy ledger | `unresolved_static_only` | trace mode records hit true false unresolved labels only |
| `picker_status_label` | descriptor label with blocked runtime peer | `pinned` | tripwire marks picker status as runtime-adjacent label only |
| `visible_count_label` | descriptor policy ledger | `pinned` | null mode keeps visible count policy as scalar label |
| `rendered_count_label` | descriptor policy ledger | `pinned` | null mode keeps rendered count policy as scalar label |
| `render_cap_label` | descriptor policy ledger | `pinned` | substitute mode keeps render cap as policy label |
| `adaptive_sampling_label` | descriptor policy ledger | `pinned` | substitute mode keeps adaptive sampling as label-only policy |
| `selection_staleness_fault` | descriptor policy ledger | `unresolved_static_only` | trace mode records stale selection as known fault ledger only |
| `hit_test_dependency_fault` | descriptor label with blocked runtime peer | `blocked_runtime_only` | tripwire marks hit-test dependency as blocked runtime peer |
| `render_policy_guard_flag` | descriptor policy ledger | `pinned` | substitute mode preserves guard flags without runtime policy execution |
| `controller_selection_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if controller selection mutation is required |
| `picker_hit_test_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if picker or hit-test execution is required |
| `datashader_sampling_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if dataframe sampling runtime is required |
| `renderer_host_runtime_dependency` | blocked runtime dependency | `blocked_runtime_only` | tripwire must stop extraction if renderer host runtime is required |

The matrix is descriptor-only. Rollback is either restoration of a test-local descriptor label or not applicable because no runtime patch is used.

## Phase B: Deterministic Boundary Fill

| filled cell | value |
| --- | --- |
| `future_helper_target` | `render_core\dynamic_point_selection_render_policy_boundary.py` |
| `import_boundary_checker_needed` | `true` |
| `existing_checker_reusable` | `false` |
| `new_checker_required` | `true` |
| `selection_render_policy_planning_candidate` | `true` |
| `selection_render_policy_extraction_candidate` | `false` |
| `helper_module_creation_authorized` | `false` |
| `source_movement_authorized` | `false` |

The existing aggregate dynamic point checker and source-lineage checker are not modified in this slice. Because the future target is a narrower second-layer selection/render-policy helper, a dedicated checker is required before extraction planning can advance.

## Candidate families assessment

Descriptor-only candidate families:

- `build_dynamic_point_selection_label_descriptor`
- `build_dynamic_point_hit_state_label_descriptor`
- `build_dynamic_point_picker_status_descriptor`
- `build_dynamic_point_render_count_policy_descriptor`
- `build_dynamic_point_render_cap_policy_descriptor`
- `build_dynamic_point_adaptive_sampling_policy_descriptor`
- `build_dynamic_point_selection_render_known_fault_ledger`
- `dynamic_point_selection_render_policy_boundary_descriptor`
- `dynamic_point_selection_render_policy_planning_bundle`

Assessment: these are planning candidates only. They are not extraction candidates in this slice.

## Blocked runtime surfaces

Blocked surfaces:

- controller selection mutation
- selected vehicle runtime object
- picker / hit-test execution
- datashader / pandas / numpy runtime sampling
- renderer / Qt / VisPy / Taichi runtime
- projection / flip / mask formula
- SQL / WebSocket / live AIS / live ADS-B
- real AIS / ADS-B / cache / database read
- metadata / artifact writer
- alpha / apply / composition hot path
- readiness / performance / visual parity / bug-fix / live-data claims

These surfaces remain blocked and must not appear in a future descriptor helper.

## Phase C: Next-gate decision

Recommended next gate: `dynamic_point_selection_render_policy_import_boundary_checker_gate`.

Reason: the future target `render_core\dynamic_point_selection_render_policy_boundary.py` is distinct from the existing aggregate `render_core\dynamic_point_boundary.py` and from `render_core\dynamic_point_source_lineage_boundary.py`. Selection/render-policy has controller and picker runtime risks that need a dedicated checker before any minimal extraction planning.

## Explicit exclusions

This gate excludes:

- creating `render_core\dynamic_point_selection_render_policy_boundary.py`
- modifying `render_core\dynamic_point_boundary.py`
- modifying `render_core\dynamic_point_source_lineage_boundary.py`
- modifying `taichi_global_bathymetry.py`
- creating or modifying import-boundary checker scripts
- importing or executing monolith
- importing or executing controller, picker, datashader, dataframe, renderer, Qt, VisPy, or Taichi runtime dependencies
- changing selection, hit-test, render policy, projection, controller, or render behavior
- authorizing source movement
- declaring extraction candidate status
- live-data, readiness, bug-fix, visual parity, or performance claims

## Boundary statement

Docs/test-only dynamic point selection/render policy craton ablation capability matrix and deterministic boundary fill gate. No helper module creation, no source movement, no production source change, no import-boundary checker change, no monolith import, no controller/picker/hit-test/datashader/runtime execution, no real AIS/ADS-B/cache/database read, no projection/flip/mask formula change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix claim.

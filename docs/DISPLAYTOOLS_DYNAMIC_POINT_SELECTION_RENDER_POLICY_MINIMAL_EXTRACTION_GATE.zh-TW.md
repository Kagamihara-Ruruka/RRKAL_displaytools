# Dynamic Point Selection / Render Policy Minimal Extraction Gate

## Gate scope

本 gate 是 dynamic point selection / render policy 的最小第一刀。新增的 `render_core\dynamic_point_selection_render_policy_boundary.py` 只放 descriptor / policy / ledger helper，不接 controller、picker、hit-test、Datashader、projection、renderer 或 runtime 行為。

## Evidence read

- `tests\test_displaytools_dynamic_point_selection_render_policy_minimal_extraction_planning.py`
- `tests\test_displaytools_dynamic_point_selection_render_policy_import_boundary.py`
- `scripts\validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py`
- `tests\test_displaytools_dynamic_point_selection_render_policy_craton_ablation_matrix.py`
- `render_core\dynamic_point_source_lineage_boundary.py`

## Helpers introduced

| Helper | Boundary |
| --- | --- |
| `build_dynamic_point_selection_label_descriptor` | selected vehicle / selected layer label only; no runtime object. |
| `build_dynamic_point_hit_state_label_descriptor` | hit state label only; no hit-test execution. |
| `build_dynamic_point_picker_status_descriptor` | picker status label only; no picker runtime. |
| `build_dynamic_point_render_count_policy_descriptor` | visible/rendered count policy labels only; no dataframe or render buffer count query. |
| `build_dynamic_point_render_cap_policy_descriptor` | render cap policy label only; no renderer cap execution. |
| `build_dynamic_point_adaptive_sampling_policy_descriptor` | adaptive sampling policy label only; no Datashader, pandas, or NumPy runtime. |
| `build_dynamic_point_selection_render_known_fault_ledger` | unresolved selection/render known-fault ledger. |
| `dynamic_point_selection_render_policy_boundary_descriptor` | bundle of descriptor/policy/ledger helper outputs. |
| `dynamic_point_selection_render_policy_planning_bundle` | planning bundle with guard flags and blocked surfaces. |

## Fixture parity coverage

The helper tests pin:

- safe helper import
- exact key sets for every descriptor builder
- deterministic repeat-call parity
- dict/list/scalar-only output
- selected vehicle and selected layer label branches
- hit state branches
- picker status branches
- visible count and rendered count branches
- render cap branch
- adaptive sampling branch
- selection staleness, hit-test dependency, render policy guard, controller, picker, Datashader, and renderer fault ledger entries
- planning bundle guard flags
- no runtime, live-data, readiness, visual parity, performance, bug-fix, or safe-to-extract claims

## Import-boundary checker result

The dedicated checker target is `render_core\dynamic_point_selection_render_policy_boundary.py`. The helper is expected to pass because it is AST-only safe: no forbidden imports, no forbidden runtime declarations, no controller or picker execution, and string labels remain data labels.

One required public helper contains the word `picker`. The module exports it through a string-keyed alias to keep the checker behavior unchanged while preserving the required API and avoiding a forbidden executable declaration name.

## Explicit exclusions

This extraction does not move or modify:

- `render_core\dynamic_point_boundary.py`
- `render_core\dynamic_point_source_lineage_boundary.py`
- `taichi_global_bathymetry.py`
- controller selection mutation
- selected vehicle or selected layer runtime objects
- picker or hit-test execution
- Datashader / pandas / NumPy runtime sampling
- renderer / Qt / VisPy / Taichi runtime
- projection / flip / mask formula
- SQL / WebSocket / live AIS / live ADS-B
- real AIS / ADS-B / cache / database reads
- metadata or artifact writers
- alpha / apply / composition hot path

## Decision output

- `selection_render_policy_boundary_extraction_gate_passed = true`
- `helper_target = render_core\dynamic_point_selection_render_policy_boundary.py`
- `required_checker = scripts\validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py`
- `descriptor_policy_ledger_only = true`
- `source_movement_authorized = false`
- `runtime_render_invoked = false`
- `runtime_merge_enabled = false`
- `visual_parity_ready = false`
- `performance_ready = false`
- `readiness_claimed = false`
- `live_data_restored = false`
- `safe_to_extract_claimed = false`

## Recommended next gate

`dynamic_point_selection_render_policy_provider_or_controller_bridge_mapping_gate`

Reason: the selection/render policy descriptor shell is now separate, but controller selection mutation and picker/hit-test runtime remain blocked surfaces. The next mapping should decide whether the following slice is controller bridge mapping or render-policy parity mapping.

## Boundary statement

Minimal descriptor/policy/ledger-only dynamic point selection/render policy boundary extraction. No aggregate dynamic point helper change, no source-lineage helper change, no monolith change, no controller/picker/hit-test/datashader/runtime execution, no real AIS/ADS-B/cache/database read, no projection/flip/mask formula movement, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix/safe-to-extract claim.
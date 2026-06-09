# Displaytools Dynamic Point Selection / Render Policy Minimal Extraction Planning Gate

## Scope

本文件定義 dynamic point selection / render policy 的 docs/test-only minimal extraction planning gate。此 slice 不建立 `render_core\dynamic_point_selection_render_policy_boundary.py`，不修改 `render_core\dynamic_point_boundary.py`，不修改 `render_core\dynamic_point_source_lineage_boundary.py`，不修改 checker，不修改或 import `taichi_global_bathymetry.py`。

目的只是在專屬 import-boundary checker 已存在後，把下一刀可建立的 descriptor-only helper 範圍、fixture parity plan、checker expectation 與 stop lines 固定下來。

## Evidence read

- `scripts\validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py`
- `tests\test_displaytools_dynamic_point_selection_render_policy_import_boundary.py`
- `tests\test_displaytools_dynamic_point_selection_render_policy_craton_ablation_matrix.py`
- `render_core\dynamic_point_boundary.py`
- `render_core\dynamic_point_source_lineage_boundary.py`
- current `taichi_global_bathymetry.py` remains read-only and is not imported or executed

## Candidate target summary

Pinned candidate target:

- `future_helper_target = render_core\dynamic_point_selection_render_policy_boundary.py`
- `required_checker = scripts\validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py`
- `helper_module_creation_authorized = false`
- `source_movement_authorized = false`
- `selection_render_policy_planning_candidate = true`
- `selection_render_policy_extraction_candidate = false`

This gate is a construction plan only. It does not authorize creating the future helper module.

## Candidate helper list

The next slice may consider only these descriptor-only helper candidates:

| helper | candidate | runtime dependency allowed | expected output shape |
| --- | --- | --- | --- |
| `build_dynamic_point_selection_label_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_hit_state_label_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_picker_status_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_render_count_policy_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_render_cap_policy_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_adaptive_sampling_policy_descriptor` | yes | false | dict/list/scalar descriptor |
| `build_dynamic_point_selection_render_known_fault_ledger` | yes | false | dict/list/scalar ledger |
| `dynamic_point_selection_render_policy_boundary_descriptor` | yes | false | dict/list/scalar bundle descriptor |
| `dynamic_point_selection_render_policy_planning_bundle` | yes | false | dict/list/scalar planning packet |

Every candidate requires `scripts\validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py` and fixture parity before source movement.

## Fixture parity plan

Future extraction must have fixture parity for:

- helper import safety
- exact key-set parity for every descriptor builder
- deterministic repeat-call parity
- dict/list/scalar-only output
- selected vehicle label branch
- selected layer label branch
- hit state label branch
- picker status label branch
- visible count label branch
- rendered count label branch
- render cap label branch
- adaptive sampling label branch
- selection staleness fault branch
- hit-test dependency fault branch
- render policy guard flag branch
- known fault ledger branch
- planning bundle guard flags
- checker candidate PASS
- checker negative forbidden dependency FAIL

## Checker expectation

Pinned checker expectation:

| expectation | value |
| --- | --- |
| current checker missing target behavior | PASS |
| expected clean candidate behavior | PASS |
| expected runtime dependency behavior | FAIL |
| `string_labels_allowed_as_data` | true |
| forbidden executable references fail | true |
| forbidden declaration names fail | true |

The checker must continue to allow labels as data while blocking imports, executable names, attributes, calls, and declarations from forbidden families.

## Blocked surfaces

These surfaces remain blocked and are not extraction candidates:

- controller selection mutation
- selected vehicle runtime object
- selected layer runtime object
- selection state mutation
- picker / hit-test execution
- datashader / pandas / numpy runtime sampling
- renderer / Qt / VisPy / Taichi runtime
- projection / flip / mask formula
- SQL / WebSocket / live AIS / live ADS-B
- real AIS / ADS-B / cache / database read
- metadata / artifact writer
- alpha / apply / composition hot path
- readiness / performance / visual parity / bug-fix / live-data claims

## Decision output

Pinned decision output:

- `minimal_extraction_planning_gate_passed = true`
- `future_helper_target = render_core\dynamic_point_selection_render_policy_boundary.py`
- `required_checker = scripts\validate_displaytools_dynamic_point_selection_render_policy_import_boundary.py`
- `selection_render_policy_planning_candidate = true`
- `selection_render_policy_extraction_candidate = false`
- `helper_module_creation_authorized = false`
- `source_movement_authorized = false`
- `a1_macro_observer_required_before_source_movement = false`
- `recommended_next_gate = dynamic_point_selection_render_policy_minimal_extraction_gate`

The `a1_macro_observer_required_before_source_movement` cell is false for this narrow third-layer planning gate because the craton ablation matrix and dedicated checker have already constrained the target to descriptor-only selection/render-policy helpers. This is not a source movement authorization.

## Explicit exclusions

This gate excludes:

- creating `render_core\dynamic_point_selection_render_policy_boundary.py`
- modifying `render_core\dynamic_point_boundary.py`
- modifying `render_core\dynamic_point_source_lineage_boundary.py`
- modifying import-boundary checker scripts
- modifying `taichi_global_bathymetry.py`
- importing or executing monolith
- importing or executing controller, picker, hit-test, datashader, dataframe, renderer, Qt, VisPy, or Taichi runtime dependencies
- reading real AIS, ADS-B, cache, or database data
- changing selection, hit-test, render policy, projection, controller, or render behavior
- authorizing source movement
- declaring extraction candidate status
- live-data, readiness, bug-fix, visual parity, or performance claims

## Boundary statement

Docs/test-only dynamic point selection/render policy minimal extraction planning gate. No helper module creation, no source movement, no production source change, no checker change, no monolith import, no controller/picker/hit-test/datashader/runtime execution, no real AIS/ADS-B/cache/database read, no projection/flip/mask formula change, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no live-data/readiness/performance/visual parity/bug-fix claim.
# Dynamic Point LOD View-frame One-shot Runtime Probe Execution Authorization Gate

## Gate 性質

本 gate 是 Good Hope 之後的第一次 one-shot synthetic runtime probe execution 授權審查。它只判斷下一張 gate 是否可以在嚴格邊界內執行一次 synthetic runtime probe；本 gate 不建立 runtime adapter、不 import 21k monolith、不執行 runtime、不寫 artifact。

## Evidence read

- `scripts/dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_probe_adapter_static_wiring.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_PROBE_ADAPTER_STATIC_WIRING_GATE.zh-TW.md`
- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe_adapter_dry_contract.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_RUNTIME_PROBE_ADAPTER_DRY_CONTRACT_GATE.zh-TW.md`
- `scripts/dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_probe_dry_harness.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_PROBE_DRY_HARNESS_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_synthetic_probe_design.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_ONE_SHOT_SYNTHETIC_PROBE_DESIGN_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_runtime_probe_authorization_review.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_RUNTIME_PROBE_AUTHORIZATION_REVIEW_GATE.zh-TW.md`
- current `taichi_global_bathymetry.py` static scan only

## Static scan summary

Static scan confirms the first execution candidate seams exist in the current 21k surface: `project_ais_to_screen`, `project_aircraft_to_screen`, `mask_overlay_to_globe`, and `render_if_needed`.

It also confirms observation and risk surfaces exist: `current_projected`, `current_sampled_projected`, `visible_count`, `rendered_count`, `frame_rgba`, `output_path`, `write_preview_frame_png`, `Image.fromarray`, `save`, `horizon_eps`, `yaw`, `pitch`, `zoom`, and `alpha_compose`.

This scan is evidence only. It does not import or execute the monolith, renderer, Qt, VisPy, Taichi, Datashader, Matplotlib, SQL, WebSocket, cache, database, or live-source paths.

## Phase A: prerequisite review

| prerequisite | result |
| --- | --- |
| dry harness exists and self-test passes | pass |
| adapter dry contract exists and self-test passes | pass |
| static wiring exists and self-test passes | pass |
| a_1 Starlink observation completed | pass |
| schema is evidence-derived | pass |
| static wiring keeps runtime adapter call unauthorized | pass |
| `id()` remains future candidate only | pass |

The prerequisite packet supports continuing to authorization review. It does not authorize execution in this gate.

## Phase B: first runtime probe candidate scope

The first execution scope is constrained to:

- `synthetic_data_only = true`
- `one_shot = true`
- `stdout_only_result = true`
- `persistent_artifact = false`
- no GUI interaction
- no live source
- no SQL, WebSocket, cache, or database path
- no PNG, runtime JSON, or state write

Candidate entrypoint review:

| entrypoint | first execution candidate | renderer init | artifact write | real source | expected output |
| --- | --- | --- | --- | --- | --- |
| `project_ais_to_screen` | yes | no | no | no | projection or horizon responsibility packet |
| `project_aircraft_to_screen` | yes | no | no | no | projection or horizon responsibility packet |
| `mask_overlay_to_globe` | yes | no | no | no | globe mask responsibility packet |
| `render_if_needed` | no | yes | no | no | controller one-shot reference packet |

`render_if_needed` remains reference-only for the first execution because it is more likely to cross renderer initialization boundaries. The narrow execution candidates are projection and mask seams only.

## Phase C: authorization decision matrix

| item | status | blocking |
| --- | --- | --- |
| synthetic payload readiness | pass | yes |
| token packet readiness | pass | yes |
| oracle readiness | pass | yes |
| side-effect risk containment | pass | yes |
| artifact containment | pass | yes |
| source-lineage guard | pass | yes |
| transparent globe leak remains candidate | pass | yes |
| correctness claim blocked | pass | yes |
| rollback anchor available | pass | yes |

If any row fails in the next gate, execution must stop rather than widen scope.

## Phase D: allowed authorization ceiling

This gate allows only:

- `one_shot_runtime_probe_execution_authorized = true`
- `runtime_probe_execution_authorized_only_for_next_gate = true`

It keeps the following blocked:

- `production_source_change_authorized = false`
- `formula_mutation_authorized = false`
- `renderer_behavior_mutation_authorized = false`
- `artifact_write_authorized = false`
- `live_source_authorized = false`
- `correctness_claim_authorized = false`
- `readiness_claim_authorized = false`

This means the next gate may attempt one bounded execution, but it may not mutate source, formulas, renderer behavior, data lineage, artifacts, or claims.

## Phase E: execution stop lines

The next execution gate must stop if:

- import 21k fails
- runtime init exceeds one-shot scope
- any artifact would be written
- any live source, database, cache, or WebSocket path activates
- any formula or renderer mutation is needed
- token packet cannot be produced
- oracle cannot classify
- result tries to claim correctness, readiness, or fix

## Decision output

```text
runtime_execution_authorization_gate_passed = true
prerequisites_satisfied = true
first_probe_scope_defined = true
authorization_matrix_defined = true
execution_stop_lines_defined = true
one_shot_runtime_probe_execution_authorized = true
runtime_probe_execution_authorized_only_for_next_gate = true
production_source_change_authorized = false
formula_mutation_authorized = false
renderer_behavior_mutation_authorized = false
artifact_write_authorized = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
transparent_globe_leak_fix_claimed = false
readiness_claimed = false
recommended_next_gate = dynamic_point_lod_view_frame_one_shot_runtime_probe_execution_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame one-shot runtime probe execution authorization gate. Authorization review only; no production source change, no runtime adapter creation, no monolith import in this gate, no render_core import in this gate, no runtime execution in this gate, no runtime probe execution in this gate, no renderer execution in this gate, no 21k function execution in this gate, no real AIS/ADS-B/cache/database read, no SQL/WebSocket/live-source execution, no artifact read/write, no PNG/runtime JSON/state generation, no monkey patch implementation, no `__getattribute__` implementation, no runtime id trace, no `sys.settrace`, no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/safe-to-extract claim.

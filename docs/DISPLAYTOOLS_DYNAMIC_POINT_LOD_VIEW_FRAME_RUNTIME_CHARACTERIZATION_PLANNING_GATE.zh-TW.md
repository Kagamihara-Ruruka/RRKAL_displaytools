# Dynamic Point LOD View-frame Runtime Characterization Planning Gate

本 gate 是 Good Hope 之後第一張 runtime characterization planning gate。它只設計未來觀測矩陣，不執行 runtime probe，不插 instrumentation，不實作 monkey patch，不實作 `__getattribute__` trace，不使用 `sys.settrace`，不產生 PNG、runtime JSON 或 state artifact。

核心設計是：

```text
entrypoint × monkey_condition × contrast_token → oracle_rule
```

這張 gate 的目的不是證明 visual correctness，也不是修 transparent globe leak。它只定義未來若要觀測 dynamic point LOD、view-frame、occlusion、presentation seam，應從哪些入口進去、用哪些猴子條件敲、放哪些顯影 token、用哪些裁判尺判讀。

## Evidence read

靜態 evidence 來源：

- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_OCCLUSION_RESPONSIBILITY_BOUNDARY_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_grafting_path_minimal_evidence.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_GRAFTING_PATH_MINIMAL_EVIDENCE_GATE.zh-TW.md`
- `tests/test_displaytools_early_runtime_pipeline_characterization.py`
- `docs/DISPLAYTOOLS_EARLY_RUNTIME_PIPELINE_CHARACTERIZATION_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_structure_settlement.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_VIEW_FRAME_OCCLUSION_STRUCTURE_SETTLEMENT_GATE.zh-TW.md`
- current repo static scan

Static scan covered `render_if_needed`、`project_ais_to_screen`、`mask_overlay_to_globe`、`render_globe`、`apply_zoom`、`yaw`、`pitch`、`zoom`、`LOD`、`lod`、`horizon`、`mask`、`alpha_compose`、`visible_count`、`rendered_count`、`frame_rgba`、`source_lineage`、`current_projected` 與 `current_sampled_projected`。

## Phase A: representative slice strategy

| slice | role | dynamic point | planning use |
| --- | --- | --- | --- |
| `5_12_core_baseline` | early view-frame and globe runtime core reference | false | core reference |
| `current_21k_target` | dynamic point graft, LOD, occlusion, presentation target | true | primary runtime characterization target |
| `5_29_grafting_reference` | dynamic point grafting reference | true | compare graft prototype to current metamorphosis |
| `5_10_geometry_lighting_seed` | geometry and lighting seed without dynamic point graft path | false | excluded for dynamic point runtime characterization |

5/10 is excluded because it lacks the dynamic point graft path. 5/12 is useful as a core view-frame baseline. 5/29 is useful as a grafting reference. Current 21k is the target for future planning, not for execution in this gate.

## Phase B: entrypoint matrix

| entrypoint | slice owner | runtime probe candidate | runtime probe authorized |
| --- | --- | --- | --- |
| `render_if_needed` | `current_21k_target` | true | false |
| `project_ais_to_screen` | `current_21k_target` | true | false |
| `mask_overlay_to_globe` | `current_21k_target` | true | false |
| `controller_fixed_one_shot_render_path` | `current_21k_target` | true | false |
| `early_5_12_render_globe_baseline` | `5_12_core_baseline` | true | false |
| `early_5_29_dynamic_point_grafting_reference` | `5_29_grafting_reference` | true | false |

Every entrypoint keeps:

- `source_lineage_mutation_allowed = false`
- `formula_mutation_allowed = false`
- `renderer_behavior_mutation_allowed = false`

## Phase C: monkey condition matrix

Monkey conditions are planning labels only:

- `zoom_state`
- `rotation_state`
- `lod_policy`
- `horizon_eps`
- `sampling_policy`
- `mask_gate`
- `compose_presentation_gate`

No monkey patch is implemented in this gate.

## Phase D: contrast token matrix

Contrast tokens:

- `source_present_token`
- `projected_visible_token`
- `sampled_visible_token`
- `overlay_rendered_token`
- `mask_visible_token`
- `frame_visible_token`
- `source_lineage_integrity_token`

Future upgrade path:

| level | status |
| --- | --- |
| `L0_explicit_token` | mainline allowed now |
| `L1_repr_string_token` | future candidate only |
| `L2_identity_guard_token` | future candidate only |
| `L3_context_scope_token` | future candidate only |
| `L4_getattribute_read_trace_token` | future candidate only, not implemented |
| `L5_numeric_pipeline_token` | future candidate only |

This planning gate only uses `L0_explicit_token` as the mainline. `__getattribute__` is recorded only as a future candidate and is not implemented.

## Phase E: selected Katyusha matrix plan

| entrypoint | monkey condition | contrast token | oracle |
| --- | --- | --- | --- |
| `project_ais_to_screen` | `horizon_eps` | `projected_visible_token` | projected dropped while source present maps to projection or horizon responsibility |
| `project_ais_to_screen` | `zoom_state` | `source_lineage_integrity_token` | source token change is source lineage pollution fail |
| `render_if_needed` | `sampling_policy` | `sampled_visible_token` | sampled dropped while projected present maps to sampling responsibility |
| `mask_overlay_to_globe` | `mask_gate` | `mask_visible_token` | mask hidden while overlay present maps to globe mask responsibility |
| `controller_fixed_one_shot_render_path` | `compose_presentation_gate` | `frame_visible_token` | frame visible while mask invisible maps to transparent globe leak candidate |
| `early_5_12_render_globe_baseline` | `rotation_state` | `mask_visible_token` | source absent is invalid probe for dynamic point |
| `early_5_29_dynamic_point_grafting_reference` | `lod_policy` | `overlay_rendered_token` | overlay absent while sampled present maps to overlay or presentation responsibility |
| `render_if_needed` | `compose_presentation_gate` | `source_present_token` | source present while frame hidden supports computed-but-hidden |

This is a selected matrix, not full Cartesian enumeration.

## Phase F: allowed probe mode

Allowed probe rule for future review:

| rule | value |
| --- | --- |
| `synthetic_data_only` | true |
| `one_shot` | true |
| `persistent_artifact` | false |

Derived exclusions:

- no live source
- no real AIS or ADS-B
- no SQL, DB, or cache read
- no WebSocket
- no long-running GUI
- no human GUI interaction
- no persistent runtime state

## Phase G: forbidden mutation and claim rules

| rule | value |
| --- | --- |
| `formula_mutation_forbidden` | true |
| `renderer_behavior_mutation_forbidden` | true |
| `compose_order_mutation_forbidden` | true |
| `frame_semantics_mutation_forbidden` | true |
| `correctness_claim_forbidden` | true |
| `transparent_globe_leak_fix_claim_forbidden` | true |
| `readiness_claim_forbidden` | true |

## Phase H: oracle rules

| observation | verdict |
| --- | --- |
| source token changed | `source_lineage_pollution_fail` |
| source absent | `invalid_probe` |
| projected dropped while source present | `projection_or_horizon_responsibility` |
| sampled dropped while projected present | `sampling_responsibility` |
| overlay absent while sampled present | `overlay_or_presentation_responsibility` |
| mask hidden while overlay present | `globe_mask_responsibility` |
| frame visible while mask invisible | `transparent_globe_leak_candidate` |
| source present while frame hidden | `computed_but_hidden_supported` |

## Decision output

| decision | value |
| --- | --- |
| `planning_gate_passed` | true |
| `representative_slice_strategy_defined` | true |
| `entrypoint_matrix_defined` | true |
| `monkey_condition_matrix_defined` | true |
| `contrast_token_matrix_defined` | true |
| `katyusha_matrix_plan_defined` | true |
| `oracle_rules_defined` | true |
| `runtime_characterization_candidate` | true |
| `runtime_characterization_authorized` | false |
| `runtime_execution_authorized` | false |
| `formula_mutation_authorized` | false |
| `renderer_behavior_mutation_authorized` | false |
| `source_lineage_mutation_authorized` | false |
| `persistent_artifact_authorized` | false |
| `visual_correctness_claimed` | false |
| `coordinate_correctness_claimed` | false |
| `transparent_globe_leak_fix_claimed` | false |

## Recommended next gate

Recommended next gate is `dynamic_point_lod_view_frame_runtime_probe_authorization_review_gate`.

This next gate should review whether the planning matrix is narrow enough to authorize a future one-shot, synthetic-data-only runtime characterization probe. This gate itself does not authorize that probe.

## Boundary statement

Docs/test-only dynamic point LOD view-frame runtime characterization planning gate. No helper module creation, no source movement, no production source change, no checker script change, no monolith import, no runtime execution, no instrumentation, no monkey patch implementation, no `__getattribute__` implementation, no `sys.settrace`, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no runtime characterization authorization, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.

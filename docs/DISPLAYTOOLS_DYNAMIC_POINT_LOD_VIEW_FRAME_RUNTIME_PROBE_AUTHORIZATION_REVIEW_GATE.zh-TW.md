# Dynamic Point LOD View-frame Runtime Probe Authorization Review Gate

本 gate 是 Good Hope 之後第一輪 one-shot synthetic runtime probe 的 authorization review。它不是 runtime probe，不建立 probe harness，不執行 Taichi、Qt、VisPy、Datashader 或 Matplotlib runtime，也不讀真 AIS、ADS-B、cache、database 或 live source。

本 gate 最多只授權下一張 probe harness design gate。它不授權 runtime probe execution，不授權 runtime execution，不授權 production source change，不授權 formula mutation，不授權 renderer behavior mutation，也不宣稱 visual correctness、coordinate correctness、transparent globe leak fix、readiness、performance、visual parity 或 safe-to-extract。

## Evidence read

靜態 evidence 來源：

- `tests/test_displaytools_dynamic_point_lod_view_frame_runtime_characterization_planning.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_RUNTIME_CHARACTERIZATION_PLANNING_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_OCCLUSION_RESPONSIBILITY_BOUNDARY_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_grafting_path_minimal_evidence.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_GRAFTING_PATH_MINIMAL_EVIDENCE_GATE.zh-TW.md`
- `tests/test_displaytools_early_runtime_pipeline_characterization.py`
- `docs/DISPLAYTOOLS_EARLY_RUNTIME_PIPELINE_CHARACTERIZATION_GATE.zh-TW.md`
- current repo static scan

Static scan covered `render_if_needed`、`project_ais_to_screen`、`mask_overlay_to_globe`、`render_globe`、`apply_zoom`、`yaw`、`pitch`、`zoom`、`LOD`、`lod`、`horizon`、`mask`、`alpha_compose`、`visible_count`、`rendered_count`、`frame_rgba`、`source_lineage`、`current_projected`、`current_sampled_projected`、`synthetic`、`one-shot`、`oneshot`、`probe` 與 `runtime`。

## Phase A: authorization prerequisite packet

| prerequisite | value |
| --- | --- |
| `planning_gate_available` | true |
| `representative_slice_strategy_available` | true |
| `entrypoint_matrix_available` | true |
| `monkey_condition_matrix_available` | true |
| `contrast_token_matrix_available` | true |
| `oracle_rules_available` | true |
| `occlusion_responsibility_boundary_available` | true |
| `grafting_path_minimal_evidence_available` | true |
| `early_runtime_pipeline_characterization_available` | true |
| `authorization_review_passed` | true |

All prerequisites are present. If any prerequisite had been missing, this gate would stop at docs/test and keep `authorization_review_passed = false`.

## Phase B: entrypoint authorization matrix

| entrypoint | recommendation | scope |
| --- | --- | --- |
| `render_if_needed` | `candidate_for_future_probe_design` | current 21k one-shot synthetic render path design |
| `project_ais_to_screen` | `candidate_for_future_probe_design` | projection horizon and screen bounds design |
| `mask_overlay_to_globe` | `candidate_for_future_probe_design` | mask alpha gate design |
| `controller_fixed_one_shot_render_path` | `candidate_for_future_probe_design` | fixed one-shot controller path design only |
| `early_5_12_render_globe_baseline` | `reference_only` | core globe view-frame reference only |
| `early_5_29_dynamic_point_grafting_reference` | `reference_only` | dynamic point grafting reference static design only |

Every entrypoint keeps:

- `formula_mutation_required = false`
- `renderer_behavior_mutation_required = false`
- `source_lineage_mutation_required = false`
- `persistent_artifact_required = false`

No row grants `runtime_probe_authorized = true`.

## Phase C: synthetic adapter contract review

Synthetic adapter review:

| question | decision |
| --- | --- |
| synthetic payload can cover AIS and ADS-B minimal fields | true |
| synthetic adapter can replace SQL, WebSocket, cache, live AIS, and live ADS-B source | true |
| source lineage token can be fixed | true |
| deterministic fixture can represent point id, coordinate payload, timestamp, and source label | true |
| real data read needed | false |

Required outputs:

| output | value |
| --- | --- |
| `synthetic_data_only_sufficient` | true |
| `real_source_required` | false |
| `sql_required` | false |
| `websocket_required` | false |
| `cache_database_required` | false |

Synthetic data is sufficient for the next design gate. This does not authorize execution.

## Phase D: one-shot execution review

One-shot review:

| item | decision |
| --- | --- |
| fixed zoom, rotation, LOD, horizon, mask, compose labels possible | true |
| single projection, masking, composition characterization possible | true |
| `one_shot_sufficient` | true |
| `long_running_gui_required` | false |
| `human_gui_interaction_required` | false |
| `persistent_runtime_state_required` | false |
| `persistent_artifact_required` | false |

The next design can remain one-shot. This gate still does not authorize interactive runtime or long-running GUI.

## Phase E: mutation and claim stop-line review

| stop line | value |
| --- | --- |
| `formula_mutation_required` | false |
| `renderer_behavior_mutation_required` | false |
| `compose_order_mutation_required` | false |
| `frame_semantics_mutation_required` | false |
| `coordinate_correctness_claim_allowed` | false |
| `visual_correctness_claim_allowed` | false |
| `transparent_globe_leak_fix_claim_allowed` | false |
| `readiness_claim_allowed` | false |
| `performance_claim_allowed` | false |

If any of these became true, this gate would fail.

## Phase F: oracle sufficiency review

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

Sufficiency outputs:

| output | value |
| --- | --- |
| `oracle_rules_sufficient_for_probe_design` | true |
| `transparent_globe_leak_kept_as_candidate` | true |
| `computed_but_hidden_rule_preserved` | true |
| `source_lineage_pollution_guard_preserved` | true |

The oracle is sufficient for the next probe design gate. It does not prove correctness and does not fix a fault.

## Phase G: authorization review decision

| decision | value |
| --- | --- |
| `authorization_review_passed` | true |
| `runtime_probe_design_authorized` | true |
| `runtime_probe_execution_authorized` | false |
| `runtime_execution_authorized` | false |
| `probe_harness_creation_authorized` | false |
| `production_source_change_authorized` | false |
| `formula_mutation_authorized` | false |
| `renderer_behavior_mutation_authorized` | false |
| `persistent_artifact_authorized` | false |
| `coordinate_correctness_claimed` | false |
| `visual_correctness_claimed` | false |
| `transparent_globe_leak_fix_claimed` | false |
| `readiness_claimed` | false |
| `global_methodology_promotion_authorized` | false |

The authorization is limited to the next design gate. This gate does not create a probe harness and does not execute runtime.

## Recommended next gate

Recommended next gate is `dynamic_point_lod_view_frame_one_shot_synthetic_probe_design_gate`.

The next gate may design a one-shot synthetic probe harness, but still requires separate review before any runtime execution.

## Boundary statement

Docs/test-only dynamic point LOD view-frame runtime probe authorization review gate. No helper module creation, no source movement, no production source change, no checker script change, no probe harness creation, no monolith import, no runtime execution, no runtime probe execution, no instrumentation, no monkey patch implementation, no `__getattribute__` implementation, no `sys.settrace`, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, no renderer behavior change, no compose order change, no metadata/output schema change, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no runtime characterization execution authorization, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.

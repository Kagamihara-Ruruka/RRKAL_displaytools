# Dynamic Point LOD View-frame One-shot Synthetic Probe Design Gate

本 gate 是 docs/test-only 的 one-shot synthetic probe contract design。它不執行 21k runtime，不建立 probe harness，不改 production source，不寫入 `L:\RRKAL_lab`，也不產生 PNG、runtime JSON 或 state artifact。

核心目標是從 current 21k static evidence 萃取未來 one-shot synthetic probe 需要的欄位，並把欄位分成 payload、lineage guard、view-frame condition、visibility observation、presentation observation 與 excluded fields。Schema 不能憑空手寫，必須綁回 21k static evidence。

## Evidence read

靜態 evidence 來源：

- `tests/test_displaytools_dynamic_point_lod_view_frame_runtime_probe_authorization_review.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_RUNTIME_PROBE_AUTHORIZATION_REVIEW_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_lod_view_frame_runtime_characterization_planning.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_RUNTIME_CHARACTERIZATION_PLANNING_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_OCCLUSION_RESPONSIBILITY_BOUNDARY_GATE.zh-TW.md`
- `tests/test_displaytools_dynamic_point_grafting_path_minimal_evidence.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_GRAFTING_PATH_MINIMAL_EVIDENCE_GATE.zh-TW.md`
- current `taichi_global_bathymetry.py` static scan only

Static scan covered `normalize_ais_frame`、`normalize_aircraft_frame`、`project_ais_to_screen`、`project_aircraft_to_screen`、`render_if_needed`、`mask_overlay_to_globe`、`current_projected`、`current_sampled_projected`、`visible_count`、`rendered_count`、`frame_rgba`、`source`、`source_id`、`lat`、`lon`、`timestamp`、`heading`、`speed`、`horizon`、`mask`、`alpha_compose`、`LOD`、`lod`、`zoom` 與 `rotation`。

## Phase A: 21k schema source audit

Candidate fields are accepted only when they carry source evidence, observed surface, pipeline owner, and probe reason.

| field | evidence surface | role |
| --- | --- | --- |
| `point_id` | source lineage identity and current hit or pin identity surfaces | `lineage_guard_candidate` |
| `source_label` | `AISSource`, `AircraftSource`, source labels | `lineage_guard_candidate` |
| `timestamp` | timestamp filtering and authorization minimal fields | `payload_input_candidate` |
| `lat` | normalize and projection source flow | `payload_input_candidate` |
| `lon` | normalize and projection source flow | `payload_input_candidate` |
| `speed_or_altitude_label` | `sog`, `speed_kt`, `altitude_m`, overlay color roles | `adapter_only_candidate` |
| `yaw` | projection and view-frame scan | `view_frame_condition_candidate` |
| `pitch` | projection and view-frame scan | `view_frame_condition_candidate` |
| `zoom` | projection and render globe scan | `view_frame_condition_candidate` |
| `horizon_eps` | AIS and aircraft projection horizon filter | `view_frame_condition_candidate` |
| `lod_label` | LOD static scan and prior planning monkey condition | `view_frame_condition_candidate` |
| `projected_visible_token` | `current_projected`, `visible_count` | `visibility_observation_candidate` |
| `sampled_visible_token` | `current_sampled_projected`, `rendered_count` | `visibility_observation_candidate` |
| `overlay_rendered_token` | `AISDatashaderOverlay`, `AircraftDatashaderOverlay` | `visibility_observation_candidate` |
| `mask_visible_token` | `mask_overlay_to_globe`, `globe_mask` | `visibility_observation_candidate` |
| `frame_visible_token` | `frame_rgba`, `alpha_compose` | `presentation_observation_candidate` |
| `visible_count_observation` | `visible_count` | `presentation_observation_candidate` |
| `rendered_count_observation` | `rendered_count` | `presentation_observation_candidate` |
| `frame_rgba_buffer` | `frame_rgba` runtime buffer | `excluded_candidate` |

`frame_rgba_buffer` is excluded because buffer access would imply renderer output dependency. The probe can observe token labels and counts, but this design gate does not permit renderer buffer references.

## Phase B: schema candidate matrix

Every candidate is checked against hard exclusions:

- `requires_real_source = false`
- `requires_sql_or_cache = false`
- `requires_websocket = false`
- `requires_formula_access = false`
- `requires_renderer_buffer = false`, otherwise excluded

The cooled schema excludes `frame_rgba_buffer` because it requires renderer buffer access. All included fields remain synthetic, label, token, count, or condition fields.

## Phase C: cooled probe schema

The cooled schema is derived from 21k evidence:

| group | fields |
| --- | --- |
| `synthetic_payload_fields` | `point_id`, `source_label`, `timestamp`, `lat`, `lon`, `speed_or_altitude_label` |
| `lineage_guard_fields` | `point_id`, `source_label` |
| `view_frame_condition_fields` | `yaw`, `pitch`, `zoom`, `horizon_eps`, `lod_label` |
| `visibility_observation_fields` | `projected_visible_token`, `sampled_visible_token`, `overlay_rendered_token`, `mask_visible_token` |
| `presentation_observation_fields` | `frame_visible_token`, `visible_count_observation`, `rendered_count_observation` |
| `excluded_fields` | `frame_rgba_buffer` |

Required decisions:

- `cooled_probe_schema_derived_from_21k_evidence = true`
- `hardcoded_schema_forbidden = true`

No true runtime values are filled in this schema. It is a contract shape only.

## Phase D: one-shot synthetic probe contract

Contract:

| item | value |
| --- | --- |
| `target` | `current_21k_only` |
| `synthetic_data_only` | true |
| `one_shot` | true |
| `persistent_artifact` | false |
| `runtime_execution_authorized` | false |
| `probe_harness_creation_authorized` | false |
| `formula_mutation_authorized` | false |
| `renderer_behavior_mutation_authorized` | false |
| `source_lineage_mutation_authorized` | false |

Conceptual flow:

```text
synthetic payload
-> selected entrypoint
-> token observation packet
-> oracle judgment
```

This flow is not implemented in this gate.

## Phase E: entrypoint-to-schema mapping

Active design targets:

| entrypoint | required groups | design status |
| --- | --- | --- |
| `render_if_needed` | lineage, view-frame, visibility, presentation | `design_candidate_only` |
| `project_ais_to_screen` | AIS payload, view-frame, horizon, projected token | `design_candidate_only` |
| `project_aircraft_to_screen` | ADS-B payload, view-frame, horizon, projected token | `design_candidate_only` |
| `mask_overlay_to_globe` | overlay token, mask token, frame token | `design_candidate_only` |
| `controller_fixed_one_shot_render_path` | lineage, view-frame, LOD, horizon, visibility tokens | `design_candidate_only` |

Historical references:

```text
historical references already absorbed by previous gates
```

5/12 and 5/29 are no longer active design targets in this gate.

## Phase F: contrast-agent upgrade path

Upgrade path:

- `L0_explicit_token`
- `L1_repr_string_token`
- `L2_identity_guard_token`
- `L3_context_scope_token`
- `L4_getattribute_read_trace_token`
- `L5_numeric_pipeline_token`

Active level:

```text
active_contrast_agent_level = L0_explicit_token
```

Forbidden in this gate:

- `__getattribute__` implementation
- `__array__` or NumPy protocol implementation
- `sys.settrace`
- debugger or IDE automation

## Phase G: a_1 Starlink observation slot

| item | value |
| --- | --- |
| `a1_external_observation_candidate` | true |
| `a1_required_before_probe_execution` | true |
| `a1_required_before_this_design_gate` | false |
| `a1_product_repo_edit_allowed` | false |
| `a1_runtime_authorization_allowed` | false |
| `a1_replaces_o1_review` | false |

Observation scope:

- methodology consistency
- schema derivation
- claim boundary
- probe design observability

This gate does not modify `L:\RRKAL_lab` and does not let a_1 replace o_1 review.

## Phase H: decision output

| decision | value |
| --- | --- |
| `probe_design_gate_passed` | true |
| `schema_source_audit_completed` | true |
| `schema_candidate_matrix_defined` | true |
| `cooled_probe_schema_defined` | true |
| `cooled_probe_schema_derived_from_21k_evidence` | true |
| `hardcoded_schema_forbidden` | true |
| `one_shot_synthetic_probe_contract_defined` | true |
| `entrypoint_schema_mapping_defined` | true |
| `active_contrast_agent_level` | `L0_explicit_token` |
| `a1_starlink_observation_slot_defined` | true |
| `runtime_probe_execution_authorized` | false |
| `runtime_execution_authorized` | false |
| `probe_harness_creation_authorized` | false |
| `production_source_change_authorized` | false |
| `persistent_artifact_authorized` | false |
| `coordinate_correctness_claimed` | false |
| `visual_correctness_claimed` | false |
| `transparent_globe_leak_fix_claimed` | false |
| `readiness_claimed` | false |

## Recommended next gate

Recommended next gate is `a1_dynamic_point_one_shot_synthetic_probe_design_starlink_observation_note`.

## Boundary statement

Docs/test-only dynamic point LOD view-frame one-shot synthetic probe design gate. No helper module creation, no source movement, no production source change, no checker script change, no probe harness creation, no monolith import, no runtime execution, no runtime probe execution, no instrumentation, no monkey patch implementation, no `__getattribute__` implementation, no NumPy protocol trace implementation, no `sys.settrace`, no debugger/IDE automation, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no Taichi/Qt/VisPy/Datashader/Matplotlib runtime execution, no projection/flip/mask/LOD/occlusion/alpha-compose formula movement or change, no renderer behavior change, no compose order change, no metadata/output schema change, no product repo to lab repo write, no coordinate/visual correctness claim, no transparent-globe leak fix claim, no runtime probe execution authorization, no probe harness creation authorization, no global methodology promotion, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.

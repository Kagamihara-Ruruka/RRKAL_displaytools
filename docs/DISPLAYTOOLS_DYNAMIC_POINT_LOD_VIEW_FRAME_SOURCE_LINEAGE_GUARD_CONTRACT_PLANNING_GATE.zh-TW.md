# Dynamic Point LOD View-Frame Source-Lineage Guard Contract Planning Gate

## Gate 結論

本 gate 只規劃 `source_lineage_guard_contract`，不建立 helper、不建立 checker、不修改 `render_core`。目標是固定 source identity 與 lineage guard，使 sampling、presentation count、computed-but-hidden、mask、occlusion 的 visibility state 不會被解讀成 source loss。

## Future targets

- Future helper target: `render_core/dynamic_point_source_lineage_guard_boundary.py`
- Future checker target: `scripts/validate_displaytools_dynamic_point_source_lineage_guard_import_boundary.py`

## Guard surface matrix

| surface | contract role | protected surface | forbidden interpretation |
| --- | --- | --- | --- |
| `source_present_token` | source presence contract label | `computed_but_hidden_boundary` | source token is not frame visibility truth |
| `source_label` | source identity label | sampling / computed-hidden surfaces | source label must not trigger real source read |
| `point_id` | stable payload identity label | sampling / computed-hidden surfaces | point id is not coordinate correctness |
| `source_lineage_integrity_token` | lineage integrity guard token | sampling / presentation / computed-hidden surfaces | visibility state cannot rewrite source lineage |
| `payload_identity_guard` | payload identity guard contract | source-lineage guard contract | payload guard is not runtime readiness |
| `sampling_does_not_mutate_source` | sampling source guard | sampling visibility boundary | sampled false is not missing source |
| `presentation_count_does_not_mutate_source` | presentation count source guard | presentation count boundary | rendered lower than visible is not source loss |
| `hidden_visibility_does_not_mutate_source` | hidden visibility source guard | computed-but-hidden boundary | hidden is not missing |
| `mask_visibility_does_not_mutate_source` | mask visibility source guard | sampling visibility and future mask contract | mask hidden is not source deletion |
| `occlusion_visibility_does_not_mutate_source` | occlusion source guard | computed-hidden and future occlusion contract | occluded is not source lineage loss |
| `reduced_count_is_not_source_loss` | reduction source-loss guard | presentation count boundary | reduced count as source loss |
| `hidden_is_not_missing` | hidden / missing guard | computed-but-hidden boundary | hidden-as-missing interpretation |
| `occluded_is_not_source_lineage_loss` | occluded lineage-loss guard | computed-hidden and occlusion surfaces | occluded-as-source-lineage-loss interpretation |

## Planned helper families

- `build_dynamic_point_source_identity_contract_descriptor`
- `build_dynamic_point_source_lineage_integrity_descriptor`
- `build_dynamic_point_sampling_source_guard_descriptor`
- `build_dynamic_point_presentation_count_source_guard_descriptor`
- `build_dynamic_point_hidden_visibility_source_guard_descriptor`
- `build_dynamic_point_mask_occlusion_source_guard_descriptor`
- `build_dynamic_point_source_lineage_guard_stop_line_ledger`
- `dynamic_point_source_lineage_guard_boundary_descriptor`
- `dynamic_point_source_lineage_guard_planning_bundle`

## Dependency-cycle watch

`dependency_cycle_watch_enabled = true`。此 guard 先保護三個已抽離 surface:

- `sampling_visibility_boundary`
- `presentation_count_boundary`
- `computed_but_hidden_boundary`

這讓後續 `occlusion_responsibility_contract`、`mask_visibility_contract`、`presentation_reduction_contract` 不必各自重新證明 hidden、reduced、occluded 不是 source loss。

## Decision output

- `source_lineage_guard_contract_planning_passed = true`
- `source_lineage_guard_helper_candidate_supported = true`
- `descriptor_contract_ledger_candidate = true`
- `helper_creation_authorized = false`
- `checker_creation_authorized = false`
- `runtime_execution_authorized = false`
- `source_lineage_mutation_authorized = false`
- `hidden_as_missing_authorized = false`
- `reduced_count_as_source_loss_authorized = false`
- `occluded_as_source_loss_authorized = false`
- `transparent_globe_leak_inferred = false`
- `dependency_cycle_watch_enabled = true`
- `recommended_next_gate = dynamic_point_lod_view_frame_source_lineage_guard_import_boundary_checker_planning_gate`

## Boundary statement

Docs/test-only dynamic point LOD view-frame source-lineage guard contract planning gate. No helper creation, no checker creation, no `render_core` change, no runtime probe change, no `taichi_global_bathymetry.py` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no real AIS/ADS-B/SQL/WebSocket/cache/database read, no source-lineage mutation, no hidden-as-missing interpretation, no reduced-count-as-source-loss interpretation, no occluded-as-source-loss interpretation, no transparent-globe leak inference, no correctness or visual parity claim, no readiness claim, no leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_contract_planning_gate_committed_for_o1_review_no_push`

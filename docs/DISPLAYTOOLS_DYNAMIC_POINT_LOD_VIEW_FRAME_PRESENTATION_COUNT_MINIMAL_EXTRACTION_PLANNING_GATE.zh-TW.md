# Dynamic Point LOD View-Frame Presentation Count Minimal Extraction Planning Gate

## Gate scope

本 gate 只規劃未來 `render_core/dynamic_point_presentation_count_boundary.py` 的 minimal extraction surface。checker 已建立，但本 gate 不建立 helper，不修改 checker，不修改 runtime probe，也不碰 renderer、frame buffer、formula、source loss、leak inference 或 readiness claim。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_import_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_contract_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_next_andesite_bridge_selection.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_sampling_visibility_cartography_update.py`

## Future helper target

```text
render_core/dynamic_point_presentation_count_boundary.py
```

本 gate 只規劃，不建立 helper。

## Planned helper families

| Helper family | Intended output keys | Allowed labels | Forbidden fields | Source-lineage impact | Renderer/frame dependency | Formula dependency | Readiness level | Checker coverage | Helper creation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `build_dynamic_point_visible_count_contract_descriptor` | `visible_count`, `visible_count_observation`, `presentation_count_contract` | count contract labels | runtime, renderer, frame, formula, source-loss, leak, claim fields | read-only no mutation | none | none | minimal extraction candidate | presentation count checker required | false |
| `build_dynamic_point_rendered_count_contract_descriptor` | `rendered_count`, `rendered_count_observation`, `presentation_count_contract` | rendered count labels | runtime, renderer, frame, formula, source-loss, leak, claim fields | read-only no mutation | none | none | minimal extraction candidate | presentation count checker required | false |
| `build_dynamic_point_presentation_reduction_candidate_descriptor` | `rendered_lower_than_visible`, `sampling_or_presentation_reduction_candidate` | reduction candidate labels | source loss and all runtime surfaces | source loss not inferred | none | none | minimal extraction candidate | source-loss interpretation must fail | false |
| `build_dynamic_point_presentation_count_source_lineage_guard_descriptor` | `source_lineage_integrity_token`, `source_loss_not_inferred` | lineage guard labels | source-loss, runtime, renderer, frame, formula, claim fields | guard only | none | none | minimal extraction candidate | source-loss interpretation must fail | false |
| `build_dynamic_point_presentation_count_stop_line_ledger` | `frame_visible_not_observed`, `transparent_globe_leak_not_inferred`, `visual_correctness_not_claimed`, `readiness_not_claimed` | stop-line labels | frame truth, leak inference, leak fix, readiness, runtime surfaces | none | blocked stop-line only | none | stop-line ledger candidate | frame buffer and leak claim must fail | false |
| `dynamic_point_presentation_count_boundary_descriptor` | `allowed_outputs`, `owned_semantics`, `blocked_actions` | all allowed labels | all forbidden families | descriptor only | none | none | minimal extraction candidate | full forbidden family coverage required | false |
| `dynamic_point_presentation_count_planning_bundle` | `minimal_extraction_planning_passed`, `checker_protected`, `helper_creation_authorized` | all allowed labels | all forbidden families | bundle only | none | none | planning bundle candidate | checker must pass before helper creation | false |

## Checker protection decision

`presentation_count` 專用 checker 已存在：

```text
scripts/validate_displaytools_dynamic_point_presentation_count_import_boundary.py
```

它可以保護 future helper，因為它會阻擋 runtime probe、`render_if_needed`、controller、renderer、frame buffer、artifact writer、projection formula、mask formula、sampling formula movement、dataframe runtime、live source、cache/database IO、source-loss interpretation、transparent-globe leak inference、correctness claim、visual parity claim、readiness claim、transparent-globe leak fix claim，以及 label executable reference。

## Planning answers

1. 已有 checker 可保護 future helper。
2. future helper 只需要 dict/list/scalar output。
3. `visible_count` 與 `rendered_count` 可安全作為 contract field。
4. `rendered_count < visible_count` 只能保留為 reduction candidate。
5. source-loss interpretation 仍禁止。
6. frame truth 與 transparent globe leak inference 仍禁止。
7. helper creation 尚未授權。
8. 下一張 gate 應該是 minimal extraction gate，不需要再補 planning。

## Forbidden interpretation summary

- `rendered_count < visible_count` 不得解讀成 source loss。
- `visible_count` 或 `rendered_count` 不得解讀成 frame truth。
- `frame_visible_not_observed` 不得推導 transparent globe leak behavior。
- count contract 不得宣稱 coordinate correctness、visual parity、readiness、safe-to-extract 或 leak fix。

## Recommended next gate

`dynamic_point_lod_view_frame_presentation_count_minimal_extraction_gate`

## Boundary statement

Docs/test-only dynamic point LOD view-frame presentation count minimal extraction planning gate. No helper creation, no `render_core/dynamic_point_presentation_count_boundary.py` creation, no checker modification, no runtime probe change, no `taichi_global_bathymetry` change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no projection/mask/sampling formula movement, no source-loss interpretation, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_lod_view_frame_presentation_count_minimal_extraction_planning_gate_committed_for_o1_review_no_push`
# Dynamic Point LOD View-Frame Presentation Count Contract Planning Gate

## Gate scope

本 gate 只做 docs/test-only planning。目標是把已觀測到的 `visible_count`、`rendered_count`、`rendered_count < visible_count` 冷卻成 presentation count contract 候選，並固定它不需要 renderer、frame buffer、runtime probe expansion 或 formula movement。

## Evidence read

- `tests/test_displaytools_dynamic_point_lod_view_frame_next_andesite_bridge_selection.py`
- `tests/test_displaytools_dynamic_point_sampling_visibility_cartography_update.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_runtime_probe_result_interpretation.py`

## Presentation count planning matrix

| Row | Observed evidence | Semantic meaning | Allowed contract field | Forbidden interpretation | Runtime dependency | Renderer or frame dependency | Source-lineage impact | Readiness | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `visible_count_observation` | 第二刀判讀固定 `visible_count_observation = 2` | 可見計數可以作為 observation label | `visible_count` | source lineage completeness 或 coordinate correctness | prior observation only | none | 不可改 source lineage | ready for checker planning | 規劃 presentation count import boundary checker |
| `rendered_count_observation` | 第二刀判讀固定 `rendered_count_observation = 1` | rendered count 可以作為 presentation count observation label | `rendered_count` | visual correctness 或 final frame truth | prior observation only | none | 不可改 source lineage | ready for checker planning | 規劃 presentation count import boundary checker |
| `rendered_lower_than_visible` | `visible_count = 2` 且 `rendered_count = 1` | 只能表示 sampling 或 presentation reduction candidate | `rendered_lower_than_visible` | source loss 或 missing source | prior observation only | none | source lineage preserved | ready for checker planning | 保留 reduction candidate，不轉成 source loss |
| `sampling_or_presentation_reduction_candidate` | reduced sample case 保留 source identity 並降低 rendered count | count reduction 暫屬 sampling 或 presentation 語意 | `reduction_candidate_label` | provider filter 或 database loss | prior observation only | none | source lineage guard required | ready for checker planning | 只允許 descriptor / contract / ledger |
| `presentation_count_contract` | next andesite bridge selection 選出此候選 | visible 與 rendered count 可冷卻成本地 contract | `presentation_count_contract_descriptor` | renderer behavior 或 frame output semantics | none for planning | none | read-only guard | planning candidate | 先規劃 checker，再談 helper |
| `frame_visible_not_observed` | `frame_visible_token = not_observed` | frame visibility 仍是 stop-line 欄位，不是 runtime truth | `frame_visible_not_observed` | transparent globe leak inference | blocked | blocked | none | blocked stop-line | 排除在 count contract 之外 |
| `source_lineage_integrity_token` | 第二刀判讀固定 `source_lineage_integrity_token = true` | sampling 與 mask count observation 不可改 source identity | `source_lineage_integrity_token` | source lineage mutation allowed | prior observation only | none | must remain true | ready for checker planning | 作為 guard field |
| `transparent_globe_leak_not_inferred` | frame visibility 與 renderer path 未觀測 | leak 留在 stop-line，不在本 contract 推論 | `transparent_globe_leak_not_inferred` | leak fix 或 fault proof | blocked | blocked | none | contract-only stop-line | 保留 leak claim guard |

## Contract field decision

`visible_count` 與 `rendered_count` 可以作為 contract field。它們的語意是 presentation count observation，不是 renderer correctness、frame truth、source completeness 或 coordinate correctness。

`rendered_count < visible_count` 只能表示 sampling 或 presentation reduction candidate。它不可被解讀為 source loss、missing source、provider filter、cache loss 或 database loss。

`frame_visible_not_observed` 仍會阻擋 transparent globe leak inference。因為 frame buffer、renderer、`render_if_needed` 與 controller 都沒有被觀測，本 gate 不允許把 count observation 推到 leak behavior。

## Planning answers

1. `visible_count` 與 `rendered_count` 可以作為 contract field。
2. `rendered_count < visible_count` 只能表示 sampling 或 presentation reduction candidate，不能推成 source loss。
3. `frame_visible_not_observed` 仍禁止 transparent globe leak inference。
4. 本 gate 足以支持下一張 import-boundary checker planning。
5. helper creation 不授權。
6. runtime probe expansion 不授權。
7. correctness、readiness、leak-fix claim 不授權。
8. 這只是 c_3 local dynamic point pattern，不升級成 RRKAL-wide methodology。

## Runtime, renderer, and frame stop-line

- `render_if_needed_authorized = false`
- `controller_renderer_frame_buffer_authorized = false`
- `runtime_probe_expansion_authorized = false`
- `artifact_generation_authorized = false`
- `formula_movement_authorized = false`
- `transparent_globe_leak_inferred = false`
- `transparent_globe_leak_fix_claimed = false`

## Recommended next gate

`dynamic_point_lod_view_frame_presentation_count_import_boundary_checker_planning_gate`

## Boundary statement

Docs/test-only dynamic point LOD view-frame presentation count contract planning gate. No helper creation, no checker creation, no render_core change, no runtime probe change, no taichi_global_bathymetry change, no render_if_needed, no controller, no renderer, no frame buffer read, no artifact generation, no projection/mask/sampling formula movement, no source-loss interpretation from rendered lower than visible, no transparent-globe leak inference, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Final classification

`c3_displaytools_dynamic_point_lod_view_frame_presentation_count_contract_planning_gate_committed_for_o1_review_no_push`
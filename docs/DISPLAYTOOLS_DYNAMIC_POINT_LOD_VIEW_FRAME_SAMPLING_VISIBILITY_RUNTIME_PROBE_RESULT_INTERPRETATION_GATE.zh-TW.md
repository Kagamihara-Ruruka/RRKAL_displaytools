# Dynamic Point LOD View-frame Sampling Visibility Runtime Probe Result Interpretation Gate

## Gate 性質

本 gate 只解讀第二刀 sampling、visibility、count runtime probe 的 stdout JSON。它不修改 probe script，不新增 runtime execution，不呼叫 `render_if_needed`，不建立 controller，不執行 renderer，不讀 frame buffer，也不產生 artifact。

此 gate 的任務是把已觀測、未觀測、不能宣稱的邊界固定下來，作為下一張 planning gate 的輸入。

## Evidence read

- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_probe_script_update.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SAMPLING_VISIBILITY_PROBE_SCRIPT_UPDATE_GATE.zh-TW.md`
- `docs/DOCS_INDEX.zh-TW.md`

## Required runtime result fields

第二刀 `--run-probe` stdout JSON 固定下列觀測：

```text
runtime_probe_executed = true
project_ais_to_screen_called = true
project_aircraft_to_screen_called = true
mask_overlay_to_globe_called = true
render_if_needed_called = false
controller_instantiated = false
renderer_executed = false
frame_buffer_read = false
artifact_written = false
source_lineage_integrity_token = true
sampled_visible_token = true
visible_count_observation = 2
rendered_count_observation = 1
frame_visible_token = not_observed
```

## Case interpretation

| case | interpretation |
| --- | --- |
| `full_sample_case` | projected、sampled、rendered synthetic count 保持一致 |
| `reduced_sample_case` | rendered count 低於 visible count，支持 sampling 或 presentation reduction 模型 |
| `mask_visible_true` | mask-visible path 已可在 synthetic packet 中觀測 |
| `mask_visible_false_synthetic` | globe mask 可以隱藏 overlay，且不刪除 source lineage |
| `source_lineage_guard_case` | sampling 與 mask label 不污染 source identity |
| `frame_remains_not_observed` | frame visibility 未觀測，不能推論 transparent globe leak |

## Key conclusion

第二刀把安山岩的一段縮小了：

- sampling 與 count 已可 synthetic 觀測。
- mask can hide overlay without deleting source。
- reduced sample 支持 `rendered < visible` 的 presentation 或 sampling reduction 模型。
- source lineage guard 仍成立。
- frame、renderer、transparent-globe leak 仍然不能碰，也不能推論。

## Decision output

```text
sampling_visibility_interpretation_passed = true
sampling_observed = true
count_surface_observed = true
mask_false_path_observed = true
source_lineage_guard_supported = true
frame_visibility_observed = false
transparent_globe_leak_inferred = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
readiness_claimed = false
```

## Next gate recommendation

推薦下一張走保守路線：

`dynamic_point_lod_view_frame_frame_visibility_stop_line_planning_gate`

理由是 sampling、count、mask 的 observation 已縮小範圍，但 frame visibility 與 transparent-globe leak 仍然完全未觀測。先把 frame stop-line 規劃清楚，可以避免 adapter 或 contract extraction 在下一步誤碰 renderer、frame buffer 或 leak claim。

提速路線 `dynamic_point_lod_view_frame_sampling_visibility_adapter_extraction_planning_gate` 可以保留為後續候選，但本 gate 不建議直接跳過 frame stop-line。

## Forbidden interpretation

本 gate 不允許：

- 宣稱 coordinate correctness
- 宣稱 visual correctness
- 宣稱 transparent-globe leak fix
- 宣稱 readiness 或 safe-to-extract
- 把 frame 未觀測解讀成 leak evidence
- 把 synthetic count observation 解讀成 renderer correctness
- 授權 probe script 修改
- 授權新的 runtime execution

## Boundary statement

Docs/test-only dynamic point LOD view-frame sampling / visibility runtime probe result interpretation gate. No probe script change, no new runtime execution, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula or renderer behavior change, no correctness/readiness/leak-fix claim, and no push.

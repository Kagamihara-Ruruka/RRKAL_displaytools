# Dynamic Point LOD View-frame Sampling Visibility Probe Script Update Gate

## Gate 性質

本 gate 將既有 one-shot runtime probe 的輸出擴充為 sampling、visibility、count 的 synthetic observation。這不是新的 runtime probe，不擴張入口，不呼叫 `render_if_needed`，不建立 controller，不執行 renderer，也不讀 frame buffer。

本次只允許在既有 probe script 內加入 synthetic-only 判讀資料，讓 stdout JSON 能帶出下一輪 interpretation 所需的欄位。

## Files changed

- `scripts/dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_one_shot_runtime_probe.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_probe_script_update.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SAMPLING_VISIBILITY_PROBE_SCRIPT_UPDATE_GATE.zh-TW.md`
- `docs/DOCS_INDEX.zh-TW.md`

## Script update summary

既有 runtime probe 仍只允許呼叫三個 seam：

- `project_ais_to_screen`
- `project_aircraft_to_screen`
- `mask_overlay_to_globe`

新增內容只在三個 seam 完成後建立 synthetic sampling 與 count observation，不加入新的 monolith 呼叫，不呼叫 renderer，不接觸 frame buffer。

## Synthetic case coverage

| case | purpose |
| --- | --- |
| `full_sample_case` | 確認 projected、sampled、rendered synthetic count 可以保持一致 |
| `reduced_sample_case` | 確認 rendered count 可以低於 visible count，形成 sampling 或 presentation reduction 候選 |
| `mask_visible_true` | 確認 overlay 與 mask-visible path 可被記錄 |
| `mask_visible_false_synthetic` | 用 synthetic mask false 表示 globe mask suppression 候選 |
| `source_lineage_guard_case` | 確認 sampling 與 mask label 不會改 source identity |
| `frame_remains_not_observed` | 明確保持 frame visibility 與 transparent globe leak 未觀測 |

## JSON stdout packet additions

stdout JSON 新增或補足：

- `sampled_visible_token`
- `visible_count_observation`
- `rendered_count_observation`
- `sampling_visibility_case_results`
- `sampling_visibility_oracle_results`

`frame_visible_token` 仍保持 `not_observed`。本 gate 不把 frame 未觀測推論成 transparent globe leak。

## Oracle result summary

| rule | result |
| --- | --- |
| full sample projected 等於 sampled 等於 rendered | `full_sample_path_preserved` |
| reduced sample rendered 小於 visible | `sampling_or_presentation_reduction_candidate` |
| overlay true 且 mask true | `mask_visible_path_preserved` |
| overlay true 且 synthetic mask false | `globe_mask_responsibility_candidate` |
| source identity 不被 sampling 或 mask 改變 | `source_lineage_guard_preserved` |
| frame 仍未觀測 | `still_not_leak_evidence` |

## Runtime boundary confirmation

本 gate 保持：

```text
render_if_needed_called = false
controller_instantiated = false
renderer_executed = false
frame_buffer_read = false
artifact_written = false
source_lineage_integrity_token = true
coordinate_correctness_claimed = false
visual_correctness_claimed = false
transparent_globe_leak_fix_claimed = false
readiness_claimed = false
```

`runtime_probe_executed = true` 只代表既有允許 seam 加上 synthetic sampling/count logic 完成，不代表 renderer、frame 或 correctness 已被觀測。

## Stop-line notes

本 gate 不允許：

- 呼叫 `render_if_needed`
- 建立 controller
- 執行 renderer 或 GUI
- 讀取 `frame_rgba` 或 frame buffer
- 寫入 PNG、runtime JSON、`state/` 或其他 artifact
- 讀取 real AIS、ADS-B、SQL、WebSocket、cache、database
- 修改 projection、mask、sampling、compose formula
- 修改 renderer behavior
- 宣稱 coordinate correctness、visual correctness、transparent globe leak fix、readiness 或 safe-to-extract

## Recommended next gate

`dynamic_point_lod_view_frame_sampling_visibility_runtime_probe_result_interpretation_gate`

下一張 gate 應解讀本次新增的 sampling、visibility、count stdout JSON，不應直接擴張到 renderer 或 frame buffer。

## Boundary statement

Tooling/test/docs dynamic point LOD view-frame sampling / visibility probe script update gate. Synthetic-only sampling/count observation added to existing one-shot runtime probe; no render_if_needed, no controller, no renderer, no frame buffer read, no artifact generation, no production source change, no formula or renderer behavior change, no correctness/readiness/leak-fix claim, and no push.

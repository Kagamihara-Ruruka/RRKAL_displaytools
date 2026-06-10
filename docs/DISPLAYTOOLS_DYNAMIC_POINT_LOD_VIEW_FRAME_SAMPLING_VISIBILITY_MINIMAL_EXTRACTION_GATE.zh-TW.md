# Dynamic Point LOD View-frame Sampling Visibility Minimal Extraction Gate

## Gate 性質

本 gate 建立 `render_core/dynamic_point_sampling_visibility_boundary.py`，只抽出 sampling / visibility 的 descriptor、contract、ledger 類 helper。此 helper 是一塊可站的安山岩橋接層，不搬 projection formula，不搬 mask formula，不搬 sampling formula，不呼叫 runtime probe，不碰 renderer、controller、frame buffer 或 artifact writer。

本 gate 是 minimal extraction，不是 runtime behavior change，也不是 correctness、readiness 或 transparent-globe leak fix claim。

## Helper target

```text
render_core/dynamic_point_sampling_visibility_boundary.py
```

Helper 只輸出 dict / list / scalar。它不 import monolith，不 import `render_core` 其他 runtime surface，不讀寫檔案，不開網路，不建立 artifact。

## Helper surface

本 gate 建立下列 helper function：

- `build_dynamic_point_sampling_visibility_observation_descriptor`
- `build_dynamic_point_visibility_count_contract_descriptor`
- `build_dynamic_point_mask_visibility_contract_descriptor`
- `build_dynamic_point_sampling_reduction_contract_descriptor`
- `build_dynamic_point_frame_visibility_stop_line_descriptor`
- `dynamic_point_sampling_visibility_boundary_descriptor`
- `dynamic_point_sampling_visibility_planning_bundle`

這些 helper 只描述已觀測語意與 stop-line，不代表 production extraction authorization。

## Captured semantics

Helper 允許表達下列已冷卻語意：

- `sampled_visible_token`
- `visible_count_observation`
- `rendered_count_observation`
- `mask_visible_token`
- `source_lineage_integrity_token`
- `sampling_or_presentation_reduction_candidate`
- `globe_mask_responsibility_candidate`
- `source_lineage_guard`
- `frame_visibility_stop_line`
- `transparent_globe_leak_not_inferred`

## Contract decisions

- Sampling / count observation 可以作為 descriptor / contract 資料。
- `rendered_count < visible_count` 只表示 sampling / presentation reduction candidate，不表示 source loss。
- Mask hidden 可以表示 overlay 被 mask 擋住，不表示 source lineage 被刪除。
- `frame_visible` 仍是 `frame_visible_not_observed` stop-line field。
- transparent-globe leak 仍是 not inferred，不宣稱修復。

## Blocked surfaces

本 gate 持續阻斷：

- `project_ais_to_screen` movement。
- `project_aircraft_to_screen` movement。
- `mask_overlay_to_globe` movement。
- sampling formula movement。
- runtime probe call。
- `render_if_needed` call。
- controller / renderer / frame buffer。
- artifact writer。
- correctness claim。
- readiness claim。
- transparent-globe leak fix claim。
- RRKAL-wide methodology promotion。

## Checker result

使用既有 checker：

```text
scripts\validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py
```

Checker 必須對 `render_core\dynamic_point_sampling_visibility_boundary.py` PASS，並且 negative self-test 必須維持 PASS。

## Boundary statement

Tooling/test/docs dynamic point LOD view-frame sampling / visibility minimal extraction gate. Descriptor, contract, and ledger helper only; no projection formula movement, no mask formula movement, no sampling formula movement, no runtime probe call, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no production behavior change, no correctness/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.

## Recommended next gate

```text
dynamic_point_lod_view_frame_sampling_visibility_minimal_extraction_o1_review_gate
```

# Dynamic Point Sampling Visibility Cartography Update Gate

## Gate 性質

本 gate 只更新 dynamic point 解耦地圖。它把剛切出的 `render_core/dynamic_point_sampling_visibility_boundary.py` 放回現有 c_3 local map，記錄已抽離 helper、仍然不能碰的 stop-line，以及下一刀的建議方向。

本 gate 不新增 helper，不修改 helper，不修改 runtime probe，不碰 `taichi_global_bathymetry.py`，不呼叫 `render_if_needed`，不進 controller、renderer 或 frame buffer。

## Evidence read

- `render_core/dynamic_point_sampling_visibility_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_SAMPLING_VISIBILITY_MINIMAL_EXTRACTION_GATE.zh-TW.md`
- `scripts/validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_frame_visibility_stop_line_planning.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_runtime_probe_result_interpretation.py`
- `tests/test_displaytools_dynamic_point_occlusion_responsibility_boundary.py`
- `tests/test_displaytools_dynamic_point_view_frame_occlusion_structure_settlement.py`
- earlier dynamic point cartography tests

## Updated cartography summary

`dynamic_point_sampling_visibility_boundary.py` 應列入已抽離 helper inventory。它的分類是：

```text
extracted_andesite_bridge_descriptor_contract_ledger
```

這代表 sampling / count / mask 的已觀測語意已經從 extraction candidate 變成一塊 descriptor / contract / ledger 小邊界。它不是 formula movement，也不是 runtime extraction。

## Extracted helper inventory delta

新增 inventory entry：

```text
surface_name = sampling_visibility_boundary_descriptors
path = render_core/dynamic_point_sampling_visibility_boundary.py
helper_kind = descriptor_contract_ledger_helper
checker = scripts/validate_displaytools_dynamic_point_sampling_visibility_import_boundary.py
helper_test = tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py
cartography_status = extracted_andesite_bridge_descriptor_contract_ledger
runtime_dependency_allowed = false
source_movement_authorized = false
formula_movement_authorized = false
```

## Required question answers

1. 新 helper 應列為已抽離的 descriptor / contract / ledger helper。
2. Dynamic point local map 有變化：sampling / visibility 從 andesite bridge extraction candidate 進到 extracted andesite bridge descriptor / contract / ledger。
3. Frame visibility 仍是 stop-line。
4. Transparent globe leak 仍不能推論，也沒有 fix claim。
5. 下一個合理 gate 建議進入下一個安山岩橋接層選擇，而不是碰 frame / renderer。
6. 本 gate 只提升 c_3 local map，不升級 RRKAL-wide 方法論。

## Remaining stop-line / andesite / granite surfaces

仍然保留：

- `frame_visibility_surface`: not observed frame stop-line。
- `transparent_globe_leak_fault`: unresolved and not inferred。
- `projection_mask_sampling_formula_surfaces`: granite or core formula stop-line。
- `controller_renderer_frame_buffer_runtime`: granite runtime stop-line。
- `artifact_writer_surface`: forbidden artifact surface。

已前進：

- `sampling_visibility_boundary_descriptors`: extracted andesite bridge descriptor / contract / ledger。
- `sampling_count_mask_semantics`: cooled descriptor / contract semantics。

## Recommended next gate

```text
dynamic_point_lod_view_frame_next_andesite_bridge_selection_gate
```

理由：sampling / count / mask 已有乾淨小邊界，frame / leak 仍是 stop-line。下一刀應先選下一個可站的安山岩橋接層，不應被未觀測 frame surface 拉進 renderer 或 leak claim。

## Boundary statement

Docs/test-only dynamic point sampling visibility cartography update gate. No helper creation, no production source change, no runtime probe change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no projection/mask/sampling formula movement, no correctness/visual parity/readiness/leak-fix claim, no RRKAL-wide methodology promotion, and no push.
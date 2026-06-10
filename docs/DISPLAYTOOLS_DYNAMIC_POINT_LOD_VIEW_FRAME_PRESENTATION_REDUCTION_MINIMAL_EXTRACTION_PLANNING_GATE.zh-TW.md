# Dynamic Point LOD View-Frame Presentation Reduction Minimal Extraction Planning Gate

## 目的

本 gate 規劃 future `presentation_reduction` 最小語意面 helper。此 helper 仍未建立；本 gate 只確認未來 helper 應如何承載 `rendered_count < visible_count` 的 presentation / sampling reduction 語意，並固定它不得漂移成 source loss、frame truth、renderer/frame/projection/mask/formula 或 readiness claim。

本 gate 不建立 `render_core/dynamic_point_presentation_reduction_boundary.py`，不修改 checker，不修改 runtime probe，不修改 `taichi_global_bathymetry.py`，也不修改既有 `render_core` helper。

## Evidence read

本 gate 引用下列 evidence：

- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_reduction_import_boundary.py`
- `scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_reduction_contract_planning.py`
- `render_core/dynamic_point_presentation_count_boundary.py`
- `render_core/dynamic_point_sampling_visibility_boundary.py`
- `render_core/dynamic_point_source_lineage_guard_boundary.py`
- `docs/DOCS_INDEX.zh-TW.md`

## Future helper target

Future helper target, planned only：

```text
render_core/dynamic_point_presentation_reduction_boundary.py
```

Planning test 採 lifecycle-tolerant assertion：只驗證 future target path 與 helper creation authorization，不永久斷言 future extraction gate 之後該 path 仍不得存在。

## Required checker

Required checker：

```text
scripts\validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py
```

目前 checker 已存在，且 missing target PASS：

```text
candidate_exists = false
status = not_applicable_candidate_missing
boundary_passed = true
target_imported = false
target_executed = false
```

## Planned helper families

Future helper family 規劃如下：

- `build_dynamic_point_presentation_reduction_candidate_descriptor`
- `build_dynamic_point_rendered_lower_than_visible_contract_descriptor`
- `build_dynamic_point_presentation_reduction_sampling_reference_descriptor`
- `build_dynamic_point_presentation_reduction_source_guard_descriptor`
- `build_dynamic_point_presentation_reduction_stop_line_ledger`
- `dynamic_point_presentation_reduction_boundary_descriptor`
- `dynamic_point_presentation_reduction_planning_bundle`

每個 planned helper family 必須記錄：intended output keys、allowed labels、forbidden interpretations、source-lineage impact、對 `presentation_count_boundary` / `sampling_visibility_boundary` / `source_lineage_guard_boundary` 的依賴、renderer/frame dependency、formula dependency、checker coverage expectation、helper creation authorization。

## Output shape decision

Future helper output 僅允許：

- nested `dict`
- `list`
- scalar

Future helper 不得輸出：

- callable
- runtime object
- dataframe
- renderer buffer
- file handle
- network object
- SQL/cache object
- live-source object
- c_1 object
- c_4/Odoriba object

## Semantic assertions

- `rendered_count < visible_count` 是 `presentation_or_sampling_reduction_candidate`。
- `rendered_count < visible_count` 不是 source loss。
- `rendered_count < visible_count` 不是 frame truth。
- `rendered_count < visible_count` 不是 visual correctness。
- `rendered_count < visible_count` 不是 readiness。
- `rendered_count < visible_count` 不授權 runtime、probe、renderer、frame buffer、formula 或 source behavior。
- Future helper 可以 reference `presentation_count_boundary` 與 `sampling_visibility_boundary` 作為 evidence，但不得 import runtime 或搬移 formula。
- Future helper 必須由 `source_lineage_guard_boundary` 保護，避免 reduction 被解讀成 source-lineage loss。

## Forbidden interpretation summary

本 gate 明確禁止：

- source-loss interpretation
- frame-truth claim
- transparent-globe leak inference
- transparent-globe leak fix claim
- visual correctness claim
- visual parity claim
- readiness claim
- performance claim
- runtime execution
- renderer/frame buffer access
- projection formula movement
- mask formula movement
- sampling formula movement
- alpha-compose formula movement
- source-lineage mutation
- c_4/Odoriba bypass

## Decision output

```text
presentation_reduction_minimal_extraction_planning_passed = true
future_helper_target = render_core/dynamic_point_presentation_reduction_boundary.py
required_checker = scripts\validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py
required_checker_available = true
required_checker_passes_missing_target = true
presentation_reduction_helper_candidate_supported = true
descriptor_contract_ledger_candidate = true
dict_list_scalar_output_only = true
helper_creation_authorized = false
checker_modification_authorized = false
render_core_change_authorized = false
runtime_probe_change_authorized = false
taichi_global_bathymetry_change_authorized = false
render_if_needed_authorized = false
controller_renderer_frame_buffer_authorized = false
artifact_generation_authorized = false
formula_movement_authorized = false
real_source_read_authorized = false
source_lineage_mutation_authorized = false
source_loss_interpretation_authorized = false
frame_truth_claim_authorized = false
transparent_globe_leak_inferred = false
transparent_globe_leak_fix_claimed = false
coordinate_correctness_claimed = false
visual_correctness_claimed = false
visual_parity_claimed = false
readiness_claimed = false
performance_claimed = false
c4_odoriba_bypass_authorized = false
```

## Recommended next gate

```text
dynamic_point_lod_view_frame_presentation_reduction_minimal_extraction_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame presentation reduction minimal extraction planning gate. No helper creation, no `render_core/dynamic_point_presentation_reduction_boundary.py` creation, no checker modification, no runtime probe change, no `taichi_global_bathymetry.py` change, no existing `render_core` helper change, no `render_if_needed`, no controller, no renderer, no frame buffer read, no artifact generation, no formula movement, no source-loss interpretation, no frame-truth claim, no transparent-globe leak inference or fix claim, no correctness/visual parity/readiness/performance claim, no c_4/Odoriba bypass, and no push.

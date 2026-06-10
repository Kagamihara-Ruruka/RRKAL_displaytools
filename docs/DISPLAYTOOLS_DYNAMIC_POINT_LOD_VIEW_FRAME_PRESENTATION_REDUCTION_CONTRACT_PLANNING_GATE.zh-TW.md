# Dynamic Point LOD View-Frame Presentation Reduction Contract Planning Gate

## 目的

本 gate 將 `presentation_reduction_contract` 冷卻成下一塊可切的 dynamic point LOD / view-frame 安山岩語意面。核心判斷是：`rendered_count < visible_count` 只能代表 presentation 或 sampling reduction candidate，不代表 source loss、frame truth、transparent-globe leak、visual correctness 或 runtime readiness。

本 gate 只做 docs/test-only planning，不建立 helper，不建立 checker，不修改 `render_core`，不修改 runtime probe，也不觸碰 `taichi_global_bathymetry.py`。

## Evidence read

本 gate 引用下列 evidence：

- `tests/test_displaytools_dynamic_point_lod_view_frame_post_source_lineage_guard_next_bridge_selection.py`
- `docs/DISPLAYTOOLS_DYNAMIC_POINT_LOD_VIEW_FRAME_POST_SOURCE_LINEAGE_GUARD_NEXT_BRIDGE_SELECTION_GATE.zh-TW.md`
- `render_core/dynamic_point_presentation_count_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_presentation_count_boundary_helpers.py`
- `render_core/dynamic_point_sampling_visibility_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_boundary_helpers.py`
- `render_core/dynamic_point_source_lineage_guard_boundary.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_source_lineage_guard_boundary_helpers.py`
- `tests/test_displaytools_dynamic_point_lod_view_frame_sampling_visibility_runtime_probe_result_interpretation.py`
- `docs/DOCS_INDEX.zh-TW.md`

## Future targets

Planned helper target only：

```text
render_core/dynamic_point_presentation_reduction_boundary.py
```

Planned checker target only：

```text
scripts/validate_displaytools_dynamic_point_presentation_reduction_import_boundary.py
```

本 gate 不授權建立上述 helper 或 checker。

## Planned helper families

未來 helper family 規劃如下：

- `build_dynamic_point_presentation_reduction_candidate_descriptor`
- `build_dynamic_point_rendered_lower_than_visible_contract_descriptor`
- `build_dynamic_point_sampling_reduction_reference_descriptor`
- `build_dynamic_point_presentation_reduction_source_guard_descriptor`
- `build_dynamic_point_presentation_reduction_stop_line_ledger`
- `dynamic_point_presentation_reduction_boundary_descriptor`
- `dynamic_point_presentation_reduction_planning_bundle`

這些 helper family 只允許成為 descriptor / contract / ledger candidate。輸出形狀應維持 nested dict、list、scalar。不得輸出 runtime object、renderer buffer、frame buffer、callable、file handle、network object、SQL/cache object、live source object、c_1 object 或 c_4/Odoriba object。

## Planning matrix summary

| Surface | Allowed meaning | Forbidden interpretation | Runtime dependency | Formula dependency | Renderer/frame dependency |
| --- | --- | --- | --- | --- | --- |
| `rendered_lower_than_visible` | `presentation_or_sampling_reduction_candidate` | source loss、frame truth、transparent-globe leak、visual correctness、runtime readiness | false | false | false |
| `presentation_or_sampling_reduction_candidate` | count difference classification without source loss | source completeness claim、renderer output truth、performance readiness | false | false | false |
| `presentation_count_boundary_reference` | visible/rendered count are existing contract fields | helper creation in this gate、formula movement | false | false | false |
| `sampling_visibility_boundary_reference` | sampled-visible and count observations support reduction candidate | sampling formula movement、runtime probe expansion | false | false | false |
| `source_lineage_guard_boundary` | reduction does not mutate source identity | source-lineage mutation、reduced-count-as-source-loss | false | false | false |
| `frame_visible_not_observed` | frame visibility remains unobserved | frame truth claim、transparent-globe leak inference | false | false | false |

## Semantic assertions

- `rendered_count < visible_count` means `presentation_or_sampling_reduction_candidate`.
- `rendered_count < visible_count` does not mean source loss.
- `rendered_count < visible_count` does not mean frame visibility truth.
- `rendered_count < visible_count` does not mean transparent-globe leak.
- `rendered_count < visible_count` does not mean visual correctness.
- `rendered_count < visible_count` does not authorize runtime, renderer, frame, or formula behavior.
- The candidate is protected by `source_lineage_guard_boundary`.
- The candidate may reference `presentation_count_boundary` and `sampling_visibility_boundary` as evidence, but must not import runtime or formulas.

## Distinct surface decision

`presentation_count_boundary` already records visible/rendered count fields and the existence of a reduction candidate. This gate is still distinct because it promotes the reduction relation itself into a future helper/checker planning surface with:

- a dedicated reduction candidate descriptor;
- a rendered-lower-than-visible contract descriptor;
- a source guard descriptor tied to `source_lineage_guard_boundary`;
- a stop-line ledger that keeps frame truth, leak inference, and visual correctness closed.

Therefore this planning does not duplicate `presentation_count_boundary` completely.

## Decision output

```text
presentation_reduction_contract_planning_passed = true
presentation_reduction_helper_candidate_supported = true
descriptor_contract_ledger_candidate = true
helper_creation_authorized = false
checker_creation_authorized = false
render_core_change_authorized = false
runtime_probe_change_authorized = false
formula_movement_authorized = false
source_loss_interpretation_authorized = false
frame_truth_claim_authorized = false
transparent_globe_leak_inferred = false
visual_correctness_claimed = false
readiness_claimed = false
```

Additional boundary decisions：

```text
checker_modification_authorized = false
taichi_global_bathymetry_change_authorized = false
render_if_needed_authorized = false
controller_renderer_frame_buffer_authorized = false
artifact_generation_authorized = false
real_source_read_authorized = false
source_lineage_mutation_authorized = false
raw_row_seam_runtime_authorized = false
direct_c3_to_c1_integration_authorized = false
c4_odoriba_bypass_authorized = false
coordinate_correctness_claimed = false
visual_parity_claimed = false
performance_claimed = false
rrkal_wide_methodology_claimed = false
```

## Recommended next gate

```text
dynamic_point_lod_view_frame_presentation_reduction_import_boundary_checker_planning_gate
```

## Boundary statement

Docs/test-only dynamic point LOD view-frame presentation reduction contract planning gate. No helper creation, no checker creation, no `render_core` change, no runtime/probe/renderer/frame/formula/source behavior change, no source-loss/frame-truth/leak/correctness/readiness claim, no c_4/Odoriba bypass, and no push.

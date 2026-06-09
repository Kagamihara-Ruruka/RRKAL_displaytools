# Dynamic Point Recursive Historical Lithology Gate

本文件定義 dynamic point 剩餘 surface 的第一版遞迴歷史岩性分析 gate。此 gate 只做 docs/test-only 分類，不建立 helper module，不移動 source，不修改 checker，不修改 generic checker，不修改或 import `taichi_global_bathymetry.py`。

## Why this is not an extraction gate

Second cutout cartography 已顯示 dynamic point 已切出五塊 descriptor / policy / ledger 外殼。剩餘 surface 多數靠近 runtime、formula、schema 或 cross-organ seam。本 gate 的目的不是繼續下刀，而是先判斷剩餘石頭的岩性，避免用切沉積岩的方法去硬切地核附近的東西。

## Historical differential method

本 gate 採用 static-only 歷史差集方法：

- 讀 current HEAD `6847d60` 的 dynamic point cartography、helper、checker、docs。
- 靜態掃描 current `taichi_global_bathymetry.py` 的 dynamic point、Datashader、projection、controller、metadata、runtime 錨點。
- 讀 second cutout cartography 的 `descriptor_sediment_remaining=false` 與 `granite_pressure_detected=true` 結論。
- 嘗試查詢 git history 與早期斷面；本輪 `git log` / history grep 查詢在本機超時，因此降級為可觀察歷史樣本清單，並在 test packet 標記 `history_query_limited`。

Evidence limit: 本 gate 沒有宣稱完成完整 ancestry diff。分類是第一版 static lithology map，依 current static scan 與既有 gate evidence 保守判斷。

## Lithology definitions

| Lithology | Definition |
| --- | --- |
| `sediment` | 晚期新增、無地核依賴黏著、descriptor/policy/ledger-only。 |
| `late_hardened_granite` | 晚期新增，但已黏到 runtime、controller、schema 或 dataflow。 |
| `core_lineage_granite` | 早期已有或高度疑似祖先延續，且連到 renderer、projection、runtime 或 data-source 主幹。 |
| `andesite` | 晚期差集新增，但依賴掃描顯示已黏到地核或熱路徑。 |
| `core_interface_only` | 不應移植 implementation，只能做 wrapper、interface 或 shadow path。 |
| `new_organ_surface` | 晚期新增但具獨立產品語義，不應視為垃圾沉積。 |
| `extinct_or_dead_surface` | 歷史曾出現但現在不再作用或只剩殘影。 |

## Decision rules

```text
sediment_candidate =
  late_diff_added
  AND NOT core_dependency_attached
  AND NOT hot_path_behavioral_effect

core_lineage_granite =
  ancestor_present
  AND core_dependency_attached

andesite_candidate =
  late_diff_added
  AND core_dependency_attached

late_hardened_granite =
  late_diff_added
  AND high_runtime_or_schema_coupling

core_interface_only =
  core_lineage_granite
  AND direct_extraction_not_authorized
```

## Remaining surface matrix

| Surface | Historical age status | Dependency attachment | Lithology | Semantic reconstruction | Implementation transplant | Recommended next gate |
| --- | --- | --- | --- | --- | --- | --- |
| `replay_live_lineage_deeper_runtime` | late diff with history limit | SQL replay, WebSocket/live stream, cache/database IO | `andesite` | required | not authorized | `dynamic_point_replay_live_lineage_semantic_reconstruction_gate` |
| `controller_selection_picker_hit_test` | late diff with controller coupling | controller mutation, picker execution, hit-test execution | `late_hardened_granite` | required | not authorized | `dynamic_point_controller_selection_interface_design_gate` |
| `datashader_runtime_sampling` | late diff with runtime sampling coupling | Datashader, pandas, numpy, renderer count runtime | `late_hardened_granite` | required | not authorized | `dynamic_point_runtime_sampling_interface_design_gate` |
| `projection_flip_mask_sync` | ancestor present or highly suspected | projection, flip, mask, renderer frame | `core_interface_only` | required | not authorized | `dynamic_point_projection_interface_shadow_gate` |
| `metadata_artifact_schema` | late diff with schema boundary | metadata sidecar writer, artifact writer, runtime JSON writer | `new_organ_surface` | required | not authorized | `o1_metadata_artifact_schema_review_gate` |
| `cross_organ_card_integration` | late diff cross-organ | o_1 governance, downstream card contract, cross-repo semantics | `new_organ_surface` | required | not authorized | `o1_cross_organ_card_integration_review_gate` |

## Andesite candidates

- `replay_live_lineage_deeper_runtime`

This is treated as andesite because it is a late dynamic point surface but already attaches to SQL replay, WebSocket/live lineage, and cache/database IO stop lines. It needs semantic reconstruction before any implementation movement.

## Core-lineage granite and interface-only candidates

- `projection_flip_mask_sync` is classified as `core_interface_only`.

Reason: projection/flip/mask sync is highly coupled to renderer frame and formula ownership. Direct extraction is not authorized. A future route would need an interface or shadow contract, not implementation transplant.

## Late-hardened granite candidates

- `controller_selection_picker_hit_test`
- `datashader_runtime_sampling`

These surfaces appear late enough to be dynamic point specific, but are already hardened by runtime coupling. They should be treated as design/interface work, not descriptor extraction work.

## New organ surfaces

- `metadata_artifact_schema`
- `cross_organ_card_integration`

These are not c_3-only helper targets. They require governance or schema review before any implementation movement.

## Decision output

| Field | Value |
| --- | --- |
| `descriptor_sediment_remaining` | `false` |
| `source_movement_authorized` | `false` |
| `helper_module_creation_authorized` | `false` |
| `runtime_merge_enabled` | `false` |
| `generic_checker_blocking` | `false` |
| `generic_checker_replacement_authorized` | `false` |
| `next_gate` | `dynamic_point_lithology_semantic_reconstruction_design_gate` |
| `next_gate_kind` | `analysis_design_not_extraction` |

## Recommended next gate

Recommended next gate: `dynamic_point_lithology_semantic_reconstruction_design_gate`.

This should be an analysis/design gate, not extraction. It should choose whether to design wrapper/interface/shadow paths for core-adjacent surfaces, or stop dynamic point slicing and move to another craton.

## Explicit exclusions

- No helper module creation.
- No source movement.
- No production source change.
- No checker script change.
- No generic checker trust-level change.
- No generic checker blocking behavior change.
- No monolith import.
- No SQL, WebSocket, live-source, cache, or database execution.
- No real AIS or ADS-B data read.
- No pandas, Datashader, or numpy runtime.
- No projection, flip, or mask formula change.
- No controller selection, picker, or hit-test mutation.
- No renderer, Qt, VisPy, or Taichi runtime execution.
- No metadata or output schema change.
- No runtime merge enablement.
- No readiness, performance, visual parity, bug-fix, live-data, or safe-to-extract claim.

## Boundary statement

Docs/test-only dynamic point recursive historical lithology gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.

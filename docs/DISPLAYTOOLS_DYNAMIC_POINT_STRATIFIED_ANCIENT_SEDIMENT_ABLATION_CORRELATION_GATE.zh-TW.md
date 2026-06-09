# Dynamic Point 分層古老沉積候選消融相關性 Gate

本文件是 dynamic point 的 docs/test-only correlation gate。它把既有 historical slice inventory、recursive lithology、semantic reconstruction、hypothesis validation 的結果合併，檢查古老地層中的沉積候選在後續切片中是否常轉為安山岩、花崗岩或接口壓力區。

本 gate 不是科學定理證明，也不是 source movement 授權。它只回答一個工程問題：這個假說在 dynamic point 局部是否足夠有用，是否值得從 `L2_local_pattern_candidate` 建議升為 `L2_local_pattern`。

## Anchor

- Base camp rollback anchor：`ad38dbe`
- Forward camps：
  - `b29b79f`
  - `71c7182`
  - `71b8e40`

## 概念規則

本 gate 固定以下規則：

- `not_scientific_theorem = true`
- `useful_engineering_hypothesis_target = true`
- `correlation_is_not_causation = true`
- `correlation_is_not_extraction_authorization = true`
- `historical_diff_is_not_lithology_verdict = true`
- `semantic_hypothesis_is_not_extraction_authorization = true`

換句話說，相關性可以降低操作熵，但不能單獨證明因果，不能授權 source movement，也不能成為 universal RRKAL doctrine。

## 為什麼需要猴子與卡秋莎消融

古老沉積候選通常不像新 helper 那樣邊界清楚。它可能在早期只是資料或標籤，後來逐漸黏到 SQL、WebSocket、projection、controller、datashader 或 schema。消融矩陣用四種模式觀察候選 surface 被遮斷時的工程反應：

- `null_mode`：候選消失時，是否只影響描述器。
- `tripwire_mode`：若碰到 runtime 或公式，是否直接觸發 stop line。
- `trace_mode`：只記錄依賴壓力，不執行 runtime。
- `substitute_mode`：用靜態 label 替代時，是否仍可維持邊界描述。

這些模式只產生 fixture 結論，不 patch production，不執行 renderer 或資料通道。

## Slice model

本 gate 保留既有 inventory 的切片語義：

- `earliest_available_import_basement`
- `early_5_10_nearest_slice`
- `intermediate_10k_nearest_slice`
- `intermediate_14k_nearest_slice`
- `current_21k_head_slice`
- `base_camp_rollback_anchor`
- `forward_camp`

其中 `intermediate_10k_nearest_slice` 與 `intermediate_14k_nearest_slice` 仍標記為 `history_query_limited`，不可硬補。

## Ancient sediment candidate matrix

| Candidate | Source slice | Later lithology | Correlation | Counterexample |
| --- | --- | --- | --- | --- |
| `replay_live_lineage_deeper_runtime` | `earliest_available_import_basement` | `andesite_bridge_candidate` | `medium_high` | false |
| `controller_selection_picker_hit_test` | `earliest_available_import_basement` | `late_hardened_granite_candidate` | `medium` | false |
| `datashader_runtime_sampling` | `earliest_available_import_basement` | `late_hardened_granite_candidate` | `high` | false |
| `projection_flip_mask_sync` | `earliest_available_import_basement` | `core_interface_only_candidate` | `high` | false |
| `metadata_artifact_schema` | `current_21k_head_slice` | `new_organ_or_schema_surface` | `counterexample_low` | true |
| `cross_organ_card_integration` | `forward_camp` | `new_organ_or_schema_surface` | `counterexample_low` | true |

前四項支持古老沉積候選逐漸轉成安山岩、花崗岩或接口壓力區的工程假說。後兩項保留為 counterexample，因為它們更像 new-organ 或 governance surface，不應被塞進古老沉積模型。

## Ablation response summary

- Replay/live lineage：`tripwire_mode` 會撞 SQL、WebSocket、cache、database stop line。
- Controller selection：`tripwire_mode` 會撞 controller mutation、picker、hit-test stop line。
- Datashader sampling：`tripwire_mode` 會撞 Datashader、pandas、numpy 與 renderer runtime stop line。
- Projection sync：`tripwire_mode` 會撞 projection、flip、mask formula stop line。
- Metadata schema：`tripwire_mode` 會撞 metadata/artifact schema governance stop line。
- Cross-organ integration：`tripwire_mode` 會撞 cross-organ handoff stop line。

所有 response 都是 fixture label，不執行 runtime。

## Threshold

本 gate 使用非百分百的工程門檻：

- `high_correlation_threshold_percent = 75`
- `high_correlation_threshold_is_100_percent = false`
- `minimum_supporting_cases_required = 3`
- `counterexample_tolerance = 2`

目前有效古老沉積候選為四項，支持變質路徑的候選為四項，因此 `high_correlation_threshold_met = true`。counterexample 被保留，用來避免把 new-organ、schema 或 cross-organ surface 誤判成古老沉積。

## Trust-level recommendation

本 gate 建議：

- Dynamic point 岩性模型可從 `L2_local_pattern_candidate` 建議升為 `L2_local_pattern`。
- 此升級只限 dynamic point 局部工程方法。
- 不升級為 universal doctrine。
- 不授權 extraction。
- 不授權 source movement。

## 下一步建議

推薦下一張 gate：

`dynamic_point_projection_interface_shadow_gate`

理由：projection/flip/mask sync 的相關性與歷史壓力最穩定，且策略是 interface-only shadow path，可先設計接口，不移動公式。

## Explicit exclusions

- 不建立 helper module。
- 不移動 source。
- 不修改 production source。
- 不修改 checker script。
- 不升級 generic checker trust level。
- 不讓 generic checker 變成 blocking。
- 不新增或修改 generic profile。
- 不 import monolith。
- 不執行 SQL、WebSocket、live-source。
- 不讀 real AIS、ADS-B、cache、database。
- 不引入 pandas、datashader、numpy runtime。
- 不修改 projection、flip、mask formula。
- 不修改 controller selection、picker、hit-test。
- 不執行 renderer、Qt、VisPy、Taichi runtime。
- 不修改 metadata/output schema。
- 不實作 cross-organ integration。
- 不啟用 runtime merge。
- 不宣稱 universal methodology doctrine。
- 不宣稱 scientific theorem。
- 不宣稱 readiness、performance、visual parity、bug-fix、safe-to-extract。

## Boundary statement

Docs/test-only dynamic point stratified ancient sediment ablation correlation gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no cross-organ integration implementation, no runtime merge enablement, no universal methodology doctrine promotion, no scientific theorem claim, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.

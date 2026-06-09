# Dynamic Point 岩性假說驗證 Gate

本文件是 dynamic point 剩餘 surface 的 docs/test-only 假說驗證 gate。它整合三張既有 gate 的結論：

- recursive historical lithology gate
- lithology semantic reconstruction design gate
- metamorphic history slice inventory gate

目的不是證明岩性模型是通用定律，而是檢查它在 dynamic point 這個局部問題上是否降低操作熵。若它能把剩餘 surface 導向較明確的 rebuild、wrapper、interface-only、schema governance 或 cross-organ handoff，則可暫列為 `L2_local_pattern_candidate`。這不等於 extraction authorization。

## Base camp 與 forward camps

- Base camp rollback anchor：`ad38dbe`
- Forward camps：
  - `b29b79f`
  - `71c7182`

`ad38dbe` 是回到 recursive lithology 之前的保守錨點。`b29b79f` 與 `71c7182` 是語義重建設計與歷史斷面 inventory 的前進營地。本 gate 只讀取這些 gate 的靜態結論，不執行 runtime。

## 驗證問題

本 gate 回答八個問題：

- `classification_stability`：同一 surface 在三張 gate 中是否保持穩定或合理修正。
- `decision_reduction`：每個 surface 是否被導向明確策略。
- `risk_reduction`：假說是否避免把硬區誤當沉積岩切。
- `evidence_support`：哪些分類被歷史斷面與依賴壓力補強。
- `evidence_limit`：哪些仍因 history query limit 或未執行 runtime 而保留低信心。
- `operational_entropy_delta`：下一步決策空間是否縮小。
- `trust_level_recommendation`：哪些部分可列為 `L2_local_pattern_candidate`，哪些仍是 `L1_supported_hypothesis`。
- `next_action`：下一張 gate 應走哪個 analysis/design 路徑。

## 六個 surface 驗證矩陣

| Surface | recursive lithology | semantic strategy | metamorphic transition | trust | next gate |
| --- | --- | --- | --- | --- | --- |
| `replay_live_lineage_deeper_runtime` | `andesite` | semantic reconstruction before rebuild or wrapper decision | `sediment_to_andesite_bridge` | `L1_supported_hypothesis` | `dynamic_point_replay_live_lineage_semantic_reconstruction_gate` |
| `controller_selection_picker_hit_test` | `late_hardened_granite` | interface or wrapper design, no direct transplant | `sediment_to_late_hardened_granite` | `L1_supported_hypothesis` | `dynamic_point_controller_selection_interface_design_gate` |
| `datashader_runtime_sampling` | `late_hardened_granite` | runtime sampling contract adapter design | `sediment_to_late_hardened_granite` | `L2_local_pattern_candidate` | `dynamic_point_runtime_sampling_contract_design_gate` |
| `projection_flip_mask_sync` | `core_interface_only` | core interface-only shadow path | `core_lineage_to_interface_only` | `L2_local_pattern_candidate` | `dynamic_point_projection_interface_shadow_gate` |
| `metadata_artifact_schema` | `new_organ_surface` | schema governance and o_1 review | `schema_surface_requires_governance` | `L2_local_pattern_candidate` | `o1_metadata_artifact_schema_review_gate` |
| `cross_organ_card_integration` | `new_organ_surface` | cross-organ handoff contract discussion | `new_organ_to_cross_organ_handoff` | `L2_local_pattern_candidate` | `o1_cross_organ_card_integration_review_gate` |

## 操作熵評估

沒有岩性假說時，六個剩餘 surface 都可能被誤判為同一類 hard problem。驗證後，決策空間被分成：

- replay/live lineage：先做語義重建，再決定 rebuild 或 wrapper。
- controller/picker/hit-test：走 interface 或 wrapper design，不直接移植。
- datashader runtime sampling：走 runtime sampling contract 或 adapter design。
- projection/flip/mask：走 core interface-only shadow path。
- metadata/artifact schema：交 o_1 做 schema governance。
- cross-organ card integration：走跨 organ handoff。

因此本 gate 判定 operational entropy 有下降，但下降範圍只限 dynamic point 局部模式候選。

## 被補強的分類

- `projection_flip_mask_sync`：歷史與語義都指向 core interface-only，避免 projection、flip、mask 公式移動。
- `datashader_runtime_sampling`：依賴壓力穩定指向 dataframe 與 renderer runtime，適合先設計 adapter contract。
- `metadata_artifact_schema`：不是 c_3-only implementation，需 schema governance。
- `cross_organ_card_integration`：不是單一 agent 可切除 surface，需 cross-organ handoff。

## 低信心或需補證據的分類

- `replay_live_lineage_deeper_runtime`：history query limited，且未執行 SQL、WebSocket、cache 或 database。
- `controller_selection_picker_hit_test`：未執行 picker 或 hit-test runtime，仍需 interface design 前的語義盤點。

## 為什麼不能升級為通用 doctrine

本 gate 只驗證 dynamic point 的局部操作熵下降。歷史差集不是岩性判決本身，語義假說也不是 extraction authorization。其他 subsystem 可能有不同歷史、依賴壓力與治理邊界，因此本 gate 不把岩性方法寫成 universal RRKAL doctrine。

## 下一步建議

推薦下一張 gate：

`dynamic_point_projection_interface_shadow_gate`

理由是該 surface 信心最高，策略最清楚，且可維持 interface-only / shadow path，不需要 projection、flip、mask 公式移動，也不需要 renderer runtime。

## 明確排除

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
- 不宣稱 readiness、performance、visual parity、bug-fix、safe-to-extract。

## Boundary statement

Docs/test-only dynamic point lithology hypothesis validation gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no cross-organ integration implementation, no runtime merge enablement, no universal methodology doctrine promotion, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.

# Dynamic Point Lithology Semantic Reconstruction Design Gate

本文件定義 dynamic point 剩餘六個 surface 的語義重建設計 gate。此 gate 只做 docs/test-only 設計，不建立 helper module，不移動 source，不修改 checker，不修改 generic checker profile，不修改或 import `taichi_global_bathymetry.py`。

## Why semantic reconstruction is not source movement

語義重建只回答兩個問題：某個 surface 原本想完成什麼事，以及目前對系統承諾什麼語義。它不搬原碼、不重建 runtime、不替換 controller、不更改 projection、不修改 metadata schema，也不授權 extraction。

本 gate 固定以下規則：

- `semantic_hypothesis_is_not_authorization = true`
- `implementation_transplant_authorized = false`
- `source_movement_authorized = false`
- `helper_module_creation_authorized = false`
- `runtime_merge_enabled = false`
- `generic_checker_blocking = false`
- `readiness_claimed = false`

## Original intent versus current semantic contract

Original intent 是歷史或功能目的假說，通常描述當初為什麼需要這個 surface。Current semantic contract 是目前其他 layer 可能依賴的語義承諾。兩者不一定相同。

如果 original intent 與 current semantic contract 發生 drift，不能直接搬 implementation。必須先設計 wrapper、interface、adapter、cross-organ handoff，或標記 evidence limit。

## Semantic reconstruction matrix

| Surface | Lithology | Original intent hypothesis | Current semantic contract hypothesis | Strategy | Confidence |
| --- | --- | --- | --- | --- | --- |
| `replay_live_lineage_deeper_runtime` | `andesite` | Explain whether points come from replay, live stream, synthetic, or unavailable source. | Lineage is provenance and availability; execution stays in provider/runtime channels. | Semantic reconstruction before rebuild or wrapper decision. | medium |
| `controller_selection_picker_hit_test` | `late_hardened_granite` | Let operators identify selected vehicle, selected layer, and hit state. | Selection semantics must be exposed through an interface without controller or picker transplant. | Interface/wrapper design, not direct transplant. | medium |
| `datashader_runtime_sampling` | `late_hardened_granite` | Cap point rendering cost while preserving useful density information. | Sampling must be represented as an adapter contract before runtime implementation is considered. | Runtime sampling contract and adapter design. | medium |
| `projection_flip_mask_sync` | `core_interface_only` | Keep points synchronized with globe projection, hemisphere mask, and flipped lon-lat frames. | Dynamic point can only consume a stable projection interface or shadow path. | Core interface-only shadow path. | high |
| `metadata_artifact_schema` | `new_organ_surface` | Make rendered output and runtime evidence explainable to reviewers and downstream tools. | Schema meaning requires governance review before c_3 can implement or alter contracts. | Schema governance and o_1 review. | high |
| `cross_organ_card_integration` | `new_organ_surface` | Align dynamic point display evidence with card or downstream review surfaces. | Integration belongs to cross-organ contract discussion, not c_3-only implementation. | Cross-organ handoff discussion. | high |

## Wrapper and interface candidates

- `replay_live_lineage_deeper_runtime`
- `controller_selection_picker_hit_test`
- `datashader_runtime_sampling`
- `projection_flip_mask_sync`

These surfaces may need wrapper, interface, adapter, or shadow-path design. None authorizes source movement.

## Cross-organ handoff candidates

- `metadata_artifact_schema`
- `cross_organ_card_integration`

These surfaces need governance or cross-agent contract alignment. They are not c_3-only implementation tasks.

## Evidence limits

- Git ancestry queries were limited in the prior lithology gate.
- Static scan cannot prove picker, projection, Datashader, or renderer behavior.
- Schema and cross-organ semantics cannot be decided by c_3 tests alone.
- Semantic hypotheses are not extraction authorization.

## Why this is design, not extraction

This gate does not identify a descriptor-only helper target. It classifies strategy shape only:

- rebuild candidate
- wrapper or interface candidate
- schema governance candidate
- cross-organ handoff candidate
- further scout candidate

No implementation transplant is authorized.

## Recommended next gate

Recommended next gate: `dynamic_point_semantic_reconstruction_strategy_review_gate`.

This should remain analysis/design. It should decide whether to open targeted wrapper/interface design gates, schema governance review, or cross-organ handoff. It should not create helper modules or move source.

## Explicit exclusions

- No helper module creation.
- No source movement.
- No production source change.
- No checker script change.
- No generic checker trust-level change.
- No generic checker blocking behavior change.
- No generic profile change.
- No monolith import.
- No SQL, WebSocket, live-source, cache, or database execution.
- No real AIS or ADS-B data read.
- No pandas, Datashader, or numpy runtime.
- No projection, flip, or mask formula change.
- No controller selection, picker, or hit-test mutation.
- No renderer, Qt, VisPy, or Taichi runtime execution.
- No metadata or output schema change.
- No cross-organ integration implementation.
- No runtime merge enablement.
- No readiness, performance, visual parity, bug-fix, live-data, or safe-to-extract claim.

## Boundary statement

Docs/test-only dynamic point lithology semantic reconstruction design gate. No helper module creation, no source movement, no production source change, no checker script change, no generic checker trust-level change, no generic checker blocking behavior change, no generic profile change, no monolith import, no SQL/WebSocket/live-source execution, no real AIS/ADS-B/cache/database read, no pandas/datashader/numpy runtime, no projection/flip/mask formula change, no controller selection/picker/hit-test mutation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no cross-organ integration implementation, no runtime merge enablement, and no readiness/performance/visual parity/bug-fix/safe-to-extract claim.

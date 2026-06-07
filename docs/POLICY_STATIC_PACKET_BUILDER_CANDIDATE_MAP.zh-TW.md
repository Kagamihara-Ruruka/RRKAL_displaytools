# Policy / Static Packet Builder Candidate Map

## TL;DR

This is a docs/evidence-only candidate map for low-risk future gates after the DataFrame normalizer extraction.

The inspected zone is the policy object and static packet builder region around `taichi_global_bathymetry.py` lines `5064-9805` in the current file, corresponding to the requested `5184-9793` monolith band before recent line movement.

No extraction is approved by this document.

## Static inventory summary

Observed shape:

- Four policy-style classes with deterministic dict/text output and no file/cache/artifact writes.
- Many static registry constants followed by `*_snapshot()` / `*_text()` functions.
- Several broad extraction/readiness packet builders that combine multiple registries and should not be treated as first leaf candidates.
- Qt facade and Qt main-window packet builders near the end of the region are hub-adjacent and should not be touched as low-risk leaves.

No renderer controller execution, Qt/VisPy/Taichi runtime call, file/cache read, file/cache write, PNG output, runtime JSON output, metadata sidecar write, or output behavior mutation is observed inside the obvious static packet builders. Some later packet builders reference Qt/controller facade concepts as static text/coverage contracts and therefore remain higher-risk.

## Candidate table

| class/function/registry | line anchor | static classification | inputs / outputs | global dependencies | reads files/cache/artifacts | writes files/cache/artifacts | renderer/controller state | Qt/VisPy/Taichi reference | pure dict/text/packet construction | candidate next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `DatashaderSamplingPolicy` | `5064` | `policy_object_candidate` | input counts/lod/scale/mode; output decision dict/text | none beyond local constants | no | no | no | no | yes | Gate A candidate after snapshot fixtures. |
| `LayerRenderBudgetPolicy` | `5086` | `policy_object_candidate` | canvas size/render timing/lod/target fps/interaction/layer visibility; output decision dict/text | `LAYER_RENDER_COSTS` | no | no | no | no | yes | Current gate: `LAYER_RENDER_BUDGET_POLICY_FIXTURE_PARITY_GATE.zh-TW.md`; higher risk because cost map movement must be reviewed. |
| `PointOverlayBudgetPolicy` | `5242` | `policy_object_candidate` | layer id/records/lod/style profile; output decision dict/text | `LAYER_RENDER_COSTS` | no | no | no | no | yes | Gate A top candidate due narrow scope. |
| `AdaptiveRenderQualityPolicy` | `5323` | `policy_object_candidate` | width/height/render_ms/lod/target fps; output decision dict/text | none observed | no | no | no | no | yes | Gate A candidate, but timing semantics need care. |
| `MODULE_SPLIT_BLUEPRINT` + `module_split_blueprint_text` | `5379`, `5446` | `static_packet_builder_candidate` | no args; output text | registry constant | no | no | no | no | yes | Gate B candidate, low runtime risk but wording risk. |
| `provider_interface_spec_text`, `renderer_data_contract_text`, `ui_localization_status_text` | `5472-5540` | `static_packet_builder_candidate` | no args; output text | inline constants | no | no | no | no | yes | Gate B candidate; simple snapshot/text tests. |
| `SYMBOL_EXTRACTION_MAP` + `symbol_extraction_map_text` | `5544`, `5747` | `static_packet_builder_candidate` | no args; output text | registry constant | no | no | no | no | yes | Gate B candidate; good for static registry snapshot. |
| `RUNTIME_CONFIGURATION_CONTRACT` + text | `5785`, `5865` | `false_leaf_risk` | optional `args`; output text | registry constant plus runtime args | no | no | no | no | mostly, but `getattr(args, ...)` | Needs fixture gate if selected; not first pick. |
| `PROJECT_GOAL_MILESTONES`, `DECOUPLING_EXTRACTION_UNITS` packet/text | `5892-6090` | `static_packet_builder_candidate` | no args; output list/text | registry constants | no | no | no | no | yes | Gate B candidate if docs wording is guarded. |
| `*_MODULE_API` snapshots/text for provider/hydrology/ocean/vector/lod/style/datashader | `6093-7535` | `static_packet_builder_candidate` | no args; output dict/text | module API registries | no | no | no | no | yes | Gate B top candidate family for snapshot contracts. |
| `*_EXTRACTION_READINESS_PACKET` snapshots/text | `6279-7656` | `broad_contract_packet_builder` | no args; output readiness packets/text | readiness registries plus `PRE_VALIDATION_EVIDENCE_PLAN` | no | no | no | no | yes, but broad semantics | Needs o_1 review; wording/false readiness risk. |
| `module_api_registry_snapshot/text` | `7659-7689` | `broad_contract_packet_builder` | no args; output composed registry | many module API snapshot functions | no | no | no | no | composed packet | Needs o_1 review before any movement. |
| `pre_extraction_readiness_audit_snapshot/text` | `7692-7750` | `broad_contract_packet_builder` | no args; output audit packet/text | module registry, extraction units, runtime config | no | no | no | no | composed packet | Do not choose as first leaf. |
| `FIRST_EXTRACTION_*` and `extraction_readiness_packet_index_*` | `7753-8097` | `broad_contract_packet_builder` | no args; output plan/index text | many readiness registries | no | no | no | no | composed packet | Needs o_1 review; broad contract source. |
| `active_goal_extraction_seam_matrix_*` | `8100-8204` | `broad_contract_packet_builder` | no args; output seam matrix/text | readiness packets | no | no | no | no | composed packet | Not first candidate. |
| `CACHE_GOVERNANCE_MATRIX` + text | `8207-8345` | `static_packet_builder_candidate` | no args; output dict/text | registry constant | no | no | no | no | yes | Gate B candidate, but cache-governance wording must stay display-only. |
| `active_goal_known_issue_matrix_*` | `8348-8445` | `static_packet_builder_candidate` | no args; output issue matrix/text | inline issue list | no | no | no | no | yes | Gate B candidate; low runtime risk. |
| `MODULE_IMPORT_BOUNDARY_MATRIX`, `module_contract_coverage_*` | `8448-8563` | `broad_contract_packet_builder` | no args; output boundary/coverage | module API registry and extraction units | no | no | no | no | composed packet | Useful for gates, not first movement target. |
| `VALIDATION_AND_ROLLBACK_PLAN`, `PRE_VALIDATION_EVIDENCE_PLAN` + text | `8566-8755` | `static_packet_builder_candidate` | no args; output list/text | registry constants | no | no | no | no | yes | Gate B candidate with wording guard. |
| `UNVERIFIED_RISK_REGISTER`, `ACTIVE_GOAL_NEXT_ACTION_QUEUE` + text | `8758-9049` | `static_packet_builder_candidate` | no args; output list/dict/text | registry constants | no | no | no | no | yes | Gate B candidate; avoid false readiness wording. |
| `QT_CONTROLLER_FACADE_API` + API text | `9052-9237` | `hub_adjacent_do_not_touch` | no args; output API dict/text | Qt facade registry | no | no | no direct state | Qt facade concept | static but Qt-adjacent | Needs o_1 review; not next. |
| `qt_controller_facade_coverage_*` | `9240-9285` | `hub_adjacent_do_not_touch` | `controller`; output coverage | Qt facade API | no | no | yes, inspects controller object | Qt/controller-adjacent | not pure static | Do not select as low-risk leaf. |
| `QT_UI_COUPLING_CLEANUP_STATUS` + text | `9288-9350` | `hub_adjacent_do_not_touch` | no args; output status/text | Qt cleanup registry | no | no | no direct state | Qt concept | static text but Qt-adjacent | Needs o_1 review. |
| `QT_CONTROLLER_FACADE_EXTRACTION_READINESS_PACKET` and `QT_MAIN_WINDOW_*` | `9353-9670` | `hub_adjacent_do_not_touch` | no args; output readiness/module packet/text | Qt registries and coverage packets | no | no | no direct state | Qt main-window concepts | broad static packets | Not next; Qt extraction semantics. |
| `module_split_readiness_text`, `DECOUPLING_EXTRACTION_GATES`, `decoupling_extraction_gates_text` | `9673-9805` | `broad_contract_packet_builder` | no args; output text | gate registries | no | no | no | no | static text | Needs o_1 review before movement. |

## Top next gate candidates

1. `PointOverlayBudgetPolicy`
   - Category: `policy_object_candidate`.
   - Why: deterministic inputs/outputs, no renderer/Qt/Taichi/file/cache/artifact touch, narrower than `LayerRenderBudgetPolicy`.
   - Suggested gate: fixture parity gate for `decision()` and `text()` with representative records/lod/style cases.

2. `DatashaderSamplingPolicy`
   - Category: `policy_object_candidate`.
   - Why: deterministic budget/sampling decision object with explicit count/lod/scale inputs.
   - Current gate: `DATASHADER_SAMPLING_POLICY_FIXTURE_PARITY_GATE.zh-TW.md` with focused fixtures for record thresholds, lod budgets, scale floor, realtime/offline modes, output keys, and text formatting.

3. `*_MODULE_API` static snapshot/text family, starting with `provider_manifests_module_api_snapshot/text`
   - Category: `static_packet_builder_candidate`.
   - Why: pure registry-to-dict/text construction with no runtime input.
   - Suggested gate: snapshot/contract gate that asserts stable keys and no false readiness wording.

## Risk table

| risk | evidence observed | required gate before extraction | stop condition |
| --- | --- | --- | --- |
| global registry drift risk | Many functions depend on large top-level registries. | Snapshot tests for registry keys and selected values. | Any movement changes registry keys, order-sensitive output, or selected text. |
| packet wording / false readiness risk | Several packet builders contain readiness/extraction/status language. | Wording scan and o_1 review for readiness semantics. | Output implies extraction approval, runtime readiness, UI readiness, or visual parity. |
| metadata schema proximity risk | This zone is mostly docs/contracts, but some names mention renderer data contracts. | Confirm no `render_core.metadata` or metadata sidecar writer dependency. | Candidate touches metadata schema, output metadata fields, or sidecar behavior. |
| output behavior proximity risk | No image/output writes observed in this zone. | Import-boundary checker and artifact audit. | Candidate starts writing files, `state/`, PNG, or runtime JSON. |
| hidden renderer state reference risk | `qt_controller_facade_coverage_*` accepts a `controller` object and inspects attributes. | Exclude controller-accepting functions from low-risk leaf selection. | Candidate requires live controller, renderer, Qt object, or runtime state. |
| duplicate contract source risk | Multiple broad packets compose other packet builders. | Keep broad composed packets in monolith until source-of-truth boundary is clear. | Extraction would duplicate or split contract ownership ambiguously. |
| import-boundary risk | Future helpers could accidentally import monolith or Qt-adjacent modules. | Candidate-specific static import-boundary checker before code movement. | Helper imports `taichi_global_bathymetry`, Qt/VisPy/Taichi, renderer, provider, parser, metadata writer, or artifact writer. |

## Recommendation

Recommended branch: `A`, then optionally `B`.

Next c_3 slice:

`PointOverlayBudgetPolicy fixture parity gate`

Reason:

- It is a true policy object candidate.
- It has deterministic scalar/list/dict inputs and dict/text outputs.
- It does not need renderer, Qt, VisPy, Taichi, files, cache, metadata, output behavior, or artifact writes.
- It is narrower than composed static packet builders and therefore lower blast radius for the next gate.

Alternative if o_1 prefers packet builders:

`provider_manifests_module_api_snapshot/text snapshot contract gate`

This is pure static packet construction, but it carries more contract wording risk than the policy object.

## Not authorized

- Policy extraction.
- Static packet builder extraction.
- Renderer readiness claim.
- Visual parity readiness claim.
- UI readiness claim.
- Performance improvement claim.
- Runtime merge.
- Metadata schema changes.
- Output behavior changes.
- Runtime artifact generation.

## Boundary statement

Docs/evidence-only candidate map. No policy extraction, no packet builder extraction, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim.

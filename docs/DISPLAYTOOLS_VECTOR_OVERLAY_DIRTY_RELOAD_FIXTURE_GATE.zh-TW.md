# Displaytools Vector Overlay Dirty/Reload Fixture Gate

## Scope

本文件是 test/docs-only 的 vector overlay dirty/reload fixture gate。目標是用純 descriptor ledger 釐清 dirty flag、reload request、visibility toggle、provider refresh、overlay rebuild、projection/mask rebuild 之間的狀態轉移。

本輪不修改 production source，不 import controller，不執行 provider/cache reload，不讀 real GeoJSON、Natural Earth、hydrology cache，不修改 projection、flip、mask formula，不執行 renderer、Qt、VisPy、Taichi，也不宣稱 safe-to-extract、bug fixed、visual parity、performance、readiness 或 runtime merge。

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `code_supported` | dirty flags, reload methods, style/LOD invalidation, projection/mask, vector cache anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_verified` | 14k basement comparison for dirty/reload and vector cache family |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_CONTROLLER_REGISTRY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | controller registry seam and decision to gate dirty/reload next |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_PROVIDER_BOUNDARY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | provider/source/cache descriptor boundary |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_MONKEY_PATCH_CRATON_ABLATION_GATE.zh-TW.md` | `product_docs_evidence` | ablation footprint for provider, projection, mask, and controller dependencies |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_COORDINATE_SYNC_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | projection/mask sync descriptors |

## Dirty/Reload State Matrix

Each fixture descriptor must include exactly these fields:

- `overlay_kind`
- `provider_ref_kind`
- `visibility_state`
- `dirty_flag_state`
- `reload_request_state`
- `dirty_reason`
- `reload_reason`
- `expected_rebuild_policy`
- `expected_provider_policy`
- `expected_projection_policy`
- `expected_mask_policy`
- `mutation_scope`
- `fixture_status`
- `forbidden_next_action`

| case | dirty | reload | visibility/provider | expected policy | classification |
| --- | --- | --- | --- | --- | --- |
| clean visible, no reload | false | false | visible + provider present | reuse existing overlay descriptor | `dirty_reload_clean` |
| dirty only | true | false | visible + provider present | rebuild overlay descriptor, no provider refresh | `dirty_flag_dependency_detected` |
| reload only | false | true | visible + provider present | provider refresh descriptor, rebuild after reload | `reload_request_dependency_detected` |
| dirty and reload | true | true | visible + provider present | reload then rebuild descriptor | `reload_request_dependency_detected` |
| hidden provider present | false | false | hidden + provider present | dormant no screen rebuild | `visibility_dependency_detected` |
| hidden reload requested | false | true | hidden + provider present | provider refresh may be requested while dormant | `reload_request_dependency_detected` |
| provider missing dirty | true | false | visible + provider missing | block rebuild until provider descriptor exists | `provider_refresh_dependency_detected` |
| provider present overlay disabled | false | false | disabled + provider present | dormant clean descriptor | `visibility_dependency_detected` |
| cache hit no dirty | false | false | cache-hit descriptor | reuse cached overlay descriptor | `dirty_reload_clean` |
| cache miss reload requested | false | true | cache-miss descriptor | provider refresh then rebuild descriptor | `provider_refresh_dependency_detected` |
| style/LOD changed | true | false | visible + provider present | rebuild with style/LOD descriptor | `dirty_flag_dependency_detected` |
| projection frame changed | true | false | visible + provider present | projection rebuild descriptor | `projection_rebuild_dependency_detected` |
| mask policy changed | true | false | visible + provider present | mask rebuild descriptor | `mask_rebuild_dependency_detected` |
| malformed dirty/reload payload | malformed | malformed | malformed | block rebuild descriptor | `malformed_descriptor` |

## Fixed Classifications

| classification | meaning |
| --- | --- |
| `dirty_reload_clean` | no descriptor-level mutation is expected |
| `dirty_flag_dependency_detected` | dirty flag drives a rebuild descriptor |
| `reload_request_dependency_detected` | reload request drives provider refresh/rebuild descriptor |
| `visibility_dependency_detected` | layer visibility or disabled state gates rebuild behavior |
| `provider_refresh_dependency_detected` | provider/cache state drives refresh/rebuild descriptor |
| `projection_rebuild_dependency_detected` | projection frame change drives rebuild descriptor |
| `mask_rebuild_dependency_detected` | mask policy change drives rebuild descriptor |
| `blocked_runtime_only` | runtime would be required to prove behavior |
| `malformed_descriptor` | malformed input remains diagnostic only |

## Mutation Seam Assessment

| seam | assessment | static evidence |
| --- | --- | --- |
| dirty flag | controller-global with overlay-local and provider-local reasons | current lines around 13384-13448 and 14840-14849 set hydrology/boundary/overlay dirty flags |
| reload request | request descriptor, not completed provider reload | reload methods assign overlay from loader and then set dirty flags, but this gate does not execute them |
| visibility toggle | can make overlay dormant while provider remains present | layer visibility is checked before render consumer use |
| provider refresh | provider/cache descriptor is separate from projection/mask formula | provider boundary gate already pins source/cache descriptors |
| overlay rebuild | descriptor-level rebuild only | render path uses dirty flags/cache/view key, but runtime rebuild is not executed here |
| projection frame change | rebuild descriptor only | flip/yaw/pitch/zoom remain formula boundaries |
| mask policy change | rebuild descriptor only | `globe_mask` clipping remains formula/runtime boundary |

## Decision Output

| question | answer |
| --- | --- |
| dirty/reload can be fixture-gated? | yes, as descriptor ledger only |
| dirty is overlay-local, provider-local, or controller-global? | controller-global with overlay-local and provider-local reasons |
| reload request equals provider reload completed? | no |
| hidden layer still allows provider reload? | descriptor says yes, but it remains a request/refresh descriptor only |
| provider present but overlay disabled is clean, dormant, or blocked? | dormant |
| next step can enter import-boundary checker? | yes for checker gate design only, not extraction |
| need narrower monkey patch gate? | no, current ledger is enough for checker preimplementation |

## Test Shape

The focused test module is `tests/test_displaytools_vector_overlay_dirty_reload.py`.

The test shape is `pure_dict_list_scalar_no_controller_provider_runtime`:

- It uses dict/list/scalar descriptors and no production imports.
- It does not import `taichi_global_bathymetry.py`.
- It does not import or instantiate controller, renderer, Qt, VisPy, Taichi, pandas, datashader, providers, SQL/WebSocket, or AIS live modules.
- It does not read real GeoJSON, Natural Earth, hydrology cache, boundary cache, provider files, PNG, runtime JSON, or state artifacts.
- It does not execute provider/cache reload, renderer, projection, mask, alpha, postprocess, metadata writer, or artifact writer paths.

## Recommended Next Gate

Recommended next gate: `vector_overlay_import_boundary_checker`.

Reason:

- Coordinate sync, ablation, provider boundary, controller registry, and dirty/reload ledgers are now represented as descriptor gates.
- This supports a tooling/docs-only import-boundary checker gate for a future vector overlay helper candidate.
- It still does not authorize source movement, helper creation, runtime execution, visual parity, bug fix, or extraction.

Fallback if o_1 wants another diagnostic slice: `projection_mask_ablation_followup_gate`.

If runtime evidence becomes required: `stop_for_o1_review`.

## Do-not-fix-yet Register

Do not modify these areas in this slice:

- `taichi_global_bathymetry.py`
- controller dirty flags or reload methods
- `_load_hydrology_overlays`
- `_load_boundary_overlays`
- provider/source/cache code
- vector overlay cache behavior
- `GeoVectorLineOverlay`
- projection, flip, mask, or depth formulas
- renderer/Qt/VisPy/Taichi runtime behavior
- SQL/MySQL/WebSocket/AIS live access
- metadata sidecar writer and artifact writer paths

## Boundary Statement

Test/docs-only vector overlay dirty/reload fixture gate. No production source change, no controller/provider/cache runtime, no real GeoJSON/cache read, no production runtime patch, no runtime execution, no source movement, no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_dirty_reload_fixture_gate_ready_for_o1_review`

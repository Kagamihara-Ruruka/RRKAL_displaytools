# Displaytools Vector Overlay Monkey-Patch Craton Ablation Gate

## Scope

本文件是 test/docs-only diagnostic gate。目標是用 test-local monkey patch / stub / sentinel 設計，描述 borders / hydrology vector overlay 被暫時遮斷、替換或追蹤時會暴露哪些依賴足跡。

本輪不修改 production source，不 patch production runtime，不讀 real GeoJSON、Natural Earth、cache files，不執行 renderer、Qt、VisPy、Taichi，不修改 `GeoVectorLineOverlay`，不改 projection、flip、mask formula，也不宣稱國界線、水系線、visual parity、performance、runtime merge、safe to extract 或 bug fix。

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `code_supported` | vector overlay, loader, projection, flip, and mask anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_verified` | vector overlay family existed in 14k basement |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_COORDINATE_SYNC_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | previous synthetic vector sync descriptors and unresolved sync faults |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_FIXTURE_DESIGN_GATE.zh-TW.md` | `product_docs_evidence` | coordinate frame descriptor precedent |
| `o1_monkey_patch_craton_ablation_methodology.zh-TW.md` | `lab_methodology_evidence` | monkey-patch craton ablation terminology, modes, rollback discipline, and stop lines |

Lab methodology is summarized only. It is not treated as product runtime authorization.

## Terminology

| term | product-gate meaning |
| --- | --- |
| `Monkey-Patch` | `猴子打劫` |
| `Monkey-Patch Craton Ablation Gate` | `猴子打劫克拉通消融法` |
| `ablation` | 暫時遮斷 / 替換 / 追蹤，不等於刪除 source |

This gate uses the terminology as diagnostic language only. It does not introduce permanent monkey patching into product architecture.

## Ablation Modes

| mode | diagnostic behavior | allowed in this gate | forbidden interpretation |
| --- | --- | --- | --- |
| `null_mode` | vector overlay returns an empty descriptor or empty draw result | test-local fake only | not proof that runtime can omit the layer |
| `tripwire_mode` | a touched dependency raises a diagnostic sentinel | test-local fake only | not a product exception path |
| `trace_mode` | record caller / frame / flip / mask usage without changing descriptor output | test-local recorder only | not runtime tracing instrumentation |
| `substitute_mode` | replace real provider/cache with synthetic line descriptors | test-local synthetic values only | not a replacement renderer or provider |

## Patch Map

Every patch map entry must include exactly these fields:

- `patch_target`
- `craton`
- `patch_mode`
- `patch_scope`
- `rollback_method`
- `observed_callers`
- `dependency_footprint`
- `claim_limit`
- `forbidden_next_action`

| patch_target | craton | patch_mode | patch_scope | rollback_method | observed_callers | dependency_footprint | claim_limit | forbidden_next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `GeoVectorLineOverlay` | shared vector overlay | `null_mode` | test-local descriptor only | context exits without persistent object mutation | controller overlay registry | optional overlay dependency | dependency footprint only; no bug fix or extraction safety proven | do not patch production runtime or modify `GeoVectorLineOverlay` |
| borders descriptor path | borders vector overlay | `tripwire_mode` | test-local diagnostic sentinel | sentinel exists only inside fake object method | boundary overlay loader, controller overlay registry | controller dependency, provider/cache dependency | hidden caller detection only; no runtime behavior validated | do not read real boundary cache or provider |
| hydrology descriptor path | hydrology vector overlay | `tripwire_mode` | test-local diagnostic sentinel | sentinel exists only inside fake object method | hydrology overlay loader, controller overlay registry | controller dependency, provider/cache dependency | hidden caller detection only; no runtime behavior validated | do not read real hydrology cache or provider |
| vector mask clipping path | mask/screen RGBA boundary | `trace_mode` | test-local recorder | recorder discarded after test | `GeoVectorLineOverlay.render`, `mask_overlay_to_globe` label | mask dependency detected | mask usage trace only; no pixel equivalence proven | do not modify `mask_overlay_to_globe` or generate PNG |
| vector flip policy path | projection/flip policy | `trace_mode` | test-local recorder | recorder discarded after test | `GeoVectorLineOverlay.render`, dynamic projection comparison label | projection dependency detected | flip usage trace only; no projection formula change | do not modify projection or flip formula |
| dynamic point sync comparison path | dynamic projection peer | `substitute_mode` | test-local synthetic line descriptor | synthetic substitute is local value only | coordinate sync fixture descriptor | optional overlay dependency, projection dependency | descriptor comparison only; no live AIS or renderer proof | do not connect SQL/WebSocket/AIS live |

## Vector Overlay Targets

This gate designs targets only. It does not import or patch product objects.

| target | diagnostic role | static evidence | status |
| --- | --- | --- | --- |
| `GeoVectorLineOverlay` | shared borders/hydrology vector overlay class | current `taichi_global_bathymetry.py:3888`; vector render path around 3909-4041 | diagnostic target only |
| borders descriptor path | boundary overlay construction and registry footprint | current `_load_boundary_overlays` around 12895 and controller registry around 11225 | provider/cache dependency candidate |
| hydrology descriptor path | hydrology overlay construction and registry footprint | current `_load_hydrology_overlays` around 12874 and controller registry around 11224 | provider/cache dependency candidate |
| vector mask clipping path | screen RGBA clipping dependency | current `mask_overlay_to_globe` around 2068-2072; vector render returns masked overlay around 4041 | mask dependency candidate |
| vector flip policy path | projection/flip dependency | current vector render receives `flip_longitude` and `flip_latitude` around 3914-3915 | projection dependency candidate |
| dynamic point sync comparison path | peer frame comparison | current AIS/aircraft projection receives flip flags around 1948-2028 | comparison target only |

## Diagnostic Outcomes

| outcome | meaning | next-gate implication |
| --- | --- | --- |
| `no_dependency_observed` | descriptor does not show a dependency edge | no extraction safety claim |
| `optional_overlay_dependency` | overlay can be represented as optional in descriptor design | candidate for narrower fixture/checker only |
| `controller_dependency_detected` | controller registry/construction is in the footprint | needs controller boundary review |
| `projection_dependency_detected` | flip/projection frame is in the footprint | needs projection or coordinate follow-up gate |
| `mask_dependency_detected` | globe mask/screen clipping is in the footprint | needs projection/mask ablation follow-up if dominant |
| `provider_cache_dependency_detected` | source/cache/provider loading is in the footprint | needs provider boundary fixture before import checker |
| `blocked_runtime_only` | only runtime execution could prove the dependency | stop for o_1 review |

## Ablation Cases

| case_id | patch_mode | target_surface | diagnostic outcome |
| --- | --- | --- | --- |
| `borders_null_ablation` | `null_mode` | borders | `optional_overlay_dependency` |
| `hydrology_null_ablation` | `null_mode` | hydrology | `optional_overlay_dependency` |
| `shared_overlay_tripwire_provider_cache` | `tripwire_mode` | shared vector overlay | `provider_cache_dependency_detected` |
| `substitute_taiwan_short_segment` | `substitute_mode` | borders | `projection_dependency_detected` |
| `substitute_hydrology_river_segment` | `substitute_mode` | hydrology | `projection_dependency_detected` |
| `malformed_substitute_descriptor` | `substitute_mode` | shared vector overlay | `no_dependency_observed` |
| `trace_projection_dependency_edge` | `trace_mode` | vector flip policy path | `projection_dependency_detected` |
| `trace_globe_mask_dependency_edge` | `trace_mode` | vector mask clipping path | `mask_dependency_detected` |
| `trace_controller_loading_edge` | `trace_mode` | controller overlay registry | `controller_dependency_detected` |
| `blocked_composition_postprocess_edge` | `trace_mode` | postprocess/composition frame | `blocked_runtime_only` |

## Dependency Footprint Summary

| surface | diagnostic classification | interpretation |
| --- | --- | --- |
| controller construction / overlay registry | `controller_dependency_detected` | vector overlay is not only a drawing primitive; registry/loading path must be mapped before movement |
| provider/source/cache loading | `provider_cache_dependency_detected` | real data-source boundary is heavier than synthetic coordinate descriptors |
| vector projection / flip policy | `projection_dependency_detected` | coordinate sync remains tied to flip/projection labels |
| globe mask clipping | `mask_dependency_detected` | mask/screen RGBA clipping is a separate dependency from provider loading |
| dynamic point projection sync | `projection_dependency_detected` | descriptor comparison is useful, but not runtime proof |
| render-plan/composition/postprocess proximity | `blocked_runtime_only` | alpha/apply/composition remains outside this gate |
| metadata/artifact writer proximity | `no_dependency_observed` | no writer dependency is introduced by this test-local design |

## Rollback Discipline

The focused test module is `tests/test_displaytools_vector_overlay_craton_ablation.py`.

Rollback rules:

- Patch scope is test-local only.
- Patch substitutes are fake classes, fake functions, local descriptors, or local sentinel exceptions.
- Rollback method must be explicitly recorded in each patch map entry.
- Global persistent patch is not allowed.
- Import-time patch is not allowed.
- Decorator-hidden patch is not allowed.
- Production runtime patch is not allowed.

The test file may define `FakeVectorOverlay`, `FakeTraceRecorder`, and `DiagnosticSentinel`. These are local harness objects only.

## Test Shape

The test shape is pure Python dict/list/scalar plus test-local fake class/function.

The tests do not:

- import `taichi_global_bathymetry.py`
- import Taichi, Qt, VisPy, pandas, datashader, GeoJSON provider modules, SQL/MySQL/WebSocket, or AIS live modules
- read Natural Earth, GeoJSON, provider cache, hydrology, or boundary files
- instantiate production `GeoVectorLineOverlay`
- patch production runtime or user-facing runtime
- call renderer, projection, mask, alpha, postprocess, metadata writer, or artifact writer paths

## Recommended Next Gate

Recommended next gate: `vector_overlay_provider_boundary_fixture_gate`.

Reason:

- The diagnostic patch map intentionally marks provider/source/cache loading as part of the vector overlay footprint.
- That footprint is heavier than a simple import-boundary checker target.
- A provider boundary fixture can separate synthetic coordinate descriptors from real Natural Earth/cache/provider loading before any checker or movement gate.

Alternative if o_1 accepts the footprint as narrow enough: `vector_overlay_import_boundary_checker`.

If projection/mask dependency becomes the dominant risk: `projection_mask_ablation_followup_gate`.

If only runtime can prove a branch: `stop_for_o1_review`.

## Do-not-fix-yet Register

Do not modify these areas in this slice:

- production `GeoVectorLineOverlay`
- `_load_hydrology_overlays`
- `_load_boundary_overlays`
- provider/source/cache loading
- `project_ais_to_screen`
- `project_aircraft_to_screen`
- vector projection, flip, line simplification, depth-mask, or mask clipping formulas
- `mask_overlay_to_globe`
- Taichi shader coordinate formulas
- renderer/controller/Qt/VisPy/Taichi runtime behavior
- alpha helpers and `build_layer_render_plan_apply_path`
- metadata sidecar writer and artifact writer paths

## Boundary Statement

Test/docs-only vector overlay monkey-patch craton ablation diagnostic gate. No production source change, no production runtime patch, no runtime execution, no real GeoJSON/cache read, no source movement, no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_monkey_patch_craton_ablation_gate_ready_for_o1_review`

# Displaytools Vector Overlay Provider Boundary Fixture Gate

## Scope

本文件是 test/docs-only 的 vector overlay provider boundary fixture gate。目標是把 borders / hydrology 的 provider/source/cache 邊界，和 vector projection、flip、mask、renderer consumer 邊界分開描述。

本輪不修改 production source，不建立 helper module，不執行 provider/loader/cache，不讀 real GeoJSON、Natural Earth、hydrology、boundary cache，不 instantiate `GeoVectorLineOverlay`，不執行 renderer、Qt、VisPy、Taichi，也不宣稱 provider、vector overlay、國界線或水系線已可抽取或已修復。

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `code_supported` | provider specs, Natural Earth cache references, hydrology/boundary loaders, controller registry, vector consumer anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_verified` | 14k basement comparison for vector provider/cache family |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_COORDINATE_SYNC_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | vector coordinate sync descriptor boundary |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_MONKEY_PATCH_CRATON_ABLATION_GATE.zh-TW.md` | `product_docs_evidence` | provider/cache dependency footprint from test-local ablation map |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_FIXTURE_DESIGN_GATE.zh-TW.md` | `product_docs_evidence` | no-runtime descriptor test shape precedent |
| `o1_monkey_patch_craton_ablation_methodology.zh-TW.md` | `lab_methodology_evidence` | rollback and diagnostic-only claim limits |

Lab-only methodology is summarized only. It does not authorize product runtime behavior.

## Provider Boundary

The provider boundary is represented as descriptor-only data:

- `borders_provider`
- `hydrology_provider`
- `natural_earth_cache_reference`
- `hydrology_cache_reference`
- `synthetic_provider`
- `malformed_provider`
- `empty_provider`

Static source anchors:

- current `taichi_global_bathymetry.py:3640-3682` includes vector source/cache and Natural Earth layer references.
- current `taichi_global_bathymetry.py:4257-4301` defines boundary and hydrology specs with Natural Earth layer names.
- current `taichi_global_bathymetry.py:12874-12895` loads hydrology and boundary overlays into controller-owned registries.
- `d90b645:taichi_global_bathymetry.py:2518-2560` and `2843-2887` show the same provider/cache family in the 14k basement.

## Consumer Boundary

| consumer | classification | boundary |
| --- | --- | --- |
| vector overlay descriptor consumer | `projection_consumer_dependency_detected` | consumes line descriptors only; does not own provider execution |
| controller overlay registry consumer | `controller_registry_dependency_detected` | controller owns overlay dictionaries and dirty flags; not provider-owned |
| projection/render path consumer | `projection_consumer_dependency_detected` | consumes geometry for screen projection; not source/cache owner |
| mask/screen RGBA consumer | `projection_consumer_dependency_detected` | consumes rendered RGBA and globe mask; not source/cache owner |

## Provider Output Contract

Each provider descriptor must include exactly these fields:

- `provider_kind`
- `source_kind`
- `cache_policy`
- `loader_owner`
- `output_shape`
- `coordinate_payload_kind`
- `geometry_payload_kind`
- `failure_mode`
- `consumer_contract`
- `fixture_status`
- `forbidden_next_action`

| provider_kind | source_kind | cache_policy | output_shape | fixture_status | forbidden_next_action |
| --- | --- | --- | --- | --- | --- |
| `borders_provider` | `synthetic_provider` | `no_cache` | synthetic borders line provider | `provider_boundary_pinned` | do not execute provider, loader, cache, or renderer |
| `hydrology_provider` | `synthetic_provider` | `no_cache` | synthetic hydrology line provider | `provider_boundary_pinned` | do not execute provider, loader, cache, or renderer |
| `natural_earth_cache_reference` | `cache_descriptor_only` | `cache_hit_descriptor_only` | cache-hit descriptor only | `provider_cache_dependency_detected` | do not read Natural Earth cache |
| `hydrology_cache_reference` | `cache_descriptor_only` | `cache_miss_descriptor_only` | cache-miss descriptor only | `provider_cache_dependency_detected` | do not read hydrology cache |
| `synthetic_provider` | `synthetic_provider` | `no_cache` | provider output compared against vector overlay sync descriptor | `provider_boundary_pinned` | do not instantiate `GeoVectorLineOverlay` |
| `malformed_provider` | `synthetic_provider` | `no_cache` | malformed provider output | `provider_boundary_unresolved_static_only` | do not patch parser/provider behavior |
| `empty_provider` | `synthetic_provider` | `no_cache` | empty provider output | `provider_boundary_pinned` | do not treat empty output as renderer success |

## Synthetic Provider Cases

| case_id | provider_kind | output_shape | classification |
| --- | --- | --- | --- |
| `synthetic_borders_line_provider` | `borders_provider` | synthetic borders line provider | `provider_boundary_pinned` |
| `synthetic_hydrology_line_provider` | `hydrology_provider` | synthetic hydrology line provider | `provider_boundary_pinned` |
| `empty_borders_provider_output` | `empty_provider` | empty borders provider output | `provider_boundary_pinned` |
| `empty_hydrology_provider_output` | `empty_provider` | empty hydrology provider output | `provider_boundary_pinned` |
| `malformed_coordinate_payload` | `malformed_provider` | malformed coordinate payload | `provider_boundary_unresolved_static_only` |
| `malformed_geometry_payload` | `malformed_provider` | malformed geometry payload | `provider_boundary_unresolved_static_only` |
| `cache_hit_descriptor_only` | `natural_earth_cache_reference` | cache-hit descriptor only | `provider_cache_dependency_detected` |
| `cache_miss_descriptor_only` | `hydrology_cache_reference` | cache-miss descriptor only | `provider_cache_dependency_detected` |
| `provider_unavailable_descriptor` | `borders_provider` | provider unavailable descriptor | `provider_boundary_unresolved_static_only` |
| `provider_output_compared_against_vector_overlay_sync_descriptor` | `synthetic_provider` | provider output compared against vector overlay sync descriptor | `projection_consumer_dependency_detected` |

## Boundary Classification

| classification | meaning | allowed conclusion |
| --- | --- | --- |
| `provider_boundary_pinned` | provider output shape can be described by synthetic descriptor | fixture candidate only |
| `provider_boundary_unresolved_static_only` | malformed/unavailable behavior cannot be proven without implementation/runtime evidence | unresolved diagnostic |
| `provider_cache_dependency_detected` | cache references are part of source boundary | provider/cache gate needed before checker |
| `controller_registry_dependency_detected` | controller overlay registry is in the footprint | controller registry seam should be gated next |
| `projection_consumer_dependency_detected` | projection/render consumer depends on provider output shape | projection/mask boundary remains separate |
| `blocked_runtime_only` | branch needs runtime to prove | stop for o_1 review |

## Decision Output

| question | answer | reason |
| --- | --- | --- |
| provider/source/cache can become fixture/checker candidate? | fixture yes, checker not yet | provider descriptors are pinnable, but controller registry remains in the static footprint |
| need controller registry seam first? | yes | `_load_hydrology_overlays`, `_load_boundary_overlays`, overlay dictionaries, and dirty flags stay controller-owned |
| need provider-specific monkey patch first? | not this round | current descriptor gate is enough to identify controller seam as the next blocker |
| still docs-only mapping only? | no | focused provider fixture can be represented with pure descriptors, but no extraction/checker authorization follows |

## Test Shape

The focused test module is `tests/test_displaytools_vector_overlay_provider_boundary.py`.

The test shape is `pure_dict_list_scalar_no_provider_execution_no_real_cache`:

- It uses fake provider descriptors, fake provider output packets, fake cache descriptors, and fake failure descriptors.
- It does not import `taichi_global_bathymetry.py`.
- It does not import Taichi, Qt, VisPy, pandas, datashader, GeoJSON provider modules, SQL/MySQL/WebSocket, or AIS live modules.
- It does not read Natural Earth, GeoJSON, hydrology, boundary, provider cache, or any real vector file.
- It does not instantiate `GeoVectorLineOverlay`.
- It does not patch production objects.
- It does not execute provider/loader/cache, renderer, projection, mask, alpha, postprocess, metadata writer, or artifact writer paths.

## Recommended Next Gate

Recommended next gate: `vector_overlay_controller_registry_fixture_gate`.

Reason:

- Provider output shapes can be pinned as descriptors.
- Provider/cache references remain in the footprint.
- Controller registry and dirty flags are the next static seam before an import-boundary checker can be useful.

Alternative if o_1 chooses provider/cache first: `vector_overlay_provider_monkey_patch_ablation_gate`.

Alternative if projection/mask remains mixed with provider output: `projection_mask_ablation_followup_gate`.

If a branch requires renderer/runtime evidence: `stop_for_o1_review`.

## Do-not-fix-yet Register

Do not modify these areas in this slice:

- production provider/loader/cache code
- `_load_hydrology_overlays`
- `_load_single_hydrology_overlay`
- `_load_boundary_overlays`
- `_load_single_boundary_overlay`
- `GeoVectorLineOverlay`
- Natural Earth, hydrology, boundary, provider, or cache files
- projection, flip, line simplification, mask, or depth formulas
- controller/renderer/Qt/VisPy/Taichi runtime behavior
- SQL/MySQL/WebSocket/AIS live access
- metadata sidecar writer and artifact writer paths

## Boundary Statement

Test/docs-only vector overlay provider boundary fixture gate. No production source change, no provider/cache execution, no real GeoJSON/cache read, no production runtime patch, no runtime execution, no source movement, no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_provider_boundary_fixture_gate_ready_for_o1_review`

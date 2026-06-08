# Displaytools Vector Overlay Controller Registry Fixture Gate

## Scope

本文件是 test/docs-only 的 vector overlay controller registry fixture gate。目標是把 borders / hydrology vector overlay 在 controller 中的 registry、dirty flag、reload request、provider descriptor reference、projection consumer reference、mask consumer reference 之間的 seam 先釘住。

本輪不修改 production source，不建立 helper module，不 import 或 instantiate controller，不執行 provider/cache/renderer，不讀 real GeoJSON、Natural Earth、hydrology、boundary cache，不修改 `GeoVectorLineOverlay`、loader、projection、flip、mask formula，也不宣稱 controller seam、vector overlay、國界線或水系線已可抽取或已修復。

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `code_supported` | controller overlay registries, dirty flags, reload methods, mask/projection consumer anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_verified` | 14k basement comparison for the same registry/dirty/reload family |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_PROVIDER_BOUNDARY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | provider boundary decision that controller registry seam is next |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_MONKEY_PATCH_CRATON_ABLATION_GATE.zh-TW.md` | `product_docs_evidence` | ablation footprint showing controller/provider/projection/mask edges |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_COORDINATE_SYNC_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | vector coordinate sync descriptor boundary |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_FIXTURE_DESIGN_GATE.zh-TW.md` | `product_docs_evidence` | no-runtime descriptor test shape precedent |

## Registry Surfaces

The registry seam is represented as descriptor-only data:

- `boundary_overlays`
- `hydrology_overlays`
- `overlay_registry`
- `layer_state_registry`
- `dirty_flag_registry`
- `reload_request`
- `provider_descriptor_ref`
- `projection_consumer_ref`
- `mask_consumer_ref`

Static source anchors:

- current `taichi_global_bathymetry.py:11224-11225` initializes `hydrology_overlays` and `boundary_overlays`.
- current `taichi_global_bathymetry.py:12874-12915` loads hydrology and boundary overlays into controller-owned registries.
- current `taichi_global_bathymetry.py:13384-13410` reloads hydrology and sets `hydrology_dirty` / `overlay_dirty`.
- current `taichi_global_bathymetry.py:14840-14849` reloads boundary and sets `boundary_dirty` / `overlay_dirty`.
- current `taichi_global_bathymetry.py:13033-13168` consumes registry entries with view keys, flip flags, and `globe_mask`.
- `d90b645:taichi_global_bathymetry.py:10033-10034`, `11015-11056`, `11460-11693` show the same family in the 14k basement.

## Controller Ownership Fields

Each registry descriptor must include exactly these fields:

- `registry_name`
- `owner_surface`
- `overlay_kind`
- `provider_ref_kind`
- `dirty_flag_kind`
- `reload_trigger_kind`
- `visibility_policy`
- `consumer_refs`
- `mutation_scope`
- `fixture_status`
- `forbidden_next_action`

| registry_name | owner_surface | overlay_kind | provider_ref_kind | dirty_flag_kind | reload_trigger_kind | visibility_policy | consumer_refs | fixture_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `boundary_overlays` | controller registry descriptor | borders | provider descriptor ref | `boundary_dirty` | none | layer visible gate | projection + mask refs | `controller_registry_pinned` |
| `hydrology_overlays` | controller registry descriptor | hydrology | provider descriptor ref | `hydrology_dirty` | none | layer visible gate | projection + mask refs | `controller_registry_pinned` |
| `overlay_registry` | controller registry descriptor | shared vector overlay | provider descriptor ref | `overlay_dirty` | none | layer visible gate | projection + mask refs | `controller_registry_pinned` |
| `layer_state_registry` | controller registry descriptor | shared vector overlay | provider descriptor ref | `overlay_dirty` | none | layer state visibility | projection + mask refs | `controller_registry_pinned` |
| `dirty_flag_registry` | controller registry descriptor | shared vector overlay | provider descriptor ref | `overlay_dirty` | none | layer visible gate | projection + mask refs | `dirty_reload_dependency_detected` |
| `reload_request` | controller registry descriptor | shared vector overlay | provider descriptor ref | `overlay_dirty` | reload hydrology/boundary | layer visible gate | projection + mask refs | `dirty_reload_dependency_detected` |
| `provider_descriptor_ref` | controller registry descriptor | shared vector overlay | provider boundary descriptor | `overlay_dirty` | none | layer visible gate | projection + mask refs | `provider_ref_dependency_detected` |
| `projection_consumer_ref` | controller registry descriptor | shared vector overlay | provider descriptor ref | `overlay_dirty` | none | layer visible gate | projection ref | `projection_consumer_dependency_detected` |
| `mask_consumer_ref` | controller registry descriptor | shared vector overlay | provider descriptor ref | `overlay_dirty` | none | layer visible gate | mask ref | `mask_consumer_dependency_detected` |

## Synthetic Registry Cases

| case_id | registry_name | classification |
| --- | --- | --- |
| `borders_overlay_registered` | `boundary_overlays` | `controller_registry_pinned` |
| `hydrology_overlay_registered` | `hydrology_overlays` | `controller_registry_pinned` |
| `both_overlays_registered` | `overlay_registry` | `controller_registry_pinned` |
| `empty_registry` | `overlay_registry` | `controller_registry_unresolved_static_only` |
| `dirty_flag_set` | `dirty_flag_registry` | `dirty_reload_dependency_detected` |
| `dirty_flag_clear` | `dirty_flag_registry` | `dirty_reload_dependency_detected` |
| `reload_requested` | `reload_request` | `dirty_reload_dependency_detected` |
| `provider_descriptor_missing` | `provider_descriptor_ref` | `provider_ref_dependency_detected` |
| `projection_consumer_missing` | `projection_consumer_ref` | `projection_consumer_dependency_detected` |
| `mask_consumer_missing` | `mask_consumer_ref` | `mask_consumer_dependency_detected` |
| `layer_hidden_but_provider_present` | `layer_state_registry` | `controller_registry_pinned` |
| `provider_present_but_overlay_disabled` | `layer_state_registry` | `provider_ref_dependency_detected` |

## Seam Classification

| classification | meaning | allowed conclusion |
| --- | --- | --- |
| `controller_registry_pinned` | registry shape can be described by synthetic descriptor | fixture candidate only |
| `controller_registry_unresolved_static_only` | empty/ambiguous registry behavior cannot be proven without runtime evidence | unresolved diagnostic |
| `provider_ref_dependency_detected` | provider descriptor reference is in the registry footprint | provider/controller bridge remains coupled |
| `projection_consumer_dependency_detected` | projection/render consumer is in the registry footprint | projection/mask remains separate follow-up |
| `mask_consumer_dependency_detected` | `globe_mask`/screen RGBA consumer is in the footprint | mask boundary remains separate follow-up |
| `dirty_reload_dependency_detected` | dirty/reload flags dominate mutation behavior | dirty/reload fixture gate is next |
| `blocked_runtime_only` | branch needs runtime to prove | stop for o_1 review |

## Decision Output

| question | answer | reason |
| --- | --- | --- |
| controller registry seam can be fixture/checker? | fixture yes, checker not yet | registry descriptors are pinnable, but dirty/reload still dominates mutation behavior |
| provider boundary can be deferred? | no | provider ref remains inside registry descriptors |
| need controller-registry monkey patch? | no for this slice | descriptor gate already exposes dirty/reload as the next blocker |
| can enter `vector_overlay_import_boundary_checker`? | no | dirty/reload and provider/controller bridge need narrower gates first |
| need projection/mask ablation follow-up? | not first | projection/mask refs are present, but dirty/reload is the next narrower seam |

## Test Shape

The focused test module is `tests/test_displaytools_vector_overlay_controller_registry.py`.

The test shape is `pure_dict_list_scalar_no_controller_import_no_runtime`:

- It uses fake registry descriptors, fake overlay registry packets, fake dirty flag packets, fake reload request packets, and fake missing dependency packets.
- It does not import `taichi_global_bathymetry.py`.
- It does not import Taichi, Qt, VisPy, pandas, datashader, provider/cache modules, SQL/MySQL/WebSocket, or AIS live modules.
- It does not instantiate controller, renderer, or `GeoVectorLineOverlay`.
- It does not patch production objects.
- It does not read real files.
- It does not execute provider/loader/cache, renderer, projection, mask, alpha, postprocess, metadata writer, or artifact writer paths.

## Recommended Next Gate

Recommended next gate: `vector_overlay_dirty_reload_fixture_gate`.

Reason:

- Registry shape is fixtureable.
- Provider ref, projection ref, and mask ref can be separated as descriptor fields.
- Dirty flags and reload requests remain the dominant mutation seam.

Alternative if o_1 wants provider/controller coupling first: `vector_overlay_provider_controller_bridge_gate`.

Alternative if projection/mask dominates review concern: `projection_mask_ablation_followup_gate`.

If reversible遮斷 is needed again: `vector_overlay_controller_registry_monkey_patch_ablation_gate`.

If a branch requires renderer/runtime evidence: `stop_for_o1_review`.

## Do-not-fix-yet Register

Do not modify these areas in this slice:

- production controller registry fields
- `_load_hydrology_overlays`
- `_load_single_hydrology_overlay`
- `_load_boundary_overlays`
- `_load_single_boundary_overlay`
- `reload_hydrology_layer`
- `reload_boundary_layer`
- `GeoVectorLineOverlay`
- provider/source/cache loading
- projection, flip, mask, or depth formulas
- controller/renderer/Qt/VisPy/Taichi runtime behavior
- SQL/MySQL/WebSocket/AIS live access
- metadata sidecar writer and artifact writer paths

## Boundary Statement

Test/docs-only vector overlay controller registry fixture gate. No production source change, no controller/provider/cache execution, no real GeoJSON/cache read, no production runtime patch, no runtime execution, no source movement, no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_controller_registry_fixture_gate_ready_for_o1_review`

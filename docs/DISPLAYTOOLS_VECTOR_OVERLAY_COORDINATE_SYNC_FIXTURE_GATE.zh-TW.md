# Displaytools Vector Overlay Coordinate Sync Fixture Gate

## Scope

本文件是 test/docs-only 的 vector overlay coordinate sync fixture gate。目標是用 synthetic line descriptors 釘住 borders / hydrology 向量圖層與 raw lon/lat、dynamic point projection、mask/screen RGBA frame 之間的同步判準。

本輪不修正國界線或水系線，不讀 real GeoJSON、Natural Earth、cache files，不執行 renderer、Qt、VisPy、Taichi，不修改 `GeoVectorLineOverlay`，不改 projection、flip、mask formula，也不產生 PNG/runtime JSON/state artifact。

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `code_supported` | vector overlay, dynamic point projection, and mask path anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_verified` | 14k basement comparison for the same vector overlay family |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_OWNERSHIP_DIAGNOSTIC_GATE.zh-TW.md` | `product_docs_evidence` | coordinate ownership matrix and active vector sync fault |
| `docs/DISPLAYTOOLS_HISTORICAL_VIEW_CONE_FIRST_CONTINENT_DECISION_GATE.zh-TW.md` | `product_docs_evidence` | vector overlay sync as ranked follow-up gate |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_FIXTURE_DESIGN_GATE.zh-TW.md` | `product_docs_evidence` | test-local descriptor approach and no-safe-import-target precedent |

## Vector Overlay Frame Contract

Each vector overlay descriptor must include exactly these fields:

- `overlay_kind`: `borders` or `hydrology`
- `source_shape`: `synthetic line`, `polyline`, `empty`, or `malformed`
- `input_frame`: raw lon/lat or declared lon/lat
- `projection_frame`: dynamic projection frame, vector-specific projection, or unresolved
- `flip_policy`: uses `flip_longitude`, `flip_latitude`, both, none, or unresolved
- `mask_policy`: clipped by globe mask, no mask, or unresolved
- `sync_expectation`: should align with dynamic points, terrain sample, raw grid, or unresolved
- `fixture_status`: `pinned`, `unresolved_static_only`, or `blocked_hot_path`
- `forbidden_next_action`

| overlay_kind | source_shape | input_frame | projection_frame | flip_policy | mask_policy | sync_expectation | fixture_status | forbidden_next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `borders` | `synthetic line` | declared lon/lat | vector-specific projection | both | clipped by globe mask | should align with dynamic points | `pinned` | do not modify `GeoVectorLineOverlay` or projection formula |
| `borders` | `polyline` | declared lon/lat | vector-specific projection | both | clipped by globe mask | should align with raw grid | `unresolved_static_only` | do not claim grid/vector sync without runtime parity |
| `hydrology` | `synthetic line` | declared lon/lat | vector-specific projection | both | clipped by globe mask | should align with dynamic points | `pinned` | do not read real hydrology cache or provider |
| `hydrology` | `empty` | declared lon/lat | unresolved | unresolved | unresolved | unresolved | `unresolved_static_only` | do not treat empty input as renderer success |
| `borders` | `malformed` | declared lon/lat | unresolved | unresolved | unresolved | unresolved | `unresolved_static_only` | do not patch parser or provider behavior |

Static anchors:

- current `taichi_global_bathymetry.py:3888` defines `GeoVectorLineOverlay`.
- current `taichi_global_bathymetry.py:3914-4041` shows vector render receiving `flip_longitude`, `flip_latitude`, and `globe_mask`.
- current `taichi_global_bathymetry.py:1948-2028` shows AIS/aircraft projection receiving `flip_longitude` and `flip_latitude`.
- `d90b645:taichi_global_bathymetry.py:2625-2734` shows the same vector overlay family already present in the 14k basement.

## Synthetic Vector Cases

These cases are synthetic descriptors only. They do not load real borders, hydrology, Natural Earth, provider cache, or GeoJSON files.

| case_id | overlay_kind | source_shape | synthetic points | expected descriptor sync | fixture_status |
| --- | --- | --- | --- | --- | --- |
| `taiwan_short_border_segment` | borders | synthetic line | `(121.0,24.8) -> (121.7,25.3)` | should align with dynamic points | `pinned` |
| `east_asia_polyline` | borders | polyline | `(120.0,23.5) -> (121.5,25.0) -> (123.0,26.5)` | raw grid alignment is unresolved | `unresolved_static_only` |
| `hydrology_river_segment` | hydrology | synthetic line | `(120.6,23.8) -> (120.8,24.1)` | should align with dynamic points | `pinned` |
| `cross_equator_line` | hydrology | polyline | `(30.0,-1.0) -> (30.2,0.0) -> (30.4,1.0)` | should align with dynamic points | `pinned` |
| `anti_meridian_crossing_candidate` | borders | polyline | `(179.5,10.0) -> (-179.5,10.2)` | unresolved | `unresolved_static_only` |
| `empty_line_collection` | borders | empty | none | unresolved | `unresolved_static_only` |
| `malformed_coordinate_payload` | hydrology | malformed | non lon/lat payload | unresolved | `unresolved_static_only` |
| `same_lonlat_against_dynamic_projection_descriptor` | borders | synthetic line | duplicate Taipei lon/lat point | should align with AIS/aircraft projection descriptor | `pinned` |

## Sync Matrix

| frame | vector relationship | fixture status | boundary |
| --- | --- | --- | --- |
| raw spherical lon/lat | input reference for synthetic declared lon/lat | `pinned` | does not authorize shader raw-frame changes |
| terrain sample frame | adjacent but not direct vector owner | `unresolved_static_only` | does not authorize terrain sample or flip formula changes |
| AIS/aircraft screen projection frame | expected screen-sync peer because both paths consume flip flags before screen placement | `pinned` | does not execute projection functions or live AIS |
| grid/starfield frame | grid alignment is unresolved because grid uses shader raw lon/lat while vector is screen overlay | `unresolved_static_only` | does not claim grid/vector sync |
| mask/screen RGBA frame | clipping owner after vector RGBA draw | `pinned` | mask clipping does not prove internal coordinate correctness |
| postprocess/composition frame | not covered | `blocked_hot_path` | alpha/apply/composition behavior remains excluded |

## Test Shape

The focused test module is `tests/test_displaytools_vector_overlay_coordinate_sync.py`.

The test shape is `pure_dict_list_scalar_no_runtime_imports_no_real_geojson`:

- It uses test-local descriptors only.
- It does not import `taichi_global_bathymetry.py`.
- It does not import Taichi, Qt, VisPy, pandas, datashader, GeoJSON provider modules, SQL/WebSocket clients, or live AIS sources.
- It does not read Natural Earth, GeoJSON, hydrology, boundary, or cache files.
- It does not instantiate `GeoVectorLineOverlay`.
- It does not call renderer, projection, mask, alpha, postprocess, or composition hot paths.

## Known Unresolved Faults

| fault | fixture treatment | forbidden next action |
| --- | --- | --- |
| borders/hydrology vector bake/sync issue | mark vector/grid alignment as `unresolved_static_only` | do not claim the line location is corrected |
| dynamic point versus vector screen sync | pin as expected descriptor relationship only | do not execute AIS/aircraft projection or renderer |
| anti-meridian crossing candidate | keep unresolved until a narrow fixture can define wrap behavior | do not patch split/wrap formula here |
| terrain sample versus vector overlay authority | mark terrain frame as adjacent, not direct vector owner | do not change terrain sample frame |
| mask clipping ambiguity | pin mask as clipping owner only | do not infer pixel or visual parity from mask clipping |

## Recommended Next Gate

Recommended next gate: `vector_overlay_monkey_patch_craton_ablation_gate`.

Reason:

- The current fixture gate identifies vector overlay as a screen-space path with flip and mask dependencies.
- A narrow ablation gate can design how to replace only the vector overlay dependency with synthetic descriptors or monkey-patched local stubs for evidence, without reading real GeoJSON/cache and without modifying production source.
- This should still be a diagnostic gate, not a renderer behavior change.

Alternative if o_1 wants a narrower static slice: `vector_overlay_import_boundary_checker`, but only after a future pure vector coordinate descriptor helper candidate exists.

Alternative for a separate active fault: `solar_frame_diagnostic_gate`.

## Do-not-fix-yet Register

Do not modify these areas in this slice:

- `GeoVectorLineOverlay`
- vector projection, flip, mask, line simplification, or depth-mask formulas
- `project_ais_to_screen`
- `project_aircraft_to_screen`
- `mask_overlay_to_globe`
- Natural Earth, hydrology, boundary, provider, or cache loading
- Taichi shader coordinate formulas
- Qt/VisPy/controller runtime behavior
- alpha helpers and `build_layer_render_plan_apply_path`
- metadata sidecar writer and artifact writer paths

## Boundary Statement

Test/docs-only vector overlay coordinate sync fixture gate. No production source change, no runtime execution, no real GeoJSON/cache read, no source movement, no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_coordinate_sync_fixture_gate_ready_for_o1_review`

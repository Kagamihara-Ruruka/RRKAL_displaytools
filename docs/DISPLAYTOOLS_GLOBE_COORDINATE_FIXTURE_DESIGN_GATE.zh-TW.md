# Displaytools Globe Coordinate Fixture Design Gate

## Scope

本文件是 test/docs-only 的 globe coordinate fixture design gate。目標是把 raw lon/lat、flipped sample frame、screen projection frame、lighting frame、vector overlay frame、mask/screen RGBA frame 的責任邊界先釘住。

本輪不修正任何座標問題，不執行 renderer、Qt、VisPy、Taichi，不連 SQL/MySQL/WebSocket/AIS live source，不輸出 PNG/runtime JSON，也不改 shader、projection、longitude/latitude flip、lighting、metadata/output schema。

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `code_supported` | coordinate frame anchors, flip handling, projection paths, mask path |
| `d90b645:taichi_global_bathymetry.py` | `git_verified` | 14k basement comparison for the same frame families |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_OWNERSHIP_DIAGNOSTIC_GATE.zh-TW.md` | `product_docs_evidence` | current coordinate ownership inventory and do-not-fix list |
| `docs/DISPLAYTOOLS_HISTORICAL_VIEW_CONE_FIRST_CONTINENT_DECISION_GATE.zh-TW.md` | `product_docs_evidence` | first-continent decision: coordinate ownership/projection frame first |
| lab-only historical/geologic maps | `lab_summary_evidence` | summarized context only; not copied as product source of truth |

## Coordinate Frame Inventory

| frame_name | source_evidence | consumer_layers | known_faults | fixture_status | forbidden_next_action |
| --- | --- | --- | --- | --- | --- |
| `raw_spherical_lon_lat` | current lines 1659-1661 compute `n_world`, `lon`, `lat`; `d90b645` lines 1724-1726 show same family | globe geometry, lat/lon grid, lighting base | East/West orientation split candidate | `pinned` | do not change `rotate_view_to_world` or raw lon/lat formula |
| `terrain_sample_frame` | current lines 1662-1670 create `sample_lon/sample_lat` and apply `flip_longitude/flip_latitude`; current canopy/wave paths also consume sample frame | terrain sampling, forest/mask sampling, ocean wave sampling | East/West split, blocky terrain/bump debt | `pinned` | do not change flip behavior or texture sampling formula |
| `lighting_frame` | current line 1644 builds `light_dir`; current lines 1741-1760 use `n_world_bump.dot(light_dir)`; `d90b645` has same family | solar lighting, ocean specular, cloud day side | Taipei local-noon dark-side candidate | `unresolved_static_only` | do not change `light_dir`, bump normal, or dot-product formula |
| `grid_starfield_frame` | current lines 1812-1819 derive `lon_deg/lat_deg`; current line 1826 uses `render_stars(yaw, pitch, zoom)` | lat/lon grid, starfield | grid flip authority unresolved | `unresolved_static_only` | do not change grid/starfield formula |
| `ais_aircraft_screen_projection_frame` | current lines 1948-2028 project AIS/aircraft lon/lat to screen x/y with flip flags | AIS points, aircraft points, screen overlay RGBA | dynamic point and vector sync not proven | `pinned` | do not change projection formula or connect live AIS |
| `vector_overlay_frame` | current `GeoVectorLineOverlay` around 3888 and render path around 3914-4041 consume flip flags and `globe_mask`; `d90b645` has same vector family | borders, hydrology, screen overlay RGBA | borders/hydrology vector bake/sync issue | `unresolved_static_only` | do not change vector renderer or provider loading |
| `mask_screen_rgba_frame` | current `globe_mask` field around 1582, mask writes around 1653-1656, `mask_overlay_to_globe` around 2068-2072 | screen RGBA overlays, pins, vehicle overlay, clipped dynamic/vector layers | mask does not prove coordinate correctness inside silhouette | `pinned` | do not change mask clipping or generate PNG |
| `postprocess_composition_frame` | `render_core/render_plan.py` owns packet helpers; monolith retains apply/composition hot path | postprocess, composition, final RGBA | alpha/apply path hot path excluded | `blocked_hot_path` | do not touch alpha helpers, apply path, or metadata/output schema |

## Synthetic Fixture Cases

These cases are contract fixtures only. They do not claim the renderer currently displays the expected visual outcome.

| case_id | raw_lon | raw_lat | flip_longitude | flip_latitude | pinned expectation | diagnostic_status |
| --- | ---: | ---: | --- | --- | --- | --- |
| `taipei_east_asia` | 121.5654 | 25.0330 | false | false | raw longitude is East-positive | `pinned` |
| `pacific_negative_longitude` | -122.4194 | 37.7749 | false | false | raw longitude is West-negative | `pinned` |
| `longitude_flip_on` | 121.5654 | 25.0330 | true | false | sample longitude becomes -121.5654 | `pinned` |
| `longitude_flip_off` | 121.5654 | 25.0330 | false | false | sample longitude remains 121.5654 | `pinned` |
| `latitude_flip_on` | 121.5654 | 25.0330 | false | true | sample latitude becomes -25.0330 | `pinned` |
| `latitude_flip_off` | 121.5654 | 25.0330 | false | false | sample latitude remains 25.0330 | `pinned` |
| `equator_prime_meridian` | 0.0 | 0.0 | true | true | sign flip is mathematically neutral at zero | `pinned` |
| `local_noon_lighting_expectation` | 121.5654 | 25.0330 | not asserted | not asserted | diagnose light frame against raw and sample frames | `unresolved_static_only` |
| `vector_border_hydrology_sync_expectation` | 121.5654 | 25.0330 | not asserted | not asserted | diagnose vector overlay frame against dynamic projection frame | `unresolved_static_only` |

## Test Shape

The focused test module is `tests/test_displaytools_globe_coordinate_fixture_design.py`.

The test shape is `fixture_design_only_no_safe_import_target`:

- It uses test-local dict/list/scalar descriptors.
- It does not import `taichi_global_bathymetry.py`.
- It does not import Taichi, Qt, VisPy, MySQL, WebSocket, live AIS sources, renderer/controller objects, or artifact writers.
- It pins ownership descriptor schema and synthetic fixture cases.
- It records unresolved diagnostics as `unresolved_static_only`, not as behavior or bug-fix claims.

No current production helper is safe enough to import for this gate without risking runtime-heavy imports. A future import-boundary checker should wait until a pure coordinate descriptor helper candidate exists.

## Ownership Output Contract

Each coordinate frame descriptor must include exactly these fields:

- `frame_name`
- `source_evidence`
- `consumer_layers`
- `known_faults`
- `fixture_status`: one of `pinned`, `unresolved_static_only`, `blocked_hot_path`
- `forbidden_next_action`

This output is a fixture design contract only. It does not assert pixel equivalence, visual parity, runtime merge, performance readiness, bug fix, or product usability.

## Known Unresolved Faults

| fault | fixture treatment | blocked implementation action |
| --- | --- | --- |
| East/West longitude orientation split | compare raw frame and terrain sample frame ownership | do not change flip formula in this slice |
| Taipei local-noon dark-side candidate | mark light frame as `unresolved_static_only` | do not change solar frame or shader lighting formula |
| borders/hydrology vector bake/sync issue | mark vector overlay frame as `unresolved_static_only` | do not change `GeoVectorLineOverlay` or provider loading |
| blocky terrain sampling/bump debt | keep terrain/bump under diagnostic ownership only | do not change terrain sampling or bump normal formula |
| mask/screen RGBA clipping ambiguity | pin mask ownership only | do not infer coordinate correctness from `globe_mask` |

## Recommended Next Gate

Recommended next gate: `vector_overlay_coordinate_sync_fixture_gate`.

Reason:

- Dynamic point projection has clearer pure-function anchors, while vector overlays are the more visible unresolved sync fault.
- A vector sync fixture can use synthetic line descriptors and screen/mask contracts without running renderer/runtime code.
- It should still avoid real GeoJSON/provider/cache loading and avoid changing `GeoVectorLineOverlay`.

Deferred gate: `globe_coordinate_import_boundary_checker`.

Reason:

- This gate found `fixture_design_only_no_safe_import_target`.
- An import-boundary checker is useful only after a future pure coordinate descriptor/helper candidate exists.

Alternative later gate: `solar_frame_diagnostic_gate`, limited to static descriptor expectations for `n_world`, `n_world_bump`, and `light_dir`.

## Do-not-fix-yet Register

Do not modify these areas in this slice:

- `rotate_view_to_world`
- raw `lon/lat`, `sample_lon/sample_lat`, `flip_longitude`, `flip_latitude`
- `n_world`, `n_world_bump`, `light_dir`, solar dot-product formula
- grid/starfield formulas
- `project_ais_to_screen`
- `project_aircraft_to_screen`
- `GeoVectorLineOverlay`
- `mask_overlay_to_globe`
- `alpha_compose`, `alpha_blend_compose`, `alpha_compose_transparent`
- `build_layer_render_plan_apply_path`
- `HybridRenderController.apply_layer_render_plan_composition`
- metadata sidecar writer and artifact writer paths

## Boundary Statement

Test/docs-only globe coordinate fixture design gate. No production source change, no runtime execution, no shader/projection/lighting formula change, no source movement, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_globe_coordinate_fixture_design_gate_ready_for_o1_review`

# Displaytools Globe Coordinate Ownership Diagnostic Gate

## Scope

This is a docs/evidence-only coordinate ownership diagnostic gate for the render globe. It maps which coordinate frame each layer family appears to consume before any longitude, solar, vector sync, terrain sampling, or composition change is attempted.

This document is static-only. It does not run the renderer, launch Qt/VisPy/Taichi, connect to MySQL/WebSocket/AIS feeds, generate PNG/JSON runtime artifacts, or change formulas.

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| `git log -1 --oneline --decorate` | `git_verified` | current HEAD observed as `fb58aa7 docs: add render globe craton tectonic closeout map` |
| current `taichi_global_bathymetry.py` | `code_supported` | coordinate frame and layer ownership anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_verified` | 14k product-import comparison; same major coordinate frame families already existed |
| `render_core/*.py` | `code_supported` | source ownership context for render-plan and helper boundaries |
| `docs/DISPLAYTOOLS_RENDER_GLOBE_CRATON_AGE_TABLE_AND_TECTONIC_CLOSEOUT_MAP.zh-TW.md` | `docs_evidence` | active fault list and craton/shell classification |
| `docs/DEVELOPMENT_LOG.zh-TW.md` | `development_log_supported` | post-import render-plan, runtime-blend, vector overlay, and metadata evidence chronology |

## Coordinate frame inventory

| coordinate frame | current anchor | observed ownership | static interpretation | unresolved_static_only |
| --- | --- | --- | --- | --- |
| raw lon/lat from world normal | `n_world = rotate_view_to_world(n_view, yaw, pitch)` then `lon = atan2(n_world.x, n_world.z)` and `lat = asin(n_world.y)` around current lines 1659-1661 | globe shader raw spherical coordinate | base spherical frame before flip flags | whether every visual layer should share this raw frame is not proven statically |
| `sample_lon` / `sample_lat` | current lines 1662-1670 assign raw lon/lat then apply `flip_longitude` / `flip_latitude` before topography texture lookup | terrain, land/forest/ocean material sampling and wave/canopy variation | sampled data frame can differ from raw geometry frame | interaction with lighting/grid needs diagnostic evidence before any fix |
| `flip_longitude` / `flip_latitude` | current lines 1626-1627, 1664-1667, 1898-1923, 1955-1967, 2015-2028; CLI flags around 17528-17529 | globe terrain/clouds/dynamic point projections and controller toggles | flip flags are broad inputs, but not consumed identically by every layer | exact intended authority for each layer remains unresolved_static_only |
| `yaw` / `pitch` / zoom | `rotate_view_to_world(v, yaw, pitch)` around 1537; render and projection calls pass yaw/pitch/zoom | camera/view frame for globe render, starfield, projections and UI camera interpolation | camera frame is shared by renderer and point projection paths | static scan cannot prove all UI camera updates are synchronized frame-by-frame |
| world normal / `n_world` | current lines 1659-1661 and bump-normal lines around 1741-1760 | shader geometry, grid, lighting base, bump normals | world normal frame is the visual geometry basis | relation to flipped sample frame is the central fault candidate |
| solar light vector | current lines 1623-1625 and `light_dir = [sun_x, sun_y, sun_z]` around 1644; `dot_l = n_world_bump.dot(light_dir)` around 1760 | lighting and ocean/specular shading | light appears coupled to `n_world_bump`, not directly to `sample_lon/sample_lat` | Taipei local-noon dark-side candidate needs a solar-frame diagnostic, not formula change here |
| screen x/y | `project_ais_to_screen` around 1948 and `project_aircraft_to_screen` around 2008 produce `screen_x` / `screen_y` | dynamic point overlays and Qt/VisPy presentation | point layers convert lon/lat to screen frame after flip flags | static scan cannot prove vector overlay and point projection share all visibility/mask semantics |
| `globe_mask` | field setup around 1582, updates around 1653-1656, `mask_overlay_to_globe` around 2068-2072 | overlay clipping boundary for screen-space RGBA overlays | screen-space overlays can be clipped to globe silhouette | mask does not prove coordinate correctness inside the silhouette |

## Layer ownership matrix

| layer family | coordinate owner observed | flip handling observed | output frame | proximity risk | diagnostic status |
| --- | --- | --- | --- | --- | --- |
| terrain sampling | shader computes raw lon/lat from `n_world`, then uses `sample_lon/sample_lat` for topography lookup | `sample_lon = -sample_lon` and `sample_lat = -sample_lat` when flip flags are set | Taichi globe image | very high shader/terrain proximity | diagnostic-only; no formula change |
| solar lighting | `light_dir` and `n_world_bump.dot(light_dir)` | no direct `sample_lon/sample_lat` ownership observed in lighting dot-product path | Taichi globe shading | very high lighting/shader proximity | active fault candidate |
| lat/lon grid | current grid lines use raw `lon_deg = lon * 180 / PI`, `lat_deg = lat * 180 / PI` around 1812-1819 | static scan did not show grid using `sample_lon/sample_lat` | Taichi globe grid overlay | high geometry/shader proximity | unresolved_static_only for flip authority |
| starfield | `render_stars(self, yaw, pitch, zoom)` around 1826 | no lon/lat flip observed in starfield path | Taichi image background | medium; camera frame only | likely separate sky/camera frame, but static-only |
| AIS/aircraft dynamic point projection | `project_ais_to_screen` and `project_aircraft_to_screen` convert frame `lat/lon` to xyz and screen x/y | both functions apply `flip_longitude` / `flip_latitude` before projection | screen-space point frames | medium/high overlay proximity | good fixture candidate with synthetic points |
| borders/hydrology vector overlay | `GeoVectorLineOverlay` and hydrology/boundary specs; screen-space vector overlay later masked by globe mask | exact flip handling for this path is not fully proven by static summary | screen-space RGBA overlay | high vector sync risk | active fault; needs separate vector coordinate gate |
| forest/mask raster layer | `load_forest_density`, terrain-aligned forest sampling in shader, land/ice masks use lon/lat grids | forest sampling uses same `sample_lon/sample_lat` texture coordinate path inside globe shader | Taichi globe surface | high terrain/mask proximity | diagnostic-only with terrain sampling |
| Qt/VisPy screen layer | `VisPyHybridViewer`, `QtHybridWindow`, image visual and UI controls | toggles call controller flip methods; exact visual timing not proven statically | UI/screen presentation | high UI/runtime proximity | facade/runtime gate later, not here |
| postprocess/composition layer | `apply_layer_render_plan_composition`, alpha helpers, style postprocess, extracted render-plan packet helpers | packet labels may mention alpha/runtime/apply paths; real composition is hot path | final RGBA frame | very high ndarray/hot-path proximity | do-not-fix-yet |

## Known active faults

| fault | static evidence | risk | current gate result |
| --- | --- | --- | --- |
| East/West longitude orientation split | terrain sampling uses flipped `sample_lon`; grid uses raw `lon_deg`; lighting uses `n_world_bump.dot(light_dir)` | one layer can appear corrected while another remains in a different frame | active fault candidate; needs coordinate diagnostic fixture before implementation |
| Taipei local-noon dark-side candidate | craton closeout map records lab-observed dark-side candidate; source shows light vector and terrain sampling can be governed by different frame variables | solar frame may disagree with oriented terrain | active fault candidate; no solar formula change here |
| borders/hydrology vector bake/sync issue | `GeoVectorLineOverlay` serves vector layer families; development log records runtime-blend/vector overlay pressure around hydrology/boundary | shared vector path can create correlated sync errors | requires vector overlay coordinate sync gate |
| blocky terrain sampling/bump debt | terrain and bump normals are deep shader/data path; topography uses sampled grid and bump normal calculation near `n_world_bump` | may be sampling/interpolation/normal issue, not only source resolution | requires terrain sampling/bump diagnostic gate |

## Do-not-fix-yet list

These functions, formulas, or hot paths must not be modified in this slice:

- `rotate_view_to_world`
- Taichi globe render shader path around raw `lon/lat`, `sample_lon/sample_lat`, `n_world`, and `n_world_bump`
- `compute_sun_direction`
- `light_dir` and `dot_l = n_world_bump.dot(light_dir)` shading formula
- `flip_longitude` / `flip_latitude` behavior and controller toggles
- lat/lon grid formula using raw `lon_deg` / `lat_deg`
- `project_ais_to_screen`
- `project_aircraft_to_screen`
- `GeoVectorLineOverlay` projection/render path
- `mask_overlay_to_globe`
- `load_forest_density` and land/ice/forest mask sampling code
- `alpha_compose`, `alpha_blend_compose`, `alpha_compose_transparent`
- `build_layer_render_plan_apply_path`
- `HybridRenderController.apply_layer_render_plan_composition`
- metadata sidecar writer and artifact writer paths

## Recommended next gates

| rank | gate | type | reason | not authorized |
| ---: | --- | --- | --- | --- |
| 1 | Globe coordinate fixture design gate | diagnostic gate | define synthetic lon/lat/camera/flip expectations across terrain sample frame, raw frame, grid and dynamic point projection | no shader or flip behavior change |
| 2 | Vector overlay coordinate sync fixture gate | diagnostic/fixture gate | isolate borders/hydrology `GeoVectorLineOverlay` coordinate and mask assumptions with synthetic line segments | no vector renderer behavior change |
| 3 | Solar frame diagnostic gate | diagnostic gate | compare declared sun vector frame, raw geometry frame, and flipped sample frame with static/contracts only | no lighting formula change |
| 4 | Terrain sampling/bump source map | docs/evidence gate | split source-data resolution, sample interpolation, bump normal, and UI style controls before any terrain change | no terrain shader change |
| 5 | AIS/aircraft projection fixture gap gate | fixture gate | dynamic point projection functions are pure enough for synthetic lon/lat flip cases | no live feed, database, or network use |

Implementation gates should come only after these diagnostic gates identify a single coordinate owner and parity evidence requirement. Direct alpha/apply work is not a recommended next slice.

## Boundary Statement

Docs/evidence-only coordinate ownership diagnostic gate. No product code change, no runtime execution, no shader/coordinate formula change, no source movement, no alpha/apply behavior change, no metadata/output schema change, no runtime merge enablement, and no visual/performance/readiness claim.

## Final Classification

`c3_displaytools_globe_coordinate_ownership_diagnostic_gate_ready_for_o1_review`

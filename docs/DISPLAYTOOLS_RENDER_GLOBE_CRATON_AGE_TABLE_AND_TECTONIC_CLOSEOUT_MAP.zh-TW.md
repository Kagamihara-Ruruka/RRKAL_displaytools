# Displaytools Render Globe Craton Age Table And Tectonic Closeout Map

## Scope

This is a docs/evidence-only closeout map for the render globe portion of `taichi_global_bathymetry.py` after the render-plan packet helper extraction sequence.

It combines two axes:

- horizontal graph cut: which responsibility continents exist now and where their dependency boundaries are.
- craton age table: which responsibilities are observed in early artifacts, product import, and current source.

This document does not authorize source movement. It separates `git_verified`, `artifact_supported`, `development_log_supported`, `code_supported`, and `owner_attested` evidence. Owner memory is not treated as proof.

## Evidence Sources

| source | evidence level | use in this map | notes |
| --- | --- | --- | --- |
| `git log -1 --oneline --decorate` | `git_verified` | current product HEAD | observed `d5dbb3b refactor: extract residual packet surface helpers` |
| `d90b645:taichi_global_bathymetry.py` | `git_verified` | 5/29 14k basement snapshot | `Initial RRKAL display tools import`, 14,324 lines |
| current `taichi_global_bathymetry.py` | `code_supported` | current 21k monolith map | 21,118 lines observed by static text/AST scan |
| current `render_core/*.py` | `code_supported` | migrated plate inventory | extracted helper modules and line counts |
| `docs/DEVELOPMENT_LOG.zh-TW.md` | `development_log_supported` | post-import sedimentation chronology | supports 5/29-6/3 product-period growth, not pre-import ancestry |
| `L:\RRKAL_lab\external_research\analysis\o1_displaytools_14k_to_21k_tectonic_map.zh-TW.md` | `lab_evidence_context` | cross-check of 14k-to-21k layer model | used as evidence context, not as implementation approval |
| `L:\RRKAL_lab\external_research\analysis\o1_displaytools_21k_sedimentary_layer_hypothesis_verification.zh-TW.md` | `lab_evidence_context` | artifact-supported pre-product hypotheses | marks K/Mac evidence and owner memory boundaries |

Product Git does not contain `taichi_global_bathymetry.py` snapshots for 2026-05-10, 2026-05-11, 2026-05-12, or 2026-05-18. Those columns below therefore use `not_observed_in_product_git` unless a lab reference reports artifact-supported evidence.

## Craton Age Table

| candidate | 5/10 | 5/11 | 5/12 | 5/18 | 5/29 14k | current 21k | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Globe geometry / Taichi globe | not observed | not observed | artifact_supported: early K global has Taichi globe, stars, grid, terrain | not observed | git_verified: `TaichiGlobeRenderer`, `rotate_view_to_world`, Taichi imports | code_supported: still core renderer host | deep craton; gate before movement |
| Terrain / bathymetry | not observed | not observed | artifact_supported: topography load and bump lighting in early K global | not observed | git_verified: `load_topography`, `synthetic_topography`, bathymetry/topography functions | code_supported: still present, 520 terrain/bathy keyword hits | deep craton; diagnostic gate first |
| Lighting / solar direction | not observed | not observed | artifact_supported: basic sun/bump lighting; Taipei branch later deepens celestial model | not observed | git_verified: `compute_sun_direction` at basement line 8885 | code_supported: current line 9988; orientation/lighting hits increased | active fault; coordinate diagnostic gate |
| Qt / VisPy host | not observed | not observed | artifact evidence says earliest K global was not Qt-hosted | not observed | git_verified: `QtHybridWindow`, `VisPyHybridViewer`, `QtWidgets`, VisPy host | code_supported: still present; controller/UI shell persists | host shell; do not cut without facade gate |
| AIS / aircraft | not observed | not observed | not supported for both together in inspected product Git | not observed | git_verified: `AISSource`, `AircraftSource`, projection helpers, Datashader overlays | code_supported: still present, live/replay boundary unresolved | source/provider boundary gate |
| Vector overlay / borders / hydrology | not observed | not observed | not observed in product Git | not observed | git_verified: `GeoVectorLineOverlay`, hydrology/boundary specs | code_supported: still shared vector path, 1,722 overlay/vector hits | active fault; vector sync diagnostic gate |
| Forest / mask | not observed | not observed | not observed / not supported in inspected early global artifact | not observed | git_verified: `load_forest_density`, forest overlay classes | code_supported: still present | raster/mask gate after coordinate map |
| Timeline / animation | not observed | not observed | not observed | not observed | limited basement timeline/playback residue | code_supported: large 21k accretion, 873 timeline hits | accreted shell; fixture gate candidate |
| Render-plan / compose packets | not observed | not observed | not observed | not observed | not present as named `layer_render_plan` surface in 14k scan | code_supported: 174 render-plan hits plus many `render_core` helpers | migrated/accreted plate; closeout gates |
| Metadata / evidence / handoff | not observed | not observed | not observed | not observed | git_verified: evidence/readiness/handoff packet functions already existed | code_supported: thickened to 732 metadata/evidence hits | accreted shell; schema-adjacent gates only |

## Horizontal Graph-Cut Map

| subsystem | owned symbols / anchors | inbound dependencies | outbound dependencies | side effects | renderer/Qt/Taichi/ndarray proximity | metadata/output proximity | possible fixture gate | difficulty | recommended next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Globe geometry | `TaichiGlobeRenderer`, `rotate_view_to_world`, camera/orientation math | controller camera state, renderer uniforms | Taichi kernels, screen projection | renderer state mutation | very high | low | coordinate ownership packet/gate only | P5 | diagnostic map, no extraction |
| Terrain / bathymetry | `load_topography`, `synthetic_topography`, topography cache path, shader sampling | file/cache paths, GEBCO/local data, renderer style | Taichi texture/height sampling | file/cache reads; shader effects | very high | medium via metadata summaries | sampling/bump diagnostic gate | P5 | terrain artifact-free static map |
| Lighting | `compute_sun_direction`, light uniforms, bump normals | time/location, orientation controls | shader illumination | renderer uniforms | very high | low | solar/orientation consistency matrix | P4 | coordinate diagnostic gate |
| Qt / VisPy host | `QtHybridWindow`, `VisPyHybridViewer`, app/window classes | UI state, controller methods | renderer calls, signals, menus | UI/event loop | high | medium via reviewer/export panels | facade intent map only | P5 | no movement in c_3 mainline |
| AIS / aircraft | `AISSource`, `AircraftSource`, `dataframe_from_*`, projection helpers, Datashader overlays | file/url/database/demo inputs, parser/normalizer | overlay arrays, point projection | possible IO/network/db if executed | medium/high | medium via layer runtime packets | provider/replay boundary gate | P3 | gate replay/live boundary first |
| Vector overlay | `GeoVectorLineOverlay`, hydrology/boundary specs, line features | GeoJSON/provider/cache, style profile, globe mask | screen-space overlay RGBA | file/cache/provider if executed | high | medium | vector coordinate sync fixture map | P4 | diagnostic gate, not extraction |
| Forest / mask | `load_forest_density`, `ForestEventSource`, mask helpers | file/cache, data frame parser | raster/point overlays | file/cache if executed | medium/high | low/medium | raster mask source map | P3 | after coordinate map |
| Timeline | `timeline_*_packet`, interpolation helpers, ack payload writer | state file, UI/controller time state | camera/layer/ocean controls | state writes if executed | medium | high via export/review packets | packet fixture/import-boundary gates | P2 | safe next shell gate |
| Render-plan / compose | `compile_layer_render_plan`, `apply_layer_render_plan_composition`, extracted render_core helpers | controller runtime facts, layer state | alpha/apply hot path, metadata summaries | hot path if executed | very high around apply/alpha | high | residual closeout and source-map gates | P4/P5 | no direct alpha/apply work |
| Metadata / evidence | `renderer_output_artifact_contract_packet`, diagnostics/review packets, `render_core.metadata`, `preview.py` | renderer facts, sidecar payloads | docs/JSON/PNG writers if executed | writer behavior if executed | medium | very high | contract-only schema proximity map | P3 | closeout gates only |

## 14k Basement Continents

The 2026-05-29 product import already contained multiple responsibility continents. It was not a clean renderer seed.

| continent | 14k evidence | current interpretation |
| --- | --- | --- |
| Qt/VisPy host shell | `QtHybridWindow`, `VisPyHybridViewer`, `QtWidgets`, `QMainWindow` | native to product import, not proven for earliest artifact ancestry |
| Taichi globe renderer | `TaichiGlobeRenderer`, Taichi imports, shader/kernel surface | deep runtime craton |
| Terrain/bathymetry | topography and bathymetry loaders, synthetic topography, cache paths | deep data/render craton |
| AIS/aircraft | source classes, projection helpers, Datashader overlays | product-import layer, live/replay boundary still unresolved |
| Vector overlays | `GeoVectorLineOverlay`, hydrology/boundary specs | shared risk surface for borders/hydrology |
| Forest/mask | forest density loader and forest event overlay | raster/mask layer persisted |
| Provider/cache/catalog text | provider manifests, cache manifests, readiness packets | evidence shell already present at import |
| Ocean/material/provider policy | ocean material and condition provider classes | product-import policy surface, not current first cut |
| Controller/runtime shell | `HybridRenderController` | central hub; avoid direct movement |

## 21k Accreted Shell

The current source has grown to 21,118 lines. Static keyword and symbol evidence indicates thickening after product import around:

- timeline/keyframe packets and interpolation helpers
- layer runtime badges, warnings, feedback, selection, lock, hover and operator packets
- boundary identity, highlight, hydrology LOD and vector identity surfaces
- render-plan/cache/compose packet families and smoke/source-map contracts
- metadata/evidence/reviewer/handoff packets
- profile launch/replay/review surfaces

These are not automatically safe to extract. They are better candidates for fixture gates, AST import-boundary gates, and source-map closeout docs because many sit near controller state or metadata/output wording.

## Migrated Plates

Source movement is distinguished from compatibility labels. Several symbols still appear through `render_core.render_plan` compatibility imports or packet source strings, but physical ownership has moved.

| plate | current physical owner | compatibility / note |
| --- | --- | --- |
| DataFrame normalizers | `render_core/dataframe_normalizers.py` | `normalize_name`, `find_column`, AIS/aircraft normalizers moved |
| Point overlay budget policy | `render_core/point_overlay_budget_policy.py` | policy-only helper |
| Datashader sampling policy | `render_core/datashader_sampling_policy.py` | scalar policy helper |
| Layer render budget policy | `render_core/layer_render_budget_policy.py` | includes cost map with policy helper |
| Adaptive render quality policy | `render_core/adaptive_render_quality_policy.py` | scalar recommendation helper |
| Layer state input helper | `render_core/layer_state.py` | runtime fact input packaging |
| Metadata payload builder | `render_core/metadata.py` | writer behavior remains outside helper |
| Preview writer helper | `render_core/preview.py` | output behavior remains guarded by existing callers |
| Batch prepare evidence helper | `render_core/batch_prepare.py` | evidence helper only |
| Compose queue helpers | `render_core/layer_render_plan_compose_queue.py` | source-map and smoke know physical owner |
| Composition dispatch helpers | `render_core/layer_render_plan_composition_dispatch.py` | dispatch packet labels only; no hot path execution |
| Cache diagnostics helpers | `render_core/layer_render_plan_cache_diagnostics.py` | cache key/invalidation/metadata summary packets |
| Execution phase timing helpers | `render_core/layer_render_plan_execution_phase_timing.py` | timing/bottleneck packets, not performance authorization |
| Adapter/preflight helpers | `render_core/layer_render_plan_adapter_preflight.py` | controller-to-core packet surface |
| Compiled/reused packet helpers | `render_core/layer_render_plan_compiled_reused_packets.py` | packet status only; not cache lifecycle proof |
| Residual packet surfaces | `render_core/layer_render_plan_residual_packet_surfaces.py` | runtime snapshot, composition input, style/timing/steps/batch decisions |
| Remaining render-plan hot core | `render_core/render_plan.py` | alpha helpers and `build_layer_render_plan_apply_path` remain excluded |

## Active Faults

| fault | evidence | risk | recommended gate |
| --- | --- | --- | --- |
| Longitude/orientation split | lab refs report `flip_longitude` terrain correction while lighting may use separate world normal/light assumptions | coordinate systems can look locally fixed while other layers desync | coordinate ownership matrix for terrain, grid, dynamic points, vectors, lighting |
| Solar lighting desync | `compute_sun_direction` exists in both 14k and current; lab refs report Taipei local noon dark-side observation | shader/light frame may disagree with terrain orientation | solar/terrain orientation diagnostic gate |
| Borders/hydrology sync | `GeoVectorLineOverlay` shared by vector features; hydrology/boundary specs stable from basement to current | one vector path can affect multiple layer families | vector overlay coordinate sync fixture gate |
| Blocky terrain | terrain/bathy and bump sampling are deep shader/data craton | source resolution tuning alone may not address shader/sampling debt | terrain sampling/bump static + fixture gate |
| AIS replay/live boundary | source supports file/url/database/demo concepts; lab ref observed current MySQL replay, not live WebSocket proof | live feed assumptions can leak into provider gates | AIS source boundary map with no network execution |
| Metadata/evidence wording | 21k shell contains many review/readiness/handoff packets | wording can imply stronger status than evidence supports | contract wording closeout gate |
| Alpha/apply hot path | alpha helpers and apply path remain in `render_core/render_plan.py` | direct movement touches ndarray/pixel behavior | do not recommend direct work; require separate parity design first |

## Next-Slice Recommendation

Do not recommend direct alpha/apply work in the next c_3 slice.

Recommended next gates by risk class:

| rank | next gate | risk class | why |
| ---: | --- | --- | --- |
| 1 | Globe coordinate ownership diagnostic gate | high value / no runtime execution | separates longitude flip, terrain sampling, solar light, grid, AIS/aircraft projection and vector overlay ownership before any fix attempt |
| 2 | Vector overlay coordinate sync fixture/source map | high value / medium risk | borders and hydrology likely share one debt class through `GeoVectorLineOverlay`; gate can stay static and synthetic |
| 3 | Timeline packet fixture/import-boundary gate | lower hot-path risk | timeline is accreted shell with many packet helpers and less direct ndarray proximity than alpha/apply |
| 4 | Metadata/evidence contract wording closeout | schema-adjacent risk | useful if o_1 wants governance cleanup before more source movement |

Stop line: alpha helpers and `build_layer_render_plan_apply_path` should remain out of scope until a separate parity and instrumentation design is reviewed.

## Boundary Statement

Docs/evidence-only craton age table and tectonic closeout map. No product code change, no runtime execution, no source movement, no alpha/apply behavior change, no metadata/output schema change, no runtime merge enablement, and no visual/performance/readiness claim.

## Final Classification

`c3_displaytools_render_globe_craton_age_table_tectonic_closeout_map_ready_for_o1_review`

# Displaytools Historical View-Cone First Continent Decision Gate

## Scope

This is a docs/evidence-only historical view-cone synthesis map. It combines pre-product artifacts, the 5/18-to-5/29 gap map, the 14k-to-21k tectonic map, the craton closeout map, and the coordinate ownership diagnostic gate into one decision map for selecting the first large continent to gate next.

This document does not authorize implementation. It ranks candidate gates only.

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| `a1_displaytools_pre_product_geologic_map_excluding_taipei.zh-TW.md` | lab summary evidence | 5/10, 5/11, 5/12, 5/18 pre-product mainline view cone |
| `a1_displaytools_518_to_529_pre_product_to_basement_gap_map.zh-TW.md` | lab summary evidence | 5/18-to-5/29 basement jump and gap-born cratons |
| `o1_displaytools_14k_to_21k_tectonic_map.zh-TW.md` | lab summary evidence | 14k-to-current plate classes and active faults |
| `o1_displaytools_21k_sedimentary_layer_hypothesis_verification.zh-TW.md` | lab summary evidence | owner-memory boundaries and current sedimentary interpretation |
| `docs/DISPLAYTOOLS_RENDER_GLOBE_CRATON_AGE_TABLE_AND_TECTONIC_CLOSEOUT_MAP.zh-TW.md` | product docs evidence | craton age table and horizontal graph-cut closeout map |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_OWNERSHIP_DIAGNOSTIC_GATE.zh-TW.md` | product docs evidence | current coordinate frame ownership and do-not-fix-yet register |
| current `taichi_global_bathymetry.py` | code-supported context | current 21k monolith surface and remaining hot paths |
| `d90b645:taichi_global_bathymetry.py` | git-verified context | 5/29 14k basement snapshot |

Lab-only reports are summarized, not copied as product-source truth. Owner memory remains `owner_attested` unless supported by artifacts or product Git.

## Historical View-Cone Table

| layer | evidence | main responsibilities observed | decision meaning |
| --- | --- | --- | --- |
| 5/10 core | lab summary: `GEBCO_test.py`, 120 lines | bathymetry data fetch, 3D globe geometry experiment, static Matplotlib view | seed is data/geometry, not product renderer shell |
| 5/12 first crust | lab summary: K global `taichi_global_bathymetry.py`, 663 lines | Taichi globe, stars, lat/lon grid, topography, bump mapping, sun/twilight, `ti.GUI` interaction | deep craton for globe/terrain/light/grid; not Qt/VisPy |
| 5/18 contract junction | lab summary: launcher contract integrated copy, 687 lines | same Taichi core plus `api_launcher.renderer_contracts` path/URL/cache injection | contract seam exists before product import; small and gateable as boundary evidence only |
| 5/18 to 5/29 gap | lab summary: 687 lines to 14,324 lines | Qt/VisPy host, AIS/aircraft, vector overlays, forest/mask, SQL replay, controller shell, embedded governance | first large continent emerged here; high risk because many unrelated continents accreted together |
| 5/29 14k basement | `d90b645` product Git | multi-layer monolith with renderer, controller, UI host, data sources, vector layers, policy/governance text | product import is already sedimentary; do not call it a clean core |
| 14k to 21k product sediment | product Git/docs | timeline, layer runtime UX, metadata/evidence/reviewer shell, render-plan/cache/compose gates | accreted shell contains safer packet/gate candidates than shader/core |
| current extracted `render_core` migration | current `render_core/*.py` | normalizers, policies, metadata/preview, layer state, render-plan packet helpers | proves helper movement method works for pure dict/scalar surfaces, not for hot paths |

## Craton Persistence Matrix

| responsibility | 5/10 | 5/12 | 5/18 | 5/29 14k | current 21k | persistence judgment | first-continent suitability |
| --- | --- | --- | --- | --- | --- | --- | --- |
| globe geometry | artifact-supported seed | artifact-supported | artifact-supported | git-verified | code-supported | deep persistent craton | gate only; no direct source movement |
| terrain/bathymetry | artifact-supported seed | artifact-supported | artifact-supported | git-verified | code-supported | deep persistent craton | diagnostic map before any implementation |
| lighting/solar frame | primitive/static light | artifact-supported basic sun/twilight | artifact-supported | git-verified `compute_sun_direction` | active fault candidate | persistent but frame ownership split | solar diagnostic gate, not formula change |
| grid/starfield | not primary | artifact-supported | artifact-supported | git-verified | code-supported | early crust persisted | coordinate fixture design candidate |
| AIS/aircraft | not observed | not observed | not observed | git-verified | code-supported | gap-born product continent | projection fixture/boundary candidate |
| vector overlays: borders/hydrology | not observed | not observed | not observed | git-verified | active fault candidate | gap-born product continent | strong candidate for coordinate sync gate |
| forest/mask | not observed | not observed in early global artifact | not observed | git-verified | code-supported | gap-born product continent | later raster/mask source map |
| Qt/VisPy host | not observed | not observed | not observed | git-verified | code-supported | gap-born host shell | not first c_3 mainline cut |
| render-plan/compose evidence shell | not observed | not observed | not observed | limited / not named as current family | heavily extracted to `render_core` | product sediment with migrated plates | closeout/checker gates only; stop before alpha/apply |
| metadata/evidence/reviewer shell | not observed | not observed | limited contract seam | git-verified governance shell | thick current shell | accreted product shell | wording/schema proximity gate, not runtime proof |

## First-Continent Candidate Ranking

| rank | candidate | evidence basis | why first / why not | recommended gate shape | implementation authorized |
| ---: | --- | --- | --- | --- | --- |
| 1 | coordinate ownership / projection frame | 5/12 core plus current diagnostic gate; active longitude/solar/vector faults | highest leverage because it intersects terrain, grid, lighting, AIS/aircraft, vector overlays and masks without requiring runtime code changes | `Globe coordinate fixture design gate` with synthetic frame expectations | no |
| 2 | vector overlay coordinate sync | gap-born `GeoVectorLineOverlay`; borders/hydrology share one path; active sync fault | high product value and more isolated than shader formulas, but still close to screen-space overlays | `Vector overlay coordinate sync fixture gate` with synthetic lines and mask assumptions | no |
| 3 | terrain sampling/bump diagnostic | deep 5/12 craton, current blocky terrain debt | important but too close to Taichi shader and sampling formulas for first movement | docs/static diagnostic plus future fixture design | no |
| 4 | AIS/aircraft projection boundary | gap-born product continent; projection functions are comparatively pure | good fixture candidate after coordinate frame rules are pinned | synthetic lon/lat flip projection fixture gate | no |
| 5 | timeline/render-plan shell | product sediment; many pure packet helpers already extracted | safe pattern exists, but less central to longitude/solar/vector faults | fixture/import-boundary closeout gates | no |
| 6 | metadata/evidence shell | thick product shell; high wording/schema proximity | useful governance cleanup, but not the first continent for coordinate bugs | contract wording/source-map gate | no |

Decision: the first continent should be **coordinate ownership / projection frame**, but only as a diagnostic/fixture design gate. Direct terrain, lighting, vector, or renderer implementation remains blocked.

## Stop-Line Register

These areas remain out of direct-cut scope:

| stop line | reason |
| --- | --- |
| alpha helpers | ndarray pixel hot path |
| `build_layer_render_plan_apply_path` | apply-helper labels and composition dispatch proximity |
| `HybridRenderController.apply_layer_render_plan_composition` | live composition hot path |
| Taichi shader formula | terrain/light/grid/pixel behavior |
| runtime renderer behavior | requires runtime/parity evidence not collected here |
| Qt behavior | event-loop/UI behavior outside this docs gate |
| metadata/output schema | schema/output behavior must stay unchanged |
| live AIS/WebSocket implementation | network/live source boundary not verified and not needed for this gate |
| SQL/MySQL replay behavior | data-source execution forbidden in this slice |
| projection formula changes | coordinate ownership is not yet proven enough for implementation |

## Recommended Next Gate

Recommended next c_3 gate:

**Globe coordinate fixture design gate**

Minimum scope:

- define synthetic lon/lat cases for raw frame, flipped sample frame, and screen projection frame.
- pin expected ownership statements for terrain sampling, grid, lighting, AIS/aircraft, vector overlay and globe mask.
- include `unresolved_static_only` where source text cannot prove a single owner.
- forbid shader formula changes, renderer execution, Qt execution, source movement, metadata/output changes and runtime claims.

Fallback if o_1 wants a narrower first fixture:

**Vector overlay coordinate sync fixture gate**

Use only synthetic line geometries and packet/coordinate evidence. Do not run renderer, do not change `GeoVectorLineOverlay`, and do not use real GeoJSON/provider/cache paths.

## Boundary Statement

Docs/evidence-only historical view-cone synthesis and first-continent decision gate. No product code change, no runtime execution, no source movement, no shader/coordinate formula change, no metadata/output schema change, no runtime merge enablement, and no visual/performance/readiness claim.

## Final Classification

`c3_displaytools_historical_view_cone_first_continent_decision_gate_ready_for_o1_review`

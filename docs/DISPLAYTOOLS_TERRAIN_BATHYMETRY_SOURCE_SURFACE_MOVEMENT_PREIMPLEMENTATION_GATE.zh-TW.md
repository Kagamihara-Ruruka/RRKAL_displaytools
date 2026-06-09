# Displaytools Terrain/Bathymetry Source Surface Movement Preimplementation Gate

## Scope

本文件是 docs/test-only terrain/bathymetry source surface movement preimplementation gate。目標是在不修改 production source 的前提下，判斷地形 / 水深大部中哪些 surface 只是 descriptor / policy / ledger，可作為未來第一刀規劃候選；哪些仍屬 provider/cache loader、shader sampling、projection / flip / lighting 或 runtime hot path，必須阻擋。

本輪不建立 helper module，不移動任何 source，不修改 `taichi_global_bathymetry.py`，不 import monolith，不執行 renderer / Qt / VisPy / Taichi runtime，不讀 real terrain/cache/provider，不改 shader、sampling、bump、projection、flip 或 lighting formula，也不宣稱修復 visual fault 或可進 runtime。

## Evidence read

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `static_source_evidence` | terrain/bathymetry provider/cache, topography field, sampling, bump, lighting, palette, and runtime host ownership |
| `d90b645:taichi_global_bathymetry.py` | `git_static_evidence` | historical comparison for the same terrain/bathymetry responsibility families |
| `docs/DISPLAYTOOLS_TERRAIN_BATHYMETRY_BOUNDARY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | descriptor fields, fixture statuses, known unresolved faults, and first recommended movement map |
| craton / historical view-cone / coordinate gates | `product_docs_evidence` | craton age, coordinate ownership, and stop-line context |
| vector overlay source-surface movement gate | `format_reference` | surface matrix, first-cut decision output, and category-based blocker style |

## Surface categories

| category | meaning | first-cut status |
| --- | --- | --- |
| `category_a_descriptor_policy_ledger` | terrain/bathymetry source descriptor, height-field descriptor, fallback/no-data descriptor, LOD/resolution label, cache status label, palette/style label, known fault ledger | candidate for future planning only |
| `category_b_provider_cache_loader` | NOAA/GEBCO/ETOPO provider execution, real cache read/write, download/fetch/load lifecycle | blocked from first cut |
| `category_c_sampling_shader_formula` | terrain sampling formula, bump/normal calculation, raymarch/sphere intersection, shader-side height lookup | blocked from first cut |
| `category_d_projection_flip_lighting` | longitude/latitude flip formula, sun direction/twilight/dot lighting, grid/starfield frame coupling | blocked from first cut |
| `category_e_runtime_renderer_host` | Taichi renderer class, Qt/VisPy host, runtime GUI/controller behavior | blocked from first cut |
| `category_f_visual_style_palette` | water/land palette and style profile behavior | behavior blocked; label descriptors only may be category A |

## Surface category matrix

| surface_name | observed_owner | movement_category | candidate_for_first_cut | reason | required_guard | forbidden_next_action |
| --- | --- | --- | --- | --- | --- | --- |
| terrain/bathymetry source descriptor | current load_topography/topography args and d90b645 GEBCO/topography family | `category_a_descriptor_policy_ledger` | yes | Source labels can be represented as data without opening providers or caches. | Fixture parity for descriptor key sets before any planning gate. | Do not execute provider or cache loader. |
| height-field descriptor | current topo field, synthetic_topography fallback, and renderer input shape labels | `category_a_descriptor_policy_ledger` | yes | Height-field metadata can be represented as dict/list/scalar descriptors. | Descriptor fixture and later no-runtime import-boundary planning. | Do not move sampling or shader height lookup. |
| fallback/no-data descriptor | current load_topography fallback branch and synthetic_topography label | `category_a_descriptor_policy_ledger` | yes | Fallback/no-data status is a ledger label when provider execution remains excluded. | Fallback descriptor fixture with malformed/no-data branch. | Do not download or generate real topography. |
| LOD/resolution label descriptor | current topo_step parser, cache path step label, and derived cache stride label | `category_a_descriptor_policy_ledger` | yes | LOD/resolution can be pinned as label data without proving sampling quality. | Exact label fixture and decision table before movement planning. | Do not change resolution or sampling behavior. |
| cache status label descriptor | current topography cache hit/miss/fallback branches | `category_a_descriptor_policy_ledger` | yes | Cache hit/miss labels can be data descriptors when lifecycle execution remains blocked. | String-label allowance and cache-lifecycle exclusion tests. | Do not read, write, download, or evict cache. |
| palette/style label descriptor | current terrain_color and water/land palette labels | `category_a_descriptor_policy_ledger` | yes | Style labels can be carried as data while visual behavior remains excluded. | Palette label fixture and no visual-readiness wording guard. | Do not change palette or style behavior. |
| known fault ledger descriptor | current coordinate/craton gates list blocky terrain, flip, and lighting faults | `category_a_descriptor_policy_ledger` | yes | Known fault ledger records unresolved diagnostics without claiming fixes. | Ledger fixture with unresolved/static-only status values. | Do not fix or mark visual fault resolved. |
| NOAA/GEBCO/ETOPO provider execution | current load_topography provider path and historical GEBCO source family | `category_b_provider_cache_loader` | no | Provider execution can read files, download, or transform real terrain data. | Provider/cache boundary fixture before any separate movement route. | Do not include provider execution in first cut. |
| real cache read/write | current topography_cache_path and cache save/load branches | `category_b_provider_cache_loader` | no | Cache IO is lifecycle behavior rather than descriptor data. | Cache lifecycle map and artifact audit guard. | Do not read or write real cache. |
| download/fetch/load lifecycle | current topography source loader and external data source branches | `category_b_provider_cache_loader` | no | Download/fetch/load changes IO and provider ownership. | Provider loader boundary before movement. | Do not fetch, download, or load real terrain data. |
| terrain sampling formula | current sample_lon/sample_lat to tx/ty and z_val sampling path | `category_c_sampling_shader_formula` | no | Sampling formula is shader behavior and can affect pixels. | Sampling diagnostic gate and parity evidence before any formula work. | Do not move or change sampling formula. |
| bump/normal calculation | current dz_dx/dz_dy, n_world_bump, and bump scale path | `category_c_sampling_shader_formula` | no | Bump/normal calculation is hot shader-side behavior. | Bump/normal diagnostic gate only. | Do not move or change bump/normal formula. |
| raymarch/sphere intersection/shader height lookup | current Taichi globe renderer shader-side geometry path | `category_c_sampling_shader_formula` | no | Shader geometry and height lookup are runtime hot path surfaces. | Separate renderer hot-path review. | Do not touch raymarch, sphere intersection, or height lookup. |
| longitude/latitude flip formula | current flip_longitude/flip_latitude branches and coordinate fixture gates | `category_d_projection_flip_lighting` | no | Flip formula owns coordinate behavior and active orientation faults. | Coordinate formula diagnostic gate before implementation. | Do not change flip formula. |
| sun direction/twilight/dot lighting | current light_dir, dot_l, n_world, and n_world_bump usage | `category_d_projection_flip_lighting` | no | Lighting changes visual output and active local-noon diagnostics. | Solar frame diagnostic gate before implementation. | Do not change lighting or twilight formula. |
| grid/starfield frame coupling | current coordinate ownership gate lists grid/starfield frame separately | `category_d_projection_flip_lighting` | no | Frame coupling is coordinate ownership, not terrain descriptor movement. | Coordinate fixture follow-up if needed. | Do not merge grid/starfield frame with terrain first cut. |
| Taichi renderer class | current TaichiGlobeRenderer owns fields, kernels, shader, and render host behavior | `category_e_runtime_renderer_host` | no | Renderer class movement would import runtime/GPU behavior. | Renderer-host decomposition map only. | Do not move or instantiate renderer class. |
| Qt/VisPy host | current UI/runtime host surfaces outside terrain descriptor layer | `category_e_runtime_renderer_host` | no | Host behavior needs runtime execution and is unrelated to descriptor first cut. | UI/host seam gate if needed. | Do not import or execute Qt/VisPy host. |
| runtime GUI/controller behavior | current controller/runtime methods set renderer args and reload behavior | `category_e_runtime_renderer_host` | no | Controller mutation is runtime behavior rather than source descriptor data. | Controller seam map before any runtime work. | Do not move controller or runtime behavior. |
| water/land palette behavior | current terrain_color visual behavior and style profile consumers | `category_f_visual_style_palette` | no | Palette behavior can affect output colors; only label descriptors are candidate. | Style label fixture before any behavior movement. | Do not move or change palette behavior. |
| style profile behavior | current style/profile labels and postprocess consumers | `category_f_visual_style_palette` | no | Style behavior is broader than terrain descriptor ownership. | Style/profile boundary map if needed. | Do not move or change style profile behavior. |

## First-cut candidate summary

The only first-cut candidate surface is:

- `category_a_descriptor_policy_ledger`

Allowed future planning content is limited to:

- terrain/bathymetry source descriptor
- height-field descriptor
- fallback/no-data descriptor
- LOD/resolution label descriptor
- cache status label descriptor
- palette/style label descriptor
- known fault ledger descriptor

This is planning eligibility only. `source_movement_authorized=false`, and `terrain_bathymetry_extraction_candidate=false`.

## Blocked surface summary

Blocked from the first cut:

- `category_b_provider_cache_loader`: provider execution, real cache read/write, download/fetch/load lifecycle
- `category_c_sampling_shader_formula`: terrain sampling, bump/normal, raymarch/sphere intersection, shader-side height lookup
- `category_d_projection_flip_lighting`: longitude/latitude flip formula, solar/twilight/dot lighting, grid/starfield coupling
- `category_e_runtime_renderer_host`: Taichi renderer class, Qt/VisPy host, runtime GUI/controller behavior
- `category_f_visual_style_palette`: water/land palette and style profile behavior, except label descriptors treated as category A data

## Decision output

| field | value |
| --- | --- |
| `first_cut_surface` | `category_a_descriptor_policy_ledger` |
| `category_b_to_f_blocked_from_first_cut` | true |
| `source_movement_authorized` | false |
| `terrain_bathymetry_extraction_candidate` | false |
| `terrain_bathymetry_planning_candidate` | true |
| `import_boundary_checker_required_now` | false |
| `import_boundary_checker_reason` | `not_required_until_a_safe_descriptor_helper_target_is_identified` |
| `recommended_next_gate` | `terrain_bathymetry_boundary_minimal_extraction_planning_gate` |

## Import-boundary checker need assessment

An import-boundary checker is not required in this slice because no helper target is identified and no source movement is authorized. The next planning gate may decide whether a future descriptor-only target exists. If such a target is identified, then a checker should be added before movement to block provider/cache loaders, renderer/runtime imports, shader formula names, projection/flip/lighting formula owners, metadata/output writers, and monolith imports.

## Recommended next gate

Recommended next gate:

- `terrain_bathymetry_boundary_minimal_extraction_planning_gate`

This should remain a planning gate. It should list exact candidate descriptor/value names, blocked symbols, required fixture parity, and checker expectations. It must not create a helper module or move source unless a later `o_1` review explicitly authorizes movement.

## Stop-line register

Do not modify or move in this route:

- `taichi_global_bathymetry.py`
- real GEBCO/NOAA/ETOPO provider/cache loader paths
- cache read/write/download/fetch/load lifecycle
- terrain sampling formula
- bump/normal calculation
- raymarch / sphere intersection / shader-side height lookup
- longitude/latitude flip formula
- sun direction / twilight / dot lighting
- grid/starfield coordinate coupling
- `TaichiGlobeRenderer`, Qt/VisPy host, runtime GUI/controller behavior
- water/land palette or style behavior
- metadata/output schema or artifact writer paths

## Boundary Statement

Docs/test-only terrain/bathymetry source surface movement preimplementation gate. No production source change, no helper module creation, no source movement, no monolith import, no renderer/Qt/VisPy/Taichi runtime execution, no real terrain/cache/provider read, no shader/sampling/bump/projection/flip/lighting formula change, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_terrain_bathymetry_source_surface_movement_preimplementation_gate_ready_for_o1_review`

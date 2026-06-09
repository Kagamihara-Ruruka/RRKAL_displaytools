# Displaytools Terrain/Bathymetry Boundary Minimal Extraction Planning Gate

## Scope

本文件是 docs/test-only terrain/bathymetry boundary minimal extraction planning gate。目標是把 terrain/bathymetry 的 `category_a_descriptor_policy_ledger` 收斂成未來第一刀候選清單，規劃可能的 descriptor-only helper target。

本輪不建立 `render_core\terrain_bathymetry_boundary.py`，不建立任何 helper module，不移動 source，不修改 production code，不 import `taichi_global_bathymetry.py`，不執行 renderer / Qt / VisPy / Taichi runtime，不讀 real terrain/cache/provider，不改 shader、sampling、bump、projection、flip 或 lighting formula，也不宣稱修復 visual fault 或授權 runtime。

## Evidence read

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `static_source_evidence` | terrain/bathymetry provider/cache, topography field, sampling, bump, lighting, palette, and runtime host ownership |
| `d90b645:taichi_global_bathymetry.py` | `git_static_evidence` | historical comparison for the same terrain/bathymetry responsibility families |
| `docs/DISPLAYTOOLS_TERRAIN_BATHYMETRY_BOUNDARY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | boundary descriptor contract and unresolved fault list |
| `docs/DISPLAYTOOLS_TERRAIN_BATHYMETRY_SOURCE_SURFACE_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md` | `product_docs_evidence` | category A candidate surface and category B-F blockers |
| vector overlay minimal extraction planning / extraction gates | `format_reference` | planning packet shape, blocked-surface table, and review-before-movement wording |

## Planning target candidate

| field | value |
| --- | --- |
| `target_candidate` | `render_core\terrain_bathymetry_boundary.py` |
| `source_movement_authorized` | false |
| `helper_module_creation_authorized` | false |
| `terrain_bathymetry_extraction_candidate` | false |
| `terrain_bathymetry_planning_candidate` | true |
| `a1_macro_observer_required_before_source_movement` | true |

This target is hypothetical only. This slice does not create the file and does not move source.

## Candidate descriptor families

Each candidate below is limited to dict/list/scalar descriptor builders or policy/ledger tables. Every candidate must keep:

- `candidate_for_minimal_extraction = true`
- `runtime_dependency_allowed = false`
- `provider_cache_execution_allowed = false`
- `shader_formula_allowed = false`
- `projection_lighting_formula_allowed = false`
- `visual_behavior_change_allowed = false`

| candidate_name | planned_target_name | allowed_content_kind | required_fixture | forbidden_next_action |
| --- | --- | --- | --- | --- |
| `build_terrain_bathymetry_source_descriptor` | same | source descriptor only | source descriptor exact key-set and repeat-call parity | do not execute `load_topography` or provider/cache |
| `build_terrain_height_field_descriptor` | same | height-field descriptor only | height-field descriptor exact key-set parity | do not move sampling or shader height lookup |
| `build_terrain_fallback_no_data_descriptor` | same | fallback/no-data descriptor only | fallback/no-data branch parity | do not generate or download real topography |
| `build_terrain_lod_resolution_label_descriptor` | same | LOD/resolution label only | LOD/resolution label-only parity | do not change resolution or sampling behavior |
| `build_terrain_cache_status_label_descriptor` | same | cache status label only | cache hit/miss label-only parity | do not read/write/load/save/evict cache |
| `build_terrain_palette_style_label_descriptor` | same | palette/style label only | palette/style label-only parity | do not change palette or visual behavior |
| `build_terrain_known_fault_ledger_descriptor` | same | known fault ledger only | unresolved/static-only fault ledger parity | do not mark visual fault fixed or ready |
| `terrain_bathymetry_boundary_descriptor` | same | optional aggregate descriptor value | aggregate descriptor exact key-set parity | do not include runtime formula or provider loader |
| `terrain_bathymetry_planning_bundle` | same | optional planning bundle value | bundle key-set and blocked-surface declaration parity | do not authorize source movement inside bundle |

## Blocked symbols and surfaces

| blocked_name | blocked_category | reason | required_future_gate | forbidden_next_action |
| --- | --- | --- | --- | --- |
| `load_topography` | provider/cache loader | loads terrain/provider/cache data | provider/cache boundary gate | do not move or call loader |
| `synthetic_topography` behavior | provider/cache loader | generates fallback terrain behavior, not a descriptor | fallback behavior parity gate | do not move or change synthetic generation |
| NOAA / GEBCO / ETOPO provider execution | provider/cache loader | external provider execution is IO/lifecycle behavior | provider/cache loader gate | do not fetch, download, or execute provider |
| topography cache read/write/load/save | provider/cache loader | cache lifecycle reads/writes files | cache lifecycle boundary gate | do not read/write/load/save cache |
| terrain sampling formula | sampling/shader formula | formula maps sample frame to height lookup | terrain sampling diagnostic gate | do not move or change sampling formula |
| bump / normal formula | sampling/shader formula | formula affects normals and lighting | bump/normal diagnostic gate | do not move or change bump formula |
| raymarch / sphere intersection / shader height lookup | sampling/shader formula | shader hot path affects pixels | renderer hot-path gate | do not touch shader geometry path |
| `flip_longitude` / `flip_latitude` formula | projection/flip/lighting formula | flip behavior owns coordinate faults | coordinate formula gate | do not change flip formula |
| `compute_sun_direction` | projection/flip/lighting formula | solar frame behavior affects lighting | solar frame diagnostic gate | do not move or change sun direction |
| `light_dir` / `dot_l` / twilight formula | projection/flip/lighting formula | lighting formula affects rendered output | lighting diagnostic gate | do not move or change lighting formula |
| `TaichiGlobeRenderer` | runtime renderer host | renderer class owns GPU/runtime state | renderer host map | do not import or instantiate renderer |
| Qt/VisPy host surfaces | runtime renderer host | UI/render host requires runtime | UI/host seam gate | do not import or execute Qt/VisPy |
| runtime GUI/controller behavior | runtime renderer host | controller behavior mutates runtime state | controller seam gate | do not move controller behavior |
| water/land palette behavior | visual style behavior | visual color behavior is not label-only data | palette behavior parity gate | do not change palette behavior |
| metadata/artifact writers | metadata/artifact writer | writer behavior changes output/artifacts | metadata/output boundary gate | do not execute or move writers |
| alpha/apply/composition hot path | hot path blocked | composition hot path is outside terrain descriptor planning | alpha/apply hot-path gate | do not touch alpha/apply/composition |

## Fixture parity plan

Before any future source movement, fixture parity must cover:

- exact key-set parity for descriptor builders
- deterministic repeat-call parity
- source descriptor branch
- height-field descriptor branch
- fallback/no-data descriptor branch
- LOD/resolution label-only branch
- cache hit/miss label-only branch
- palette/style label-only branch
- known fault ledger unresolved branch
- future import-boundary checker candidate pass
- future forbidden dependency fail

## Import-boundary checker need assessment

A future import-boundary checker is required before extraction. It is not required in this slice because this slice does not create a helper module and does not move source.

Future checker target:

- `render_core\terrain_bathymetry_boundary.py`

The checker should block:

- monolith import
- renderer / Qt / VisPy / Taichi runtime imports
- real terrain/cache/provider loader imports
- shader/sampling/bump/projection/flip/lighting formula owners
- metadata/output writers
- alpha/apply/composition hot path names

## a_1 macro observer requirement

`a1_macro_observer_required_before_source_movement = true`.

Before source movement, `a_1` should review:

- whether the candidates remain one descriptor/policy/ledger craton
- whether provider/cache loader, sampling formula, bump formula, projection/flip/lighting formula, runtime host, or palette behavior leaked into the candidate set
- whether the planned target would break the terrain/bathymetry historical craton boundary
- whether a smaller or better first-cut candidate exists
- whether more horizontal or historical evidence is needed

## Decision output

| decision item | answer |
| --- | --- |
| Next slice as actual extraction | not yet; only after `a_1` macro observer and `o_1` review |
| Helper module creation authorized now | no |
| Source movement authorized now | no |
| Terrain/bathymetry extraction candidate now | no |
| Terrain/bathymetry planning candidate now | yes |
| First-cut minimal scope | descriptor / policy / ledger only |
| Future import-boundary checker required before extraction | yes |

## Recommended next gate

Recommended next gate:

- `terrain_bathymetry_import_boundary_checker_gate`

This should remain tooling/docs-only. It should define AST-only forbidden import/name boundaries for the hypothetical `render_core\terrain_bathymetry_boundary.py` target before any source movement is considered.

## Boundary Statement

Docs/test-only terrain/bathymetry boundary minimal extraction planning gate. No helper module creation, no source movement, no production source change, no monolith import, no renderer/Qt/VisPy/Taichi runtime execution, no real terrain/cache/provider read, no shader/sampling/bump/projection/flip/lighting formula change, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_terrain_bathymetry_boundary_minimal_extraction_planning_gate_ready_for_o1_review`

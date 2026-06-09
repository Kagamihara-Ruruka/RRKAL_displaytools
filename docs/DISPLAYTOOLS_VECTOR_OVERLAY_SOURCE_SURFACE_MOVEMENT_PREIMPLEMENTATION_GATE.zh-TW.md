# Displaytools Vector Overlay Source Surface Movement Preimplementation Gate

## Scope

本文件是 docs/test-only preimplementation gate，用來判斷未來 `render_core/vector_overlay_boundary.py` 的第一批可切 surface 應該落在哪一層。此 gate 不建立 helper module、不移動 source、不修改 `taichi_global_bathymetry.py`、不執行 controller/provider/cache/runtime、不讀 real GeoJSON/Natural Earth/hydrology cache、不修改 projection/flip/mask formula，也不觸碰 alpha/apply/composition hot path。

本 gate 的結論只允許進入下一張 planning gate；不授權 source movement，不宣稱 safe-to-extract、bug fixed、visual parity、performance、readiness 或 runtime merge。

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `static_source_evidence` | current vector overlay runtime class, provider specs, dirty/reload, projection/mask, writer and hot-path anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_static_evidence` | older basement anchors showing the same broad surface categories before later sediment |
| `scripts/validate_displaytools_vector_overlay_import_boundary.py` | `tooling_evidence` | forbidden import/name families and string-label allowance |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_COORDINATE_SYNC_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | vector overlay coordinate sync descriptor vocabulary |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_MONKEY_PATCH_CRATON_ABLATION_GATE.zh-TW.md` | `product_docs_evidence` | vector overlay ablation footprint categories |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_PROVIDER_BOUNDARY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | provider/source/cache descriptor boundary |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_CONTROLLER_REGISTRY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | controller registry seam boundary |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_DIRTY_RELOAD_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | dirty/reload ledger and checker-gate route |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_IMPORT_BOUNDARY_CHECKER_GATE.zh-TW.md` | `product_docs_evidence` | AST-only checker behavior and allowed string-label distinction |

## Surface categories

| category | meaning | first-cut status |
| --- | --- | --- |
| `category_a_descriptor_policy_ledger` | dict/list/scalar descriptor builders, policy tables, dirty/reload ledgers, and provider references as data | candidate for planning only |
| `category_b_provider_cache_contract` | provider/cache contract or loader-adjacent surface | not same first cut, except descriptor labels as data |
| `category_c_projection_mask_consumer` | projection, flip, mask, or clipping consumer surface | not same first cut |
| `category_d_controller_registry_mutation` | controller registry, dirty flag mutation, reload request mutation | not same first cut |
| `category_e_runtime_overlay_class` | runtime overlay class such as `GeoVectorLineOverlay` | not first cut |
| `category_f_hot_path_blocked` | alpha/apply/composition hot path or metadata/artifact writer proximity | blocked for this route |

## Symbol / surface matrix

| symbol_or_surface | observed_owner | movement_category | candidate_for_first_cut | reason | required_guard | forbidden_next_action |
| --- | --- | --- | --- | --- | --- | --- |
| `GeoVectorLineOverlay` | `taichi_global_bathymetry.py:3888`, `d90b645:2625` | `category_e_runtime_overlay_class` | no | Runtime overlay class consumes lon/lat lines, camera, flip flags, globe mask, and screen-space render parameters. | Runtime-specific parity and controller seam review after descriptor planning. | Do not move runtime overlay class as first cut. |
| borders provider descriptor | `BOUNDARY_SPECS` in current `taichi_global_bathymetry.py:4257`, `d90b645:2843` | `category_a_descriptor_policy_ledger` | yes, preimplementation only | Static descriptor data can be represented without provider execution or cache reads. | Vector overlay import-boundary checker plus `a_1` macro observer before movement. | Do not execute boundary provider or cache. |
| hydrology provider descriptor | `HYDROLOGY_SPECS` in current `taichi_global_bathymetry.py:4289`, `d90b645:2875` | `category_a_descriptor_policy_ledger` | yes, preimplementation only | Static descriptor data can be represented separately from hydrology loader execution. | Vector overlay import-boundary checker plus `a_1` macro observer before movement. | Do not execute hydrology provider or cache. |
| vector overlay descriptor builder | future descriptor-only surface derived from fixture gates | `category_a_descriptor_policy_ledger` | yes, preimplementation only | Descriptor builders can assemble dict/list/scalar contracts without renderer or provider calls. | Fixture parity for descriptor schema and import-boundary checker. | Do not instantiate `GeoVectorLineOverlay`. |
| vector dirty/reload ledger | dirty/reload fixture gate and controller flags in current source | `category_a_descriptor_policy_ledger` | yes, preimplementation only | Ledger descriptors can record state transitions without mutating controller flags. | Dirty/reload fixture plus import-boundary checker. | Do not mutate controller dirty or reload state. |
| vector controller registry descriptor | controller registry fixture gate and controller overlay registries | `category_a_descriptor_policy_ledger` | yes, preimplementation only | Registry can be represented as data descriptors while controller mutation remains excluded. | Controller registry fixture and `a_1` macro observer before movement. | Do not import or instantiate controller. |
| vector projection policy label | projection labels from coordinate and sync fixture gates | `category_a_descriptor_policy_ledger` | yes, preimplementation only | Policy labels are data only and do not contain projection formulas. | String-label allowance plus formula exclusion tests. | Do not move or rewrite projection formula. |
| vector mask policy label | mask labels from coordinate and sync fixture gates | `category_a_descriptor_policy_ledger` | yes, preimplementation only | Mask policy labels are data only while clipping formula remains in current runtime surface. | String-label allowance plus formula exclusion tests. | Do not move or rewrite mask clipping formula. |
| provider cache status label | provider boundary and dirty/reload fixture gates | `category_a_descriptor_policy_ledger` | yes, preimplementation only | Cache hit/miss can remain a descriptor label when no cache lifecycle is executed. | Checker must allow string labels but block executable cache references. | Do not read or write provider cache. |
| actual provider/cache loader | `_load_hydrology_overlays`, `_load_boundary_overlays`, provider specs | `category_b_provider_cache_contract` | no | Loader execution reads provider/cache state and constructs runtime overlays. | Provider/cache contract gate and separate loader boundary before any movement. | Do not include loader execution in first cut. |
| projection formula | `GeoVectorLineOverlay.render` and point projection helpers | `category_c_projection_mask_consumer` | no | Projection behavior is formula-bearing and tied to camera/flip state. | Projection/mask ablation follow-up before movement. | Do not change projection or flip formula. |
| mask clipping formula | `mask_overlay_to_globe` in current `taichi_global_bathymetry.py:2068`, `d90b645:2133` | `category_c_projection_mask_consumer` | no | Mask clipping changes pixel alpha behavior and must stay out of descriptor planning. | Projection/mask ablation follow-up before movement. | Do not change mask or alpha behavior. |
| controller dirty flag mutation | `overlay_dirty`, `hydrology_dirty`, `boundary_dirty` assignments in controller methods | `category_d_controller_registry_mutation` | no | Mutation changes controller state and cannot be moved as descriptor-only content. | Controller mutation seam map before movement. | Do not mutate or move controller flags. |
| controller reload request mutation | `reload_hydrology_layer`, `reload_boundary_layer` controller methods | `category_d_controller_registry_mutation` | no | Reload request mutates args, dirty flags, and provider references. | Controller reload seam map before movement. | Do not move reload methods or provider refresh. |
| alpha/apply/composition hot path | alpha helpers, `build_layer_render_plan_apply_path`, `apply_layer_render_plan_composition` | `category_f_hot_path_blocked` | no | Pixel composition and apply path are outside vector descriptor ownership. | Separate hot-path parity and `o_1` review. | Do not touch alpha/apply/composition path. |
| metadata/artifact writer | `render_core.metadata`, `render_core.preview`, monolith writer calls | `category_f_hot_path_blocked` | no | Writer behavior affects output schema and artifacts, not vector overlay descriptor ownership. | Metadata/output boundary review if ever needed. | Do not execute or move metadata/artifact writers. |

## First-cut decision output

| field | value |
| --- | --- |
| `first_cut_surface` | `category_a_descriptor_policy_ledger` |
| `first_cut_target_candidate` | `render_core\vector_overlay_boundary.py` |
| `first_cut_allowed_content` | descriptor builders / policy tables / dirty-reload ledger descriptors / provider ref descriptors as data |
| `first_cut_forbidden_content` | `GeoVectorLineOverlay` runtime class / provider execution / projection formula / mask formula / controller mutation / cache reads |
| `requires_a1_macro_observer_before_source_movement` | true |
| `source_movement_authorized` | false |

## Decision answers

| question | answer |
| --- | --- |
| Can the first cut be `GeoVectorLineOverlay`? | no |
| Can the first cut be descriptor / policy / ledger? | yes, preimplementation only |
| Can provider/cache contract be in the same cut? | no, at most provider/cache references as data descriptors |
| Can projection/mask formula be in the same cut? | no |
| Is the import-boundary checker enough? | yes for descriptor candidate; no for runtime class |
| Is `a_1` macro observer needed? | yes before source movement |
| What is the next gate? | `vector_overlay_boundary_minimal_extraction_planning_gate` |

## Import-boundary checker adequacy assessment

The existing checker is adequate for a descriptor candidate because it blocks executable imports/name references to monolith, controller/runtime classes, Qt/VisPy/Taichi, dataframe/render-heavy dependencies, provider/cache runtime names, SQL/live stream names, alpha/apply hot path, and metadata/artifact writers while allowing string labels such as `cache_hit`, `GeoJSON`, `projection`, and `mask`.

The checker is not sufficient to authorize moving `GeoVectorLineOverlay` or formula-bearing runtime surfaces. Runtime class movement would still require separate parity evidence, controller seam review, projection/mask diagnostics, and `a_1` macro observer review.

## a_1 macro observer requirement

`requires_a1_macro_observer_before_source_movement=true`.

Reason: the descriptor/policy/ledger layer is now narrow enough for planning, but it still crosses historical vector, controller registry, provider descriptor, projection label, and mask label strata. Before physical source movement, `a_1` should side-observe whether the planned first cut preserves the historical craton boundary and does not accidentally include runtime class, provider loader, or projection/mask formula surfaces.

## Recommended next gate

Recommended next gate:

- `vector_overlay_boundary_minimal_extraction_planning_gate`

This remains a planning gate. It should propose a concrete descriptor-only surface, exact symbol names, expected test additions, import-boundary checks, and stop lines. It must still keep `source_movement_authorized=false` until `o_1` review explicitly authorizes a later movement slice.

## Do-not-fix-yet register

Do not modify or move in this slice:

- `taichi_global_bathymetry.py`
- `render_core/vector_overlay_boundary.py`
- `GeoVectorLineOverlay`
- `_load_hydrology_overlays`, `_load_boundary_overlays`, `reload_hydrology_layer`, `reload_boundary_layer`
- `HYDROLOGY_SPECS` or `BOUNDARY_SPECS` as executable provider/cache behavior
- projection, flip, or mask formulas
- `mask_overlay_to_globe`
- alpha helpers, `build_layer_render_plan_apply_path`, and composition hot path
- controller dirty flag or reload request mutation
- real GeoJSON, Natural Earth, hydrology, boundary, provider, or cache files
- SQL/MySQL/WebSocket/AIS live access
- metadata sidecar writer and artifact writer paths

## Boundary Statement

Docs/test-only vector overlay source surface movement preimplementation gate. No helper module creation, no source movement, no production source change, no controller/provider/cache runtime, no real GeoJSON/cache read, no runtime execution, no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_source_surface_movement_preimplementation_gate_ready_for_o1_review`

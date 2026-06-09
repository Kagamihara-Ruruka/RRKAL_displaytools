# Displaytools Vector Overlay Boundary Minimal Extraction Planning Gate

## Scope

本文件是 docs/test-only planning gate，用來規劃未來 `render_core/vector_overlay_boundary.py` 的最小第一刀 extraction candidate。此 gate 只制定候選清單、blocked 清單、fixture parity 需求、checker 預期與 `a_1` 宏觀側觀問題。

本輪不建立 `render_core/vector_overlay_boundary.py`，不移動任何 source，不修改 `taichi_global_bathymetry.py`，不修改 production code，不 import 或 instantiate controller/renderer/Qt/VisPy/Taichi，不讀 real GeoJSON/Natural Earth/hydrology cache，不連 SQL/WebSocket/AIS live，不修改 projection/flip/mask formula，不觸碰 alpha/apply/composition hot path，不碰 metadata/output schema。

本 gate 不宣稱 safe-to-extract、bug fixed、visual parity、performance、readiness 或 runtime merge。下一步仍需 `a_1` macro observer 與 `o_1` 再次裁決。

## Evidence read

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `static_source_evidence` | `GeoVectorLineOverlay`, `BOUNDARY_SPECS`, `HYDROLOGY_SPECS`, dirty/reload, projection/mask, writer and hot-path anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_static_evidence` | older vector overlay anchors and source-surface category continuity |
| `tests/test_displaytools_vector_overlay_source_surface_movement.py` | `test_evidence` | prior source-surface matrix and first-cut decision |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_SOURCE_SURFACE_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md` | `product_docs_evidence` | descriptor/policy/ledger first-cut boundary |
| `scripts/validate_displaytools_vector_overlay_import_boundary.py` | `tooling_evidence` | future helper import/name redline |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_IMPORT_BOUNDARY_CHECKER_GATE.zh-TW.md` | `product_docs_evidence` | missing-candidate behavior and string-label allowance |
| prior vector overlay coordinate/provider/controller/dirty gates | `product_docs_evidence` | fixture coverage needed before any later source movement |

## Planning packet

| field | value |
| --- | --- |
| `schema` | `rrkal_displaytools.vector_overlay_boundary_minimal_extraction_planning.v1` |
| `target_candidate` | `render_core\vector_overlay_boundary.py` |
| `source_movement_authorized` | false |
| `requires_a1_macro_observer_before_source_movement` | true |
| `next_gate` | `vector_overlay_boundary_minimal_extraction_gate_after_a1_macro_review` |

## Candidate symbols

Only descriptor / policy / ledger surfaces are candidate symbols. Every candidate below must keep `runtime_dependency_allowed=false`, `candidate_for_minimal_extraction=true`, and `required_checker=validate_displaytools_vector_overlay_import_boundary.py`.

| candidate_name | source_evidence | source_owner | planned_target_name | allowed_content_kind | required_fixture | forbidden_next_action |
| --- | --- | --- | --- | --- | --- | --- |
| boundary specs descriptor | `BOUNDARY_SPECS` static anchor and source-surface movement gate | `taichi_global_bathymetry.py` descriptor value | `BOUNDARY_PROVIDER_DESCRIPTOR_TABLE` | static descriptor table as data only | boundary descriptor exact key-set and empty/malformed descriptor branches | do not execute boundary provider or cache |
| hydrology specs descriptor | `HYDROLOGY_SPECS` static anchor and source-surface movement gate | `taichi_global_bathymetry.py` descriptor value | `HYDROLOGY_PROVIDER_DESCRIPTOR_TABLE` | static descriptor table as data only | hydrology descriptor exact key-set and empty/malformed descriptor branches | do not execute hydrology provider or cache |
| vector overlay descriptor builder | coordinate sync and source-surface movement gates | future descriptor-only builder surface | `build_vector_overlay_descriptor` | dict/list/scalar descriptor builder | descriptor builder exact key-set and deterministic repeat-call parity | do not instantiate `GeoVectorLineOverlay` |
| vector provider ref descriptor builder | provider boundary fixture gate | provider reference descriptor surface | `build_vector_provider_ref_descriptor` | provider reference descriptor as data only | provider present/missing and cache label-only branches | do not call provider loader or read cache |
| vector dirty reload ledger descriptor | dirty/reload fixture gate | dirty/reload ledger descriptor surface | `build_vector_dirty_reload_ledger_descriptor` | dirty/reload ledger descriptor as data only | clean branch and reload branch parity | do not mutate controller dirty or reload flags |
| vector controller registry descriptor | controller registry fixture gate | controller registry descriptor surface | `build_vector_controller_registry_descriptor` | controller registry descriptor as data only | registry present/missing and consumer ref descriptor parity | do not import or instantiate controller |
| vector projection policy label descriptor | coordinate fixture and vector coordinate sync gates | projection label descriptor surface | `build_vector_projection_policy_label_descriptor` | projection policy label only | projection label-only branch parity | do not move or rewrite projection formula |
| vector mask policy label descriptor | coordinate fixture and vector coordinate sync gates | mask label descriptor surface | `build_vector_mask_policy_label_descriptor` | mask policy label only | mask label-only branch parity | do not move or rewrite mask formula |
| vector cache status label descriptor | provider boundary and dirty/reload fixture gates | cache status label descriptor surface | `build_vector_cache_status_label_descriptor` | cache status label only | cache hit/miss string-label branch parity | do not read or write cache |

## Blocked symbols

These are not extraction candidates for the first cut.

| blocked_name | blocked_category | reason | required_future_gate | forbidden_next_action |
| --- | --- | --- | --- | --- |
| `GeoVectorLineOverlay` | `runtime_overlay_class` | Runtime class consumes camera, flip flags, mask, image drawing, and screen-space rendering state. | runtime overlay parity and controller seam gate | do not list as extraction candidate |
| actual provider/cache loader | `provider_cache_runtime` | Loader execution reads provider/cache state and constructs runtime overlays. | provider/cache loader boundary gate | do not execute or move loader |
| projection formula | `projection_mask_formula` | Formula-bearing projection depends on camera and flip state. | projection/mask ablation follow-up gate | do not change projection or flip formula |
| mask clipping formula | `projection_mask_formula` | Mask clipping changes alpha/pixel behavior. | projection/mask ablation follow-up gate | do not change mask clipping or alpha behavior |
| controller dirty flag mutation | `controller_registry_mutation` | Dirty flag assignment changes controller state. | controller mutation seam gate | do not move or mutate controller dirty flags |
| controller reload request mutation | `controller_registry_mutation` | Reload mutates args, dirty flags, and provider references. | controller reload seam gate | do not move reload methods |
| alpha/apply/composition hot path | `hot_path_blocked` | Pixel composition and render-plan apply path are outside vector boundary descriptors. | separate alpha/apply hot-path parity gate | do not touch alpha/apply/composition path |
| metadata/artifact writer | `metadata_artifact_writer` | Writer behavior affects output schema or artifacts. | metadata/output boundary gate | do not execute or move writers |
| SQL/WebSocket/AIS live path | `live_io_runtime` | Live data and SQL/WebSocket access are outside vector overlay descriptor planning. | live-source boundary gate | do not connect SQL/WebSocket/AIS live |
| Qt/VisPy/Taichi runtime host | `runtime_ui_gpu` | UI/GPU/runtime hosts are explicitly forbidden by the checker and planning boundary. | runtime host boundary review | do not import or execute runtime hosts |

## Fixture parity plan

Before a later source movement slice, the future descriptor-only candidate needs fixture parity for:

1. exact key-set parity for descriptor builders
2. deterministic repeat-call parity
3. empty provider descriptor branch
4. malformed provider descriptor branch
5. dirty/reload ledger clean branch
6. dirty/reload ledger reload branch
7. projection/mask label-only branch
8. cache status label-only branch
9. string-label allowance branch
10. import-boundary checker candidate pass
11. negative forbidden dependency fail

## Import-boundary expectation

| field | expected value |
| --- | --- |
| `target_missing_now` | true |
| `expected_checker_status_now` | `not_applicable_candidate_missing` |
| `expected_checker_after_descriptor_only_candidate` | `pass` |
| `expected_checker_after_runtime_dependency` | `fail` |

The checker is enough to guard descriptor-only candidate content. It is not enough to approve runtime class, provider loader, projection formula, mask formula, controller mutation, alpha/apply/composition, metadata writer, artifact writer, SQL/WebSocket/AIS live, or Qt/VisPy/Taichi host movement.

## a_1 macro observer requirement

Before any physical source movement, `a_1` should review:

- whether these candidates remain one descriptor/policy/ledger craton.
- whether runtime class, provider loader, projection/mask formula, controller mutation, or writer surfaces have leaked into the candidate.
- whether the plan preserves the historical view-cone vector overlay boundary.
- whether there is a better first-cut candidate.
- whether a horizontal graph or historical evidence gap should be filled first.

## Decision output

| question | answer |
| --- | --- |
| Can the next gate be actual extraction? | not yet; only after `o_1` / `a_1` review of this planning gate |
| Is `a_1` needed before movement? | yes |
| Is source movement authorized? | no |
| What is the first minimal scope? | descriptor / policy / ledger only |
| Is import-boundary checker enough? | yes for descriptor-only candidate; no for runtime surfaces |

## Recommended next gate

If this planning gate passes `o_1` review and `a_1` macro observer review, the next possible gate is:

- `vector_overlay_boundary_minimal_extraction_gate_after_a1_macro_review`

That later gate would still need explicit authorization. This document does not authorize source movement.

## Do-not-fix-yet register

Do not modify, move, import, instantiate, execute, or read:

- `render_core/vector_overlay_boundary.py`
- `taichi_global_bathymetry.py`
- `GeoVectorLineOverlay`
- provider/cache loaders or real GeoJSON/Natural Earth/hydrology cache
- projection, flip, or mask formulas
- `mask_overlay_to_globe`
- controller dirty/reload mutations
- alpha/apply/composition hot path
- metadata sidecar writer or artifact writer
- SQL/MySQL/WebSocket/AIS live path
- Qt/VisPy/Taichi runtime host

## Boundary Statement

Docs/test-only vector overlay boundary minimal extraction planning gate. No helper module creation, no source movement, no production source change, no controller/provider/cache runtime, no real GeoJSON/cache read, no runtime execution, no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_boundary_minimal_extraction_planning_gate_ready_for_o1_review`

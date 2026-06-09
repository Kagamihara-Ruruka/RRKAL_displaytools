# Displaytools Vector Overlay Boundary Minimal Extraction Gate

## Scope

本文件記錄 `render_core/vector_overlay_boundary.py` 的第一刀 minimal extraction。此 slice 只移動 descriptor / policy / ledger 層：`BOUNDARY_SPECS`、`HYDROLOGY_SPECS` 兩個純 descriptor tables，以及新 helper module 中的 dict/list/scalar descriptor builders。

本輪不移動 `GeoVectorLineOverlay`，不移動 provider/cache loader，不移動 projection/flip/mask formula，不移動 controller dirty/reload mutation，不觸碰 alpha/apply/composition hot path，不執行 runtime，不讀 real GeoJSON/Natural Earth/hydrology cache，不連 SQL/WebSocket/AIS live，不改 metadata/output schema。

## a_1 macro observer accepted summary

`a_1` macro observer report read:

- `L:\RRKAL_lab\external_research\analysis\a1_vector_overlay_boundary_minimal_extraction_macro_observer.zh-TW.md`

Accepted summary:

- Descriptor / policy / ledger is a coherent first-cut craton.
- `GeoVectorLineOverlay` remains blocked as runtime overlay class.
- Provider/cache loader remains blocked.
- Projection/mask formula remains blocked.
- Controller dirty/reload mutation remains blocked.
- `a_1` recommends proceeding only if stop lines remain explicit and `o_1` reviews before commit.

## Exact symbols moved

| symbol | old owner | new owner | line anchor evidence | movement type |
| --- | --- | --- | --- | --- |
| `BOUNDARY_SPECS` | `taichi_global_bathymetry.py` | `render_core/vector_overlay_boundary.py` | current `taichi_global_bathymetry.py:4257` before slice | pure descriptor table |
| `HYDROLOGY_SPECS` | `taichi_global_bathymetry.py` | `render_core/vector_overlay_boundary.py` | current `taichi_global_bathymetry.py:4289` before slice | pure descriptor table |

## Descriptor builders introduced in helper

These are descriptor/policy/ledger builders only. They are not runtime adapters and do not execute providers, controller mutation, projection, mask, cache lifecycle, or writers.

| helper | purpose |
| --- | --- |
| `build_vector_overlay_descriptor` | combines overlay kind, provider ref, projection label, mask label, and cache status descriptors |
| `build_vector_provider_ref_descriptor` | provider reference descriptor as data only |
| `build_vector_dirty_reload_ledger_descriptor` | dirty/reload ledger descriptor without controller mutation |
| `build_vector_controller_registry_descriptor` | controller registry descriptor without controller import or mutation |
| `build_vector_projection_policy_label_descriptor` | projection policy label only |
| `build_vector_mask_policy_label_descriptor` | mask policy label only |
| `build_vector_cache_status_label_descriptor` | cache status label only |
| `boundary_specs_descriptor` | returns a copy of `BOUNDARY_SPECS` |
| `hydrology_specs_descriptor` | returns a copy of `HYDROLOGY_SPECS` |

## Explicit symbols excluded

| excluded surface | reason |
| --- | --- |
| `GeoVectorLineOverlay` | runtime overlay class with camera, flip, mask, and render parameters |
| actual provider/cache loader | reads provider/cache state and constructs runtime overlays |
| projection formula | formula-bearing camera/flip behavior |
| mask clipping formula | pixel alpha behavior |
| controller dirty flag mutation | controller state mutation |
| controller reload request mutation | controller state and provider refresh mutation |
| alpha/apply/composition hot path | pixel composition/apply path |
| metadata/artifact writer | output schema/artifact behavior |
| SQL/WebSocket/AIS live path | live/runtime IO |
| Qt/VisPy/Taichi runtime host | runtime/UI/GPU dependency |

## Fixture parity coverage

Focused tests live in:

- `tests/test_displaytools_vector_overlay_boundary.py`

Coverage:

- helper module import is safe.
- exact key-set parity for extracted descriptor tables and descriptor builders.
- deterministic repeat-call parity.
- empty provider descriptor branch.
- malformed provider descriptor branch.
- dirty/reload clean descriptor branch.
- dirty/reload reload descriptor branch.
- projection/mask label-only branch.
- cache status label-only branch.
- no runtime dependency claim.
- no forbidden string-as-executable leakage.
- import-boundary checker candidate PASS.

## Import-boundary checker result

Expected result for current helper:

- `candidate_exists=true`
- `boundary_passed=true`
- `violations=[]`

The checker remains a static AST checker and does not import or execute the target module.

## taichi_global_bathymetry.py diff summary

Expected monolith diff:

- adds import/re-export wiring from `render_core.vector_overlay_boundary`.
- removes local `BOUNDARY_SPECS` and `HYDROLOGY_SPECS` table definitions.
- keeps all existing call sites resolving the same symbol names.
- does not touch `GeoVectorLineOverlay`, provider/cache loaders, projection/mask formulas, controller mutation, alpha/apply/composition hot path, metadata/output writer, or runtime behavior.

## Source-map / smoke reference audit

No smoke/source-map script update was required in this slice. Existing static source-map checks did not depend on physical ownership of these descriptor tables.

Full smoke was not run because this slice did not modify smoke/source-map scripts and required validation did not request full smoke.

## Boundary Statement

Minimal descriptor/policy/ledger-only vector overlay boundary extraction after a_1 macro observer. No `GeoVectorLineOverlay` movement, no provider/cache loader movement, no projection/flip/mask formula movement, no controller dirty/reload mutation movement, no alpha/apply/composition hot path change, no runtime execution, no real GeoJSON/cache read, no SQL/WebSocket/AIS live access, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_boundary_minimal_extraction_ready_for_o1_review`

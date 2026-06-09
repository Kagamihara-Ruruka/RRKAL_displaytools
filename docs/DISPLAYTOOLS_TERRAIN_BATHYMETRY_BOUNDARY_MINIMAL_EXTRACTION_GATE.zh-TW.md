# Displaytools Terrain/Bathymetry Boundary Minimal Extraction Gate

## Scope

本文件記錄 terrain/bathymetry boundary minimal extraction gate。此 slice 建立 `render_core\terrain_bathymetry_boundary.py`，只放入 descriptor / policy / ledger helper，不搬 provider/cache loader，不搬 sampling/bump/shader formula，不搬 projection/flip/lighting formula，不碰 runtime/controller，不改 palette behavior。

本輪沒有修改 `taichi_global_bathymetry.py`。原因是 monolith 目前沒有同名的 descriptor / policy / ledger helper definitions 可刪除；新增 helper 是 descriptor-only first-cut，不改現有 runtime call site。

## a_1 macro observer accepted summary

`a_1` macro observer conclusion: `accept_with_conditions`.

Accepted conditions applied in this slice:

- extraction stays descriptor / policy / ledger only
- no provider/cache loader
- no sampling/bump/shader formula
- no projection/flip/lighting formula
- no Taichi/Qt/VisPy/runtime/controller
- no palette behavior
- import-boundary checker must pass
- no safe-to-extract, visual, performance, readiness, or bug-fix claim

The lab report file was read as required, but its terminal-rendered content was not quoted because the display was not reliable. The explicit dispatch summary above is the accepted condition set for this product slice.

## Helper module introduced

New helper module:

- `render_core\terrain_bathymetry_boundary.py`

The module contains pure Python descriptor builders only. It imports only:

- `from __future__ import annotations`

## Exact helpers introduced

| helper | purpose | movement boundary |
| --- | --- | --- |
| `build_terrain_bathymetry_source_descriptor` | source label descriptor | no provider/cache execution |
| `build_terrain_height_field_descriptor` | height-field descriptor | no sampling or shader height lookup |
| `build_terrain_fallback_no_data_descriptor` | fallback/no-data descriptor | no synthetic terrain behavior movement |
| `build_terrain_lod_resolution_label_descriptor` | LOD/resolution label descriptor | no resolution or sampling behavior change |
| `build_terrain_cache_status_label_descriptor` | cache hit/miss/unknown label descriptor | no cache lifecycle execution |
| `build_terrain_palette_style_label_descriptor` | palette/style label descriptor | no visual palette behavior movement |
| `build_terrain_known_fault_ledger_descriptor` | unresolved known fault ledger | no bug-fix or visual readiness claim |
| `terrain_bathymetry_boundary_descriptor` | aggregate boundary descriptor | descriptor/policy/ledger only |
| `terrain_bathymetry_planning_bundle` | planning bundle with guard flags | no source movement authorization |

## Explicit symbols excluded

Excluded from this extraction:

- `load_topography`
- `synthetic_topography` behavior
- NOAA / GEBCO / ETOPO provider execution
- topography cache read/write/load/save
- terrain sampling formula
- bump / normal formula
- raymarch / sphere intersection / shader height lookup
- `flip_longitude` / `flip_latitude` formula
- `compute_sun_direction`
- `light_dir` / `dot_l` / twilight formula
- `TaichiGlobeRenderer`
- Qt/VisPy host surfaces
- runtime GUI/controller behavior
- water/land palette behavior
- metadata/artifact writers
- alpha/apply/composition hot path

## Descriptor constraints

All helper outputs are:

- deterministic
- dict/list/scalar only
- exact key-set fixture tested
- repeat-call fixture tested
- string labels only for cache, LOD, bump, lighting, palette, fallback, known fault, projection, and flip vocabulary

Every direct descriptor builder includes guard fields:

- `runtime_dependency_allowed = False`
- `provider_cache_execution_allowed = False`
- `shader_formula_allowed = False`
- `projection_lighting_formula_allowed = False`
- `visual_behavior_change_allowed = False`

The aggregate descriptor and planning bundle include:

- `source_movement_authorized = False`
- `runtime_render_invoked = False`
- `runtime_merge_enabled = False`
- `visual_parity_ready = False`
- `performance_ready = False`
- `readiness_claimed = False`

## Import-boundary checker result

Checker:

- `scripts\validate_displaytools_terrain_bathymetry_import_boundary.py`

Candidate:

- `render_core\terrain_bathymetry_boundary.py`

Expected result:

- `candidate_exists=true`
- `boundary_passed=true`
- `violations=[]`

The checker remains AST-only and does not import or execute the target module.

## Fixture parity coverage

Focused tests live in:

- `tests\test_displaytools_terrain_bathymetry_boundary_helpers.py`

Coverage:

- helper import safety
- exact key-set parity for every descriptor builder
- deterministic repeat-call parity
- dict/list/scalar-only output
- cache hit / cache miss / unknown label descriptor branches
- fallback/no-data descriptor branch
- LOD/resolution label branch
- palette/style label-only branch
- known fault ledger branch
- planning bundle guard flags
- no runtime/readiness claims

Import-boundary tests also verify:

- candidate target passes
- negative self-test still passes

## Source-map / smoke reference audit

This helper family has no smoke/source-map script owner in this slice. No smoke/source-map script update was needed. Full renderer smoke was not run because the boundary remains no-renderer and no runtime behavior changed.

## Cut-out note

- Lines removed from `taichi_global_bathymetry.py`: 0
- `taichi_global_bathymetry.py` touched: no
- Helper module added: `render_core\terrain_bathymetry_boundary.py`
- Symbols moved from monolith: none
- Symbols introduced: the descriptor/policy/ledger helpers listed above

## Boundary Statement

Minimal descriptor/policy/ledger-only terrain/bathymetry boundary extraction after a_1 macro observer. No provider/cache loader movement, no real terrain/cache/provider read, no sampling/bump/shader formula movement, no projection/flip/lighting formula movement, no renderer/Qt/VisPy/Taichi runtime execution, no controller behavior movement, no palette behavior change, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_terrain_bathymetry_boundary_minimal_extraction_ready_for_o1_review`

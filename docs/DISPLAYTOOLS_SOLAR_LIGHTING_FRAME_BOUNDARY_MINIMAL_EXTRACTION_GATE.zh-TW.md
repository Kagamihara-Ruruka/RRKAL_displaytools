# Displaytools Solar/Lighting Frame Boundary Minimal Extraction Gate

## Scope

本文件記錄 Solar / Lighting Frame 的 minimal extraction slice。此 slice 在 a_1 macro observer `accept_with_conditions` 後建立 `render_core\solar_lighting_frame_boundary.py`，內容只限 descriptor / policy / ledger 外殼。

本 slice 不修改 `taichi_global_bathymetry.py`，因為 monolith 內沒有同名 descriptor/policy/ledger 靜態表可做 import/re-export wiring。它不移動或修改 `compute_sun_direction`、real clock / timezone / datetime conversion、sun-vector / altitude / azimuth formula、`light_dir`、`dot_l`、Lambertian / twilight / terminator formula、world normal / bumped normal / shader / sampling / projection / flip formula、Taichi / Qt / VisPy / controller runtime。

## a_1 macro observer summary

Read:

- `L:\RRKAL_lab\external_research\analysis\a1_solar_lighting_frame_minimal_extraction_macro_observer.zh-TW.md`

Decision:

- `accept_with_conditions`

Accepted conditions applied here:

- extraction remains descriptor / policy / ledger only
- no real clock execution
- no solar formula movement
- no lighting shader formula movement
- no projection/flip formula movement
- no renderer/runtime/controller movement
- import-boundary checker must pass
- no Taipei local-noon fix claim
- no visual/performance/readiness/bug-fix claim

## Exact helpers introduced

New helper module:

- `render_core\solar_lighting_frame_boundary.py`

Introduced helpers:

- `build_solar_time_source_descriptor`
- `build_solar_direction_label_descriptor`
- `build_solar_twilight_terminator_label_descriptor`
- `build_solar_local_noon_fault_ledger_descriptor`
- `build_solar_coordinate_dependency_label_descriptor`
- `build_solar_lighting_consumer_layers_descriptor`
- `build_solar_forbidden_formula_surface_ledger_descriptor`
- `solar_lighting_frame_boundary_descriptor`
- `solar_lighting_planning_bundle`

Helper content is limited to:

- dict/list/scalar descriptor builders
- string labels as data
- unresolved fault ledger data
- guard flags showing runtime/formula/readiness behavior is not authorized

## Explicit symbols excluded

Excluded from this slice:

- `compute_sun_direction`
- current time acquisition
- UTC/local-time conversion
- real clock dependency
- solar vector / altitude / azimuth formula
- `light_dir`
- `dot_l`
- Lambertian lighting formula
- twilight / terminator formula
- world normal / bumped normal lighting formula
- longitude/latitude flip formula
- projection frame coupling
- grid/starfield frame coupling
- `TaichiGlobeRenderer`
- Qt/VisPy host surfaces
- runtime GUI/controller behavior
- terrain shader / sampling / bump formula
- metadata/artifact writers
- alpha/apply/composition hot path

## Fixture parity coverage

Focused tests live in:

- `tests/test_displaytools_solar_lighting_frame_boundary_helpers.py`

Coverage:

- helper module import is safe
- exact key-set parity for every descriptor builder
- deterministic repeat-call parity
- dict/list/scalar-only output
- time source label branch
- sun direction label branch
- twilight/terminator label branch
- local-noon unresolved fault ledger branch
- coordinate dependency label branch
- lighting consumer layer descriptor branch
- forbidden formula surface ledger branch
- planning bundle guard flags
- no runtime/readiness claims

## Import-boundary checker result

The existing checker:

- `scripts\validate_displaytools_solar_lighting_frame_import_boundary.py`

is expected to pass on:

- `render_core\solar_lighting_frame_boundary.py`

The helper keeps forbidden words such as `projection`, `flip`, `twilight`, `world_normal`, and `bump_normal` as string labels only. The checker still blocks executable imports, declarations, name references, attribute references, or call targets for forbidden families.

## Source-map / smoke reference audit

This slice does not modify smoke or source-map scripts.

Reason:

- no runtime behavior changed
- no monolith symbols were moved
- no source-map script currently owns the solar/lighting descriptor helper family
- helper is descriptor-only and covered by focused unit tests plus import-boundary checker

## Cut-out note

- Lines removed from monolith: 0
- `taichi_global_bathymetry.py` touched: no
- Helper module added: `render_core\solar_lighting_frame_boundary.py`
- Net source movement: descriptor/policy/ledger helper module added only

## Boundary Statement

Minimal descriptor/policy/ledger-only solar/lighting frame boundary extraction after a_1 macro observer. No real clock/render/provider execution, no solar/lighting/projection/flip formula movement, no renderer/Qt/VisPy/Taichi runtime execution, no controller behavior movement, no metadata/output schema change, no runtime merge enablement, and no visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_solar_lighting_frame_boundary_minimal_extraction_ready_for_o1_review`

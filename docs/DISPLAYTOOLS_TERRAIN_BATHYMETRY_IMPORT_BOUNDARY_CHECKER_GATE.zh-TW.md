# Displaytools Terrain/Bathymetry Import Boundary Checker Gate

## Scope

本文件是 tooling/docs-only terrain/bathymetry import-boundary checker gate。目標是為未來假想 target `render_core\terrain_bathymetry_boundary.py` 建立 AST-only 檢查器，確保未來 descriptor-only helper 不會混入 provider/cache、shader formula、projection/lighting、renderer runtime 或 metadata/artifact writer。

本輪不建立 `render_core\terrain_bathymetry_boundary.py`，不建立 helper module，不移動 source，不修改 production source，不 import 或 execute target module，不執行 renderer / Qt / VisPy / Taichi runtime，不讀 real terrain/cache/provider，不改 shader、sampling、bump、projection、flip 或 lighting formula，也不宣稱修復 visual fault 或授權 extraction。

## Checker behavior

Checker script:

- `scripts/validate_displaytools_terrain_bathymetry_import_boundary.py`

Checker tests:

- `tests/test_displaytools_terrain_bathymetry_import_boundary.py`

Default target:

- `render_core\terrain_bathymetry_boundary.py`

Required behavior:

| condition | expected behavior |
| --- | --- |
| missing candidate | JSON pass, `candidate_exists=false`, `status=not_applicable_candidate_missing`, `boundary_passed=true`, exit code 0 |
| existing candidate pass | JSON pass, `candidate_exists=true`, `boundary_passed=true`, `violations=[]`, exit code 0 |
| forbidden import/name hit | JSON fail, `boundary_passed=false`, nonzero exit, violation includes `kind` and `forbidden_family` |
| syntax error | JSON fail, `status=syntax_error`, nonzero exit |
| negative self-test | `negative_self_test_passed=true` and `all_forbidden_snippets_detected=true` |

The checker uses Python stdlib `ast` only and never imports or executes the target module.

## AST coverage

The checker inspects:

- `ast.Import`
- `ast.ImportFrom`
- `ast.Name`
- `ast.Attribute`
- `ast.Call` function targets
- `ast.FunctionDef.name`
- `ast.AsyncFunctionDef.name`
- `ast.ClassDef.name`

Declaration-name checks are required so a future candidate cannot re-declare forbidden names such as `load_topography`, `cache_hit`, or `TaichiGlobeRenderer`.

## Forbidden family coverage

| family | examples |
| --- | --- |
| `monolith` | `taichi_global_bathymetry` |
| `runtime_ui_gpu` | `taichi`, `PyQt6`, `PySide6`, `vispy`, `QtHybridWindow`, `VisPyHybridViewer`, `TaichiGlobeRenderer` |
| `data_provider_cache_execution` | `numpy`, `xarray`, `netCDF4`, `requests`, `urllib`, `download`, `fetch`, `load_topography`, `synthetic_topography`, `GEBCO`, `ETOPO`, `NOAA`, `cache_hit`, `cache_miss`, `topography_cache`, provider cache |
| `shader_sampling_bump` | `sample_lon`, `sample_lat`, terrain sampling, `bump`, `normal`, `raymarch`, sphere intersection, height lookup |
| `projection_flip_lighting` | `flip_longitude`, `flip_latitude`, `compute_sun_direction`, `light_dir`, `dot_l`, `twilight`, `projection`, `mask_overlay_to_globe` |
| `runtime_controller` | `HybridRenderController`, reload mutation, GUI/event loop |
| `hot_path` | `alpha_compose`, `alpha_blend_compose`, `alpha_compose_transparent`, `build_layer_render_plan_apply_path`, `apply_layer_render_plan_composition` |
| `artifact_metadata` | metadata sidecar writer, artifact writer, state writer, PNG writer, runtime JSON writer |
| `live_source_paths` | SQL, WebSocket, AIS, ADS-B |

## Allowed string-label distinction

Harmless string labels are allowed as data:

- `"cache_hit"`
- `"cache_miss"`
- `"lod"`
- `"resolution"`
- `"bump"`
- `"lighting"`
- `"palette"`
- `"fallback"`
- `"known_fault"`
- `"projection"`
- `"flip"`

Executable imports, declarations, name references, attribute references, or call targets using those forbidden families fail. This distinction lets descriptor packets preserve label vocabulary without importing provider/cache, shader, projection, lighting, runtime, or writer behavior.

## Negative self-test result

The checker includes `--self-test-negative` with test-local in-memory snippets only. It does not write product files and does not import target modules. The self-test covers monolith import, runtime/UI/GPU imports, data/provider/cache imports and names, sampling/bump names, projection/lighting names, controller/runtime names, hot-path imports, metadata/artifact writer names, live source names, and forbidden declaration names.

## Import-boundary checker need assessment

This checker is a precondition for any future descriptor-only helper movement. It does not authorize source movement by itself. A later movement slice would still need:

- a safe target helper proposal
- fixture parity for descriptor builders
- `a_1` macro observer review if required by the planning gate
- `o_1` review authorization

## Explicit exclusions

Excluded from this gate:

- helper module creation
- source movement
- production source changes
- monolith import
- renderer / Qt / VisPy / Taichi runtime execution
- real terrain/cache/provider reads
- provider/cache loader execution
- shader/sampling/bump/projection/flip/lighting formula changes
- metadata/output schema changes
- runtime merge enablement
- visual/performance/readiness/bug-fix claims

## Boundary Statement

Tooling/docs-only terrain/bathymetry import-boundary checker gate. No helper module creation, no source movement, no production source change, no monolith import, no renderer/Qt/VisPy/Taichi runtime execution, no real terrain/cache/provider read, no shader/sampling/bump/projection/flip/lighting formula change, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_terrain_bathymetry_import_boundary_checker_ready_for_o1_review`

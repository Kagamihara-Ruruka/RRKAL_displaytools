# Displaytools Solar/Lighting Frame Import Boundary Checker Gate

## Scope

本文件是 tooling/docs-only import-boundary checker gate，用來替未來假想 target `render_core\solar_lighting_frame_boundary.py` 建立 AST-only 安全門。此 gate 不建立 helper module，不移動 source，不修改 production source，不執行 target module，也不修光照或台北正午暗半球 fault。

Checker 只允許 descriptor-only helper 保留字串標籤與 dict/list/scalar 資料。若 candidate helper 出現 real clock execution、solar formula、lighting shader formula、projection/flip formula、renderer runtime、controller/runtime、metadata/artifact writer、alpha/apply/composition hot path，checker 必須回報 JSON fail。

## Checker behavior

Checker script:

- `scripts/validate_displaytools_solar_lighting_frame_import_boundary.py`

Default target:

- `render_core\solar_lighting_frame_boundary.py`

Required behavior:

- AST-only; does not import or execute the target module.
- Missing candidate returns JSON pass with `status = not_applicable_candidate_missing`.
- Existing descriptor-only candidate returns JSON pass with `violations = []`.
- Forbidden import/name/declaration/call returns JSON fail and nonzero exit.
- Syntax error returns JSON fail with `status = syntax_error`.
- `--self-test-negative` uses in-memory snippets and writes no product target file.

JSON output includes:

- `schema`
- `target`
- `candidate_exists`
- `status`
- `boundary_passed`
- `violations`
- `checked_imports`
- `checked_names`
- `forbidden_families`

## Forbidden family coverage

| family | blocked examples |
| --- | --- |
| `monolith` | `taichi_global_bathymetry` |
| `runtime_ui_gpu` | `taichi`, `PyQt6`, `PySide6`, `vispy`, `QtHybridWindow`, `VisPyHybridViewer`, `TaichiGlobeRenderer` |
| `real_clock_time_execution` | `datetime`, `time`, `timezone`, `utcnow`, `now`, `timestamp`, `localtime`, `fromtimestamp` |
| `solar_formula` | `compute_sun_direction`, `sun_vector`, `solar_altitude`, `solar_azimuth`, `julian`, `ephemeris` |
| `lighting_shader_formula` | `light_dir`, `dot_l`, `Lambert`, `Lambertian`, `twilight`, `terminator_formula`, `n_world`, `n_world_bump`, `normal` |
| `projection_flip` | `flip_longitude`, `flip_latitude`, `projection`, `mask_overlay_to_globe`, `rotate_view_to_world` |
| `terrain_shader_hot_path` | `sample_lon`, `sample_lat`, terrain sampling, `bump`, `raymarch`, sphere intersection, height lookup |
| `runtime_controller` | `HybridRenderController`, GUI/event loop, renderer mutation names |
| `hot_path` | alpha helpers, `build_layer_render_plan_apply_path`, `apply_layer_render_plan_composition` |
| `artifact_metadata` | metadata sidecar writer, artifact writer, state writer, PNG writer, runtime JSON writer |

## Allowed string-label distinction

The checker allows harmless string labels as data:

- `"time_source"`
- `"utc_local_ambiguity"`
- `"sun_direction"`
- `"local_noon_fault"`
- `"twilight"`
- `"terminator"`
- `"coordinate_dependency"`
- `"lighting_consumer"`
- `"world_normal"`
- `"bump_normal"`
- `"projection"`
- `"flip"`

The same words are blocked when they appear as executable imports, declarations, direct name references, attribute references, or call targets. This distinction keeps descriptor/policy/ledger data usable while preventing hidden runtime/formula dependencies.

## Tests

Focused tests live in:

- `tests/test_displaytools_solar_lighting_frame_import_boundary.py`

The tests cover:

- missing candidate CLI JSON pass
- valid descriptor-only candidate pass
- forbidden import fail
- forbidden import-from fail
- forbidden direct name reference fail
- forbidden attribute reference fail
- forbidden call target fail
- forbidden class definition fail
- forbidden function definition fail
- forbidden async function definition fail
- syntax error JSON fail
- allowed string labels pass
- `--self-test-negative` pass and all forbidden snippets detected

## Boundary Statement

Tooling/docs-only solar/lighting frame import-boundary checker gate. No helper module creation, no source movement, no production source change, no monolith import, no renderer/Qt/VisPy/Taichi runtime execution, no real clock/render/provider execution, no compute_sun_direction/sun-vector/light_dir/dot_l/twilight/normal/projection/flip formula change, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_solar_lighting_frame_import_boundary_checker_ready_for_o1_review`

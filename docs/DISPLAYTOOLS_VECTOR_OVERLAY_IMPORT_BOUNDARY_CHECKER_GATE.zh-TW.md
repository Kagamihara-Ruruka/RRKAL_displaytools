# Displaytools Vector Overlay Import Boundary Checker Gate

## Scope

本文件是 tooling/docs-only 的 vector overlay import-boundary checker gate。目標是為未來可能出現的 `render_core/vector_overlay_boundary.py` helper candidate 預先定義 AST-only import/name 邊界。

本輪不建立 `render_core/vector_overlay_boundary.py`，不移動 source，不修改 `taichi_global_bathymetry.py`，不執行 controller/provider/cache/runtime，不讀 real GeoJSON、Natural Earth、hydrology cache，不改 projection、flip、mask formula，不碰 alpha/apply/composition hot path，也不宣稱 safe-to-extract、bug fixed、visual parity、performance、readiness 或 runtime merge。

## Evidence sources

| source | evidence level | use |
| --- | --- | --- |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_COORDINATE_SYNC_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | vector coordinate sync descriptor boundary |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_MONKEY_PATCH_CRATON_ABLATION_GATE.zh-TW.md` | `product_docs_evidence` | vector overlay dependency footprint |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_PROVIDER_BOUNDARY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | provider/cache descriptor boundary |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_CONTROLLER_REGISTRY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | controller registry seam |
| `docs/DISPLAYTOOLS_VECTOR_OVERLAY_DIRTY_RELOAD_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence` | dirty/reload ledger and checker-gate recommendation |

## Checker behavior

Checker script:

- `scripts/validate_displaytools_vector_overlay_import_boundary.py`

Default target:

- `render_core/vector_overlay_boundary.py`

The checker:

- uses Python stdlib `ast`.
- does not import or execute the target module.
- emits JSON on stdout.
- returns exit code `0` for missing candidate or boundary pass.
- returns nonzero exit code for forbidden import/name hits or syntax errors.
- supports `--self-test-negative`.

Required JSON fields:

- `schema`
- `target`
- `candidate_exists`
- `status`
- `boundary_passed`
- `violations`
- `checked_imports`
- `checked_names`
- `forbidden_families`

Missing candidate behavior:

- `candidate_exists=false`
- `status=not_applicable_candidate_missing`
- `boundary_passed=true`
- exit code `0`

Negative self-test behavior:

- `negative_self_test_passed=true`
- `all_forbidden_snippets_detected=true`
- no product file writes.

## Forbidden family coverage

| family | examples |
| --- | --- |
| monolith | `taichi_global_bathymetry` |
| Qt / VisPy / Taichi | `PyQt6`, `PySide6`, `vispy`, `taichi` |
| GPU / dataframe / render-heavy | `numpy`, `pandas`, `datashader` |
| provider/cache/runtime | executable `GeoJSON`, `NaturalEarth`, `hydrology`, provider cache, `load_natural_earth`, `load_hydrology`, `download`, `fetch`, `cache_hit`, `cache_miss` references |
| SQL / live stream | `pymysql`, `sqlalchemy`, `websocket`, `AISStream`, ADS-B live names |
| controller / renderer | `HybridRenderController`, `TaichiGlobeRenderer`, `QtHybridWindow`, `VisPyHybridViewer`, `GeoVectorLineOverlay` |
| hot path | `alpha_compose`, `alpha_blend_compose`, `alpha_compose_transparent`, `build_layer_render_plan_apply_path`, `apply_layer_render_plan_composition` |
| artifact / metadata | metadata sidecar writer, artifact writer, state writer, PNG writer, runtime JSON writer |

## Allowed string-label distinction

The checker blocks executable imports and AST name references. It does not block harmless string labels.

Allowed examples as data labels:

- `"cache_hit"`
- `"cache_miss"`
- `"GeoJSON descriptor"`
- `"projection"`
- `"mask"`
- `"Natural Earth label"`

Forbidden examples as executable references:

- `from provider_cache_loader import cache_hit`
- `return cache_hit`
- `from natural_earth_loader import load_natural_earth`
- `return GeoVectorLineOverlay`

This distinction is required because previous fixture gates intentionally preserve `cache`, `GeoJSON`, `projection`, and `mask` as descriptor vocabulary.

## Checker tests

Focused tests live in:

- `tests/test_displaytools_vector_overlay_import_boundary.py`

They cover:

- missing candidate PASS.
- valid pure descriptor candidate PASS.
- forbidden import FAIL.
- forbidden from-import FAIL.
- forbidden direct name reference FAIL.
- forbidden controller/runtime name FAIL.
- forbidden provider/cache executable name FAIL.
- allowed string label PASS.
- malformed Python FAIL with JSON output.
- CLI JSON shape.
- `--self-test-negative` PASS.

## Do-not-fix-yet Register

Do not modify these areas in this slice:

- `taichi_global_bathymetry.py`
- `render_core/vector_overlay_boundary.py`
- production controller/renderer/provider/cache runtime
- `GeoVectorLineOverlay`
- Natural Earth, hydrology, boundary, GeoJSON, provider, or cache files
- projection, flip, mask, or depth formulas
- alpha helpers and `build_layer_render_plan_apply_path`
- SQL/MySQL/WebSocket/AIS live access
- metadata sidecar writer and artifact writer paths

## Boundary Statement

Tooling/docs-only vector overlay import-boundary checker gate. No helper module creation, no source movement, no production source change, no controller/provider/cache runtime, no real GeoJSON/cache read, no runtime execution, no projection/flip/mask formula change, no SQL/WebSocket/AIS live access, no artifact writer execution, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_vector_overlay_import_boundary_checker_ready_for_o1_review`

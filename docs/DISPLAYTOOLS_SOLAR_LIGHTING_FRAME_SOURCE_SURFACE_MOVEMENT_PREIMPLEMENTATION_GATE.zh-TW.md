# Displaytools Solar/Lighting Frame Source Surface Movement Preimplementation Gate

## Scope

本文件是 docs/test-only preimplementation gate，用來把 Solar / Lighting Frame 大部分成 source-surface 類別。它只判斷哪些 surface 可被視為 descriptor / policy / ledger 的未來第一刀候選，哪些仍屬 time runtime、solar formula、lighting shader formula、projection/flip dependency 或 renderer runtime。

本 gate 不授權 source movement，不建立 helper module，不修改 production source，不執行 renderer / Qt / VisPy / Taichi，不讀 real clock，不修台北正午暗半球，也不宣稱 safe-to-extract、bug fixed、visual parity、performance readiness 或 runtime readiness。

## Evidence read

| source | evidence level | use |
| --- | --- | --- |
| `tests/test_displaytools_solar_lighting_frame_boundary.py` | `fixture_evidence` | solar/lighting descriptor names, fault labels, blocked formula surfaces, and no-runtime guard shape |
| `docs/DISPLAYTOOLS_SOLAR_LIGHTING_FRAME_BOUNDARY_FIXTURE_GATE.zh-TW.md` | `product_docs_evidence_with_display_mojibake_caution` | boundary intent only; no text copied because terminal display showed existing unreadable characters |
| `tests/test_displaytools_terrain_bathymetry_source_surface_movement.py` | `format_reference` | source-surface matrix shape for descriptor/policy/ledger versus runtime blockers |
| `tests/test_displaytools_vector_overlay_source_surface_movement.py` | `format_reference` | first-cut decision wording and blocked-surface pattern |
| `docs/DOCS_INDEX.zh-TW.md` | `product_docs_index` | index placement for the new gate |

## Surface category matrix

| category | first-cut status | surfaces |
| --- | --- | --- |
| `category_a_descriptor_policy_ledger` | candidate for planning only | time source descriptor, sun direction label descriptor, twilight/terminator label descriptor, local-noon fault ledger, coordinate dependency label, lighting consumer layer descriptor, forbidden formula surface ledger |
| `category_b_time_source_runtime` | blocked | current time acquisition, UTC/local-time conversion, real clock dependency |
| `category_c_solar_formula` | blocked | `compute_sun_direction`, solar vector formula, sun altitude/azimuth or date/time math |
| `category_d_lighting_shader_formula` | blocked | `light_dir`, `dot_l`, Lambertian lighting, twilight formula, world normal lighting, bumped normal lighting |
| `category_e_projection_flip_dependency` | blocked | longitude/latitude flip coupling, projection frame coupling, grid/starfield frame coupling |
| `category_f_runtime_renderer_host` | blocked | Taichi renderer class, Qt/VisPy host, runtime GUI/controller behavior |

## First-cut candidate summary

The only allowed first-cut planning surface is:

- `category_a_descriptor_policy_ledger`

Allowed candidate families:

- time source descriptor
- sun direction label descriptor
- twilight/terminator label descriptor
- local-noon fault ledger
- coordinate dependency label
- lighting consumer layer descriptor
- forbidden formula surface ledger

These are planning candidates only. They can describe labels, consumers, diagnostics, and prohibitions as dict/list/scalar data, but they cannot carry formula behavior, runtime time acquisition, renderer host behavior, projection/flip behavior, or any claim that the fault is fixed.

Required decision values pinned by the fixture:

- `source_movement_authorized = false`
- `solar_lighting_extraction_candidate = false`
- `solar_lighting_planning_candidate = true`
- `local_noon_fault_resolved = false`
- `compute_sun_direction_formula_allowed = false`
- `lighting_shader_formula_allowed = false`
- `projection_flip_formula_allowed = false`

## Blocked surface summary

Blocked from any first cut:

- current time acquisition
- UTC/local-time conversion
- real clock dependency
- `compute_sun_direction`
- solar vector formula
- sun altitude/azimuth or date/time math
- `light_dir`
- `dot_l`
- Lambertian lighting
- twilight formula
- world normal lighting
- bumped normal lighting
- longitude/latitude flip coupling
- projection frame coupling
- grid/starfield frame coupling
- Taichi renderer class
- Qt/VisPy host
- runtime GUI/controller behavior

These surfaces remain outside descriptor/policy/ledger ownership because they can affect rendered lighting, coordinate alignment, time behavior, or runtime host state.

## Local-noon fault status

The Taipei local-noon dark-side candidate remains unresolved.

This gate may record it as `local-noon fault ledger` data, but it must not:

- claim the local-noon fault is fixed
- change `compute_sun_direction`
- change `light_dir`
- change `dot_l`
- change twilight, normal, projection, or flip formula
- execute renderer/runtime checks to prove visual behavior

## Import-boundary checker need assessment

No import-boundary checker is required yet.

Reason:

- There is no safe helper target identified in this slice.
- The first-cut candidate is still planning-only descriptor/policy/ledger data.
- A checker should be introduced only after a descriptor-only helper target is named and before any source movement.

## Recommended next gate

Recommended next gate:

- `solar_lighting_frame_boundary_minimal_extraction_planning_gate`

That planning gate should still be docs/test-only. It should name a hypothetical descriptor-only target, define candidate descriptor helper families, block time/runtime/formula surfaces, and require another review before movement.

## Validation scope

Focused tests live in:

- `tests/test_displaytools_solar_lighting_frame_source_surface_movement.py`

The tests pin:

- exact source-surface categories
- category A as the only planning candidate
- category B through F as blocked from first cut
- local-noon fault unresolved status
- formula blockers for `compute_sun_direction`, `light_dir`, `dot_l`, twilight, normal, projection, and flip surfaces
- no monolith/runtime import shape
- no safe-to-extract, bug-fix, visual parity, performance readiness, or runtime readiness claim

## Boundary Statement

Docs/test-only solar/lighting frame source surface movement preimplementation gate. No production source change, no helper module creation, no source movement, no monolith import, no renderer/Qt/VisPy/Taichi runtime execution, no real clock/render/provider execution, no compute_sun_direction/sun-vector/light_dir/dot_l/twilight/normal/projection/flip formula change, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_solar_lighting_frame_source_surface_movement_preimplementation_gate_ready_for_o1_review`

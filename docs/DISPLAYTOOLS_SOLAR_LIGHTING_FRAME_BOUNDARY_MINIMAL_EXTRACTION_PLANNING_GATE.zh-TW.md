# Displaytools Solar/Lighting Frame Boundary Minimal Extraction Planning Gate

## Scope

本文件是 docs/test-only planning gate，用來把 Solar / Lighting Frame 的 `category_a_descriptor_policy_ledger` 收斂成未來第一刀候選清單。它只規劃假想 helper target，不建立 helper module，不移動 source，不修改 production source，也不修光照。

假想 target:

- `render_core\solar_lighting_frame_boundary.py`

本 gate 不授權 real clock execution、`compute_sun_direction`、solar vector formula、`light_dir`、`dot_l`、twilight formula、normal formula、projection/flip formula、renderer runtime、Qt/VisPy/Taichi host、controller behavior、metadata/output writer、alpha/apply/composition hot path。

## Evidence read

| source | evidence level | use |
| --- | --- | --- |
| `tests/test_displaytools_solar_lighting_frame_boundary.py` | `fixture_evidence` | descriptor names, local-noon unresolved ledger, and blocked formula surfaces |
| `tests/test_displaytools_solar_lighting_frame_source_surface_movement.py` | `fixture_evidence` | category A candidate set and category B through F blockers |
| `docs/DISPLAYTOOLS_SOLAR_LIGHTING_FRAME_SOURCE_SURFACE_MOVEMENT_PREIMPLEMENTATION_GATE.zh-TW.md` | `product_docs_evidence` | source-surface decision output and next-gate recommendation |
| `tests/test_displaytools_terrain_bathymetry_boundary_minimal_extraction_planning.py` | `format_reference` | planning packet shape, candidate entry shape, blocked entry shape, and checker-need wording |
| `docs/DOCS_INDEX.zh-TW.md` | `product_docs_index` | index placement for this planning gate |

## Candidate target summary

| field | value |
| --- | --- |
| `first_cut_target_candidate` | `render_core\solar_lighting_frame_boundary.py` |
| `source_movement_authorized` | `false` |
| `helper_module_creation_authorized` | `false` |
| `solar_lighting_extraction_candidate` | `false` |
| `solar_lighting_planning_candidate` | `true` |
| `local_noon_fault_resolved` | `false` |
| `a1_macro_observer_required_before_source_movement` | `true` |

This is a planning gate only. The target path is hypothetical and must not be created in this slice.

## Candidate descriptor families

Every candidate is limited to dict/list/scalar descriptor builders or policy/ledger tables.

| candidate | planned target name | required fixture | forbidden next action |
| --- | --- | --- | --- |
| `build_solar_time_source_descriptor` | `build_solar_time_source_descriptor` | time source descriptor exact key-set and repeat-call parity | do not execute real clock or change time source |
| `build_solar_direction_label_descriptor` | `build_solar_direction_label_descriptor` | sun direction label-only parity | do not move or execute `compute_sun_direction` |
| `build_solar_twilight_terminator_label_descriptor` | `build_solar_twilight_terminator_label_descriptor` | twilight/terminator label-only parity | do not change twilight or terminator formula |
| `build_solar_local_noon_fault_ledger_descriptor` | `build_solar_local_noon_fault_ledger_descriptor` | local-noon unresolved ledger parity | do not claim Taipei local-noon fix |
| `build_solar_coordinate_dependency_label_descriptor` | `build_solar_coordinate_dependency_label_descriptor` | coordinate dependency label-only parity | do not change projection or flip formula |
| `build_solar_lighting_consumer_layers_descriptor` | `build_solar_lighting_consumer_layers_descriptor` | lighting consumer descriptor parity | do not change lighting consumer behavior |
| `build_solar_forbidden_formula_surface_ledger_descriptor` | `build_solar_forbidden_formula_surface_ledger_descriptor` | forbidden formula ledger parity | do not move or modify solar/lighting formula |
| `solar_lighting_frame_boundary_descriptor` | `solar_lighting_frame_boundary_descriptor` | aggregate descriptor exact key-set parity | do not include time runtime, formula, or renderer host |
| `solar_lighting_planning_bundle` | `solar_lighting_planning_bundle` | bundle key-set and blocked-surface declaration parity | do not authorize source movement inside bundle |

Each candidate must keep:

- `candidate_for_minimal_extraction = true`
- `runtime_dependency_allowed = false`
- `real_clock_execution_allowed = false`
- `solar_formula_allowed = false`
- `lighting_shader_formula_allowed = false`
- `projection_flip_formula_allowed = false`
- `visual_behavior_change_allowed = false`

## Blocked surface summary

Blocked from the first cut:

- current time acquisition
- UTC/local-time conversion
- real clock dependency
- `compute_sun_direction`
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

These surfaces remain blocked because they can affect time behavior, lighting pixels, coordinate alignment, renderer runtime state, output artifacts, or composition hot paths.

## Local-noon fault status

The Taipei local-noon dark-side candidate remains unresolved.

This planning gate may include `build_solar_local_noon_fault_ledger_descriptor` as a future ledger candidate, but the ledger must not:

- claim the fault is fixed
- execute renderer/runtime checks
- change time source behavior
- change solar direction formula
- change lighting formula
- change normal, projection, or flip formula

## Fixture parity plan

Future extraction planning must require:

- exact key-set parity for descriptor builders
- deterministic repeat-call parity
- time source descriptor branch
- sun direction label-only branch
- twilight/terminator label-only branch
- local-noon fault unresolved ledger branch
- coordinate dependency label-only branch
- lighting consumer layer descriptor branch
- forbidden formula surface ledger branch
- future import-boundary checker candidate pass
- future forbidden runtime/formula dependency fail

## Import-boundary checker need assessment

A future import-boundary checker is required before extraction.

Current status:

- `required_before_extraction = true`
- `required_now = false`
- `future_checker_target = render_core\solar_lighting_frame_boundary.py`

Reason:

- This slice is planning-only.
- No helper module is created.
- A checker should be introduced after this planning gate and before any source movement.

## a_1 macro observer requirement

`a_1` macro observer review is required before source movement.

Questions for that observer:

- Are the candidate descriptor families still one descriptor/policy/ledger craton.
- Did any time runtime, formula, projection/flip, renderer, or controller behavior leak into the candidate set.
- Does the local-noon fault ledger remain unresolved.
- Is there a smaller first-cut candidate than the listed aggregate target.
- Is additional historical or horizontal graph evidence needed before movement.

## Recommended next gate

Recommended next gate:

- `solar_lighting_frame_import_boundary_checker_gate`

That next gate should still be tooling/docs-only. It should validate a missing candidate target, allow string labels, and block real clock execution, solar formula, lighting shader formula, projection/flip formula, renderer runtime, metadata/artifact writers, and alpha/apply/composition hot paths.

## Boundary Statement

Docs/test-only solar/lighting frame boundary minimal extraction planning gate. No helper module creation, no source movement, no production source change, no monolith import, no renderer/Qt/VisPy/Taichi runtime execution, no real clock/render/provider execution, no compute_sun_direction/sun-vector/light_dir/dot_l/twilight/normal/projection/flip formula change, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_solar_lighting_frame_boundary_minimal_extraction_planning_gate_ready_for_o1_review`

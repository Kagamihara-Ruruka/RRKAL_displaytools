# Displaytools Solar/Lighting Frame Boundary Fixture Gate

## Scope

本文件是 test/docs-only solar/lighting frame boundary fixture gate。目標是先測繪 Solar / Lighting Frame 大部的外圍，包括時間來源、太陽方向、world normal consumer、bump normal consumer、twilight / terminator label、local-noon fault ledger、coordinate-frame dependency、lighting consumer layers，以及 forbidden formula surfaces。

本輪不修改 production source，不建立 helper module，不移動任何 source symbol，不 import 或執行 `taichi_global_bathymetry.py`，不啟動 renderer / Qt / VisPy / Taichi runtime，不讀 real terrain/cache/provider，不修改 `compute_sun_direction`、`light_dir`、`dot_l`、twilight / terminator formula、world normal / bumped normal formula、projection / flip formula、terrain shader / sampling / bump formula，也不宣稱修復台北正午暗半球。

## Evidence read

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `static_source_evidence` | `compute_sun_direction`, `light_dir`, `dot_l`, `n_world`, `n_world_bump`, twilight, and lighting consumer anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_static_evidence` | historical comparison for the same solar/lighting responsibility family |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_OWNERSHIP_DIAGNOSTIC_GATE.zh-TW.md` | `product_docs_evidence` | coordinate frame inventory, Taipei local-noon dark-side candidate, and do-not-fix-yet list |
| terrain/bathymetry boundary gates | `product_docs_evidence` | terrain/bump normal consumer and blocky terrain/bump debt stop lines |
| historical view-cone / craton docs | `product_docs_evidence` | solar/lighting active-fault context and no direct formula-change route |
| vector overlay gates | `format_reference` | descriptor matrix style and boundary wording |

## Descriptor contract

Every descriptor has exactly these fields:

- `surface_name`
- `source_evidence`
- `input_frame`
- `consumer_layers`
- `policy_labels`
- `known_faults`
- `fixture_status`
- `forbidden_next_action`

Allowed `fixture_status` values:

- `pinned`
- `unresolved_static_only`
- `blocked_hot_path`

## Solar/lighting boundary matrix

| descriptor_id | surface_name | input_frame | consumer_layers | policy_labels | known_faults | fixture_status | forbidden_next_action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `time_source_descriptor` | time source descriptor | UTC/local time source label | sun direction descriptor, static frozen-light fallback label | UTC time label, local time ambiguity label | UTC/local-time source ambiguity label | `unresolved_static_only` | do not change time source or `compute_sun_direction` |
| `sun_direction_descriptor` | sun direction descriptor | solar direction label | `light_dir` consumer, `dot_l` lighting consumer | sun vector label, frozen light label | Taipei local-noon dark-side candidate | `blocked_hot_path` | do not execute or move `compute_sun_direction` |
| `world_normal_consumer_descriptor` | world normal consumer descriptor | world normal frame label | grid, base lighting, terrain geometry | `n_world` label | world normal versus sample frame dependency unresolved | `unresolved_static_only` | do not change world normal formula |
| `bump_normal_consumer_descriptor` | bump normal consumer descriptor | bumped normal frame label | terrain lighting, ocean specular, bump normal diagnostics | `n_world_bump` label, bump normal label | blocky terrain/bump debt, local-noon diagnostic depends on normal consumer | `blocked_hot_path` | do not change bump or normal formula |
| `twilight_terminator_label_descriptor` | twilight / terminator label descriptor | terminator label only | terrain lighting, terminator diagnostics | twilight label, terminator label | twilight formula unresolved | `unresolved_static_only` | do not change twilight or terminator formula |
| `local_noon_fault_ledger_descriptor` | local-noon fault ledger descriptor | diagnostic ledger label | solar frame diagnostics, terrain sample frame diagnostics | Taipei local-noon fault label | Taipei local-noon dark-side candidate remains unresolved | `unresolved_static_only` | do not claim Taipei local-noon fix |
| `coordinate_frame_dependency_descriptor` | coordinate frame dependency descriptor | coordinate dependency labels | solar lighting, grid/starfield, terrain sampling | longitude flip dependency label, latitude flip dependency label, grid/starfield dependency label | lighting frame relation to flipped sample frame unresolved | `unresolved_static_only` | do not change projection, flip, or grid formula |
| `lighting_consumer_layers_descriptor` | lighting consumer layers descriptor | consumer layer label | terrain, bathymetry, ocean, cloud, grid dependency | terrain bump lighting consumer label, world normal consumer label | consumer split requires diagnostic only | `pinned` | do not change lighting consumer behavior |
| `forbidden_formula_surface_descriptor` | forbidden formula surface descriptor | formula surface labels only | solar lighting hot path, terrain shader hot path | blocked formula surface label | formula movement blocked | `blocked_hot_path` | do not move or modify solar, lighting, normal, projection, or flip formula |

## Fixture cases added

Focused tests live in:

- `tests/test_displaytools_solar_lighting_frame_boundary.py`

The test module covers:

- Taipei local-noon diagnostic label
- UTC/local-time source ambiguity label
- `compute_sun_direction` formula surface blocked
- `light_dir` vector consumer blocked
- `dot_l` / Lambertian lighting formula blocked
- twilight / terminator label-only descriptor
- world normal vs bumped normal consumer split
- terrain/bump lighting consumer label
- grid/starfield coordinate dependency label
- longitude flip dependency label
- latitude flip dependency label
- static/frozen-light fallback label
- no-runtime/no-renderer guard flags

The tests use only pure dict/list/scalar descriptors and do not import `taichi_global_bathymetry.py`.

## Known unresolved faults

| fault | fixture treatment | blocked implementation action |
| --- | --- | --- |
| Taipei local-noon dark-side candidate | unresolved fault ledger only | do not claim a fix or alter solar formula |
| UTC/local-time source ambiguity | time source label only | do not change time source behavior |
| solar direction frame relation to terrain sample frame | descriptor-only dependency label | do not change `compute_sun_direction`, `light_dir`, or `dot_l` |
| world normal vs bumped normal consumer split | consumer split descriptor | do not change world normal or bump normal formula |
| twilight / terminator formula ambiguity | label-only descriptor | do not change twilight or terminator formula |
| longitude/latitude flip dependency | coordinate dependency descriptor | do not change projection or flip formula |

## Explicit exclusions

Excluded from this gate:

- production `.py` source changes
- helper module creation
- source movement
- monolith import
- renderer / Qt / VisPy / Taichi runtime execution
- real terrain/cache/provider reads
- `compute_sun_direction` execution or movement
- `light_dir`, `dot_l`, twilight / terminator formula changes
- world normal / bumped normal formula changes
- projection / flip formula changes
- terrain shader / sampling / bump formula changes
- metadata/output schema changes
- runtime merge enablement
- visual/performance/readiness/bug-fix claims

## Recommended next gate

Recommended next gate:

- `solar_lighting_frame_source_surface_movement_preimplementation_gate`

Reason:

- The boundary matrix identifies descriptor-only labels and formula-bearing hot paths.
- A source-surface movement map should decide whether any time/source/fault ledger labels are dry enough for planning.
- Direct solar formula, normal formula, projection/flip, or runtime implementation remains blocked.

Alternative if `o_1` wants a narrower diagnostic first:

- `solar_frame_local_noon_fault_diagnostic_gate`

That gate should still remain fixture/docs-only and must not modify formulas.

## Boundary Statement

Test/docs-only solar/lighting frame boundary fixture gate. No production source change, no helper module creation, no source movement, no monolith import, no renderer/Qt/VisPy/Taichi runtime execution, no real terrain/cache/provider read, no compute_sun_direction/light_dir/dot_l/twilight/normal/projection/flip formula change, no metadata/output schema change, no runtime merge enablement, and no safe-to-extract/visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_solar_lighting_frame_boundary_fixture_gate_ready_for_o1_review`

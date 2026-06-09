# Displaytools Terrain/Bathymetry Boundary Fixture Gate

## Scope

本文件是 test/docs-only terrain/bathymetry boundary fixture gate。目標是先把地形 / 水深大部的外圍責任釘住，包含資料來源標籤、height-field / raster descriptor、sampling frame、flip policy label、LOD / resolution label、bump / normal consumer label、lighting consumer label、water / land palette label、cache hit/miss label，以及 blocky terrain artifact descriptor。

本輪不修改 production source，不移動 source symbol，不 import 或執行 `taichi_global_bathymetry.py`，不啟動 renderer / Qt / VisPy / Taichi runtime，不讀 real terrain/cache/provider，不修改 shader、terrain sampling、projection、flip、mask 或 lighting formula，也不修 blocky terrain、左右反、光照、海水粗糙等 visual fault。

## Evidence read

| source | evidence level | use |
| --- | --- | --- |
| current `taichi_global_bathymetry.py` | `static_source_evidence` | GEBCO/topography cache, synthetic fallback, terrain sampling, masks, bump normal, lighting, palette, and cache anchors |
| `d90b645:taichi_global_bathymetry.py` | `git_static_evidence` | 14k basement comparison for the same terrain/bathymetry responsibility families |
| `docs/DISPLAYTOOLS_GLOBE_COORDINATE_FIXTURE_DESIGN_GATE.zh-TW.md` | `product_docs_evidence` | coordinate frame and terrain sample ownership boundaries |
| `docs/DISPLAYTOOLS_RENDER_GLOBE_CRATON_AGE_TABLE_AND_TECTONIC_CLOSEOUT_MAP.zh-TW.md` | `product_docs_evidence` | terrain/bathymetry as deep craton and diagnostic-first candidate |
| `docs/DISPLAYTOOLS_HISTORICAL_VIEW_CONE_FIRST_CONTINENT_DECISION_GATE.zh-TW.md` | `product_docs_evidence` | first-continent ranking and terrain sampling/bump stop line |
| lab-only geologic maps | `lab_summary_evidence` | summarized context only; not copied as product source of truth |

## Descriptor contract

Every fixture descriptor has exactly these fields:

- `surface_name`
- `source_evidence`
- `input_frame`
- `sampling_frame`
- `consumer_layers`
- `policy_labels`
- `known_faults`
- `fixture_status`
- `forbidden_next_action`

Allowed `fixture_status` values:

- `pinned`
- `unresolved_static_only`
- `blocked_hot_path`

## Terrain/bathymetry boundary matrix

| case_id | surface_name | input_frame | sampling_frame | consumer_layers | policy_labels | known_faults | fixture_status | forbidden_next_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ocean_depth_sample` | bathymetry depth sample | GEBCO/synthetic height-field descriptor | terrain sample frame with `sample_lon/sample_lat` | terrain shader, water material label, bathymetry layer | bathymetry source, water depth | blocky terrain artifact unresolved | `pinned` | do not execute renderer or modify shader formula |
| `land_elevation_sample` | land elevation sample | height-field descriptor | terrain sample frame with land/elevation threshold | terrain shader, land palette label, land mask consumer | elevation source, land palette | blocky terrain artifact unresolved | `pinned` | do not execute renderer or modify shader formula |
| `coast_transition_sample` | coast transition sample | height-field plus land/water mask descriptor | terrain sample frame with coast mix | terrain shader, land/water palette label, sea-level label | coast transition, sea-level policy | coastline classification static-only | `unresolved_static_only` | do not execute renderer or modify shader formula |
| `no_data_fallback_terrain` | no-data fallback terrain | fallback terrain descriptor | synthetic height-field descriptor | terrain shader, startup progress label | fallback terrain, no-data | provider/cache execution not covered | `unresolved_static_only` | do not download or read real topography cache |
| `longitude_flip_label` | longitude flip label | raw lon/lat descriptor | flipped terrain sample frame label | terrain sampling, bump normal consumer, water material label | `flip_longitude` label | East/West orientation split candidate | `pinned` | do not execute renderer or modify shader formula |
| `latitude_flip_label` | latitude flip label | raw lon/lat descriptor | flipped terrain sample frame label | terrain sampling, bump normal consumer, water material label | `flip_latitude` label | latitude flip authority unresolved | `pinned` | do not execute renderer or modify shader formula |
| `lod_resolution_label` | LOD/resolution label | topography step descriptor | height-field resolution label | terrain source selector, cache descriptor, renderer input shape label | topo step, resolution | LOD/resolution does not prove sampling quality | `pinned` | do not execute renderer or modify shader formula |
| `bump_normal_consumer_label` | bump/normal consumer label | height-field descriptor | bump normal consumer label | lighting, terrain shader, ocean material | bump scale, normal consumer | blocky terrain/bump debt | `blocked_hot_path` | do not change bump or normal formula |
| `lighting_consumer_label` | lighting consumer label | world normal descriptor | lighting frame label | solar lighting, terrain shader, ocean specular | light direction, bumped normal | Taipei local-noon dark-side candidate | `blocked_hot_path` | do not change lighting formula |
| `water_land_palette_label` | water/land palette label | height-field plus land/water mask descriptor | palette/style label | terrain shader, water material, land palette | water palette, land palette, style profile | style label does not authorize visual parity | `pinned` | do not execute renderer or modify shader formula |
| `cache_hit_descriptor` | cache hit descriptor | topography cache descriptor | cache status label | provider/cache boundary, terrain source selector | cache hit label | cache lifecycle not covered | `pinned` | do not read or write cache |
| `cache_miss_descriptor` | cache miss descriptor | topography cache descriptor | cache status label | provider/cache boundary, terrain source selector | cache miss label | cache download/write not covered | `unresolved_static_only` | do not download or write cache |
| `blocky_terrain_artifact_descriptor` | blocky terrain artifact descriptor | visual fault descriptor | artifact label only | terrain sampling diagnostics, bump normal diagnostics | blocky terrain fault label | blocky terrain unresolved; no bug fix claim | `unresolved_static_only` | do not fix terrain sampling or bump formula |

## Fixture cases added

Focused tests live in:

- `tests/test_displaytools_terrain_bathymetry_boundary.py`

The test module covers:

- ocean depth sample
- land elevation sample
- coast transition sample
- no-data / fallback terrain
- longitude flip label
- latitude flip label
- LOD/resolution label
- bump/normal consumer label
- lighting consumer label
- water/land palette label
- cache hit descriptor
- cache miss descriptor
- blocky terrain artifact descriptor

The tests use only pure dict/list/scalar descriptors and do not import `taichi_global_bathymetry.py`.

## Known unresolved faults

| fault | fixture treatment | blocked implementation action |
| --- | --- | --- |
| blocky terrain sampling/bump debt | `unresolved_static_only` or `blocked_hot_path` descriptor | do not change sampling or bump normal formula |
| East/West orientation split | longitude flip label only | do not change `flip_longitude` behavior |
| latitude flip authority | latitude flip label only | do not change `flip_latitude` behavior |
| Taipei local-noon dark-side candidate | lighting consumer label only | do not change `light_dir`, `n_world`, or `n_world_bump` formula |
| coastline / land-water classification ambiguity | static descriptor only | do not execute Natural Earth, GEBCO, or mask provider |
| cache hit/miss lifecycle ambiguity | cache status label only | do not read, write, download, or evict cache |

## Explicit exclusions

Excluded from this gate:

- production `.py` source changes
- source movement
- monolith import
- renderer / Qt / VisPy / Taichi runtime
- real GEBCO/NOAA/Natural Earth/cache/provider reads
- shader, terrain sampling, projection, flip, mask, lighting formulas
- blocky terrain, orientation, lighting, water roughness, or visual fault fixes
- `GeoVectorLineOverlay`
- AIS/aircraft, SQL/WebSocket, metadata/output schema, artifact writer

## Recommended next gate

Recommended next gate:

- `terrain_bathymetry_source_surface_movement_preimplementation_gate`

Reason:

- The boundary matrix identifies descriptor-only surfaces, provider/cache surfaces, sampling-frame labels, and hot-path consumers.
- A source-surface movement map should decide which descriptor/policy labels, if any, are dry enough for a later planning gate.
- Direct shader, sampling, bump, lighting, provider/cache, or visual-fault implementation remains blocked.

Alternative if `o_1` wants a narrower path:

- `terrain_sampling_frame_import_boundary_checker_gate`

This should only happen after a pure descriptor helper candidate exists.

## Boundary Statement

Test/docs-only terrain/bathymetry boundary fixture gate. No production source change, no source movement, no monolith import, no renderer/Qt/VisPy/Taichi runtime execution, no real terrain/cache/provider read, no shader/projection/flip/mask/lighting formula change, no metadata/output schema change, no runtime merge enablement, and no visual/performance/readiness/bug-fix claim.

## Final Classification

`c3_displaytools_terrain_bathymetry_boundary_fixture_gate_ready_for_o1_review`

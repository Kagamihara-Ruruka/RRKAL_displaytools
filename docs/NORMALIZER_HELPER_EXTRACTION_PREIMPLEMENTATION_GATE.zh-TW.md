# Normalizer Helper Extraction Preimplementation Gate

## TL;DR

This gate defines the evidence required before any future helper extraction for `normalize_ais_frame` and `normalize_aircraft_frame`.

Current status: fixture observability exists, but helper movement is not authorized by this document.

This is a docs/evidence-only preimplementation gate. It does not change source code, tests, scripts, renderer behavior, metadata behavior, output behavior, or runtime behavior.

## Extraction boundary inventory

Candidate functions:

| candidate | source anchor | current classification | required dependencies if moved | forbidden dependencies |
| --- | --- | --- | --- | --- |
| `normalize_ais_frame` | `taichi_global_bathymetry.py:1286` | future candidate only | `find_column`, `normalize_name`, `LAT_ALIASES`, `LON_ALIASES`, `COLUMN_ALIASES`, `pd` | renderer/controller state, Qt, VisPy, Taichi runtime, file/cache/artifact writes, metadata sidecar writer, parser functions, provider/source loading |
| `normalize_aircraft_frame` | `taichi_global_bathymetry.py:1331` | future candidate only | `find_column`, `normalize_name`, `LAT_ALIASES`, `LON_ALIASES`, `AIRCRAFT_COLUMN_ALIASES`, `pd`, `np` | renderer/controller state, Qt, VisPy, Taichi runtime, file/cache/artifact writes, metadata sidecar writer, parser functions, provider/source loading |

Shared dependencies:

- `normalize_name`
- `find_column`
- `LAT_ALIASES`
- `LON_ALIASES`
- `COLUMN_ALIASES`
- `AIRCRAFT_COLUMN_ALIASES`
- `pandas as pd`
- `numpy as np`

Observed source evidence:

- Normalizers transform in-memory `pd.DataFrame` inputs.
- Normalizers do not read files.
- Normalizers do not write cache entries.
- Normalizers do not create preview artifacts.
- Normalizers do not call renderer/controller methods.
- Normalizers do not launch Qt, VisPy, or Taichi runtime.
- Normalizers do not call parser functions; they consume already-parsed DataFrames.

## Possible future module shape

Possible future module:

```text
render_core/dataframe_normalizers.py
```

Potential contained symbols:

- `normalize_name`
- `find_column`
- `LAT_ALIASES`
- `LON_ALIASES`
- `COLUMN_ALIASES`
- `AIRCRAFT_COLUMN_ALIASES`
- `normalize_ais_frame`
- `normalize_aircraft_frame`

Hard constraints for the future module:

- It must keep public behavior equivalent for current fixture coverage.
- It must pass normalizer fixture tests before and after movement.
- It must not import renderer/controller modules.
- It must not import Qt, VisPy, or Taichi runtime modules.
- It must not add dynamic import, plugin, dependency-injection, or runtime discovery behavior.
- It must not read provider/source data.
- It must not write files, cache, state, PNG, or runtime JSON artifacts.

This module shape is a candidate only. It is not approved for implementation in this checkpoint.

## Before/after parity requirements

Before any future helper movement, run and compare:

```powershell
py -3 -m unittest tests.test_dataframe_normalizers
py -3 -m unittest tests.test_dataframe_parsers
py -3 -m unittest tests.test_generated_artifact_audit
py -3 -B scripts\generated_artifact_audit_leaf_provider.py
```

Additional required evidence:

- Import scan proving the candidate helper module does not import renderer, Qt, VisPy, Taichi runtime, provider/source loader, parser dispatcher, metadata sidecar writer, or artifact writer modules.
- `git diff` proving any future `taichi_global_bathymetry.py` change is limited to import and delegation wiring.
- Artifact audit proving no `state/`, PNG, or runtime JSON artifacts are produced or staged.
- Explicit confirmation that metadata behavior and output behavior are unchanged.
- Explicit confirmation that helper movement is not being treated as performance work.

Any future movement must stop if fixture behavior changes, import boundaries widen, or source changes exceed import/delegation wiring.

## Risk table

| risk | evidence currently available | gate required before future extraction | stop condition |
| --- | --- | --- | --- |
| alias map drift risk | Alias maps are shared globals in `taichi_global_bathymetry.py`. | Snapshot fixture coverage for canonical and alias columns. | Alias list movement changes selected columns. |
| `find_column` normalized-name collision behavior | Current fixture pins last-column-wins behavior for normalized collisions. | Keep collision test passing before and after any movement. | Candidate helper changes collision resolution. |
| dtype coercion drift | Fixture tests pin numeric coercion for selected AIS and aircraft fields. | Confirm coercion with `pd.to_numeric(..., errors="coerce")` remains equivalent. | Pandas conversion behavior is changed by wrapper logic. |
| `np.nan` serialization boundary risk | Missing aircraft speed defaults to `np.nan`; tests use `pd.isna`. | Keep this as DataFrame behavior only; do not add JSON serialization behavior here. | Future task tries to validate JSON serialization in this helper gate. |
| pandas version behavior drift | Tests assert values and columns, not brittle exact dtype objects. | Continue avoiding exact dtype dependency unless product code depends on it. | Future tests overfit pandas internal dtype details. |
| accidental renderer import risk | Current normalizers do not need renderer modules. | Import scan for candidate helper module. | Candidate helper imports renderer/controller/Qt/VisPy/Taichi runtime. |
| accidental behavior change through column ordering | Empty schemas and optional output columns are now fixture-pinned. | Before/after fixture parity for output columns. | Column ordering differs without explicit approval. |
| false performance claim risk | Current work is fixture/evidence only. | Keep performance claims out of the helper movement gate. | Future report treats helper movement as optimization evidence. |

## Next-step recommendation

Branch options:

| branch | recommendation | reason |
| --- | --- | --- |
| A:補 normalizer fixture gaps | not next | Current first fixture set covers the requested AIS and aircraft matrix. |
| B:進行 actual normalizer helper extraction | not authorized | Gate exists, but movement still needs import-boundary checker and explicit review. |
| C:新增 extraction validator / import-boundary checker | recommended next | This is the smallest next evidence step before any physical helper movement. |
| D:轉向另一個小型 policy object / static packet builder | backlog | Viable later, but current normalizer thread should first close import-boundary evidence. |
| E:回 graph/risk map | not needed now | No contradiction was observed that requires returning to the broad graph. |

Recommended next c_3 slice: create an import-boundary checker or docs/test gate proving the future normalizer helper module can stay free of renderer, Qt, VisPy, Taichi runtime, provider/source loading, parser dispatch, metadata writer, and artifact writer dependencies.

## Not authorized

- Normalizer extraction.
- Parser extraction.
- Renderer/runtime parity claim.
- Visual parity claim.
- UI operation claim.
- Performance improvement claim.
- Runtime merge.
- Dynamic import/plugin/DI/runtime discovery introduction.
- Provider/source loading movement.
- Metadata sidecar or output artifact behavior changes.

## Boundary statement

Docs/evidence-only normalizer helper extraction preimplementation gate. No normalizer extraction, no parser extraction, no renderer/Qt/Taichi runtime execution, no metadata/output behavior change, no performance claim, no visual parity readiness claim, no helper movement approval.

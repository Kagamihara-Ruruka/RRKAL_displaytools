# Demo Readiness Baseline

Last evidence rerun: 2026-06-03 16:08 +08

Baseline command set:

| command | result | elapsed |
| --- | --- | --- |
| `scripts\render_quick_smoke.ps1` | PASS | 16.880 s |
| `scripts\render_repeated_quick_smoke.ps1 -Frames 3` | PASS | 41.187 s |
| `scripts\render_warm_frame_smoke.ps1` | PASS | 46.308 s |
| `scripts\render_warm_frame_smoke.ps1 -HighDensityCompose` | PASS | 40.156 s |
| `scripts\render_warm_frame_smoke.ps1 -RuntimeBlendTiming` | PASS | 36.591 s |
| `scripts\render_warm_frame_smoke.ps1 -HighDensityCompose -RuntimeBlendTiming` | PASS | 40.144 s |
| `scripts\smoke.ps1` | PASS | 171.640 s |

## Preview path status

- The renderer preview path emitted quick-smoke PNG, preview frame, and metadata artifacts.
- Repeated quick render completed 3 process-per-frame runs and emitted `state/showcase/repeated_quick_smoke/summary.json`.
- Warm-frame smoke completed in-process 3-frame evidence for default, high-density, runtime_blend timing, and high-density runtime_blend timing modes.
- Generated PNG/JSON/Markdown artifacts are local evidence under ignored `state/` paths and are not committed.

## Timing snapshot

| mode | first frame render | warm render avg | warm prepare avg | warm compose avg | final warm slowest phase |
| --- | ---: | ---: | ---: | ---: | --- |
| default warm-frame | 961.076 ms | 97.351 ms | 41.358 ms | 50.104 ms | `compose_overlays` |
| high-density warm-frame | 2148.813 ms | 570.805 ms | 506.326 ms | 59.380 ms | `compose_overlays` |
| runtime_blend timing | 949.788 ms | 77.123 ms | 37.300 ms | 34.716 ms | `compose_overlays` |
| high-density runtime_blend timing | 2648.251 ms | 519.712 ms | 454.564 ms | 58.088 ms | `compose_overlays` |

Repeated quick render remains process-per-frame evidence:

| frame | render | prepare_batches | compose_overlays | slowest phase |
| --- | ---: | ---: | ---: | --- |
| 1 | 957.338 ms | 917.199 ms | 35.611 ms | `prepare_batches` |
| 2 | 973.795 ms | 932.861 ms | 36.131 ms | `prepare_batches` |
| 3 | 1001.787 ms | 959.475 ms | 37.390 ms | `prepare_batches` |

Additional 5-frame process-per-frame stability rerun at 2026-06-03 16:20 +08:

| frame | render | prepare_batches | compose_overlays | slowest phase |
| --- | ---: | ---: | ---: | --- |
| 1 | 1202.949 ms | 1157.801 ms | 36.767 ms | `prepare_batches` |
| 2 | 973.808 ms | 933.590 ms | 35.392 ms | `prepare_batches` |
| 3 | 961.468 ms | 921.175 ms | 35.530 ms | `prepare_batches` |
| 4 | 967.843 ms | 927.154 ms | 36.071 ms | `prepare_batches` |
| 5 | 972.716 ms | 932.181 ms | 35.909 ms | `prepare_batches` |

Runtime-blend timing review:

| mode | runtime_blend runs | total avg | first-step avg | non-first avg | interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| default | 3 | 25.978 ms | 8.685 ms | 8.646 ms | roughly uniform steps |
| high-density | 6 | 49.950 ms | 8.436 ms | 8.303 ms | roughly uniform steps |

## Interpretation

- The quick and repeated quick paths are still dominated by `prepare_batches` because each run starts a renderer process.
- The 5-frame repeated quick rerun kept preview emission stable; frame 1 was slower than later runs, but all five runs remained in the same `prepare_batches` bottleneck class.
- In-process warm-frame evidence shifts the final warm-frame target toward `compose_overlays`.
- Runtime-blend cost scales roughly with step count in the current evidence.
- First runtime_blend step timing is close to later steps in this run, so data-ready wait remains possible but was not dominant in this baseline.
- This is not a UI interactive frame-rate claim. It is renderer preview and warm-frame evidence for demo-readiness judgment.

## Preview interaction readiness boundary

This baseline is renderer/preview artifact evidence only.

It does not prove:

- Qt event loop responsiveness.
- preview refresh timing inside the running UI.
- user interaction latency.
- interactive FPS readiness.
- full UI readiness.

The next UI-facing evidence gate is documented in `docs/PREVIEW_INTERACTION_READINESS_BOUNDARY.zh-TW.md`. Until that gate has UI-path evidence, demo-readiness wording must stay limited to renderer preview artifacts and warm-frame timing.

## Next safe action

Use the data-ready boundary timing gate before any deeper runtime_blend instrumentation:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\export_runtime_blend_data_ready_gate.ps1 -ContractOnly
```

Any deeper boundary timing should be reviewed as a separate renderer-core slice before commit. Do not use this baseline as approval for runtime_blend optimization, alpha/blending changes, layer ordering changes, metadata schema changes, runtime merge, or output pixel behavior changes.

## Data-ready gate baseline rerun

Rerun time: 2026-06-03 22:02 +08

| command | result | elapsed |
| --- | --- | ---: |
| `scripts\render_quick_smoke.ps1` | PASS | 29.417 s |
| `scripts\render_repeated_quick_smoke.ps1 -Frames 3` | PASS | 41.439 s |
| `scripts\render_repeated_quick_smoke.ps1 -Frames 5` | PASS | 66.601 s |
| `scripts\render_warm_frame_smoke.ps1` | PASS | 36.199 s |
| `scripts\render_warm_frame_smoke.ps1 -HighDensityCompose` | PASS | 43.916 s |
| `scripts\render_warm_frame_smoke.ps1 -RuntimeBlendTiming` | PASS | 34.737 s |
| `scripts\render_warm_frame_smoke.ps1 -HighDensityCompose -RuntimeBlendTiming` | PASS | 38.574 s |
| `scripts\smoke.ps1` | PASS | 266.525 s |

Latest 5-frame repeated quick summary:

| metric | value |
| --- | ---: |
| render avg | 966.313 ms |
| prepare_batches avg | 927.076 ms |
| compose_overlays avg | 34.454 ms |
| slowest phase ids | `prepare_batches` |

Latest runtime_blend timing summary:

| mode | runtime_blend runs | total avg | first-step avg | non-first avg |
| --- | ---: | ---: | ---: | ---: |
| default | 3 | 27.228 ms | 8.979 ms | 9.125 ms |
| high-density | 6 | 51.615 ms | 8.621 ms | 8.599 ms |

Interpretation:

- Preview artifacts and metadata were emitted during the repeated quick runs.
- Process-per-frame evidence remains dominated by `prepare_batches`.
- In-process warm-frame evidence still shifts the final warm target toward `compose_overlays`.
- First runtime_blend step timing was roughly uniform with later steps in both default and high-density timing modes.
- Data-ready wait remains possible but is not dominant in this rerun; the next safe classification remains `need_data_ready_boundary_timing_design`.

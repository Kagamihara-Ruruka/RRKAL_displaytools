# Layer Render Plan Compiled/Reused Packets Movement Preimplementation Gate

## Scope

This is a tooling/docs-only movement preimplementation gate for a possible future helper module:

- Future candidate path: `render_core/layer_render_plan_compiled_reused_packets.py`
- Current physical owner: `render_core/render_plan.py`

No helper module is created in this slice and no source is moved.

## Future helper family

The future checker boundary corresponds to these packet builders:

- `build_compiled_layer_render_plan_packet_from_adapter_payload`
- `build_reused_compiled_layer_render_plan_packet_from_adapter_payload`
- `build_compiled_layer_render_plan_packet`
- `build_reused_compiled_layer_render_plan_packet`

If future physical movement needs private scalar helpers such as `_payload_list`, `_payload_dict`, or `_payload_schema`, they must remain private implementation details and must not become new public helper surface.

## Allowed future ownership

A future helper may only own dict/list/scalar compiled/reused packet assembly.

Allowed data-field names include:

- `cache_key`
- `cache_status`
- `cache_reuse_decision`
- `metadata`
- `source`
- `apply_path`
- `batch_decisions`
- `runtime_path_unchanged`
- `runtime_optimization_applied`

These names are allowed only as packet fields or string labels. They do not authorize executable dependencies.

## Forbidden dependencies

The import-boundary checker rejects:

- monolith/controller imports or direct controller/runtime class and method references
- Qt, VisPy, Taichi, GPU, dataframe, datashader, and pyais dependencies
- `render_core.render_plan` imports
- alpha helper, apply-path behavior, and batch decision behavior dependencies
- metadata sidecar writer or artifact writer dependencies
- provider, source, loader, fetch, download, or cache lifecycle module dependencies
- parser or normalizer imports
- sibling extracted render-plan helper modules unless future o_1 review explicitly narrows that boundary
- existing policy helper modules/classes

## Status semantics

- `compiled` means packet status only; it does not prove the runtime compile path has been refactored.
- `reused` means packet status only; it does not prove cache lifecycle correctness.
- `apply_path` may appear as a packet data field only; apply-path behavior remains excluded.
- `batch_decisions` may appear as a packet data field only; batch decision behavior remains excluded.
- Future helper movement must not execute metadata sidecar writer or artifact writer code.

## Required future validation before movement

```powershell
py -3 -m unittest tests.test_layer_render_plan_compiled_reused_packets
py -3 -m unittest tests.test_layer_render_plan_compiled_reused_packets_import_boundary
py -3 -B scripts\validate_layer_render_plan_compiled_reused_packets_import_boundary.py render_core\layer_render_plan_compiled_reused_packets.py
py -3 -B scripts\validate_layer_render_plan_compiled_reused_packets_import_boundary.py --self-test-negative
py -3 -m unittest tests.test_generated_artifact_audit
py -3 -B scripts\generated_artifact_audit_leaf_provider.py
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\inspect_render_plan_compose_source_map.ps1
git diff --check
```

If physical movement happens later, smoke/source-map tooling must reflect the new physical source owner while keeping compatibility/provenance labels stable where tests require them.

## Boundary statement

Tooling/docs-only compiled/reused packet import-boundary checker and movement preimplementation gate. No helper module creation, no source movement, no alpha/apply path behavior test or change, no batch decision change, no metadata sidecar writer change, no artifact writer execution, no controller instantiation, no renderer/Qt/VisPy/Taichi runtime execution, no metadata/output schema change, no runtime merge enablement, and no pixel-equivalence/performance/readiness claim.

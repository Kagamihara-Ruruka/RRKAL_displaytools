# C3 Prior Semantic Dictionary YAML Skeleton Planning Gate

## 目的

本 gate 是 docs/test-only planning。它在 c_3 prior law material settlement 通過後，規劃未來先驗語意字典的 YAML skeleton 形狀、檔案邊界、top-level sections、entry shape、prior term families、stop-lines 與 validator expectations。

本 gate 不建立 YAML dictionary、不建立 schema、不建立 validator、不建立 contract test、不建立 prototype，也不執行 runtime 或 renderer。

## Evidence read

- `tests/test_displaytools_c3_prior_law_material_settlement.py`
- `docs/DISPLAYTOOLS_C3_PRIOR_LAW_MATERIAL_SETTLEMENT_GATE.zh-TW.md`
- `tests/test_displaytools_c3_prior_dictionary_international_law_registry.py`
- `docs/DISPLAYTOOLS_C3_PRIOR_DICTIONARY_INTERNATIONAL_LAW_REGISTRY_GATE.zh-TW.md`

## Future file topology planning

The following future files are planned only. They are not created in this gate.

```text
docs/c3_prior_dictionary/README.zh-TW.md
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json
scripts/validate_displaytools_c3_prior_semantic_dictionary.py
tests/test_displaytools_c3_prior_semantic_dictionary_contract.py
```

## YAML top-level section plan

```text
dictionary_metadata
authority_sources
phenomenon_translation_map
prior_terms
view_families
layer_taxonomy
recipe_authoring
c4_mediation
legacy_fossil_translation
stop_lines
unknown_stop_lines
validator_expectations
```

## Prior term family plan

Initial planned term families:

```text
composition_stack_prior
host_shell_docking_layout_prior
rendered_viewport_ui_prior
viewport_camera_transformation_prior
interaction_state_dispatcher_prior
temporal_playback_controller_prior
tabular_data_inspector_prior
plugin_extension_registry_prior
globe_view
map_projection_view
time_series_view
table_view
multi_view_layout
layered_occluding_body_visibility_contract
recipe_owns_truth_prior
c4_mediates_both_ingress_and_egress
multispatial_coordinate_transform_prior
declarative_alpha_compositing_policy
multiresolution_data_lod_prior
```

## Minimum entry shape plan

Each future prior term entry must be planned to include:

```text
term_id
definition
authority_family
source_evidence_refs
allowed_use
forbidden_use
example
counterexample
schema_field_candidate
validator_rule_candidate
prototype_behavior_candidate
stop_line
confidence
lifecycle_status
```

## Stop-line preservation summary

The future YAML skeleton must preserve these stop-lines:

```text
legacy_mask_direct_adoption_stop_line
projection_formula_stop_line
frame_buffer_truth_stop_line
transparent_globe_leak_unresolved_stop_line
render_if_needed_runtime_stop_line
renderer_controller_runtime_stop_line
prototype_authorization_stop_line
runtime_replacement_stop_line
host_shell_rendered_viewport_relation_stop_line
```

## YAML governance decision

- YAML is a human / agent-maintained semantic source.
- Runtime JSON may be compiled later, not now.
- Schema validator is planned, not created.
- No YAML file is created in this gate.
- No schema file is created in this gate.
- No validator script is created in this gate.
- No dictionary contract test is created in this gate.
- No term becomes implementation authorization by being planned.

## Decision output

```text
yaml_skeleton_planning_gate_passed = true
allowed_only_after_prior_law_settlement = true
settlement_passed = true
graphics_geospatial_materials_incorporated = true
yaml_dictionary_creation_authorized = false
schema_creation_authorized = false
prior_card_schema_creation_authorized = false
prototype_authorized = false
runtime_execution_authorized = false
product_source_change_authorized = false
formula_movement_authorized = false
c4_implementation_change_authorized = false
readiness_claimed = false
correctness_claimed = false
leak_fix_claimed = false
runtime_replacement_authorized = false
```

## Expected next gate

```text
c3_prior_semantic_dictionary_yaml_contract_gate
```

## Boundary statement

Docs/test-only c_3 prior semantic dictionary YAML skeleton planning gate. This gate plans future dictionary topology, sections, entry shape, prior term families, stop-lines, and validator expectations. It does not create YAML dictionary, schema files, validator scripts, contract tests, prototype code, runtime behavior, renderer behavior, formula movement, repo topology change, readiness claim, correctness claim, leak-fix claim, or runtime replacement authorization.

## Final classification

```text
c3_prior_semantic_dictionary_yaml_skeleton_planning_gate_committed_for_o1_review_no_push
```
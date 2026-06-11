# C3 Prior Semantic Dictionary YAML Contract Gate

## 摘要

本 gate 是 docs/test-only contract。它接在 c_3 prior semantic dictionary YAML skeleton planning 之後，先固定未來 YAML 字典的 section、entry、term、validator、stop-line、recipe、c_4 mediation 與 legacy fossil translation 不變量。

本 gate 不建立 YAML dictionary、不建立 schema、不建立 validator、不建立未來 dictionary contract test、不建立 prototype，也不執行 runtime 或 renderer。

## Evidence read

- `tests/test_displaytools_c3_prior_semantic_dictionary_yaml_skeleton_planning.py`
- `docs/DISPLAYTOOLS_C3_PRIOR_SEMANTIC_DICTIONARY_YAML_SKELETON_PLANNING_GATE.zh-TW.md`
- `tests/test_displaytools_c3_prior_law_material_settlement.py`
- `docs/DISPLAYTOOLS_C3_PRIOR_LAW_MATERIAL_SETTLEMENT_GATE.zh-TW.md`
- `tests/test_displaytools_c3_prior_dictionary_international_law_registry.py`
- `docs/DISPLAYTOOLS_C3_PRIOR_DICTIONARY_INTERNATIONAL_LAW_REGISTRY_GATE.zh-TW.md`

## Contract level

```text
semantic_dictionary_contract_only
```

此 gate 只固定未來字典的約束，不授權產生字典本體。

## Section contract summary

未來 YAML 必須只使用 skeleton planning gate 已規劃的 top-level sections。每個 section 都必須有 entry kind、required fields、forbidden fields。

Required sections:

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

## Prior term entry contract

每個 future prior term entry 必須保留 skeleton planning gate 規劃的 minimum entry shape:

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

Contract interpretation:

- `source_evidence_refs` 必須指向可追溯 evidence 或 local reference。
- `allowed_use` 與 `forbidden_use` 必須同時存在。
- `example` 與 `counterexample` 必須同時存在。
- `confidence` 必須允許 `evidence_gap`，讓不確定項不會被偽裝成確定項。
- `lifecycle_status` 必須能標示 `unknown_stop_line` 與 `legacy_fossil_evidence`。
- term entry 不得因為被列入字典而變成 implementation authorization。

## Initial term contract coverage

本 gate 要求所有 skeleton planning gate 已列出的 initial term families 都必須在 future validator 看到契約約束。

Examples:

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

## Validator rule contract

Future validator planning must preserve at least these invariant families:

```text
top_level_sections_exact_match
required_entry_fields_present
no_unknown_top_level_sections
no_bare_high_risk_term_ids
authority_refs_must_be_known_or_local_ref
legacy_fossils_must_require_translation
stop_lines_must_not_authorize_implementation
unknown_stop_lines_require_resolution_gate
recipe_must_own_truth
c4_mediation_required_for_ingress_and_egress
runtime_json_compilation_not_authorized
prototype_runtime_renderer_formula_changes_forbidden
```

## Bare-term rule

以下 high-risk bare terms 不能直接當作 future prior term id:

```text
layer
mask
view
projection
frame
render
recipe
```

它們必須被轉譯成 qualified term，例如 `composition_stack_prior`、`layered_occluding_body_visibility_contract`、`rendered_viewport_ui_prior`、`recipe_owns_truth_prior`。

## Stop-line contract

本 gate 保留既有 stop-lines，並新增 future creation stop-lines:

```text
legacy_mask_direct_adoption_stop_line
projection_formula_stop_line
frame_buffer_truth_stop_line
transparent_globe_leak_unresolved_stop_line
render_if_needed_runtime_stop_line
renderer_controller_runtime_stop_line
prototype_authorization_stop_line
runtime_replacement_stop_line
yaml_creation_stop_line
schema_creation_stop_line
validator_creation_stop_line
dictionary_contract_test_creation_stop_line
runtime_json_compilation_stop_line
```

## Future actual files remain absent

The following files are still future files only:

```text
docs/c3_prior_dictionary/README.zh-TW.md
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml
docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json
scripts/validate_displaytools_c3_prior_semantic_dictionary.py
tests/test_displaytools_c3_prior_semantic_dictionary_contract.py
```

## Decision output

```text
yaml_contract_gate_passed = true
skeleton_planning_gate_passed = true
settlement_passed = true
international_law_registry_passed = true
yaml_dictionary_creation_authorized = false
schema_creation_authorized = false
validator_script_creation_authorized = false
future_dictionary_contract_test_creation_authorized = false
prior_card_schema_creation_authorized = false
prototype_authorized = false
runtime_execution_authorized = false
runtime_json_compilation_authorized = false
renderer_behavior_change_authorized = false
formula_movement_authorized = false
c4_implementation_change_authorized = false
repo_topology_change_authorized = false
readiness_claimed = false
correctness_claimed = false
leak_fix_claimed = false
runtime_replacement_authorized = false
```

## Expected next gate

```text
c3_prior_semantic_dictionary_yaml_schema_validator_planning_gate
```

## Boundary statement

Docs/test-only c_3 prior semantic dictionary YAML contract gate. This gate fixes section, entry, term, validator, stop-line, recipe, c_4 mediation, and legacy-fossil invariants for a future YAML dictionary. It does not create YAML dictionary files, schema files, validator scripts, future dictionary contract tests, prototype code, runtime behavior, renderer behavior, formula movement, repo topology change, readiness claim, correctness claim, leak-fix claim, or runtime replacement authorization.

## Final classification

```text
c3_prior_semantic_dictionary_yaml_contract_gate_committed_for_o1_review_no_push
```

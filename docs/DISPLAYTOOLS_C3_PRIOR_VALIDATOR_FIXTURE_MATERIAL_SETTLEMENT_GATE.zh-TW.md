# C3 prior validator fixture material settlement gate

## Purpose

This docs and test gate settles the current validator fixture materials before any formal c_3 prior YAML dictionary is created.

The gate classifies lab evidence for validator positive fixtures, negative fixtures, failure card edges, and minimal entry shape pressure.

## Evidence read

- `L:/RRKAL_lab/external_research/analysis/c4_c3_validator_failure_card_edge_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c2_c3_display_hint_validator_negative_fixture_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/c1_c3_reference_envelope_validator_positive_fixture_scout.zh-TW.md`
- `L:/RRKAL_lab/external_research/analysis/a1_c3_prior_dictionary_minimal_yaml_entry_shape_scout.zh-TW.md`
- `tests/test_displaytools_c3_prior_semantic_dictionary_validator.py`
- `tests/test_displaytools_c3_prior_semantic_dictionary_schema_json_contract.py`
- `tests/test_displaytools_c3_prior_semantic_dictionary_yaml_schema_validator_planning.py`

Lab notes remain lab-only prose. This gate uses stable token-level material from those notes and does not adopt their prose as product dictionary text.

## Settlement categories

- `prior_dictionary_candidate`
- `schema_field_candidate`
- `validator_rule_candidate`
- `authority_reference_only`
- `lab_evidence_reference`
- `caveat_required`
- `stop_line`
- `not_yet_allowed`

## Material settlement

| material | settlement | fixture use | caveat |
| --- | --- | --- | --- |
| `c4_c3_validator_failure_card_edge_scout` | schema field candidate, validator rule candidate, lab evidence reference, caveat required | failure card edge fixture candidate | Failure cards may carry `validation_result_ref`, `failed_rule_id`, `error_code`, `diagnostics_ref`, `dictionary_ref`, `schema_ref`, `evidence_refs`, `status`, `producer`, and `schema_version`, but no raw YAML payload, dataframe, frame buffer, or runtime handoff. |
| `c2_c3_display_hint_validator_negative_fixture_scout` | validator rule candidate, lab evidence reference, caveat required, stop-line | display hint negative fixture candidate | Negative fixtures may cover unknown `lod_hint`, ambiguous `bbox`, missing `coord_ref`, invalid `time_window`, credential-bearing `tile_ref`, unitless density or sample budget, and budget-as-SLA drift. They do not transfer c_2 compression or preaggregation ownership. |
| `c1_c3_reference_envelope_validator_positive_fixture_scout` | prior dictionary candidate, schema field candidate, validator rule candidate, lab evidence reference, caveat required | reference envelope positive fixture candidate | Positive fixtures must stay sealed, redacted, opaque, non-payload, and non-fetchable. They do not create a c_1 consumption API. |
| `a1_c3_prior_dictionary_minimal_yaml_entry_shape_scout` | prior dictionary candidate, schema field candidate, validator rule candidate, lab evidence reference, caveat required | minimal YAML entry shape fixture candidate | Only stable surfaces such as `prior_terms`, `view_families`, `layer_taxonomy`, `c4_mediation`, `stop_lines`, `unknown_stop_lines`, and forbidden field families are settled. This does not create YAML. |
| `current_validator_gate` | authority reference only, validator rule candidate, stop-line | current validator behavior reference | The validator exists, but the formal YAML dictionary remains absent. Schema JSON is not changed by this gate. |

## Stop-lines preserved

- No YAML dictionary creation.
- No schema JSON modification.
- No validator script modification.
- No runtime execution.
- No renderer behavior.
- No formula movement.
- No c_1, c_2, or c_4 integration.
- No raw payload, dataframe, DB query, frame buffer, or fetchable live source.
- No readiness, visual parity, correctness, performance, or runtime replacement claim.

## Decision output

- `validator_fixture_material_settlement_passed = true`
- `fixture_materials_settled = true`
- `yaml_dictionary_creation_authorized = false`
- `schema_json_modification_authorized = false`
- `validator_script_modification_authorized = false`
- `runtime_execution_authorized = false`
- `renderer_behavior_authorized = false`
- `formula_movement_authorized = false`
- `c1_c2_c4_integration_authorized = false`
- `readiness_claimed = false`
- `visual_parity_claimed = false`
- `correctness_claimed = false`
- `runtime_replacement_authorized = false`

## Recommended next gate

`c3_prior_semantic_dictionary_minimal_yaml_fixture_planning_gate`

## Boundary statement

Docs and test only c_3 prior validator fixture material settlement gate. This gate classifies validator fixture materials from c_4, c_2, c_1, a_1, and the current validator gate into prior candidates, schema field candidates, validator rule candidates, lab evidence references, caveats, and stop-lines. It does not create a YAML dictionary, does not modify schema JSON, does not modify the validator script, does not implement prototype, runtime, renderer, formula, or cross-agent integration behavior, and does not claim readiness, visual parity, correctness, performance, or runtime replacement.

## Final classification

`c3_prior_validator_fixture_material_settlement_gate_committed_for_o1_review_no_push`

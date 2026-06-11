# -*- coding: utf-8 -*-
"""Unittests for c3 prior semantic dictionary validator."""

import os
import sys
import unittest
import tempfile
import subprocess

class TestC3PriorSemanticDictionaryValidator(unittest.TestCase):
    def setUp(self):
        self.script_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "scripts", "validate_displaytools_c3_prior_semantic_dictionary.py"
        ))
        self.default_schema_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "docs", "c3_prior_dictionary", "c3_prior_semantic_dictionary.schema.v0.json"
        ))

    def run_validator(self, yaml_path, schema_path=None):
        cmd = [sys.executable, self.script_path, yaml_path]
        if schema_path:
            cmd.append(schema_path)

        # 執行並捕獲輸出
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode, result.stdout, result.stderr

    def build_minimal_yaml(self, legacy_direct_adoption_forbidden="true", include_legacy_field=True):
        legacy_field = ""
        if include_legacy_field:
            legacy_field = f"\n    direct_adoption_forbidden: {legacy_direct_adoption_forbidden}"
        return f"""
dictionary_metadata:
  dictionary_id: test_dict
  version: v0
  owner: c_3
  lifecycle_status: planned
  source_commit: abc1234
authority_sources: []
phenomenon_translation_map: []
prior_terms: []
view_families: []
layer_taxonomy: []
recipe_authoring:
  recipe_owns_truth: true
  preview_consumes_recipe: true
  export_consumes_recipe: true
  ui_does_not_own_truth: true
c4_mediation:
  ingress_mediated_by_c4: true
  egress_mediated_by_c4: true
  direct_c3_to_c1_forbidden: true
legacy_fossil_translation:
  - legacy_term: legacy_mask
    observed_need: observed historical pressure
    translated_ideal_candidate: layered_occluding_body_visibility_contract_candidate{legacy_field}
stop_lines: []
unknown_stop_lines: []
validator_expectations: []
"""

    def test_missing_yaml_target_passes_as_not_applicable(self):
        # 使用一個不存在的 YAML 檔
        non_existent_yaml = "docs/c3_prior_dictionary/non_existent_file.yaml"
        code, stdout, stderr = self.run_validator(non_existent_yaml, self.default_schema_path)
        self.assertEqual(code, 0)
        self.assertIn("not_applicable_dictionary_missing", stdout)

    def test_missing_schema_target_fails(self):
        # 建立一個臨時的 YAML 檔案以防止因為 YAML 遺失而 PASS
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8") as f:
            f.write("dictionary_metadata:\n  dictionary_id: test\n")
            temp_yaml = f.name

        try:
            non_existent_schema = "docs/c3_prior_dictionary/non_existent_schema.json"
            code, stdout, stderr = self.run_validator(temp_yaml, non_existent_schema)
            self.assertEqual(code, 1)
            self.assertIn("Schema JSON target is missing", stderr)
        finally:
            if os.path.exists(temp_yaml):
                os.remove(temp_yaml)

    def test_malformed_schema_fails(self):
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8") as fy:
            fy.write("dictionary_metadata:\n  dictionary_id: test\n")
            temp_yaml = fy.name
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w", encoding="utf-8") as fs:
            fs.write("{malformed json")
            temp_schema = fs.name

        try:
            code, stdout, stderr = self.run_validator(temp_yaml, temp_schema)
            self.assertEqual(code, 1)
            self.assertIn("Schema JSON is malformed", stderr)
        finally:
            if os.path.exists(temp_yaml):
                os.remove(temp_yaml)
            if os.path.exists(temp_schema):
                os.remove(temp_schema)

    def test_yaml_with_forbidden_keys_fails(self):
        # 建立包含 forbidden family 'runtime_state' 的 YAML 內容
        bad_yaml_content = """
dictionary_metadata:
  dictionary_id: test_dict
  version: v0
  owner: c_3
  lifecycle_status: planned
  source_commit: abc1234
  runtime_state: should_fail_here
authority_sources: []
phenomenon_translation_map: []
prior_terms: []
view_families: []
layer_taxonomy: []
recipe_authoring:
  recipe_owns_truth: true
  preview_consumes_recipe: true
  export_consumes_recipe: true
  ui_does_not_own_truth: true
c4_mediation:
  ingress_mediated_by_c4: true
  egress_mediated_by_c4: true
  direct_c3_to_c1_forbidden: true
legacy_fossil_translation: []
stop_lines: []
unknown_stop_lines: []
validator_expectations: []
"""
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8") as f:
            f.write(bad_yaml_content)
            temp_yaml = f.name

        try:
            code, stdout, stderr = self.run_validator(temp_yaml, self.default_schema_path)
            self.assertEqual(code, 1)
            self.assertIn("Forbidden key detected", stderr)
        finally:
            if os.path.exists(temp_yaml):
                os.remove(temp_yaml)

    def test_yaml_with_bare_high_risk_term_id_fails(self):
        bad_term_yaml = """
dictionary_metadata:
  dictionary_id: test_dict
  version: v0
  owner: c_3
  lifecycle_status: planned
  source_commit: abc1234
authority_sources: []
phenomenon_translation_map: []
prior_terms:
  - term_id: layer
    definition: high risk bare term
    authority_family: external_standard
    source_evidence_refs:
      - ref_id: ref01
        ref_kind: spec
        source: test
    allowed_use: use
    forbidden_use: forbidden
    example: ex
    counterexample: cex
    schema_field_candidate: true
    validator_rule_candidate: true
    prototype_behavior_candidate: false
    stop_line: stop
    confidence: high
    lifecycle_status: planned
view_families: []
layer_taxonomy: []
recipe_authoring:
  recipe_owns_truth: true
  preview_consumes_recipe: true
  export_consumes_recipe: true
  ui_does_not_own_truth: true
c4_mediation:
  ingress_mediated_by_c4: true
  egress_mediated_by_c4: true
  direct_c3_to_c1_forbidden: true
legacy_fossil_translation: []
stop_lines: []
unknown_stop_lines: []
validator_expectations: []
"""
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8") as f:
            f.write(bad_term_yaml)
            temp_yaml = f.name

        try:
            code, stdout, stderr = self.run_validator(temp_yaml, self.default_schema_path)
            self.assertEqual(code, 1)
            self.assertIn("bare_high_risk_term_id", stderr)
        finally:
            if os.path.exists(temp_yaml):
                os.remove(temp_yaml)

    def test_valid_yaml_structure_passes(self):
        valid_yaml = """
dictionary_metadata:
  dictionary_id: test_dict
  version: v0
  owner: c_3
  lifecycle_status: planned
  source_commit: abc1234
authority_sources:
  - source_id: src_01
    authority_family: external_standard
    source_ref: ref_doc
    adoption_status: adopted
    forbidden_overread: disallowed
phenomenon_translation_map:
  - naive_observed_phrase: test
    formal_engineering_term: test_formal
    rrkal_prior_candidate: candidate
    stop_line: stop_id
prior_terms:
  - term_id: c3_qualified_term
    definition: this is qualified
    authority_family: external_standard
    source_evidence_refs:
      - ref_id: ref01
        ref_kind: spec
        source: test
    allowed_use: use
    forbidden_use: forbidden
    example: ex
    counterexample: cex
    schema_field_candidate: true
    validator_rule_candidate: true
    prototype_behavior_candidate: false
    stop_line: stop
    confidence: high
    lifecycle_status: planned
view_families:
  - view_family_id: view_01
    view_kind: standard
    input_contract: input
    output_contract: output
    non_goals: []
layer_taxonomy:
  - layer_kind: map_layer
    owns_truth: true
    consumer: client
    forbidden_confusion: error
recipe_authoring:
  recipe_owns_truth: true
  preview_consumes_recipe: true
  export_consumes_recipe: true
  ui_does_not_own_truth: true
c4_mediation:
  ingress_mediated_by_c4: true
  egress_mediated_by_c4: true
  direct_c3_to_c1_forbidden: true
legacy_fossil_translation:
  - legacy_term: old_term
    observed_need: needed
    translated_ideal_candidate: new_candidate
    direct_adoption_forbidden: true
stop_lines:
  - stop_line_id: stop_01
    reason: blocking
    blocked_claims: []
    reopen_condition: when_done
    status: blocked
unknown_stop_lines:
  - unknown_id: unk_01
    why_unknown: missing
    allowed_reference_use: ref
    resolution_gate: gate_id
validator_expectations:
  - rule_id: rule_01
    checked_surface: surface
    fail_condition: fail
    error_code: error
"""
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8") as f:
            f.write(valid_yaml)
            temp_yaml = f.name

        try:
            code, stdout, stderr = self.run_validator(temp_yaml, self.default_schema_path)
            self.assertEqual(code, 0)
            self.assertIn("Validation passed successfully", stdout)
        finally:
            if os.path.exists(temp_yaml):
                os.remove(temp_yaml)

    def test_legacy_fossil_direct_adoption_false_fails(self):
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8") as f:
            f.write(self.build_minimal_yaml(legacy_direct_adoption_forbidden="false"))
            temp_yaml = f.name

        try:
            code, stdout, stderr = self.run_validator(temp_yaml, self.default_schema_path)
            self.assertEqual(code, 1)
            self.assertIn("legacy_fossil_direct_adoption", stderr)
        finally:
            if os.path.exists(temp_yaml):
                os.remove(temp_yaml)

    def test_legacy_fossil_direct_adoption_missing_fails(self):
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8") as f:
            f.write(self.build_minimal_yaml(include_legacy_field=False))
            temp_yaml = f.name

        try:
            code, stdout, stderr = self.run_validator(temp_yaml, self.default_schema_path)
            self.assertEqual(code, 1)
            self.assertIn("legacy_fossil_direct_adoption", stderr)
        finally:
            if os.path.exists(temp_yaml):
                os.remove(temp_yaml)

    def test_legacy_fossil_direct_adoption_true_passes_this_rule(self):
        with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w", encoding="utf-8") as f:
            f.write(self.build_minimal_yaml(legacy_direct_adoption_forbidden="true"))
            temp_yaml = f.name

        try:
            code, stdout, stderr = self.run_validator(temp_yaml, self.default_schema_path)
            self.assertEqual(code, 0, stderr)
            self.assertIn("Validation passed successfully", stdout)
        finally:
            if os.path.exists(temp_yaml):
                os.remove(temp_yaml)

if __name__ == "__main__":
    unittest.main()

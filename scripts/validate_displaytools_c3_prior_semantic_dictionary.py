# -*- coding: utf-8 -*-
"""Validator script for displaytools c3 prior semantic dictionary."""

import os
import sys
import json

def main():
    # 1. 檢查 YAML 解析器依賴
    try:
        import yaml
    except ImportError:
        sys.stderr.write("YAML parser (PyYAML) is not installed. Terminating validator gate.\n")
        sys.exit(1)

    # 取得命令列參數
    yaml_path = "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.v0.yaml"
    if len(sys.argv) > 1:
        yaml_path = sys.argv[1]

    # schema 的路徑
    schema_path = "docs/c3_prior_dictionary/c3_prior_semantic_dictionary.schema.v0.json"
    if len(sys.argv) > 2:
        schema_path = sys.argv[2]

    # 2. 檢查與載入 Schema JSON
    if not os.path.exists(schema_path):
        sys.stderr.write("Schema JSON target is missing.\n")
        sys.exit(1)

    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
    except Exception:
        sys.stderr.write("Schema JSON is malformed.\n")
        sys.exit(1)

    # 3. 檢查 YAML 是否存在
    if not os.path.exists(yaml_path):
        # YAML 遺失視為 PASS 並輸出特定的 not_applicable 狀態
        sys.stdout.write("not_applicable_dictionary_missing\n")
        sys.exit(0)

    # 4. 載入並解析 YAML
    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        sys.stderr.write("YAML parsing failed: {}\n".format(e))
        sys.exit(1)

    if not isinstance(data, dict):
        sys.stderr.write("YAML root must be a mapping.\n")
        sys.exit(1)

    # 5. 進行結構與欄位檢驗
    # A. 檢查 top-level sections
    required_sections = schema.get("required", [])
    for sec in required_sections:
        if sec not in data:
            sys.stderr.write("missing_required_section: {}\n".format(sec))
            sys.exit(1)

    for key in data.keys():
        if key not in required_sections:
            sys.stderr.write("unknown_top_level_section: {}\n".format(key))
            sys.exit(1)

    # B. 走訪整份 YAML 檢查 forbidden fields
    # 定義所有禁止的 key/名稱
    forbidden_keys = {
        "runtime_state", "renderer_state", "frame_buffer", "framebuffer",
        "import_module", "runtime_loader", "network_fetch",
        "ui_widget_class", "renderer_object", "implementation_snippet",
        "callable", "runtime_object", "dataframe", "raw_payload", "raw_payload_contract",
        "earth_only_assumption", "qt_widget_binding", "renderer_host",
        "bare_layer", "implicit_stack_order", "legacy_mask_direct_use",
        "ui_state_as_truth", "viewport_state_as_export_contract",
        "c1_direct_dependency", "odoriba_bypass",
        "legacy_term_as_final_api", "legacy_runtime_patch_as_ideal_form",
        "implementation_authorized", "readiness_claimed", "readiness",
        "silent_default", "implicit_prior_term",
        "runtime_execution", "monolith_import", "renderer_call"
    }

    def scan_for_forbidden(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in forbidden_keys:
                    sys.stderr.write("Forbidden key detected: {}\n".format(k))
                    sys.exit(1)
                scan_for_forbidden(v)
        elif isinstance(node, list):
            for item in node:
                if isinstance(item, str) and item in forbidden_keys:
                    sys.stderr.write("Forbidden value detected: {}\n".format(item))
                    sys.exit(1)
                scan_for_forbidden(item)

    scan_for_forbidden(data)

    # C. 特殊關卡規則校驗
    # (1) no_bare_high_risk_term_ids: prior_terms 中的 term_id 不能是高風險字
    high_risk_bare_terms = {"layer", "mask", "view", "projection", "frame", "render", "recipe"}
    prior_terms = data.get("prior_terms", [])
    if isinstance(prior_terms, list):
        for entry in prior_terms:
            if isinstance(entry, dict):
                term_id = entry.get("term_id")
                if term_id in high_risk_bare_terms:
                    sys.stderr.write("bare_high_risk_term_id: {}\n".format(term_id))
                    sys.exit(1)
                # 確保 prior_term_entry 的所有 required columns 都存在
                required_term_fields = [
                    "term_id", "definition", "authority_family", "source_evidence_refs",
                    "allowed_use", "forbidden_use", "example", "counterexample",
                    "schema_field_candidate", "validator_rule_candidate",
                    "prototype_behavior_candidate", "stop_line", "confidence", "lifecycle_status"
                ]
                for field in required_term_fields:
                    if field not in entry:
                        sys.stderr.write("missing_required_entry_field: {} in prior_terms\n".format(field))
                        sys.exit(1)

    # (2) stop_lines_must_not_authorize_implementation
    # stop_lines 中的 blocked_claims 不能包含 implementation_authorized
    stop_lines = data.get("stop_lines", [])
    if isinstance(stop_lines, list):
        for entry in stop_lines:
            if isinstance(entry, dict):
                blocked_claims = entry.get("blocked_claims", [])
                if isinstance(blocked_claims, list):
                    if "implementation_authorized" in blocked_claims:
                        sys.stderr.write("stop_line_authorizes_implementation detected\n")
                        sys.exit(1)

    # (3) unknown_stop_lines_require_resolution_gate
    unknown_stop_lines = data.get("unknown_stop_lines", [])
    if isinstance(unknown_stop_lines, list):
        for entry in unknown_stop_lines:
            if isinstance(entry, dict):
                resolution_gate = entry.get("resolution_gate")
                if not resolution_gate:
                    sys.stderr.write("unknown_stop_line_without_resolution_gate detected\n")
                    sys.exit(1)

    # (4) recipe_must_own_truth
    recipe_authoring = data.get("recipe_authoring", {})
    if isinstance(recipe_authoring, dict):
        if recipe_authoring.get("recipe_owns_truth") is not True or recipe_authoring.get("ui_does_not_own_truth") is not True:
            sys.stderr.write("recipe_truth_owned_by_ui: recipe_owns_truth and ui_does_not_own_truth must be True\n")
            sys.exit(1)

    # (5) c4_mediation_required_for_ingress_and_egress
    c4_mediation = data.get("c4_mediation", {})
    if isinstance(c4_mediation, dict):
        if (c4_mediation.get("ingress_mediated_by_c4") is not True or
            c4_mediation.get("egress_mediated_by_c4") is not True or
            c4_mediation.get("direct_c3_to_c1_forbidden") is not True):
            sys.stderr.write("c4_mediation_bypassed detected\n")
            sys.exit(1)

    sys.stdout.write("Validation passed successfully.\n")
    sys.exit(0)

if __name__ == "__main__":
    main()

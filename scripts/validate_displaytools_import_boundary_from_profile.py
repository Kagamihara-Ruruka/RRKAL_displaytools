"""Generic import-boundary checker driven by a JSON profile.

This is an L1 shadow checker. It parses Python source with ast and never imports
or executes the candidate module. Handwritten checkers remain the source of
truth for formal gates.
"""

from __future__ import annotations

import argparse
import ast
import fnmatch
import json
from pathlib import Path


SCHEMA = "rrkal_displaytools.import_boundary_from_profile.v1"
PROFILE_SCHEMA = "rrkal.import_boundary_profile.v1"
REQUIRED_AST_NODES = {
    "Import",
    "ImportFrom",
    "Name",
    "Attribute",
    "Call",
    "FunctionDef",
    "AsyncFunctionDef",
    "ClassDef",
}


def load_profile(path: Path) -> dict[str, object]:
    profile = json.loads(path.read_text(encoding="utf-8"))
    if profile.get("schema") != PROFILE_SCHEMA:
        raise ValueError("unsupported profile schema")
    ast_nodes = set(profile.get("ast_nodes", []))
    missing = REQUIRED_AST_NODES - ast_nodes
    if missing:
        raise ValueError(f"profile missing ast node coverage: {sorted(missing)}")
    return profile


def _normalized_token(token: str) -> str:
    return token.lower().replace("_", " ").replace("-", " ")


def _identifier_token(token: str) -> str:
    chars = []
    for char in token.lower():
        chars.append(char if char.isalnum() else "_")
    return "_".join(part for part in "".join(chars).split("_") if part)


def _profile_terms(profile: dict[str, object]) -> list[tuple[str, str]]:
    terms: list[tuple[str, str]] = []
    families = profile.get("forbidden_families", {})
    if isinstance(families, dict):
        for family, values in families.items():
            if isinstance(values, list):
                for value in values:
                    if isinstance(value, str):
                        terms.append((family, value))
    return terms


def _term_matches_identifier(term: str, name: str) -> bool:
    term_identifier = _identifier_token(term)
    name_identifier = _identifier_token(name)
    if not term_identifier:
        return False
    if name_identifier == term_identifier:
        return True
    if term_identifier in name_identifier:
        return True
    wildcard = "*" + "*".join(term_identifier.split("_")) + "*"
    return fnmatch.fnmatch(name_identifier, wildcard)


def _term_matches_module(term: str, module: str) -> bool:
    term_identifier = _identifier_token(term)
    module_identifier = _identifier_token(module)
    module_lower = module.lower()
    if module_lower == term.lower() or module_lower.startswith(term.lower() + "."):
        return True
    return bool(term_identifier and term_identifier in module_identifier)


def _family_for_token(profile: dict[str, object], token: str) -> tuple[str, str]:
    for family, term in _profile_terms(profile):
        if _term_matches_identifier(term, token):
            return family, f"forbidden_profile_term:{term}"
    return "", ""


def _module_is_forbidden(profile: dict[str, object], module: str) -> tuple[bool, str, str]:
    for family, term in _profile_terms(profile):
        if _term_matches_module(term, module):
            return True, family, f"forbidden_profile_module_term:{term}"
    return False, "", ""


def _name_is_forbidden(profile: dict[str, object], name: str) -> tuple[bool, str, str]:
    family, reason = _family_for_token(profile, name)
    return (bool(family), family, reason)


def _call_target_name(func: ast.AST) -> str:
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


def _iter_imported_names(node: ast.ImportFrom):
    for alias in node.names:
        yield alias.name
        if alias.asname:
            yield alias.asname


def _base_packet(profile: dict[str, object], profile_path: str, target: str) -> dict[str, object]:
    runtime_flags = profile.get("runtime_flags", {})
    if not isinstance(runtime_flags, dict):
        runtime_flags = {}
    return {
        "schema": SCHEMA,
        "profile_schema": profile.get("schema"),
        "profile": profile_path,
        "capability": profile.get("capability"),
        "target": target,
        "candidate_exists": True,
        "status": "pass",
        "boundary_passed": True,
        "violations": [],
        "checked_imports": [],
        "checked_names": [],
        "forbidden_families": profile.get("forbidden_families", {}),
        "allowed_string_labels": profile.get("allowed_string_labels", []),
        "string_labels_allowed_as_data": True,
        "trust_level": profile.get("trust_level"),
        "blocking": profile.get("blocking"),
        "handwritten_checker_is_source_of_truth": profile.get("handwritten_checker_is_source_of_truth"),
        "replacement_authorized": False,
        "runtime_render_invoked": bool(runtime_flags.get("runtime_render_invoked", False)),
        "runtime_merge_enabled": bool(runtime_flags.get("runtime_merge_enabled", False)),
        "readiness_claimed": bool(runtime_flags.get("readiness_claimed", False)),
        "boundary": "Generic AST import-boundary profile shadow check only; does not import or execute target module.",
    }


def _append_name_violation(profile: dict[str, object], violations: list[dict[str, object]], node: ast.AST, kind: str, name: str) -> None:
    forbidden, family, reason = _name_is_forbidden(profile, name)
    if forbidden:
        violations.append(
            {
                "line": getattr(node, "lineno", 0),
                "kind": kind,
                "module": "",
                "name": name,
                "forbidden_family": family,
                "reason": reason,
            }
        )


def validate_source(profile: dict[str, object], source: str, source_name: str = "<memory>", profile_path: str = "<profile>") -> dict[str, object]:
    packet = _base_packet(profile, profile_path, source_name)
    violations: list[dict[str, object]] = []
    checked_imports: list[str] = []
    checked_names: list[str] = []

    try:
        tree = ast.parse(source, filename=source_name)
    except SyntaxError as exc:
        packet.update(
            {
                "status": "syntax_error",
                "boundary_passed": False,
                "violations": [
                    {
                        "line": exc.lineno or 0,
                        "kind": "syntax_error",
                        "module": "",
                        "name": "",
                        "forbidden_family": "syntax_error",
                        "reason": "syntax_error",
                        "message": exc.msg,
                    }
                ],
            }
        )
        return packet

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                checked_imports.append(alias.name)
                forbidden, family, reason = _module_is_forbidden(profile, alias.name)
                if forbidden:
                    violations.append({"line": node.lineno, "kind": "import", "module": alias.name, "name": alias.asname or "", "forbidden_family": family, "reason": reason})
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            checked_imports.append(module)
            forbidden, family, reason = _module_is_forbidden(profile, module)
            imported_names = list(_iter_imported_names(node))
            checked_names.extend(imported_names)
            name_hits = []
            name_families = []
            for name in imported_names:
                name_forbidden, name_family, name_reason = _name_is_forbidden(profile, name)
                if name_forbidden:
                    name_hits.append({"name": name, "forbidden_family": name_family, "reason": name_reason})
                    name_families.append(name_family)
            if forbidden or name_hits:
                violations.append({"line": node.lineno, "kind": "from_import", "module": module, "names": name_hits, "forbidden_family": family or sorted(set(name_families))[0], "reason": reason or "forbidden_imported_name"})
        elif isinstance(node, ast.Name):
            checked_names.append(node.id)
            _append_name_violation(profile, violations, node, "name_reference", node.id)
        elif isinstance(node, ast.Attribute):
            checked_names.append(node.attr)
            _append_name_violation(profile, violations, node, "attribute_reference", node.attr)
        elif isinstance(node, ast.Call):
            name = _call_target_name(node.func)
            if name:
                checked_names.append(name)
                _append_name_violation(profile, violations, node, "call_target", name)
        elif isinstance(node, ast.FunctionDef):
            checked_names.append(node.name)
            _append_name_violation(profile, violations, node, "function_definition", node.name)
        elif isinstance(node, ast.AsyncFunctionDef):
            checked_names.append(node.name)
            _append_name_violation(profile, violations, node, "async_function_definition", node.name)
        elif isinstance(node, ast.ClassDef):
            checked_names.append(node.name)
            _append_name_violation(profile, violations, node, "class_definition", node.name)

    packet.update({"status": "fail" if violations else "pass", "boundary_passed": not violations, "violations": violations, "checked_imports": sorted(set(checked_imports)), "checked_names": sorted(set(checked_names))})
    return packet


def validate_target(profile: dict[str, object], profile_path: str, target: Path) -> dict[str, object]:
    target_text = str(target)
    if not target.exists():
        packet = _base_packet(profile, profile_path, target_text)
        packet.update(
            {
                "candidate_exists": False,
                "status": "not_applicable_candidate_missing",
                "boundary_passed": True,
                "violations": [],
                "checked_imports": [],
                "checked_names": [],
                "boundary": "Profile target candidate is missing; generic shadow checker did not import or execute a target module.",
            }
        )
        return packet
    return validate_source(profile, target.read_text(encoding="utf-8"), target_text, profile_path)


def run_negative_self_test(profile: dict[str, object], profile_path: str) -> dict[str, object]:
    snippets = profile.get("negative_self_test_snippets", [])
    results = []
    if not isinstance(snippets, list):
        snippets = []
    for index, item in enumerate(snippets):
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", f"snippet_{index}"))
        source = str(item.get("source", ""))
        packet = validate_source(profile, source, f"<self-test:{name}>", profile_path)
        results.append({"name": name, "detected": not packet["boundary_passed"], "violations": packet["violations"]})
    all_detected = bool(results) and all(result["detected"] for result in results)
    packet = _base_packet(profile, profile_path, "<negative-self-test>")
    packet.update(
        {
            "candidate_exists": True,
            "status": "pass" if all_detected else "fail",
            "boundary_passed": all_detected,
            "negative_self_test_passed": all_detected,
            "all_forbidden_snippets_detected": all_detected,
            "violations": [] if all_detected else results,
            "checked_imports": [],
            "checked_names": [],
        }
    )
    return packet


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("profile")
    parser.add_argument("--target")
    parser.add_argument("--self-test-negative", action="store_true")
    args = parser.parse_args()

    profile_path = Path(args.profile)
    profile = load_profile(profile_path)
    target = Path(args.target or str(profile["target"]))
    packet = run_negative_self_test(profile, str(profile_path)) if args.self_test_negative else validate_target(profile, str(profile_path), target)
    print(json.dumps(packet, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if packet.get("boundary_passed") else 1


if __name__ == "__main__":
    raise SystemExit(main())

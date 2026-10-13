"""
Print the public API of onto_engine.py (signature, first docstring line,
and returned keys). Run it at the start of engine mode; the output is the
API reference for the session, so read it in full.

Usage:
    python scripts/extract_api.py
"""
import inspect
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import onto_engine  # noqa: E402

SECTIONS = {
    "World and files": ["create_world", "import_ontology", "save_ontology",
                        "diff_ontology", "save_all_outputs"],
    "TBox": ["build_class", "build_object_property", "build_data_property",
             "build_annotation_property", "build_sub_property",
             "build_equivalent_properties"],
    "ABox": ["create_individual", "add_to_class", "destroy_individual",
             "build_same_as", "update_property", "remove_property_value",
             "clear_property", "set_with_provenance"],
    "OWL axioms": ["build_equivalent_class", "build_disjoint_group",
                   "build_disjoint_union", "build_min_cardinality",
                   "build_max_cardinality", "build_exact_cardinality",
                   "build_all_values_from", "build_has_value", "build_one_of",
                   "build_all_different", "close_world_scope",
                   "build_swrl_rule", "list_swrl_rules", "delete_swrl_rule"],
    "Reasoner": ["run_hermit_reasoner", "run_hermit_analysis",
                 "snapshot_classifications", "check_inferred_reclassification"],
    "Lookup and export": ["get_class_hierarchy", "get_all_individuals",
                          "export_tbox_markdown", "export_abox_markdown",
                          "export_mermaid_class_diagram",
                          "export_mermaid_instance_graph",
                          "export_mermaid_aggregated_graph",
                          "export_summary_statistics",
                          "export_smart_visualization", "as_rdflib_graph"],
    "SPARQL and routing": ["query_onto", "query_sparql", "run_sparql_check",
                           "suggest_sparql_queries", "suggest_axioms",
                           "auto_route_advanced_checks"],
    "Checks": ["check_mece", "check_coverage", "check_bidirectional_coverage",
               "check_shared_reference", "check_cardinality",
               "check_value_range", "check_mandatory_outputs",
               "check_process_completeness", "check_causal_chain",
               "check_reverse_chain", "check_provenance",
               "check_unsupported_assumptions", "check_constraint_conflicts",
               "check_assumption_impact", "check_pipeline_trace",
               "check_cross_mapping", "check_mapping_chain",
               "check_conditional_branch"],
    "Presets": ["run_preset_cross_factor", "run_preset_multi_axis",
                "run_preset_regulated_procedure", "run_preset_causal",
                "run_preset_logic_model", "run_preset_mapping_chain",
                "run_preset_decision_tree"],
    "Full run": ["run_full_analysis"],
}


def returned_keys(doc: str) -> str:
    """Return the text of the 'Returns:' section of a docstring."""
    match = re.search(r"Returns:\s*(.*?)(?:\n\s*\n|\Z)", doc or "", re.DOTALL)
    if not match:
        return ""
    return " ".join(line.strip() for line in match.group(1).splitlines())


def main():
    funcs = {name: obj for name, obj in inspect.getmembers(onto_engine, inspect.isfunction)
             if obj.__module__ == "onto_engine" and not name.startswith("_")}
    print("=" * 70)
    print("onto_engine.py API reference")
    print("=" * 70)
    printed = set()
    for section, names in SECTIONS.items():
        present = [n for n in names if n in funcs]
        if not present:
            continue
        print(f"\n--- {section} ---")
        for name in present:
            obj = funcs[name]
            doc = inspect.getdoc(obj) or ""
            first = doc.split("\n")[0].strip()
            print(f"  {name}{inspect.signature(obj)}" + (f"  # {first}" if first else ""))
            keys = returned_keys(doc)
            if keys and "{" in keys:
                print(f"    returns: {keys}")
            printed.add(name)
    rest = sorted(set(funcs) - printed)
    if rest:
        print("\n--- Other ---")
        for name in rest:
            print(f"  {name}{inspect.signature(funcs[name])}")
    print(f"\nPublic functions: {len(funcs)}")
    print(f"SPARQL_CHECKS: {', '.join(onto_engine.SPARQL_CHECKS)}")
    print("=" * 70)


if __name__ == "__main__":
    main()

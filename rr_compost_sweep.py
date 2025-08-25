import json
from rr_audit_log import log_event

def sweep_fragments(fragment_store):
    """
    Sweep fragment store for stale, orphaned, or malformed fragments.

    Args:
        fragment_store (list): List of fragment dicts with keys: id, text, flags, audit_trail

    Returns:
        dict: Summary of anomalies detected
    """
    anomalies = {
        "missing_metadata": [],
        "stale_flags": [],
        "orphaned_fragments": [],
        "audit_mismatch": []
    }

    for frag in fragment_store:
        fid = frag.get("id", "unknown")

        # Check for missing metadata
        if not all(k in frag for k in ["id", "text", "flags", "audit_trail"]):
            anomalies["missing_metadata"].append(fid)
            continue

        # Check for stale flags
        if "echo_reinterpreted" in frag["flags"] and not any(
            entry.get("action") == "semantic_rehearsal" for entry in frag["audit_trail"]
        ):
            anomalies["stale_flags"].append(fid)

        # Check for orphaned synthesized fragments
        if "synthesized" in frag["flags"] and not frag.get("source_ids"):
            anomalies["orphaned_fragments"].append(fid)

        # Check audit mismatch
        recent_log = frag["audit_trail"][-1] if frag["audit_trail"] else {}
        if recent_log.get("source") not in ["echo_logic", "rr_synthesis_engine", "dimulste", "rr_governance_reflex"]:
            anomalies["audit_mismatch"].append(fid)

    # Log sweep summary
    log_event(
        event_type="compost_sweep",
        module="rr_compost_sweep",
        details={
            "summary": {k: len(v) for k, v in anomalies.items()},
            "timestamped": True
        }
    )

    return anomalies

# Example usage
if __name__ == "__main__":
    # Placeholder fragment store
    fragment_store = [
        {
            "id": "frag_001",
            "text": "vector agency_conflict",
            "flags": ["echo_reinterpreted"],
            "audit_trail": [{"source": "echo_logic", "action": "semantic_rehearsal"}]
        },
        {
            "id": "frag_002",
            "text": "drift detected",
            "flags": ["synthesized"],
            "audit_trail": [],
            # Missing source_ids
        },
        {
            "id": "frag_003",
            "text": "paradox unresolved",
            "flags": ["contradiction_detected"],
            "audit_trail": [{"source": "rr_governance_reflex", "action": "epistemic_tension"}]
        }
    ]

    results = sweep_fragments(fragment_store)
    print("Compost Sweep Results:")
    for category, items in results.items():
        print(f"{category}: {items}")

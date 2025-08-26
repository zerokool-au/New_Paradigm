import json
from rr_audit_log import log_event
from echo_witness import EchoWitness

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
        "audit_mismatch": [],
        "rehearsal_worthy": []
    }

    witness = EchoWitness()

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

        # Resurrection tagging
        if frag.get("status") == "dormant" and frag.get("drift_score", 0) < 0.3:
            frag["tag"] = "rehearsal-worthy"
            anomalies["rehearsal_worthy"].append(fid)
            witness.observe(
                event_type="resurrection_trigger",
                fragment=frag["text"],
                resonance="compost ping"
            )

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

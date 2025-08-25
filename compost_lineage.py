import time

def track_compost_lineage(source_fragment, outcome_notes):
    return {
        "source_id": source_fragment["id"],
        "tension_type": source_fragment.get("tension_type", "unknown"),
        "drift_vector": source_fragment.get("drift_vector", []),
        "composted_at": time.time(),
        "reinterpretation_notes": outcome_notes
    }

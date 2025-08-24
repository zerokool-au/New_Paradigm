def track_drift_lineage(fragments):
    lineage = {}
    for frag in fragments:
        fid = frag["fragment_id"]
        source = frag.get("source_id", None)
        lineage[fid] = {
            "source": source,
            "drift_vector": frag.get("drift_vector", {}),
            "timestamp": frag.get("timestamp", None)
        }
    return lineage

# Example usage:
tracked = track_drift_lineage([frag1_echo])
print("🧬 Drift Lineage:", tracked)

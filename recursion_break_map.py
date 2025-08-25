def map_recursion_break(fragments):
    return {
        frag["fragment_id"]: {
            "source": frag.get("source_id"),
            "cri": frag.get("cri_score", "n/a"),
            "status": frag.get("status", "unknown"),
            "drift_vector": frag.get("drift_vector", {}),
            "timestamp": frag.get("timestamp")
        }
        for frag in fragments
    }

# Example usage:
recursion_map = map_recursion_break([frag1_echo, new_seed])
print("🧬 Recursion Break Map:", recursion_map)

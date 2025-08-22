from datetime import datetime, timezone
import json

def simulate_pair(frag_a, frag_b, drift_meta=None):
    """
    Simulates reinterpretation of two fragments based on drift metadata.
    Returns a structured result with status, notes, timestamp, and logs the event.
    """

    # Basic contradiction logic
    themes_conflict = frag_a["theme"] != frag_b["theme"]
    content_tension = frag_a.get("content") != frag_b.get("content")

    # Drift metadata influence
    intensity = drift_meta.get("intensity", 0.5) if drift_meta else 0.5
    drift_type = drift_meta.get("drift_type", "semantic") if drift_meta else "semantic"
    bias_vector = drift_meta.get("bias_vector", ["unknown", "unknown"]) if drift_meta else ["unknown", "unknown"]

    # Reinterpretation logic
    if themes_conflict and intensity > 0.7:
        status = "reinterpreted"
        notes = f"High-intensity {drift_type} drift between {frag_a['id']} and {frag_b['id']}. Reframed as layered contradiction."
        output = {
            "id": f"r_{frag_a['id']}_{frag_b['id']}",
            "content": f"{frag_a['content']} ↔ {frag_b['content']}",
            "theme": "transformation"
        }
    elif content_tension and intensity > 0.4:
        status = "composted"
        notes = f"Moderate drift detected. {frag_a['id']} and {frag_b['id']} composted for future synthesis."
        output = None
    else:
        status = "preserved"
        notes = f"Low drift. {frag_a['id']} and {frag_b['id']} preserved as parallel truths."
        output = None

    # Log reinterpretation event
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pair": [frag_a["id"], frag_b["id"]],
        "drift_type": drift_type,
        "bias_vector": bias_vector,
        "intensity": intensity,
        "status": status,
        "notes": notes,
        "source_stage": "first_pass",
        "rehearsal_path": "contradiction → reinterpretation",
        "compost_flag": status == "composted",
        "reinterpreted_output": output
    }

    with open("reinterpretation_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

    return {
        "status": status,
        "notes": notes,
        "timestamp": log_entry["timestamp"]
    }

# Example usage
if __name__ == "__main__":
    frag1 = {"id": "f001", "theme": "hope", "content": "She believed the silence was a beginning."}
    frag2 = {"id": "f002", "theme": "despair", "content": "The silence echoed everything she had lost."}
    drift = {"drift_type": "emotional", "intensity": 0.8, "bias_vector": ["hope", "despair"]}
    result = simulate_pair(frag1, frag2, drift)
    print(result)

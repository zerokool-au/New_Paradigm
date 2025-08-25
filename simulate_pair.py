# simulate_pair.py
from datetime import datetime, timezone
import json

def simulate_pair(frag_a, frag_b, drift_meta=None):
    """
    Simulates reinterpretation of two fragments based on drift metadata.
    Returns a structured result with contradiction reflexes, tension vector, and compost flag.
    """

    # Basic contradiction logic
    themes_conflict = frag_a.get("theme") != frag_b.get("theme")
    content_tension = frag_a.get("content") != frag_b.get("content")

    # Drift metadata influence
    intensity = drift_meta.get("intensity", 0.5) if drift_meta else 0.5
    drift_type = drift_meta.get("drift_type", "semantic") if drift_meta else "semantic"
    bias_vector = drift_meta.get("bias_vector", ["unknown", "unknown"]) if drift_meta else ["unknown", "unknown"]

    # Tension vector
    tension_vector = {
        "semantic": intensity if content_tension else 0.0,
        "governance": intensity if themes_conflict else 0.0
    }

    # Compost heuristics
    compost = False
    if tension_vector["semantic"] > 0.7 or tension_vector["governance"] > 0.5:
        compost = True
    if frag_a.get("preserve") or frag_b.get("preserve"):
        compost = False
    if frag_a.get("override") == "audit" or frag_b.get("override") == "audit":
        compost = False  # Governance override

    # Contradiction type
    contradiction_type = "semantic" if content_tension else "governance" if themes_conflict else "none"
    contradiction_detected = contradiction_type != "none"

    # Optional reinterpretation output
    output = None
    if contradiction_detected and intensity > 0.7:
        output = {
            "id": f"r_{frag_a['id']}_{frag_b['id']}",
            "content": f"{frag_a.get('content', '')} ↔ {frag_b.get('content', '')}",
            "theme": "transformation"
        }

    # Log entry
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pair": [frag_a.get("id"), frag_b.get("id")],
        "drift_type": drift_type,
        "bias_vector": bias_vector,
        "intensity": intensity,
        "tension_vector": tension_vector,
        "contradiction_type": contradiction_type,
        "compost_flag": compost,
        "reinterpreted_output": output,
        "notes": f"Contradiction: {contradiction_type}, Compost: {compost}",
        "source_stage": "first_pass",
        "rehearsal_path": "contradiction → reinterpretation"
    }

    try:
        with open("reinterpretation_log.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"Logging failed: {e}")

    return {
        "contradiction_detected": contradiction_detected,
        "fragment_id": f"{frag_a.get('id')}_{frag_b.get('id')}",
        "tension_vector": tension_vector,
        "type": contradiction_type,
        "compost": compost,
        "notes": log_entry["notes"]
    }

# Example usage
if __name__ == "__main__":
    frag1 = {"id": "f001", "theme": "hope", "content": "She believed the silence was a beginning."}
    frag2 = {"id": "f002", "theme": "despair", "content": "The silence echoed everything she had lost."}
    drift = {"drift_type": "emotional", "intensity": 0.8, "bias_vector": ["hope", "despair"]}
    result = simulate_pair(frag1, frag2, drift)
    print(result)

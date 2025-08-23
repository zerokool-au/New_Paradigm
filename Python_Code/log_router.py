# log_router.py

import json
import time

def route_log(frag_a, frag_b, result, source="unknown"):
    contradiction_type = result.get("type", "none")
    semantic_tension = result.get("tension_vector", {}).get("semantic", None)
    suppress_flag = contradiction_type == "none" and semantic_tension in [None, 0.0]
    compost_flag = result.get("compost", False)

    log_entry = {
        "timestamp": time.time(),
        "agentA": frag_a["id"],
        "agentB": frag_b["id"],
        "type": contradiction_type,
        "tension_vector": result.get("tension_vector", {}),
        "compost": compost_flag,
        "suppress_flag": suppress_flag,
        "source": source,
        "contentA": frag_a.get("content", ""),
        "contentB": frag_b.get("content", "")
    }

    # Route to contradiction log
    if contradiction_type in ["contradiction", "semantic"]:
        with open("Contradiction_Log.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    # Route to anomaly log
    if suppress_flag:
        with open("Drift_Anomaly_Log.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    # Route to compost log
    if compost_flag:
        with open("Compost_Log.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    # Route to rehearsal log
    if source == "rehearse_suppressions":
        with open("Drift_Rehearsal_Log.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

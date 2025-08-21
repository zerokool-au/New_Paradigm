import json
import time

def classify_drift_direction(agentA, agentB, score, history_sample):
    avg_history = sum(history_sample) / len(history_sample)
    delta = score - avg_history

    if delta > 0.1:
        direction = "divergent"
    elif delta < -0.1:
        direction = "convergent"
    else:
        direction = "stable"

    log_entry = {
        "timestamp": time.time(),
        "agentA": agentA,
        "agentB": agentB,
        "score": score,
        "avg_history": avg_history,
        "delta": delta,
        "direction": direction
    }

    with open("Drift_Direction_Log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return direction

# Test run
direction = classify_drift_direction("A335", "B335", 0.33620584, [0.49250445, 0.17990723])
print("Drift direction:", direction)

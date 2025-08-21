import json
import time

def classify_drift_direction(agentA, agentB, score, history_sample):
    if not history_sample:
        print(f"⚠️ No history sample for {agentA} vs {agentB} → defaulting to 'no-history'")
        return "no-history"  # Prevent ZeroDivisionError and flag for compost

    avg_history = sum(history_sample) / len(history_sample)

    # Example drift classification logic
    if score > avg_history + 0.2:
        return "forward-drift"
    elif score < avg_history - 0.2:
        return "backward-drift"
    else:
        return "stable"

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

def route_fragment(agentA, agentB, score, history_sample, fragment):
    direction = classify_drift_direction(agentA, agentB, score, history_sample)

    if direction == "divergent":
        target_file = "composted.jsonl"
    elif direction == "convergent":
        target_file = "preserved.jsonl"
    else:
        target_file = "neutral.jsonl"

    log_entry = {
        "timestamp": time.time(),
        "agentA": agentA,
        "agentB": agentB,
        "score": score,
        "direction": direction,
        "fragment": fragment
    }

    with open(target_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return direction

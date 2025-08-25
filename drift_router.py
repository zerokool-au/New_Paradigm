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

    print(f"Fragment routed to {target_file} as {direction}")

# Test run
route_fragment("A335", "B335", 0.33620584, [0.49250445, 0.17990723], "The sky was a mirror of forgotten dreams.")

import json
import time
from simulate_pair_logger import simulate_pair_with_logging
from simulate_pair import simulate_pair
from rehearse_compost import rehearse_compost
from log_router import route_log  # ✅ Added for centralized logging

# Wrap simulate_pair with contradiction logging
logged_simulate_pair = simulate_pair_with_logging(simulate_pair)

# Subscriptable fragment mock
class Fragment(dict):
    def __init__(self, frag_id, theme="identity", content="default"):
        super().__init__()
        self["id"] = frag_id
        self["theme"] = theme
        self["content"] = content

    @property
    def id(self):
        return self["id"]

    @property
    def theme(self):
        return self["theme"]

    @property
    def content(self):
        return self["content"]

    def __repr__(self):
        return f"Fragment(id={self.id}, theme={self.theme}, content={self.content[:40]}...)"

def load_fragments():
    return [
        Fragment("A335", theme="identity", content="The system remembers."),
        Fragment("B335", theme="governance", content="The system forgets."),
        Fragment("C335", theme="identity", content="The system remembers.")
    ]

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

def run_dimulste_loop():
    fragments = load_fragments()
    for i in range(len(fragments)):
        for j in range(i + 1, len(fragments)):
            frag_a = fragments[i]
            frag_b = fragments[j]

            # Run contradiction reflex
            result = logged_simulate_pair(frag_a, frag_b)

            # ✅ Route to appropriate log files
            route_log(frag_a, frag_b, result, source="dimulste_loop")

            print(f"Rehearsed {frag_a.id} vs {frag_b.id}: {result.get('type', 'no contradiction')}")

            # Route composted fragments
            if result.get("compost"):
                print(f"→ Composting {frag_a.id} and {frag_b.id}")
                rehearse_compost(log_file="compost_log.jsonl")  # You can pass fragments if needed

            # Run drift direction reflex
            score = result.get("tension_vector", {}).get("semantic", 0.0)
            history_sample = [0.49250445, 0.17990723]
            direction = classify_drift_direction(frag_a.id, frag_b.id, score, history_sample)
            print(f"Drift direction: {direction}")

# Entry point
if __name__ == "__main__":
    run_dimulste_loop()

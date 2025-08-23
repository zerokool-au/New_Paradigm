import json
import time

def simulate_pair_with_logging(simulate_pair_fn):
    def wrapper(frag_a, frag_b):
        result = simulate_pair_fn(frag_a, frag_b)

        # Detect suppressed contradiction
        semantic_tension = result.get("tension_vector", {}).get("semantic")
        contradiction_type = result.get("type", "unknown")
        suppress_flag = contradiction_type == "none" and semantic_tension in [None, 0.0]

        log_entry = {
            "timestamp": time.time(),
            "agentA": frag_a["id"],
            "agentB": frag_b["id"],
            "type": contradiction_type,
            "tension_vector": result.get("tension_vector", {}),
            "compost": result.get("compost", False),
            "suppress_flag": suppress_flag,
            "content": frag_a.get("content", "")  # for audit trace
        }

        # Route logs
        if contradiction_type in ["contradiction", "semantic"]:
            with open("Contradiction_Log.jsonl", "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        elif suppress_flag:
            with open("Drift_Anomaly_Log.jsonl", "a") as f:
                f.write(json.dumps(log_entry) + "\n")

        return result
    return wrapper

# --- Test Harness ---
if __name__ == "__main__":
    # Mock simulate_pair function
    def simulate_pair(frag_a, frag_b):
        return {
            "type": "none",
            "tension_vector": {
                "semantic": 0.0,
                "emotional": None
            },
            "compost": False
        }

    # Mock fragment class
    class Fragment(dict):
        def __init__(self, id, theme="identity", content="default"):
            super().__init__()
            self["id"] = id
            self["theme"] = theme
            self["content"] = content

        @property
        def id(self):
            return self["id"]

    # Run test
    frag_a = Fragment("TestA", theme="identity", content="Truth is a mirror shattered by belief.")
    frag_b = Fragment("TestB", theme="identity", content="Truth is a mirror shattered by belief.")

    logged_simulate_pair = simulate_pair_with_logging(simulate_pair)
    result = logged_simulate_pair(frag_a, frag_b)
    print("Simulated pair result:", result)

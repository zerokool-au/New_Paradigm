# dreamstate_router.py
import json
import time
from dimulste_loop import Fragment  # Reuse fragment structure
from simulate_pair_logger import simulate_pair_with_logging
from simulate_pair import simulate_pair

# Load reinterpretation entries from log
def load_reinterpretations(log_file="Reinterpretation_Log.jsonl"):
    reinterpretations = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                reinterpretations.append(json.loads(line))
        print(f"Loaded {len(reinterpretations)} reinterpretation entries")
    except FileNotFoundError:
        print(f"No reinterpretation log found at {log_file}")
    return reinterpretations

# Route each reinterpretation into Dimulste simulation
def route_to_dimulste(reinterpretation):
    try:
        # Extract required fields
        summary = reinterpretation["reinterpretation"]["summary"]
        source_ids = reinterpretation["source_fragments"]
        status = reinterpretation["reinterpretation"]["status"]

        # Create synthetic fragments
        frag_a = Fragment(source_ids[0], theme="echo", content=summary)
        frag_b = Fragment(source_ids[1], theme="echo", content=summary)

        # Simulate tension
        logged_simulate_pair = simulate_pair_with_logging(simulate_pair)
        result = logged_simulate_pair(frag_a, frag_b)

        # Output result
        print(f"🧪 Simulated reinterpretation ({status}): {frag_a.id} vs {frag_b.id}")
        print(f"→ Result: {result.get('type', 'no contradiction')}")
        print(f"→ Semantic tension: {result.get('tension_vector', {}).get('semantic', 'n/a')}")
        print("-" * 60)

    except KeyError as e:
        print(f"⚠️ Skipped malformed reinterpretation entry: missing {e}")
        print("-" * 60)

        # Optional: log anomaly for future composting
        with open("Drift_Anomaly_Log.jsonl", "a") as f:
            f.write(json.dumps({
                "timestamp": time.time(),
                "error": str(e),
                "entry": reinterpretation
            }) + "\n")

# Run the router across all reinterpretations
def run_dreamstate_router():
    reinterpretations = load_reinterpretations()
    for reinterpretation in reinterpretations:
        route_to_dimulste(reinterpretation)

# Entry point
if __name__ == "__main__":
    run_dreamstate_router()

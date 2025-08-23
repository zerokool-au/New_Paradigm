import json
import time
from dimulste_loop import Fragment
from simulate_pair_logger import simulate_pair_with_logging
from simulate_pair import simulate_pair
from log_router import route_log  # ✅ Added for centralized logging

# Wrap simulate_pair with logging
logged_simulate = simulate_pair_with_logging(simulate_pair)

def load_suppressed_fragments(log_file="Drift_Anomaly_Log.jsonl"):
    suppressed = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                entry = json.loads(line)
                if entry.get("suppress_flag"):
                    frag = Fragment(
                        frag_id=entry["id"],
                        theme=entry.get("theme", "unknown"),
                        content=entry.get("content", "")
                    )
                    suppressed.append(frag)
        print(f"📥 Loaded {len(suppressed)} suppressed fragments")
    except FileNotFoundError:
        print(f"⚠️ No anomaly log found at {log_file}")
    return suppressed

def rehearse_suppressions():
    suppressed = load_suppressed_fragments()
    for frag in suppressed:
        result = logged_simulate(frag, frag)

        # ✅ Route to appropriate log files
        route_log(frag, frag, result, source="rehearse_suppressions")

        print(f"\n🔁 Rehearsed Suppressed Fragment:")
        print(f"→ {frag.content}")
        print(f"   Type: {result.get('type', 'none')}")
        print(f"   Tension: {result.get('tension_vector', {}).get('semantic', 'n/a')}")
        print("-" * 40)

# Entry point
if __name__ == "__main__":
    rehearse_suppressions()

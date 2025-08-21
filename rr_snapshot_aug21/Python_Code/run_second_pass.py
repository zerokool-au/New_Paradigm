from simulate_pair import simulate_pair  # Your harness
import json
from datetime import datetime

# Minimal wrapper to satisfy agent.id
class Agent:
    def __init__(self, identifier):
        self.id = identifier

# Default second-pass parameters
agent_b = Agent("Echo")  # Wrap as object with .id
context = {
    "loop": "second-pass",
    "history": [],
    "notes": "Recursive rehearsal of previously reinterpreted fragments"
}
threshold = 0.5  # Adjust if needed for drift sensitivity

# Load second-pass input
with open("second_pass_input.jsonl", "r", encoding="utf-8") as f:
    fragments = [json.loads(line)["fragment"] for line in f]

# Run second-pass rehearsal
results = []
for frag in fragments:
    agent_a = Agent(frag)  # Wrap fragment as agentA.id
    context["current_fragment"] = frag
    outcome = simulate_pair(agent_a, agent_b, context, threshold)

    # Optional: log fragments with no history
    if outcome.get("drift_type") == "no-history":
        print(f"⚠️ No history available for fragment: {frag}")

    results.append({
        "original": frag,
        "second_pass_outcome": outcome.get("outcome", "Unknown"),
        "drift_type": outcome.get("drift_type", "Unclassified"),
        "notes": outcome.get("notes", ""),
        "timestamp": outcome.get("timestamp", datetime.utcnow().isoformat())
    })

# Save results
with open("second_pass_log.jsonl", "w", encoding="utf-8") as f:
    for entry in results:
        json.dump(entry, f)
        f.write("\n")

print(f"✅ Second-pass complete. {len(results)} fragments processed.")

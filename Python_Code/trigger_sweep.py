import json

# Load synthesis queue
with open("synthesis_queue.json", "r") as f:
    queue = json.load(f)

# Filter fragments
triggers = [
    frag for frag in queue
    if frag.get("contradiction_score", 0) > 0.0 and frag.get("status") == "flagged_for_rehearsal"
]

# Save to synthesis_trigger.json
with open("synthesis_trigger.json", "w") as f:
    json.dump(triggers, f, indent=2)

print(f"✅ Routed {len(triggers)} fragments to synthesis_trigger.json")

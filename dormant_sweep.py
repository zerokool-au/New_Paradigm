import json

# Load synthesis queue
with open("synthesis_queue.json", "r") as f:
    queue = json.load(f)

# Define dormancy threshold (e.g. untouched for >3 cycles)
dormant_fragments = [
    frag for frag in queue
    if frag.get("cycle_count", 0) < 1 and frag.get("status") == "composted"
]

# Save dormant fragments
with open("dormant_trigger.json", "w") as f:
    json.dump(dormant_fragments, f, indent=2)

print(f"🌱 Surfaced {len(dormant_fragments)} dormant fragments for latent rehearsal")

import json

# Load manual trigger
with open("manual_trigger.json", "r") as f:
    fragments = json.load(f)

# Define echo cues
echo_cues = ["again", "still", "return", "loop", "mirror", "silence", "heard"]

# Flag echo drift
for frag in fragments:
    text = frag.get("text", "").lower()
    notes = json.dumps(frag.get("notes", "")).lower()
    if any(cue in text for cue in echo_cues) or any(cue in notes for cue in echo_cues):
        frag["echo_flag"] = True
    else:
        frag["echo_flag"] = False

# Save output
with open("echo_flagged.json", "w") as f:
    json.dump(fragments, f, indent=2)

print(f"🔍 Echo Logic Pass complete. Output saved to echo_flagged.json")

import json
from datetime import datetime
import os

def run_dimulste(agentA, agentB, fragment):
    print(f"🌀 Rehearsing: {agentA}–{agentB} → Fragment: {fragment}")
    status = "reinterpreted" if "?" in fragment else "preserved"
    notes = "Fragment showed semantic tension and was reinterpreted." if status == "reinterpreted" else "Fragment retained original meaning."
    return {
        "status": status,
        "notes": notes
    }

def load_logged_fragments(log_file="rehearsal_log.jsonl"):
    if not os.path.exists(log_file):
        return set()
    with open(log_file, "r", encoding="utf-8") as f:
        return set(json.loads(line)["original"] for line in f if line.strip())

def log_rehearsal(fragment, result, log_file="rehearsal_log.jsonl"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "original": fragment,
        "outcome": result["status"],
        "notes": result.get("notes", "")
    }
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def rehearse_compost(log_file="compost_log.jsonl"):
    logged_fragments = load_logged_fragments()
    composted = []

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                composted.append(entry)
            except json.JSONDecodeError as e:
                print(f"⚠️ Malformed JSON: {e}")
                continue

    # Sort by score (lowest first), fallback to 1.0 if missing
    composted.sort(key=lambda x: x.get("score", 1.0))

    for entry in composted:
        try:
            pair = entry["pair"]
            fragment = entry["fragment"]

            normalized_pair = pair.replace("â€“", "-").replace("–", "-")
            if "-" in normalized_pair:
                agentA, agentB = normalized_pair.split("-")
            else:
                raise ValueError(f"Invalid pair format: {pair}")

            if fragment in logged_fragments:
                print(f"⏭️ Skipping duplicate fragment: {fragment}")
                continue

            result = run_dimulste(agentA, agentB, fragment)
            log_rehearsal(fragment, result)

        except Exception as e:
            print(f"⚠️ Error processing line: {e}")

if __name__ == "__main__":
    rehearse_compost()

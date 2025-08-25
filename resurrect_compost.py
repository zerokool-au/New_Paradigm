import json
from datetime import datetime, timezone
from simulate_pair import simulate_pair
import random

def load_composted_entries(path="reinterpretation_log.jsonl"):
    with open(path, "r", encoding="utf-8") as f:
        return [
            json.loads(line) for line in f
            if line.strip() and json.loads(line)["compost_flag"]
        ]

def generate_fresh_bias_vector():
    # You can evolve this list over time
    bias_pool = [
        ["memory", "forgetting"],
        ["freedom", "constraint"],
        ["truth", "illusion"],
        ["presence", "absence"],
        ["growth", "decay"],
        ["connection", "isolation"]
    ]
    return random.choice(bias_pool)

def log_resurrection(entry, result, output=None):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pair": entry["pair"],
        "original_bias_vector": entry["bias_vector"],
        "fresh_bias_vector": output["bias_vector"] if output else ["unknown", "unknown"],
        "drift_type": entry["drift_type"],
        "intensity": entry["intensity"] + 0.2,
        "status": result["status"],
        "notes": result["notes"],
        "source_stage": "resurrection_pass",
        "rehearsal_path": "composted → resurrected → " + result["status"],
        "compost_flag": result["status"] == "composted",
        "reinterpreted_output": output["fragment"] if output else None
    }
    with open("resurrection_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

def resurrect_composted(entries):
    for entry in entries:
        fresh_bias = generate_fresh_bias_vector()
        frag_a = {
            "id": entry["pair"][0],
            "theme": fresh_bias[0],
            "content": entry.get("reinterpreted_output", {}).get("content", "")
        }
        frag_b = {
            "id": entry["pair"][1],
            "theme": fresh_bias[1],
            "content": entry.get("reinterpreted_output", {}).get("content", "")
        }
        drift_meta = {
            "drift_type": entry["drift_type"],
            "intensity": entry["intensity"] + 0.2,
            "bias_vector": fresh_bias
        }

        result = simulate_pair(frag_a, frag_b, drift_meta)

        output = {
            "bias_vector": fresh_bias,
            "fragment": {
                "id": f"rx_{frag_a['id']}_{frag_b['id']}",
                "content": f"{frag_a['content']} ↻ {frag_b['content']}",
                "theme": "resurrected synthesis"
            }
        } if result["status"] == "reinterpreted" else None

        log_resurrection(entry, result, output)
        print(f"Resurrected {entry['pair'][0]} vs {entry['pair'][1]} → {result['status']}: {result['notes']}")

if __name__ == "__main__":
    composted_entries = load_composted_entries()
    resurrect_composted(composted_entries)

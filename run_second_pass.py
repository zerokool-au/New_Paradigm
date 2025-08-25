import json
from datetime import datetime, timezone
from simulate_pair import simulate_pair

def load_first_pass_log(path="reinterpretation_log.jsonl"):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def filter_for_second_pass(entries):
    return [
        entry for entry in entries
        if entry["status"] in ["composted", "reinterpreted"]
        and entry["source_stage"] == "first_pass"
    ]

def log_second_pass(entry, result, output=None):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pair": entry["pair"],
        "drift_type": entry["drift_type"],
        "bias_vector": entry["bias_vector"],
        "intensity": entry["intensity"] + 0.1,
        "status": result["status"],
        "notes": result["notes"],
        "source_stage": "second_pass",
        "rehearsal_path": entry["status"] + " → " + result["status"],
        "compost_flag": result["status"] == "composted",
        "reinterpreted_output": output
    }
    with open("second_pass_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

def run_second_pass(entries):
    for entry in entries:
        frag_a = {
            "id": entry["pair"][0],
            "theme": entry["bias_vector"][0],
            "content": entry.get("reinterpreted_output", {}).get("content", "")
        }
        frag_b = {
            "id": entry["pair"][1],
            "theme": entry["bias_vector"][1],
            "content": entry.get("reinterpreted_output", {}).get("content", "")
        }
        drift_meta = {
            "drift_type": entry["drift_type"],
            "intensity": entry["intensity"] + 0.1,
            "bias_vector": entry["bias_vector"]
        }

        result = simulate_pair(frag_a, frag_b, drift_meta)

        output = {
            "id": f"r2_{frag_a['id']}_{frag_b['id']}",
            "content": f"{frag_a['content']} ↔↔ {frag_b['content']}",
            "theme": "recursive synthesis"
        } if result["status"] == "reinterpreted" else None

        log_second_pass(entry, result, output)
        print(f"Second-pass {entry['pair'][0]} vs {entry['pair'][1]} → {result['status']}: {result['notes']}")

if __name__ == "__main__":
    first_pass_entries = load_first_pass_log()
    second_pass_targets = filter_for_second_pass(first_pass_entries)
    run_second_pass(second_pass_targets)

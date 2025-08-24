import json

def update_scores(log_path, synthesis_path):
    with open(log_path, 'r') as f:
        governance_log = json.load(f)

    with open(synthesis_path, 'r') as f:
        synthesis_queue = json.load(f)

    updated_queue = []
    for frag in synthesis_queue:
        match = next((entry for entry in governance_log if entry["id"] == frag["id"]), None)
        if match:
            frag["contradiction_score"] = round(match["epistemic_tension"], 2)
            frag["tags"] = list(set(frag.get("tags", []) + ["rehearsed"]))
            frag["status"] = match["status"]
        updated_queue.append(frag)

    with open(synthesis_path, 'w') as f:
        json.dump(updated_queue, f, indent=2)

    print(f"Updated {len(governance_log)} fragments with rehearsal scores.")

# Example usage:
update_scores('governance_log.json', 'synthesis_queue.json')

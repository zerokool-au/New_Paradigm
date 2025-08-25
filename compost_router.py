import json

def route_to_compost(audit_path, compost_path):
    with open(audit_path, 'r') as f:
        flagged = json.load(f)

    compost_queue = []
    for frag in flagged:
        compost_queue.append({
            "id": frag["id"],
            "content": frag["content"],
            "status": "awaiting_reintegration",
            "notes": f"Missing fields: {', '.join(frag['missing_fields'])}"
        })

    with open(compost_path, 'w') as f:
        json.dump(compost_queue, f, indent=2)

    print(f"Compost queue populated with {len(compost_queue)} fragments.")

# Example usage:
route_to_compost('logging_integrity_report.json', 'compost_queue.json')

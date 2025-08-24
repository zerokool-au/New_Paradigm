import json

def reintegrate_fragments(compost_path, synthesis_path):
    with open(compost_path, 'r') as f:
        compost_queue = json.load(f)

    reintegrated_queue = []
    for frag in compost_queue:
        reintegrated = {
            "id": frag["id"],
            "content": frag["content"],
            "bias_score": 0.0,
            "drift_score": 0.0,
            "contradiction_score": 0.0,
            "tags": ["reintegrated", "from_compost"],
            "status": "reintegration_complete"
        }
        reintegrated_queue.append(reintegrated)

    with open(synthesis_path, 'w') as f:
        json.dump(reintegrated_queue, f, indent=2)

    print(f"Overwrote synthesis queue with {len(reintegrated_queue)} reintegrated fragments.")

# Example usage:
reintegrate_fragments('compost_queue.json', 'synthesis_queue.json')

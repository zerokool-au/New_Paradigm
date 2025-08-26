# compost_audit.py

import json
from datetime import datetime

# Sample compost queue
compost_queue = [
    {
        "id": "frag4",
        "content": "Closure is not the end—it’s rehearsal for reinterpretation.",
        "last_rehearsed": "2025-08-12T10:00:00",
        "status": "stale",
        "tags": ["closure", "rehearsal", "reinterpretation"]
    },
    {
        "id": "frag5",
        "content": "Drift is not deviation—it’s the signal that synthesis is near.",
        "last_rehearsed": "2025-08-25T08:00:00",
        "status": "fresh",
        "tags": ["drift", "signal", "synthesis"]
    }
]

def sweep_compost(queue):
    flagged = []
    for frag in queue:
        if frag["status"] == "stale":
            frag["routed_to"] = "reinterpretation_queue"
            frag["timestamp"] = datetime.now().isoformat()
            flagged.append(frag)
            print(f"Fragment flagged: {frag['id']} → reinterpretation_queue")

    with open("compost_log.json", "w") as file:
        json.dump(flagged, file, indent=2)

# Run the sweep
sweep_compost(compost_queue)

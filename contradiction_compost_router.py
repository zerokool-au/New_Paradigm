import time

def route_contradiction_outcome(fragment_id, cri_score, outcome, drift_vector):
    if outcome == "reinterpreted":
        return {
            "fragment_id": fragment_id,
            "status": "preserved",
            "notes": "Contradiction metabolized via reinterpretation",
            "drift_vector": drift_vector,
            "timestamp": time.time()
        }
    else:
        return {
            "fragment_id": fragment_id,
            "status": "composted",
            "notes": "Contradiction unresolved, routed to compost",
            "drift_vector": drift_vector,
            "timestamp": time.time()
        }

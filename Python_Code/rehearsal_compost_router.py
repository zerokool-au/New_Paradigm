import time

def route_rehearsal_to_compost(fragment_id, outcome, drift_vector):
    if outcome == "unresolved":
        return {
            "fragment_id": fragment_id,
            "status": "composted",
            "reason": "Rehearsal failed to metabolize contradiction",
            "drift_vector": drift_vector,
            "timestamp": time.time()
        }
    else:
        return {
            "fragment_id": fragment_id,
            "status": "preserved",
            "reason": "Rehearsal successfully reinterpreted contradiction",
            "drift_vector": drift_vector,
            "timestamp": time.time()
        }

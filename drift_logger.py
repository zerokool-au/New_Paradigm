import time

def log_fragment_event(fragment_id, event_type, tension_score, outcome, iteration):
    return {
        "fragment_id": fragment_id,
        "event_type": event_type,  # preserve, rehearse, compost
        "tension_score": tension_score,
        "outcome": outcome,        # resolved, escalated, composted
        "timestamp": time.time(),
        "iteration": iteration
    }

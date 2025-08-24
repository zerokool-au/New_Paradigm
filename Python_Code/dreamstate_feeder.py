import time

def feed_to_dreamstate(fragment_id, reinterpretation, drift_vector):
    return {
        "fragment_id": fragment_id,
        "dream_payload": {
            "text": reinterpretation,
            "drift": drift_vector
        },
        "status": "queued for Dimulste loop",
        "timestamp": time.time()
    }

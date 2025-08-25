import time

def log_reinterpretation(fragment_id, original_text, reinterpretation, drift_vector, iteration):
    return {
        "fragment_id": fragment_id,
        "original_text": original_text,
        "reinterpretation": reinterpretation,
        "drift_vector": drift_vector,
        "iteration": iteration,
        "timestamp": time.time()
    }

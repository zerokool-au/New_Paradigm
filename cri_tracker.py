import time

def track_cri_over_time(fragment_id, cri_history):
    avg_cri = sum(cri_history) / len(cri_history) if cri_history else 0
    return {
        "fragment_id": fragment_id,
        "cri_history": cri_history,
        "average_cri": round(avg_cri, 3),
        "timestamp": time.time()
    }

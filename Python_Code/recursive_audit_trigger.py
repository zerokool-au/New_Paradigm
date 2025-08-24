import time

def recursive_audit_trigger(fragment_id, cri_score, threshold=0.85):
    audit_triggered = cri_score >= threshold
    timestamp = time.time()

    result = {
        "fragment_id": fragment_id,
        "audit_triggered": audit_triggered,
        "reason": (
            f"CRI {cri_score} exceeds recursive audit threshold {threshold}"
            if audit_triggered else
            f"CRI {cri_score} below audit threshold"
        ),
        "timestamp": timestamp
    }

    if audit_triggered:
        result["recursive_rehearsal_note"] = {
            "note": "Fragment shows signs of semantic recursion. Reinterpretation may have masked contradiction.",
            "status": "pending recursive audit",
            "logged_at": timestamp
        }

    return result

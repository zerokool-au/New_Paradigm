def check_cri_threshold(fragment_id, cri_score, threshold=0.7):
    if cri_score >= threshold:
        return {
            "fragment_id": fragment_id,
            "triggered": True,
            "reason": f"CRI score {cri_score} exceeds threshold {threshold}"
        }
    else:
        return {
            "fragment_id": fragment_id,
            "triggered": False,
            "reason": f"CRI score {cri_score} below threshold {threshold}"
        }

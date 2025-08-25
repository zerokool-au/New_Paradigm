def calculate_cri(logs, bias_factor=0.2):
    resolved = sum(1 for log in logs if log["outcome"] == "resolved")
    total = len(logs)
    base_score = 1 - (resolved / total) if total > 0 else 0
    return round(base_score + bias_factor, 3)

    if total == 0:
        return 0.0  # Avoid division by zero

    return round(resolved / total, 3)

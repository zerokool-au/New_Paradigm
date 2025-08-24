def calculate_volatility(fragment):
    # Synthetic volatility from metadata or fallback
    return fragment.get("volatility", 0.05)

def calculate_bias(fragment):
    # Synthetic bias from metadata or fallback
    return fragment.get("bias", 0.0)

def compost_count(fragment):
    # Count compost cycles from history
    return len(fragment.get("compost_history", []))

def detect_contradiction(fragment, anchor):
    # Simple contradiction check: does anchor appear in fragment text?
    return anchor not in fragment.get("text", "")
    
def calculate_tension(fragment, anchor):
    # Tension = weighted sum of volatility and bias
    volatility = calculate_volatility(fragment)
    bias = abs(calculate_bias(fragment))
    contradiction = detect_contradiction(fragment, anchor)

    tension = (volatility * 0.5) + (bias * 0.4)
    if contradiction:
        tension += 0.2
    return round(tension, 3)

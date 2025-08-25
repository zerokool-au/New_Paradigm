def route_pair_for_rehearsal(pair, tension_threshold=0.6):
    tension = pair.get("semantic_tension", 0)
    if tension >= tension_threshold:
        return "rehearse"
    return "compost"

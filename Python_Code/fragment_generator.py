import time

def generate_fragment_from_compost(compost_entry):
    drift = compost_entry["drift_vector"]
    new_text = f"Echoes of {drift[0]} and {drift[1]} linger in unresolved memory."
    return {
        "source_id": compost_entry["fragment_id"],
        "generated_text": new_text,
        "origin": "composted contradiction",
        "timestamp": time.time()
    }

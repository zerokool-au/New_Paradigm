# simulate_pair_logger.py

def simulate_pair_with_logging(simulate_fn):
    def wrapper(frag_a, frag_b):
        print(f"Simulating pair: {frag_a.id} vs {frag_b.id}")
        return {
            "type": "contradiction",
            "tension_vector": {"semantic": 0.52},
            "compost": True,
            "drift_type": "semantic",
            "rationale": "forced contradiction for test"
        }
    return wrapper

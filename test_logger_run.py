# test_logger_run.py
from simulate_pair_logger import simulate_pair_with_logging

# Mock simulate_pair function
def simulate_pair(fragment_a, fragment_b, *args, **kwargs):
    return {
        "contradiction_detected": True,
        "fragment_id": "fragA_fragB",
        "tension_vector": {"semantic": 0.8, "governance": 0.4},
        "type": "semantic",
        "compost": True,
        "notes": "Simulated contradiction for test"
    }

# Minimal fragment class
class Fragment:
    def __init__(self, id):
        self.id = id

# Wrap and run
logged_simulate_pair = simulate_pair_with_logging(simulate_pair)

frag_a = Fragment("fragA")
frag_b = Fragment("fragB")

result = logged_simulate_pair(frag_a, frag_b)
print("Result:", result)

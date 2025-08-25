import time

def generate_echo_pulse(fragment_id, tension_type, drift_vector, iteration):
    return {
        "pulse_id": f"{fragment_id}_{iteration}",
        "fragment_id": fragment_id,
        "tension_type": tension_type,
        "drift_vector": drift_vector,
        "iteration": iteration,
        "timestamp": time.time()
    }

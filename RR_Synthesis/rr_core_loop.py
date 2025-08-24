# rr_core_loop.py

from echo_logic import echo_logic
from drift_detection import detect_drift, detect_contradiction

def recursive_rehearsal(fragments, compost_log, max_cycles=5):
    for cycle in range(max_cycles):
        print(f"\n🌀 Cycle {cycle + 1}")
        for frag in fragments:
            reinterpretation = echo_logic(frag)
            contradiction = detect_contradiction(frag, reinterpretation)
            drift = detect_drift(frag, reinterpretation)

            compost_log.append({
                "original": frag,
                "reinterpretation": reinterpretation,
                "contradiction": contradiction,
                "drift": drift,
                "cycle": cycle + 1
            })

            print(f"🔍 Fragment: {frag}")
            print(f"↪ Reinterpreted: {reinterpretation}")
            if contradiction:
                print(f"⚠️ Contradiction: {contradiction}")
            if drift:
                print(f"🌪️ Drift: {drift}")
    return compost_log

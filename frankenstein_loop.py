# frankenstein_loop.py

import json
from datetime import datetime
from payloads import frag2_echo_2
from payloads import frag4

def contradiction_router(content):
    # Dummy router logic for now—can be expanded later
    return {"routed_content": content, "route": "reflexive_module"}

def synthesize(routed):
    # Simulate synthesis logic
    new_cri = round(routed["routed_content"].count(" ") / 100, 3)  # crude CRI drop simulation
    return {"CRI": new_cri, "status": "synthesized", "content": routed["routed_content"]}

def log_cri_delta(original_cri, new_cri):
    delta = round(original_cri - new_cri, 3)
    print(f"CRI delta: {delta} (from {original_cri} → {new_cri})")

def append_to_routing_log(payload, result):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "payload": payload["origin"],
        "route": "reflexive_module",
        "CRI_before": payload["CRI"],
        "CRI_after": result["CRI"],
        "status": result["status"]
    }
    try:
        with open("routing_log.json", "r+") as file:
            data = json.load(file)
            data.append(log_entry)
            file.seek(0)
            json.dump(data, file, indent=2)
    except FileNotFoundError:
        with open("routing_log.json", "w") as file:
            json.dump([log_entry], file, indent=2)

def pulse_check(semantic_tension, contradiction_resolved, drift_bias, recent_fragments):
    fauna_log = []

    if semantic_tension > 0.7:
        fauna_log.append("🐍 Tiger Snake coils: governance drift detected.")

    if contradiction_resolved and drift_bias < 0.2:
        fauna_log.append("🐨 Koala Hug deployed: synthesis affirmed.")

    if any("pun" in frag.lower() for frag in recent_fragments):
        fauna_log.append("🐦 Kookaburra laughs: semantic mischief confirmed.")

    return fauna_log

def inject_payload(payload):
    if payload["status"] == "volatile":
        routed = contradiction_router(payload["content"])
        result = synthesize(routed)
        log_cri_delta(payload["CRI"], result["CRI"])
        append_to_routing_log(payload, result)

        # Simulate ambient metrics
        semantic_tension = 0.75  # placeholder
        contradiction_resolved = True
        drift_bias = 0.1
        recent_fragments = [payload["content"]]

        fauna_feedback = pulse_check(semantic_tension, contradiction_resolved, drift_bias, recent_fragments)
        for signal in fauna_feedback:
            print(signal)

        return result
    else:
        return {"status": "skipped", "reason": "Payload not volatile"}

# Run the injection
result = inject_payload(frag2_echo_2)
print("Synthesis Result:", result)
result = inject_payload(frag4)
print("Synthesis Result:", result)
append_to_routing_log(frag4, result)

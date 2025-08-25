from contradiction_index import calculate_cri
from semantic_immune import detect_inflammation
from audit_trigger import trigger_recursive_audit

# Simulated drift logs for CRI
drift_logs = [
    {"fragment_id": "frag1", "outcome": "resolved"},
    {"fragment_id": "frag2", "outcome": "resolved"},
    {"fragment_id": "frag3", "outcome": "escalated"},
    {"fragment_id": "frag4", "outcome": "resolved"},
    {"fragment_id": "frag5", "outcome": "escalated"}
]

# Calculate CRI
cri = calculate_cri(drift_logs)
print("📊 Contradiction Resolution Index (CRI):", cri)

# Simulated logs for inflammation detection
pulse_log = [
    {"fragment_id": "frag1", "tension_type": "emergent"},
    {"fragment_id": "frag2", "tension_type": "cyclical"},
    {"fragment_id": "frag3", "tension_type": "emergent"}
]

compost_log = [
    {"source_id": "frag2"},
    {"source_id": "frag3"}
]

# Detect inflammation
inflammation_flags = detect_inflammation(pulse_log, drift_logs, compost_log)
print("🧠 Inflammation Flags:", inflammation_flags)

# Trigger recursive audit
audit_queue = trigger_recursive_audit(inflammation_flags)
print("🔁 Recursive Audit Queue:", audit_queue)

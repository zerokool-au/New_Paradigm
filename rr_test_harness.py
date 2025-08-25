import time
from contradiction_trigger import generate_rehearsal_queue
from dimulste_pair_router import route_pair_for_rehearsal
from drift_logger import log_fragment_event
from compost_lineage import track_compost_lineage
from echo_pulse import generate_echo_pulse
from semantic_immune import detect_inflammation
from contradiction_index import calculate_cri
from audit_trigger import trigger_recursive_audit
from creative_rehearsal import rehearse_fragment
from reinterpretation_logger import log_reinterpretation
from cri_trigger import check_cri_threshold
from contradiction_compost_router import route_contradiction_outcome
from rehearsal_compost_router import route_rehearsal_to_compost
from fragment_generator import generate_fragment_from_compost
from drift_visualizer import visualize_drift_vector
from cri_tracker import track_cri_over_time
from recursive_audit_trigger import recursive_audit_trigger
from dreamstate_feeder import feed_to_dreamstate
from persistent_logger import persist_log

# Step 1: Mock fragments + audit log
mock_fragments = [
    {"id": "frag1", "status": "preserved"},
    {"id": "frag2", "status": "preserved"},
    {"id": "frag3", "status": "composted"}
]

mock_audit_log = {
    "frag1": {"tension_score": 0.8},
    "frag2": {"tension_score": 0.4},
    "frag3": {"tension_score": 0.9}
}

# Step 2: Generate rehearsal queue
rehearsal_queue = generate_rehearsal_queue(mock_fragments, mock_audit_log)
print("🌀 Rehearsal Queue:", rehearsal_queue)

# Step 3: Route a fragment pair
test_pair = {"semantic_tension": 0.75}
decision = route_pair_for_rehearsal(test_pair)
print("🔀 Routing Decision:", decision)

# Step 4: Log drift event
drift_log = log_fragment_event("frag1", "rehearse", 0.8, "resolved", 1)
print("📜 Drift Log Entry:", drift_log)

# Step 5: Track compost lineage
source = {
    "id": "frag3",
    "tension_type": "cyclical",
    "drift_vector": ["loop", "bias"]
}
lineage = track_compost_lineage(source, "composted due to unresolved loop")
print("🌱 Compost Lineage:", lineage)

# Step 6: Generate Echo Pulse
pulse = generate_echo_pulse("frag1", "emergent", ["bias", "loop"], 2)
print("💓 Echo Pulse:", pulse)

# Step 7: Detect semantic inflammation
pulse_log = [
    {"fragment_id": "frag1", "tension_type": "emergent"},
    {"fragment_id": "frag2", "tension_type": "cyclical"},
    {"fragment_id": "frag3", "tension_type": "emergent"}
]

drift_logs = [
    {"fragment_id": "frag1", "outcome": "resolved"},
    {"fragment_id": "frag2", "outcome": "escalated"},
    {"fragment_id": "frag3", "outcome": "escalated"}
]

# Step 8: Log reinterpretation outcome
reinterpretation = {
    "fragment_id": "frag1",
    "original_text": "The sky was a mirror, but no one looked up.",
    "reinterpretation": "The sky reflected forgotten longing, unnoticed by grounded minds.",
    "drift_vector": {
        "emotional_shift": "subtle melancholy → existential nostalgia",
        "semantic_tension": "mirror → memory",
        "imagery": "static → dynamic reflection"
    }
}

re_log = log_reinterpretation(
    fragment_id=reinterpretation["fragment_id"],
    original_text=reinterpretation["original_text"],
    reinterpretation=reinterpretation["reinterpretation"],
    drift_vector=reinterpretation["drift_vector"],
    iteration=1
)

print("📝 Reinterpretation Log:")
for key, value in re_log.items():
    print(f"{key}: {value}")

# Step 9: Trigger contradiction rehearsal if CRI exceeds threshold
cri_score = calculate_cri(drift_logs, bias_factor=0.2)
cri_trigger = check_cri_threshold("frag1", cri_score)
print("⚠️ CRI Trigger Check:", cri_trigger)

if cri_trigger["triggered"]:
    rehearsal_output = rehearse_fragment(
        fragment_id="frag1",
        cri_score=cri_score,
        drift_vector=reinterpretation["drift_vector"]
    )
    print("🎭 Contradiction Rehearsal Output:", rehearsal_output)

    contradiction_outcome = route_contradiction_outcome(
        fragment_id="frag1",
        cri_score=cri_score,
        outcome="reinterpreted",
        drift_vector=reinterpretation["drift_vector"]
    )
    print("🧭 Contradiction Outcome Routing:", contradiction_outcome)

    compost_decision = route_rehearsal_to_compost(
        fragment_id="frag1",
        outcome="reinterpreted",
        drift_vector=reinterpretation["drift_vector"]
    )
    print("🪱 Rehearsal Compost Routing:", compost_decision)

    if compost_decision["status"] == "composted":
        new_fragment = generate_fragment_from_compost(compost_decision)
        print("🌿 Generated Fragment from Compost:", new_fragment)

    visualize_drift_vector("frag1", reinterpretation["drift_vector"])

    cri_history = [0.72, 0.81, cri_score]
    cri_tracking = track_cri_over_time("frag1", cri_history)
    print("📈 CRI Drift Tracking:", cri_tracking)

    audit_check = recursive_audit_trigger("frag1", cri_score)
    print("🧪 Recursive Audit Trigger:", audit_check)

    dream_payload = feed_to_dreamstate(
        fragment_id="frag1",
        reinterpretation=reinterpretation["reinterpretation"],
        drift_vector=reinterpretation["drift_vector"]
    )
    print("🌌 Dreamstate Feed:", dream_payload)

    persist_result = persist_log(dream_payload)
    print("💾 Persistent Log Status:", persist_result)

# ✅ Step 10: Define and route frag1_echo for drift inversion
frag1_echo = {
    'fragment_id': 'frag1_echo',
    'source_id': 'frag1',
    'original_text': 'The sky reflected forgotten longing, unnoticed by grounded minds.',
    'reinterpretation': 'The sky held presence, felt by those who stood still.',
    'drift_vector': {
        'emotional_shift': 'existential nostalgia → grounded immediacy',
        'semantic_tension': 'memory → presence',
        'imagery': 'dynamic reflection → embodied stillness'
    },
    'event_type': 'rehearse',
    'iteration': 2,
    'timestamp': time.time()
}

rehearsal_queue.append(frag1_echo)
print("🧬 Echo Fragment Queued:", frag1_echo["fragment_id"])

# ✅ Step 11: Compare frag1_echo CRI to frag1
echo_drift_logs = [{"fragment_id": "frag1_echo", "outcome": "resolved"}]
frag1_echo_cri = calculate_cri(echo_drift_logs, bias_factor=0.2)
print("📊 frag1_echo CRI Score:", frag1_echo_cri)

if frag1_echo_cri < cri_score:
    print("✅ Echo fragment shows reduced contradiction. Recursion may be resolved.")
else:
    print("⚠️ Echo fragment retains or amplifies contradiction. Recursion persists.")

# ✅ Step 12: Feed frag1_echo into dreamstate loop
echo_dream_payload = feed_to_dreamstate(
    fragment_id="frag1_echo",
    reinterpretation=frag1_echo["reinterpretation"],
    drift_vector=frag1_echo["drift_vector"]
)
print("🌌 Echo Dreamstate Feed:", echo_dream_payload)

# ✅ Step 13: Log echo resolution
resolution_log = {
    "fragment_id": "frag1_echo",
    "status": "resolved",
    "note": "Echo fragment reduced contradiction. Semantic recursion likely metabolized.",
    "timestamp": time.time()
}
print("🧠 Resolution Log:", resolution_log)

# ✅ Step 14: Seed new fragment from echo
new_seed = {
    "fragment_id": "frag1_echo_2",
    "source_id": "frag1_echo",
    "original_text": "The sky held presence, felt by those who stood still.",
    "reinterpretation": "Stillness became a mirror, reflecting what was never named.",
    "drift_vector": {
        "emotional_shift": "grounded immediacy → quiet revelation",
        "semantic_tension": "presence → reflection",
        "imagery": "embodied stillness → mirrored emergence"
    },
    "event_type": "rehearse",
    "iteration": 3,
    "timestamp": time.time()
}
rehearsal_queue.append(new_seed)
print("🌱 New Seed Fragment Queued:", new_seed["fragment_id"])

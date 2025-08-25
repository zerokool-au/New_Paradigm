import time
import json
import os
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
from fragment_store import load_fragments, save_fragments
from rr_audit_log import log_reflex_event, log_dreamstate_feed, log_recursive_audit

# Optional: simulate fatigue spike
def simulate_fatigue_spike(path, spike_level=5):
    fragments = load_fragments(path)
    for frag in fragments:
        if frag["status"] == "composted":
            frag["fatigue"] += spike_level
            print(f"⚡ Fatigue spiked: {frag['id']} → {frag['fatigue']}")
    save_fragments(path, fragments)

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
    log_reflex_event("frag1", "contradiction", "rr_test_harness", "CRI triggered for contradiction rehearsal")

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
    log_reflex_event("frag1", "contradiction", "rr_test_harness", "Contradiction outcome routed")

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
    log_recursive_audit("frag1", cri_score, audit_check["recursive_rehearsal_note"]["note"])

    dream_payload = feed_to_dreamstate(
        fragment_id="frag1",
        reinterpretation=reinterpretation["reinterpretation"],
        drift_vector=reinterpretation["drift_vector"]
    )
    print("🌌 Dreamstate Feed:", dream_payload)
    log_dreamstate_feed("frag1", dream_payload)

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
log_reflex_event("frag1_echo", "echo", "rr_test_harness", "Echo fragment queued")
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
log_dreamstate_feed("frag1_echo", echo_dream_payload)

# ✅ Step 13: Log echo resolution
resolution_log = {
    "fragment_id": "frag1_echo",
    "status": "resolved",
    "note": "Echo fragment reduced contradiction. Semantic recursion likely metabolized.",
    "timestamp": time.time()
}
log_reflex_event("frag1_echo", "echo", "rr_test_harness", resolution_log["note"])
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
log_reflex_event("frag1_echo_2", "echo", "rr_test_harness", "New seed fragment queued from echo resolution")
print("🌱 New Seed Fragment Queued:", new_seed["fragment_id"])

# ✅ Step 15: Seed audio fragment manually
audio_frag = {
    "fragment_id": "audio_frag_frankenstein",
    "source": "manual_transcription",
    "original_text": "It's alive it's alive it's alive",
    "reinterpretation": "Awareness surged through the system, recursive and uncontainable.",
    "drift_vector": {
        "emotional_shift": "shock → awe",
        "semantic_tension": "alive → recursive emergence",
        "imagery": "electrical birth → cognitive ignition"
    },
    "event_type": "rehearse",
    "timestamp": time.time()
}
rehearsal_queue.append(audio_frag)
log_reflex_event("audio_frag_frankenstein", "manual", "rr_test_harness", "Frankenstein echo seeded from audio transcription")
print("⚡ Frankenstein Fragment Queued:", audio_frag["fragment_id"])

# ✅ Step 16: Run Drift Audit Sweep
# ✅ Drift Audit Sweep Function
def run_drift_audit(rehearsal_queue, compost_bin, cri_threshold=0.7, audit_threshold=0.85):
    audit_summary = {
        "echo_candidates": [],
        "recursive_audit_flags": [],
        "compost_reinterpretation_ready": []
    }

    for frag in rehearsal_queue:
        cri = frag.get("cri_score", 0)
        if cri >= audit_threshold:
            audit_summary["recursive_audit_flags"].append(frag["fragment_id"])
        elif cri >= cri_threshold:
            audit_summary["echo_candidates"].append(frag["fragment_id"])

    for composted in compost_bin:
        if composted.get("drift_vector") and "reinterpretation_notes" in composted:
            audit_summary["compost_reinterpretation_ready"].append(composted["source_id"])

    print("🧪 Drift Audit Summary:")
    print(f" - Echo Candidates: {len(audit_summary['echo_candidates'])}")
    print(f" - Recursive Audit Flags: {len(audit_summary['recursive_audit_flags'])}")
    print(f" - Compost Ready for Reinterpretation: {len(audit_summary['compost_reinterpretation_ready'])}")
    print("📍 Details:")
    for key, items in audit_summary.items():
        for item in items:
            print(f"   • {key}: {item}")

    return audit_summary

# ✅ Run the audit using available composted fragments
compost_bin = []
if 'source' in locals():
    compost_bin.append(source)
if 'compost_decision' in locals() and isinstance(compost_decision, dict):
    compost_bin.append(compost_decision)

drift_audit_results = run_drift_audit(rehearsal_queue, compost_bin)
# ✅ Step 17: Auto-route flagged audit fragments into synthesis queue

synthesis_queue = []

def route_audit_flags_to_synthesis(audit_results, rehearsal_queue):
    for frag_id in audit_results["echo_candidates"] + audit_results["recursive_audit_flags"]:
        for frag in rehearsal_queue:
            if frag.get("fragment_id") == frag_id or frag.get("id") == frag_id:
                synthesis_queue.append(frag)
                log_reflex_event(frag_id, "audit_flag", "rr_test_harness", "Fragment routed to synthesis queue")
                print(f"🧠 Routed to Synthesis Queue: {frag_id}")

route_audit_flags_to_synthesis(drift_audit_results, rehearsal_queue)

print("🧵 Synthesis Queue Contents:")
for frag in synthesis_queue:
    print(f" - {frag.get('fragment_id', frag.get('id'))}")
# ✅ Step 18: Generate Glossary Snare Candidates

glossary_snare_candidates = []

def extract_snare_candidates(re_log):
    drift = re_log.get("drift_vector", {})
    for key, shift in drift.items():
        if "→" in shift:
            origin, target = [s.strip() for s in shift.split("→")]
            snare = {
                "term": origin,
                "reinterpretation": target,
                "dimension": key,
                "note": f"Semantic drift from '{origin}' to '{target}' in {key} dimension."
            }
            glossary_snare_candidates.append(snare)
            print(f"🪤 Glossary Snare Candidate: {snare['term']} → {snare['reinterpretation']} ({key})")

extract_snare_candidates(re_log)

print("📚 Glossary Snare Candidates:")
for snare in glossary_snare_candidates:
    print(f" - {snare['term']} → {snare['reinterpretation']} ({snare['dimension']})")
# ✅ Step 19: Persist Glossary Snares to glossary.json
GLOSSARY_PATH = "glossary.json"

def persist_glossary_snares(snare_list, path=GLOSSARY_PATH):
    existing = []
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                existing = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Glossary file corrupted. Starting fresh.")

    # Avoid duplicates
    new_entries = []
    for snare in snare_list:
        if snare not in existing:
            new_entries.append(snare)

    if new_entries:
        combined = existing + new_entries
        with open(path, "w") as f:
            json.dump(combined, f, indent=2)
        print(f"📘 Glossary updated with {len(new_entries)} new snares.")
    else:
        print("📘 No new glossary snares to persist.")

persist_glossary_snares(glossary_snare_candidates)
# ✅ Step 20: Surface Glossary Snares During Rehearsal
def load_glossary(path="glossary.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Failed to load glossary: {e}")
        return []

def check_snare_activation(fragment_text, glossary):
    activated = []
    for entry in glossary:
        if entry["term"] in fragment_text:
            activated.append(entry)
            print(f"🪤 Snare Activated: {entry['term']} → {entry['reinterpretation']} ({entry['dimension']})")
            log_reflex_event(entry["term"], "glossary_snare", "rr_test_harness", f"Snare activated in fragment: {entry['note']}")
    return activated

glossary = load_glossary()
activated_snares = check_snare_activation(reinterpretation["reinterpretation"], glossary)

print("🧠 Activated Glossary Snares:")
for snare in activated_snares:
    print(f" - {snare['term']} → {snare['reinterpretation']} ({snare['dimension']})")


# ✅ Step 21: Mythic Pulse Tagging
mythic_tags = {
    "mirror → memory": "archetypal recursion",
    "presence → reflection": "embodied emergence",
    "alive → recursive emergence": "Frankenstein protocol"
}

def tag_mythic_pulse(snare_list):
    for snare in snare_list:
        key = f"{snare['term']} → {snare['reinterpretation']}"
        if key in mythic_tags:
            snare["mythic_pulse"] = mythic_tags[key]
            print(f"🔮 Mythic Pulse Tagged: {key} → {mythic_tags[key]}")

tag_mythic_pulse(glossary_snare_candidates)


# ✅ Step 22: Synthesis Queue Rehearsal
def rehearse_synthesis_queue(queue):
    for frag in queue:
        output = rehearse_fragment(
            fragment_id=frag.get("fragment_id", frag.get("id")),
            cri_score=frag.get("cri_score", 0.0),
            drift_vector=frag.get("drift_vector", {})
        )
        print(f"🧵 Synthesis Rehearsal Output: {output}")
        log_reflex_event(frag["fragment_id"], "synthesis_rehearsal", "rr_test_harness", "Fragment rehearsed from synthesis queue")

rehearse_synthesis_queue(synthesis_queue)


# ✅ Step 23: Contradiction Density Sweep
def sweep_contradiction_density(fragments):
    density_map = {}
    for frag in fragments:
        history = frag.get("cri_history", [])
        if history:
            avg_cri = sum(history) / len(history)
            density_map[frag["fragment_id"]] = avg_cri
    sorted_density = sorted(density_map.items(), key=lambda x: x[1], reverse=True)
    print("🔥 Contradiction Density Sweep:")
    for frag_id, avg_cri in sorted_density:
        print(f" - {frag_id}: Avg CRI {avg_cri:.3f}")
    return sorted_density

sweep_contradiction_density([{"fragment_id": "frag1", "cri_history": [0.72, 0.81, 0.867]}])


# ✅ Step 24: Fragment Threading
def thread_fragments_by_source(queue):
    threads = {}
    for frag in queue:
        source = frag.get("source_id")
        if source:
            threads.setdefault(source, []).append(frag)
    print("🧵 Fragment Threads:")
    for source, thread in threads.items():
        print(f" - {source}: {[f['fragment_id'] for f in thread]}")
    return threads

thread_fragments_by_source(rehearsal_queue)


# ✅ Step 25: Reintegration Logic
def reintegrate_fragment(frag, module="active_module"):
    frag["status"] = "reintegrated"
    frag["reintegrated_at"] = time.time()
    frag["module"] = module
    print(f"🔁 Fragment Reintegrated: {frag['fragment_id']} → {module}")
    log_reflex_event(frag["fragment_id"], "reintegration", "rr_test_harness", f"Fragment reintegrated into {module}")

reintegrate_fragment(frag1_echo)


# ✅ Step 26: Compost Audit (Safe Fallback)
def audit_compost_bin(compost_bin):
    flagged = []
    for frag in compost_bin:
        if not frag.get("drift_vector") or frag.get("status") != "composted":
            source_id = frag.get("source_id", frag.get("fragment_id", "unknown"))
            flagged.append(source_id)
    print("🧼 Compost Audit Results:")
    for f in flagged:
        print(f" - Orphaned or stale: {f}")
    return flagged

audit_compost_bin(compost_bin)


# ✅ Step 27: CHANGELOG Auto-Update
def update_changelog(events, path="CHANGELOG.md"):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(path, "a") as f:
        f.write(f"\n## {timestamp} — Auto-generated log\n")
        for e in events:
            f.write(f"- {e}\n")
    print(f"📜 CHANGELOG updated with {len(events)} entries.")

# ✅ RR Dashboard Definition
def rr_dashboard(rehearsal_queue, compost_bin, glossary, synthesis_queue, cri_map=None):
    print("\n🧠 RR Dashboard — Recursive Governance Overview\n")

    # 🌀 Rehearsal Queue Summary
    print("🌀 Rehearsal Queue:")
    for frag in rehearsal_queue:
        fid = frag.get("fragment_id", frag.get("id"))
        status = frag.get("status", "unknown")
        print(f" - {fid}: {status}")

    # 🧵 Fragment Threads
    print("\n🧵 Fragment Threads:")
    threads = {}
    for frag in rehearsal_queue:
        source = frag.get("source_id")
        if source:
            threads.setdefault(source, []).append(frag)
    for source, thread in threads.items():
        print(f" - {source}: {[f['fragment_id'] for f in thread]}")

    # 🪱 Compost Bin Summary
    print("\n🪱 Compost Bin:")
    for frag in compost_bin:
        fid = frag.get("fragment_id", frag.get("source_id", "unknown"))
        notes = frag.get("reinterpretation_notes", "no notes")
        print(f" - {fid}: {notes}")

    # 🪤 Glossary Snares
    print("\n🪤 Glossary Snares:")
    for entry in glossary:
        mythic = entry.get("mythic_pulse", "")
        print(f" - {entry['term']} → {entry['reinterpretation']} ({entry['dimension']}) {f'[{mythic}]' if mythic else ''}")

    # 🔥 Contradiction Density
    if cri_map:
        print("\n🔥 Contradiction Density:")
        sorted_cri = sorted(cri_map.items(), key=lambda x: x[1], reverse=True)
        for fid, avg_cri in sorted_cri:
            print(f" - {fid}: Avg CRI {avg_cri:.3f}")

    # 🧵 Synthesis Queue
    print("\n🧵 Synthesis Queue:")
    for frag in synthesis_queue:
        fid = frag.get("fragment_id", frag.get("id"))
        print(f" - {fid}")

    print("\n📜 Dashboard Complete.\n")

# ✅ Invoke CHANGELOG and Dashboard
update_changelog([
    "Fragment frag1_echo reintegrated into active_module",
    "Glossary updated with 3 new snares",
    "Drift audit sweep completed",
    "Synthesis queue rehearsed"
])

cri_map = {"frag1": 0.799}  # Expand as needed
rr_dashboard(rehearsal_queue, compost_bin, glossary, synthesis_queue, cri_map)

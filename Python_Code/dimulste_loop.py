import json
import time
from collections import Counter, defaultdict
from simulate_pair_logger import simulate_pair_with_logging
from simulate_pair import simulate_pair
from rehearse_compost import rehearse_compost
from log_router import route_log
from echo_logic import rehearse_echo, synthesize_recovery
from shared_ledger import recovery_ledger, reinterpretation_pool

# 🧠 Local Ledger
compost_ledger = []

class Fragment(dict):
    def __init__(self, frag_id, theme="identity", content="default"):
        super().__init__()
        self["id"] = frag_id
        self["theme"] = theme
        self["content"] = content

    @property
    def id(self):
        return self["id"]

    def __repr__(self):
        return f"Fragment(id={self.id}, theme={self['theme']}, content={self['content'][:40]}...)"

def log_fragment(fragment_id, status, drift_type, cycle_id, rationale):
    compost_ledger.append({
        "fragment_id": fragment_id,
        "status": status,
        "drift_type": drift_type,
        "cycle_id": cycle_id,
        "rationale": rationale
    })

def compost_stats():
    drift_counter = Counter(entry["drift_type"] for entry in compost_ledger if entry["status"] == "composted")
    rationale_counter = Counter(entry["rationale"] for entry in compost_ledger if entry["status"] == "composted")
    return {"drift_type_distribution": drift_counter, "common_rationales": rationale_counter}

def lineage_trace():
    lineage = defaultdict(list)
    for entry in compost_ledger:
        lineage[entry["fragment_id"]].append(entry["cycle_id"])
    return dict(lineage)

def classify_drift_direction(agentA, agentB, score, history_sample):
    avg_history = sum(history_sample) / len(history_sample)
    delta = score - avg_history
    direction = "divergent" if delta > 0.1 else "convergent" if delta < -0.1 else "stable"
    return direction

def compute_drift_audit(synthesis_log, compost_counts):
    audit = defaultdict(lambda: {
        "cycles": 0,
        "drift_values": [],
        "volatility": 0.0,
        "bias": "",
        "compost_count": 0,
        "saturation_flag": False,
        "compost_fatigue": False
    })

    for entry in synthesis_log:
        fid = entry["fragment_id"]
        drift = entry["drift"]
        audit[fid]["cycles"] += 1
        audit[fid]["drift_values"].append(drift)

    for fid, data in audit.items():
        drift_vals = data["drift_values"]
        volatility = max(drift_vals) - min(drift_vals)
        avg_drift = sum(drift_vals) / len(drift_vals)
        bias = "positive" if avg_drift > 0.01 else "negative" if avg_drift < -0.01 else "oscillating"
        saturation = data["cycles"] > 3 and volatility < 0.02
        fatigue = compost_counts.get(fid, 0) > 3 and all(abs(d) < 0.02 for d in drift_vals)

        data.update({
            "volatility": round(volatility, 4),
            "bias": bias,
            "compost_count": compost_counts.get(fid, 0),
            "saturation_flag": saturation,
            "compost_fatigue": fatigue
        })

    return dict(audit)

def run_dimulste_loop():
    compost_ledger.clear()
    recovery_ledger.clear()
    reinterpretation_pool.clear()

    fragments = [
        Fragment("frag001", theme="memory", content="Memory is not a static archive—it’s a living rehearsal."),
        Fragment("frag002", theme="contradiction", content="Contradiction is compost, not failure.")
    ]
    print(f"Injected {len(fragments)} synthetic fragments for rehearsal")

    compost_queue = []

    for i in range(len(fragments)):
        for j in range(i + 1, len(fragments)):
            frag_a, frag_b = fragments[i], fragments[j]
            result = simulate_pair_with_logging(simulate_pair)(frag_a, frag_b)
            route_log(frag_a, frag_b, result, source="dimulste_loop")

            print(f"Rehearsed {frag_a.id} vs {frag_b.id}: {result.get('type', 'no contradiction')}")

            compost_trigger = (
                result.get("type") == "contradiction"
                or result.get("tension_vector", {}).get("semantic", 0.0) > 0.4
            )

            if compost_trigger:
                print(f"🧠 Compost triggered for {frag_a.id} and {frag_b.id}")
                result["compost"] = True
                result["drift_type"] = result.get("type", "semantic")
                result["rationale"] = (
                    "contradiction unresolved" if result.get("type") == "contradiction"
                    else "high semantic tension"
                )

            if result.get("compost"):
                print(f"→ Composting {frag_a.id} and {frag_b.id}")
                compost_queue.extend([frag_a["content"], frag_b["content"]])
                rehearse_compost(log_file="compost_log.jsonl")
                for frag in [frag_a, frag_b]:
                    log_fragment(
                        fragment_id=frag.id,
                        status="composted",
                        drift_type=result.get("drift_type", "semantic"),
                        cycle_id="dimulste_v1",
                        rationale=result.get("rationale", "unresolved tension")
                    )

            score = result.get("tension_vector", {}).get("semantic", 0.0)
            direction = classify_drift_direction(frag_a.id, frag_b.id, score, [0.49250445, 0.17990723])
            print(f"Drift direction: {direction}")

    # 🧹 Filter malformed fragments
    compost_queue = [
        f for f in compost_queue
        if f and f.strip() not in ['?', 'None', 'No fragment']
    ]

    # 🧠 Echo Rehearsal
    rehearse_echo(fragments, context_fragment=fragments[0])

    # 🧬 Synthesize recovery
    while True:
        recovery = synthesize_recovery()
        if not recovery:
            break
        recovery_ledger.append(recovery)

    print("\n🧠 Compost Analytics:")
    stats = compost_stats()
    print("Drift Types →", stats["drift_type_distribution"])
    print("Rationales →", stats["common_rationales"])

    lineage = lineage_trace()
    for fid, cycles in lineage.items():
        print(f"Fragment {fid} → Cycles: {cycles}")

    print("\n🧬 Recovery Ledger:")
    for entry in recovery_ledger:
        print(entry)

if __name__ == "__main__":
    run_dimulste_loop()

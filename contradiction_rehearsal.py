import json
from collections import defaultdict
from datetime import datetime
from dimulste_loop import Fragment
from simulate_pair_logger import simulate_pair_with_logging
from simulate_pair import simulate_pair

# Load reinterpretation log entries
def load_reinterpretations(log_file="Reinterpretation_Log.jsonl"):
    entries = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                entries.append(json.loads(line))
        print(f"Loaded {len(entries)} reinterpretations")
    except FileNotFoundError:
        print(f"No reinterpretation log found at {log_file}")
    return entries

# Group entries by fragment ID
def group_by_fragment(entries):
    fragment_map = defaultdict(lambda: {"preserved": [], "composted": []})
    for entry in entries:
        fragments = entry.get("source_fragments", [])
        reinterpretation = entry.get("reinterpretation", {})
        status = reinterpretation.get("status", "unknown")
        summary = reinterpretation.get("summary", "")
        for frag_id in fragments:
            if status == "preserved":
                fragment_map[frag_id]["preserved"].append(summary)
            elif status == "composted":
                fragment_map[frag_id]["composted"].append(summary)
    return fragment_map

# Batch contradiction rehearsal across fragment map
def simulate_contradictions_batch(fragment_map):
    logged_simulate_pair = simulate_pair_with_logging(simulate_pair)
    for frag_id, branches in fragment_map.items():
        preserved = branches["preserved"]
        composted = branches["composted"]
        if preserved and composted:
            print(f"\n🧪 Contradiction Rehearsal for Fragment {frag_id}:")
            for p_summary in preserved:
                for c_summary in composted:
                    frag_a = Fragment(frag_id, theme="preserved", content=p_summary)
                    frag_b = Fragment(frag_id, theme="composted", content=c_summary)
                    result = logged_simulate_pair(frag_a, frag_b)
                    print(f"→ {frag_a.theme} vs {frag_b.theme}")
                    print(f"   Type: {result.get('type', 'none')}")
                    print(f"   Semantic tension: {result.get('tension_vector', {}).get('semantic', 'n/a')}")
                    print("-" * 40)

# Single-fragment contradiction simulation (used by rehearsal_queue)
def simulate_contradictions_single(fragment):
    """
    Simulates contradiction rehearsal for a single fragment string.
    Returns a list of mock contradiction objects.
    """
    return [
        {"tension": 0.78, "reason": "Conflicts with prior composted reinterpretation"},
        {"tension": 0.65, "reason": "Semantic drift from preserved lineage"}
    ]

# Governance-aware contradiction filter
def detect_contradictions(fragment, threshold=0.7):
    raw_results = simulate_contradictions_single(fragment)
    filtered = [c for c in raw_results if c.get("tension", 0) >= threshold]
    print(f"[Detect] {len(filtered)} contradictions passed threshold ({threshold}).")
    return filtered

# Recursive rehearsal metabolizer
def rehearse_contradiction(fragment, contradictions):
    tension_score = sum(c.get("tension", 0) for c in contradictions) / len(contradictions)
    reasons = [c.get("reason", "Unspecified") for c in contradictions]
    if tension_score < 0.5:
        status = "preserve"
        reason = f"Low average tension ({tension_score:.2f})"
    else:
        status = "compost"
        reason = f"High average tension ({tension_score:.2f})"
    print(f"[Rehearse] {status.upper()} fragment — {reason}")
    return {
        "status": status,
        "reason": reason,
        "contradictions": contradictions,
        "reasons": reasons
    }

# Entry point for batch rehearsal
def run_contradiction_rehearsal():
    entries = load_reinterpretations()
    fragment_map = group_by_fragment(entries)
    simulate_contradictions_batch(fragment_map)

if __name__ == "__main__":
    run_contradiction_rehearsal()

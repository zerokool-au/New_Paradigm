import json
from rr_metrics import detect_contradiction, calculate_tension

GOVERNANCE_LOG = []

def load_synthesis_queue(path="synthesis_queue.json"):
    with open(path, "r") as f:
        return json.load(f)

def rehearse_fragment(fragment, anchor):
    contradiction = detect_contradiction(fragment, anchor)
    tension = calculate_tension(fragment, anchor)

    log_entry = {
        "id": fragment["id"],
        "content": fragment["content"],
        "contradiction": contradiction,
        "epistemic_tension": tension,
        "anchor": anchor,
        "tags": fragment.get("tags", []),
        "status": "flagged_for_rehearsal" if tension > 0.7 else "stable"
    }

    GOVERNANCE_LOG.append(log_entry)
    print(f"Rehearsed fragment {fragment['id']} → Tension: {tension:.2f}")

def run_governance_loop(anchor="SYN001"):
    fragments = load_synthesis_queue()
    for frag in fragments:
        if frag.get("status") == "reintegration_complete" and frag.get("contradiction_score") == 0.0:
            rehearse_fragment(frag, anchor)

def save_log(path="governance_log.json"):
    with open(path, "w") as f:
        json.dump(GOVERNANCE_LOG, f, indent=2)
    print(f"Governance log saved with {len(GOVERNANCE_LOG)} entries.")

if __name__ == "__main__":
    run_governance_loop()
    save_log()

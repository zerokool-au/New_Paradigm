# rr_governance_rehearsal.py
import json
import time
from echo_logic import generate_echo_prompt
from reinterpret_fragments import reinterpret_fragments

def load_contradiction_log(log_file="Contradiction_Log.jsonl"):
    contradictions = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                entry = json.loads(line)
                if entry.get("type") in ["contradiction", "semantic"]:
                    contradictions.append(entry)
        print(f"Loaded {len(contradictions)} contradiction entries")
    except FileNotFoundError:
        print(f"No contradiction log found at {log_file}")
    return contradictions

def audit_contradictions(contradictions):
    audit_report = []
    for entry in contradictions:
        semantic_tension = entry.get("tension_vector", {}).get("semantic", 0.0)
        threshold = 0.5  # You can tune this dynamically later
        governance_flag = semantic_tension >= threshold

        audit_entry = {
            "timestamp": time.time(),
            "agentA": entry.get("agentA"),
            "agentB": entry.get("agentB"),
            "semantic_tension": semantic_tension,
            "governance_flag": governance_flag,
            "notes": "High tension—requires reinterpretation" if governance_flag else "Stable contradiction"
        }

        audit_report.append(audit_entry)

    with open("Governance_Audit_Log.jsonl", "a") as f:
        for report in audit_report:
            f.write(json.dumps(report) + "\n")

    return audit_report

def rehearse_governance_fragments(audit_report):
    for entry in audit_report:
        if entry["governance_flag"]:
            print(f"⚠️ Governance-critical contradiction between {entry['agentA']} and {entry['agentB']}")
            print(f"→ Rehearsing epistemic fault line: {entry['notes']}")

            echo_prompt = generate_echo_prompt(entry["agentA"], entry["agentB"], entry["semantic_tension"])
            print("\n🌀 Echo Logic Prompt:")
            print(echo_prompt)

            reinterpretation = reinterpret_fragments(
                prompt=echo_prompt,
                agentA=entry["agentA"],
                agentB=entry["agentB"]
            )

            print("\n🌱 Reinterpretation Output:")
            print(json.dumps(reinterpretation["reinterpretation"], indent=2))
            print("-" * 60)

def run_governance_rehearsal():
    contradictions = load_contradiction_log()
    audit_report = audit_contradictions(contradictions)
    rehearse_governance_fragments(audit_report)

# Entry point
if __name__ == "__main__":
    run_governance_rehearsal()

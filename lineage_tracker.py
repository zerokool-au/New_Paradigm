# lineage_tracker.py
import json
from collections import defaultdict

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

def build_lineage_map(entries):
    lineage = defaultdict(list)

    for entry in entries:
        fragments = entry.get("source_fragments", [])
        reinterpretation = entry.get("reinterpretation", {})
        status = reinterpretation.get("status", "unknown")
        summary = reinterpretation.get("summary", "")

        for frag_id in fragments:
            lineage[frag_id].append({
                "status": status,
                "summary": summary
            })

    return lineage

def display_lineage(lineage):
    print("\n🧬 Fragment Lineage Map:")
    for frag_id, branches in lineage.items():
        print(f"\nFragment ID: {frag_id}")
        for i, branch in enumerate(branches, 1):
            print(f"  Gen {i}: Status → {branch['status']}")
            print(f"         Summary → {branch['summary'][:80]}...")
        print("-" * 60)

def run_lineage_tracker():
    entries = load_reinterpretations()
    lineage = build_lineage_map(entries)
    display_lineage(lineage)

# Entry point
if __name__ == "__main__":
    run_lineage_tracker()

# semantic_lineage.py

import json
from collections import defaultdict
from datetime import datetime

LINEAGE_LOG = "Fragment_Log.jsonl"

def load_fragment_log(log_file=LINEAGE_LOG):
    try:
        with open(log_file, "r") as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        print(f"[Lineage] No fragment log found at {log_file}")
        return []

def trace_lineage():
    entries = load_fragment_log()
    lineage_map = defaultdict(lambda: {"preserved": [], "composted": []})

    for entry in entries:
        frag = entry.get("fragment", "")
        status = entry.get("status", "unknown")
        reason = entry.get("reason", "")
        timestamp = entry.get("timestamp", "")

        if status == "preserve":
            lineage_map[frag]["preserved"].append((timestamp, reason))
        elif status == "compost":
            lineage_map[frag]["composted"].append((timestamp, reason))

    return lineage_map

def print_lineage_summary(lineage_map):
    for frag, branches in lineage_map.items():
        print(f"\n🧬 Lineage for Fragment: {frag}")
        if branches["preserved"]:
            print("  ✅ Preserved:")
            for ts, reason in branches["preserved"]:
                print(f"    - {ts}: {reason}")
        if branches["composted"]:
            print("  🌀 Composted:")
            for ts, reason in branches["composted"]:
                print(f"    - {ts}: {reason}")

# CLI trigger
if __name__ == "__main__":
    lineage = trace_lineage()
    print_lineage_summary(lineage)

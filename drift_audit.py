import json
import time
from collections import defaultdict

def load_log_entries(log_file="Drift_Anomaly_Log.jsonl"):
    entries = []
    try:
        with open(log_file, "r") as f:
            for line in f:
                entries.append(json.loads(line))
        print(f"📥 Loaded {len(entries)} entries from {log_file}")
    except FileNotFoundError:
        print(f"⚠️ No log file found at {log_file}")
    return entries

def audit_entries(entries):
    missing_fields = defaultdict(list)
    suppressed_flags = []

    for entry in entries:
        ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(entry.get("timestamp", 0)))

        # Check for missing tension vector
        if "tension_vector" not in entry or entry["tension_vector"].get("semantic") is None:
            missing_fields["tension_vector"].append(ts)

        # Check for contradiction type
        if entry.get("type", "none") == "none":
            missing_fields["contradiction_type"].append(ts)

        # Check for suppressed tension
        if entry.get("suppress_flag"):
            suppressed_flags.append(ts)

    print("\n📊 Drift Audit Summary:")
    for field, timestamps in missing_fields.items():
        print(f"→ Missing {field}: {len(timestamps)} occurrences")
        for ts in timestamps[:3]:
            print(f"   - {ts}")
        if len(timestamps) > 3:
            print(f"   ...and {len(timestamps) - 3} more")
        print("-" * 40)

    if suppressed_flags:
        print(f"🚨 Suppressed Tension Detected: {len(suppressed_flags)} cases")
        for ts in suppressed_flags[:3]:
            print(f"   - {ts}")
        if len(suppressed_flags) > 3:
            print(f"   ...and {len(suppressed_flags) - 3} more")
        print("-" * 40)

def run_drift_audit(log_file="Drift_Anomaly_Log.jsonl"):
    entries = load_log_entries(log_file)
    audit_entries(entries)

# Entry point
if __name__ == "__main__":
    run_drift_audit()

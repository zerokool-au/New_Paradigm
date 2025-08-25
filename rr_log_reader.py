import json, os
from datetime import datetime

LOG_FILE = os.path.join("logs", "rr_audit_log.json")

def load_logs():
    if not os.path.exists(LOG_FILE):
        print("No audit log found.")
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def filter_logs(logs, reflex_type=None, fragment_id=None, override_only=False):
    filtered = []
    for entry in logs:
        if reflex_type and entry.get("reflex_type") != reflex_type:
            continue
        if fragment_id and entry["details"].get("fragment_id") != fragment_id:
            continue
        if override_only and not entry.get("ambient_override"):
            continue
        filtered.append(entry)
    return filtered

def print_log(entry):
    ts = entry["timestamp"]
    etype = entry["event_type"]
    module = entry["module"]
    details = entry["details"]
    reflex = entry.get("reflex_type", "—")
    override = "🦘" if entry.get("ambient_override") else ""
    print(f"[{ts}] {etype.upper()} ({module}) {override}")
    print(f"  Reflex Type: {reflex}")
    for k, v in details.items():
        print(f"  {k}: {v}")
    print("-" * 40)

def tail_logs(count=5):
    logs = load_logs()
    for entry in logs[-count:]:
        print_log(entry)

def query_logs(reflex_type=None, fragment_id=None, override_only=False):
    logs = load_logs()
    filtered = filter_logs(logs, reflex_type, fragment_id, override_only)
    for entry in filtered:
        print_log(entry)

# Local test block
if __name__ == "__main__":
    print("🧠 RR Audit Log Tail (last 5 entries):")
    tail_logs()

    print("\n🔍 Filter: Reflex Type = 'echo'")
    query_logs(reflex_type="echo")

    print("\n🔍 Filter: Override Events Only")
    query_logs(override_only=True)

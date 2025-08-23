import datetime

class DriftAudit:
    def __init__(self):
        self.audit_log = []

    def log_drift(self, fragment, preserved, composted):
        timestamp = datetime.datetime.now().isoformat()

        entry = {
            "timestamp": timestamp,
            "fragment": fragment,
            "preserved": preserved,
            "composted": composted
        }

        self.audit_log.append(entry)

        # Optional: write to file using UTF-8 encoding
        with open("rr_drift_audit_log.txt", "a", encoding="utf-8") as log:
            log.write(f"{timestamp} | Fragment: {fragment}\n")
            log.write(f"  Preserved: {preserved}\n")
            log.write(f"  Composted: {composted}\n\n")

        print(f"\n📚 Drift audit logged at {timestamp}")

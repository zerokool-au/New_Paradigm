import json, os
from datetime import datetime, timezone

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "rr_audit_log.json")
os.makedirs(LOG_DIR, exist_ok=True)

def timestamp():
    return datetime.now(timezone.utc).isoformat()

def log_event(event_type, module, details, reflex_type=None, override=False):
    entry = {
        "timestamp": timestamp(),
        "event_type": event_type,
        "module": module,
        "details": details
    }
    if reflex_type:
        entry["reflex_type"] = reflex_type
    if override:
        entry["ambient_override"] = True
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[rr_audit_log] Failed to write log entry: {e}")

# 🧪 Reflex Logging Shortcuts
def log_reflex_event(fragment_id, reflex_type, module, note, override=False):
    log_event(
        event_type="reflex",
        module=module,
        details={
            "fragment_id": fragment_id,
            "note": note
        },
        reflex_type=reflex_type,
        override=override
    )

def log_dreamstate_feed(fragment_id, payload):
    log_event(
        event_type="dreamstate_feed",
        module="dimulste",
        details={
            "fragment_id": fragment_id,
            "payload": payload
        }
    )

def log_contradiction_outcome(fragment_id, outcome, drift_vector):
    log_event(
        event_type="contradiction_outcome",
        module="contradiction_router",
        details={
            "fragment_id": fragment_id,
            "outcome": outcome,
            "drift_vector": drift_vector
        },
        reflex_type="contradiction"
    )

def log_recursive_audit(fragment_id, cri_score, note):
    log_event(
        event_type="recursive_audit",
        module="audit_trigger",
        details={
            "fragment_id": fragment_id,
            "cri_score": cri_score,
            "note": note
        },
        reflex_type="audit"
    )

# Local test block
if __name__ == "__main__":
    log_reflex_event(
        fragment_id="frag_test",
        reflex_type="echo",
        module="rr_test_harness",
        note="Echo fragment queued for recursion test",
        override=True
    )
    log_dreamstate_feed(
        fragment_id="frag_test",
        payload={"text": "Test dreamstate payload", "drift": {"semantic_tension": "test → echo"}}
    )
    print("Audit log test entries written.")

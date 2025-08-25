# fragment_logger.py

import json
from datetime import datetime

LOG_FILE = "Fragment_Log.jsonl"

def log_fragment(fragment, outcome):
    """
    Logs fragment outcome to persistent JSONL file.
    Includes timestamp, status, tension, and contradiction metadata.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "fragment": fragment,
        "status": outcome.get("status"),
        "reason": outcome.get("reason"),
        "contradictions": outcome.get("contradictions", []),
        "reasons": outcome.get("reasons", [])
    }

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[Logger] Logged fragment with status: {entry['status']}")
    except Exception as e:
        print(f"[Logger] Failed to log fragment: {e}")

def read_log():
    try:
        with open(LOG_FILE, "r") as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    test_fragment = "The map is not the territory."
    test_outcome = {
        "status": "preserve",
        "reason": "Low semantic tension",
        "contradictions": [],
        "reasons": []
    }
    log_fragment(test_fragment, test_outcome)



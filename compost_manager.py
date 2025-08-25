# compost_manager.py

import json
from datetime import datetime

COMPOST_FILE = "Composted_Fragments.jsonl"
PRESERVE_FILE = "Preserved_Fragments.jsonl"

def compost_fragment(fragment, reason=""):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "fragment": fragment,
        "status": "composted",
        "reason": reason
    }
    try:
        with open(COMPOST_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[Compost] Fragment composted: {reason}")
    except Exception as e:
        print(f"[Compost] Failed to log composted fragment: {e}")

def preserve_fragment(fragment, reason=""):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "fragment": fragment,
        "status": "preserved",
        "reason": reason
    }
    try:
        with open(PRESERVE_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[Preserve] Fragment preserved: {reason}")
    except Exception as e:
        print(f"[Preserve] Failed to log preserved fragment: {e}")

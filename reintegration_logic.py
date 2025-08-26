# reintegration_logic.py

import json
from datetime import datetime
from fragment_store import load_fragments, save_fragments
from synthesis_queue import enqueue_fragment
from rr_audit_log import log_event
from rr_memory import update_memory

def reintegrate_fragments(store_path, threshold=0.7):
    fragments = load_fragments(store_path)
    reintegrated = []

    for frag in fragments:
        if frag.get("drift_score", 1.0) < threshold and frag.get("status") == "composted":
            frag["status"] = "reintegrated"
            frag["reintegration_timestamp"] = datetime.utcnow().isoformat()

            # Enqueue for synthesis or further rehearsal
            enqueue_fragment(frag)

            # Update RR memory system
            update_memory({
                "id": frag["id"],
                "text": frag["text"],
                "tag": frag.get("tag", ""),
                "drift_score": frag["drift_score"],
                "status": "reintegrated",
                "timestamp": frag["reintegration_timestamp"]
            })

            # Log the reintegration event
            log_event(
                event_type="reintegration",
                module="reintegration_logic",
                details={
                    "fragment_id": frag["id"],
                    "drift_score": frag["drift_score"],
                    "tag": frag.get("tag", ""),
                    "timestamp": frag["reintegration_timestamp"]
                }
            )

            print(f"Reintegrated: {frag['id']}")
            reintegrated.append(frag["id"])

    # Save updated fragment store
    save_fragments(store_path, fragments)

    return reintegrated

if __name__ == "__main__":
    reintegrate_fragments("fragment_store.json")

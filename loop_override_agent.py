# loop_override_agent.py

from fragment_store import load_fragments, save_fragments
from rr_audit_log import log_event
from glossary_engine import echo_glossary
from datetime import datetime, timezone

def override_loops(store_path):
    fragments = load_fragments(store_path)
    updated = []

    for frag in fragments:
        if frag.get("status") == "recursive_loop":
            drift = frag.get("drift_score", 0)
            fatigue = frag.get("fatigue", 0)
            loop_count = frag.get("loop_count", 1)

            frag["loop_count"] = loop_count + 1

            # Ambient override trigger
            if fatigue >= drift and loop_count >= 3:
                frag["status"] = "composted"
                frag["tag"] = "closure-penalty"
                frag["override_timestamp"] = datetime.now(timezone.utc).isoformat()

                echo_glossary(
                    fragment=frag["text"],
                    tag="Closure Penalty",
                    resonance="loop fatigue override"
                )

                log_event(
                    event_type="loop_override",
                    module="loop_override_agent",
                    details={
                        "fragment_id": frag["id"],
                        "text": frag["text"],
                        "loop_count": loop_count,
                        "fatigue": fatigue,
                        "drift_score": drift,
                        "override": "composted"
                    }
                )

                print(f"[Override] Composting fragment: {frag['id']}")

            updated.append(frag["id"])

    save_fragments(store_path, fragments)
    return updated

if __name__ == "__main__":
    override_loops("fragment_store.json")

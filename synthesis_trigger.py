# synthesis_trigger.py

from fragment_store import load_fragments, save_fragments
from rr_audit_log import log_event
from glossary_engine import echo_glossary
from datetime import datetime, timezone

def trigger_synthesis(store_path):
    fragments = load_fragments(store_path)
    finalized = []

    for frag in fragments:
        if frag.get("tag") == "ready-for-glossary":
            frag["status"] = "glossary_finalized"
            frag["finalized_timestamp"] = datetime.now(timezone.utc).isoformat()
            frag["tag"] = "mythic-seeded"

            echo_glossary(
                fragment=frag["text"],
                tag="Mythic Glossary Entry",
                resonance="final synthesis echo"
            )

            log_event(
                event_type="synthesis_finalized",
                module="synthesis_trigger",
                details={
                    "fragment_id": frag["id"],
                    "text": frag["text"],
                    "timestamp": frag["finalized_timestamp"]
                }
            )

            print(f"[Synthesis] Finalized glossary entry: {frag['id']}")
            finalized.append(frag["id"])

    save_fragments(store_path, fragments)
    return finalized

if __name__ == "__main__":
    trigger_synthesis("fragment_store.json")

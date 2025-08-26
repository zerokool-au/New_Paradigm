# contradiction_router.py

from fragment_store import load_fragments, save_fragments
from rr_audit_log import log_event
from synthesis_queue import enqueue_fragment
from echo_witness import EchoWitness
from datetime import datetime

def route_contradictions(store_path):
    fragments = load_fragments(store_path)
    routed = []
    witness = EchoWitness()

    for frag in fragments:
        if frag.get("flagged") and (
            "contradiction_detected" in frag.get("flags", []) or
            frag.get("status") == "contradiction"
        ):
            frag["status"] = "contradiction_routed"
            from datetime import datetime, timezone
            frag["routing_timestamp"] = datetime.now(timezone.utc).isoformat()
            frag["tag"] = "contradiction-pending"

            enqueue_fragment(frag)

            log_event(
                event_type="contradiction_routing",
                module="contradiction_router",
                details={
                    "fragment_id": frag["id"],
                    "text": frag["text"],
                    "timestamp": frag["routing_timestamp"]
                }
            )

            witness.observe(
                event_type="contradiction_routed",
                fragment=frag["text"],
                resonance="epistemic tension"
            )

            print(f"Contradiction routed: {frag['id']}")
            routed.append(frag["id"])

    save_fragments(store_path, fragments)
    return routed

if __name__ == "__main__":
    route_contradictions("fragment_store.json")

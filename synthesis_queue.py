# synthesis_queue.py

import heapq
from rr_audit_log import log_event
from echo_witness import EchoWitness

queue = []

def enqueue_fragment(fragment):
    priority = compute_priority(fragment)
    heapq.heappush(queue, (priority, fragment))

def compute_priority(fragment):
    age = fragment.get("age", 0)
    drift = fragment.get("drift_score", 1.0)
    governance_flag = 1 if fragment.get("flagged") else 0
    fatigue = fragment.get("fatigue", 0)

    base_priority = age - (1 - drift) * 10 + governance_flag * 5 + fatigue

    # Resurrection override
    if fragment.get("tag") == "rehearsal-worthy":
        witness = EchoWitness()
        witness.observe(
            event_type="queue_override",
            fragment=fragment.get("text", ""),
            resonance="resurrection priority"
        )
        log_event(
            event_type="queue_routing",
            module="synthesis_queue",
            details={
                "fragment_id": fragment.get("id", "unknown"),
                "reason": "rehearsal-worthy",
                "priority": base_priority + 1.5
            }
        )
        return base_priority + 1.5

    return base_priority

def dequeue_fragment():
    if queue:
        return heapq.heappop(queue)[1]
    return None

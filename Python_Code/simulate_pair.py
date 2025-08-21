from notifier import issue_notifier
from fragment_router import route_fragment
import json
from datetime import datetime

def simulate_pair(agent_a, agent_b, context, threshold):
    """
    Compute a real ‘final_score’ from the history values,
    issue a notifier if it falls below threshold,
    route the fragment based on drift direction,
    and return the outcome payload.
    """
    # 1. Grab the history list (all floats) from context
    history = context.get("history", [])

    # 2. Compute final_score by averaging history values
    final_score = sum(history) / len(history) if history else 0.0

    # 3. Build the alert dict
    alert = {
        "agentA": agent_a.id,
        "agentB": agent_b.id,
        "score": final_score,
        "history_sample": history[:2]  # keep first two as example
    }

    # 4. Fire notifier if below threshold
    if final_score < threshold:
        issue_notifier(alert)

    # 5. Route the fragment based on drift direction
    fragment_text = context.get("fragment", "No fragment provided")
    direction = route_fragment(agent_a.id, agent_b.id, final_score, history[:2], fragment_text)
    print(f"Fragment routed as {direction}")

    # 6. Compost logging if no rehearsal lineage
    if direction == "no-history":
        with open("compost_queue.jsonl", "a", encoding="utf-8") as compost:
            json.dump({
                "fragment": agent_a.id,
                "agentB": agent_b.id,
                "score": final_score,
                "timestamp": datetime.now(datetime.UTC).isoformat(),
                "notes": "No rehearsal lineage—flagged for contradiction composting"
            }, compost)
            compost.write("\n")

    # 7. Return structured outcome
    return {
        "outcome": "processed",
        "drift_type": direction,
        "notes": "Second-pass complete",
        "timestamp": datetime.utcnow().isoformat()
    }
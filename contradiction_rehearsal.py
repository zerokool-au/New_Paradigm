# contradiction_rehearsal.py

from fragment_store import load_fragments, save_fragments
from rr_audit_log import log_contradiction_outcome
from glossary_engine import echo_glossary
from datetime import datetime, timezone

def rehearse_contradictions(store_path):
    fragments = load_fragments(store_path)
    updated = []

    for frag in fragments:
        if frag.get("tag") == "contradiction-pending":
            drift = frag.get("drift_score", 0)
            fatigue = frag.get("fatigue", 0)

            # Synthesis trigger logic
            if drift > 0.75 and fatigue < 3:
                frag["status"] = "synthesis_triggered"
                frag["tag"] = "ready-for-glossary"
                frag["rehearsal_timestamp"] = datetime.now(timezone.utc).isoformat()

                echo_glossary(
                    fragment=frag["text"],
                    tag="Contradiction Bloom",
                    resonance="signal-noise tension"
                )

                log_contradiction_outcome(
                    fragment_id=frag["id"],
                    outcome="synthesis_triggered",
                    drift_vector={"drift_score": drift, "fatigue": fatigue}
                )

                print(f"[Rehearsal] Synthesis triggered: {frag['id']}")

            # Recursive loop fallback
            else:
                frag["status"] = "recursive_loop"
                frag["tag"] = "looped-for-rehearsal"
                frag["rehearsal_timestamp"] = datetime.now(timezone.utc).isoformat()

                log_contradiction_outcome(
                    fragment_id=frag["id"],
                    outcome="looped_for_rehearsal",
                    drift_vector={"drift_score": drift, "fatigue": fatigue}
                )

                print(f"[Rehearsal] Looping fragment: {frag['id']}")

            updated.append(frag["id"])

    save_fragments(store_path, fragments)
    return updated

if __name__ == "__main__":
    rehearse_contradictions("fragment_store.json")

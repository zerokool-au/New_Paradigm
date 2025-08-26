def sweep_fragments(store_path, drift_threshold=0.8, fatigue_threshold=3):
    """
    Identify fragments with high drift or fatigue, or flagged for contradiction.
    """
    from fragment_store import load_fragments
    from synthesis_queue import enqueue_fragment
    from rr_audit_log import log_event

    fragments = load_fragments(store_path)
    candidates = []

    for frag in fragments:
        drift = frag.get("drift_score", 0)
        fatigue = frag.get("fatigue", 0)
        flagged = frag.get("flagged", False)

        if drift > drift_threshold or fatigue >= fatigue_threshold or flagged:
            frag["status"] = "driftkeeper_hold"
            enqueue_fragment(frag)
            candidates.append(frag["id"])

            log_event(
                event_type="driftkeeper_hold",
                module="driftkeeper",
                details={
                    "fragment_id": frag["id"],
                    "drift_score": drift,
                    "fatigue": fatigue,
                    "flagged": flagged
                }
            )

            print(f"Driftkeeper hold: {frag['id']}")

    return candidates

if __name__ == "__main__":
    sweep_fragments("fragment_store.json")


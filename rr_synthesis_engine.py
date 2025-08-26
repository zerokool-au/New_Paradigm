from rr_audit_log import log_event

def synthesize_fragment(fragment):
    """
    Perform reinterpretation or recursive synthesis on a fragment.
    """
    text = fragment.get("text", "")
    drift_score = fragment.get("drift_score", 0)
    tag = fragment.get("tag", "")

    # Simple reinterpretation logic (placeholder)
    if tag == "rehearsal-worthy":
        reinterpreted = f"[Rehearsed] {text} — contradiction metabolized."
    else:
        reinterpreted = f"[Synthesized] {text} — drift score: {drift_score}"

    # Optionally log synthesis
    from rr_audit_log import log_event
    log_event(
        event_type="synthesis",
        module="rr_synthesis_engine",
        details={
            "fragment_id": fragment.get("id", "unknown"),
            "output": reinterpreted
        }
    )

    return reinterpreted


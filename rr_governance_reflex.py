from rr_audit_log import log_event

def detect_contradiction(fragment):
    """
    Detect epistemic tension or contradiction in a fragment.

    Args:
        fragment (dict): Fragment object with .id and .text

    Returns:
        bool: True if contradiction detected, else False
    """
    contradiction_keywords = ["conflict", "tension", "paradox", "drift"]
    detected = any(kw in fragment["text"].lower() for kw in contradiction_keywords)

    if detected:
        fragment["flags"].append("contradiction_detected")

        # Reflex log
        log_event(
            event_type="governance_trigger",
            module="rr_governance_reflex",
            details={
                "fragment_id": fragment["id"],
                "trigger": "epistemic_tension",
                "content_preview": fragment["text"][:50],
                "flags": fragment["flags"]
            }
        )

    return detected

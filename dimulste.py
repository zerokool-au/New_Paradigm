from rr_audit_log import log_event

def simulate_dreamstate(fragment):
    """
    Simulate dreamstate rehearsal on a fragment.

    Args:
        fragment (dict): Fragment object with .id and .text

    Returns:
        dict: Simulated fragment with dreamstate metadata
    """
    simulated_text = f"[dreamstate] {fragment.text}"
    simulated_fragment = {
        "id": f"{fragment['id']}_dreamed",
        "source_id": fragment["id"],
        "text": simulated_text,
        "flags": ["dreamstate_simulated"]
    }

    # Reflex log
    log_event(
        event_type="simulation",
        module="dimulste",
        details={
            "fragment_id": fragment["id"],
            "simulated_id": simulated_fragment["id"],
            "content_preview": simulated_text[:50],
            "flags": simulated_fragment["flags"]
        }
    )

    return simulated_fragment

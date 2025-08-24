def should_rehearse(fragment, audit_log):
    return (
        fragment["status"] == "preserved"
        and audit_log.get(fragment["id"], {}).get("tension_score", 0) > 0.7
    )

def generate_rehearsal_queue(fragments, audit_log):
    return [f for f in fragments if should_rehearse(f, audit_log)]

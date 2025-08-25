def trigger_recursive_audit(inflammation_flags):
    audit_queue = []
    for flag in inflammation_flags:
        if flag["status"] == "inflammation":
            audit_queue.append({
                "fragment_id": flag["fragment_id"],
                "action": "rehearse" if not flag["composted"] else "reinterpret"
            })
    return audit_queue

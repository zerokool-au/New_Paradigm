def detect_inflammation(pulse_log, drift_log, compost_log):
    inflammation_flags = []

    for pulse in pulse_log:
        frag_id = pulse["fragment_id"]
        tension_type = pulse["tension_type"]

        # Check for cyclical tension or unresolved drift
        unresolved = any(
            log["fragment_id"] == frag_id and log["outcome"] == "escalated"
            for log in drift_log
        )

        composted = any(
            lineage["source_id"] == frag_id
            for lineage in compost_log
        )

        if tension_type == "cyclical" or unresolved:
            inflammation_flags.append({
                "fragment_id": frag_id,
                "tension_type": tension_type,
                "status": "inflammation",
                "composted": composted
            })

    return inflammation_flags

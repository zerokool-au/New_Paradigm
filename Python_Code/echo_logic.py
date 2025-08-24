from shared_ledger import reinterpretation_pool, recovery_ledger

def rehearse_echo(fragments, context_fragment):
    """
    Aligns each fragment with a context anchor to detect echo drift.
    Populates reinterpretation_pool with echo scores and context metadata.
    """
    for frag in fragments:
        content = frag.get("content", "")
        context = context_fragment.get("content", "")
        echo_score = 0.5 + 0.1 * ((len(content) + len(context)) % 5)  # Placeholder logic
        reinterpretation_pool.append({
            "fragment_id": frag["id"],
            "echo_score": round(echo_score, 4),
            "context": context,
            "status": "ready"
        })

def synthesize_recovery():
    """
    Synthesizes recovery fragments from reinterpretation_pool.
    Updates recovery_ledger with finalized entries.
    """
    while reinterpretation_pool:
        entry = reinterpretation_pool.pop(0)
        fid = entry["fragment_id"]
        echo_score = entry["echo_score"]
        context = entry["context"]

        reinterpretation = f"{context} → {fid} metabolized at echo score {echo_score}"
        recovery_ledger.append({
            "fragment_id": fid,
            "echo_score": echo_score,
            "reinterpreted": reinterpretation,
            "status": "ready"
        })
        print(f"🧬 Synthesized recovery for {fid}: {reinterpretation}")

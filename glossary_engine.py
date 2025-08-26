# Manual echo for frag_002
from rr_audit_log import log_event
from datetime import datetime, timezone

def echo_ambient_override():
    frag_text = "Semantic fatigue triggers ambient override."
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fragment": frag_text,
        "tag": "Ambient Override",
        "resonance": "fatigue bloom"
    }

    log_event(
        event_type="glossary_echo",
        module="glossary_engine",
        details=entry
    )

    print(f"[Glossary] Echoed 'Ambient Override' for fragment: {frag_text[:40]}...")

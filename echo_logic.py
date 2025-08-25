import re
import random
from rr_audit_log import log_event

class EchoLogic:
    def __init__(self):
        self.reinterpretation_log = []

    def reinterpret(self, fragment):
        new_text = self._rehearse_text(fragment.text)
        fragment.text = new_text
        fragment.flags.append("echo_reinterpreted")
        fragment.audit_trail.append({
            "source": "echo_logic",
            "action": "semantic_rehearsal"
        })
        self.reinterpretation_log.append(fragment.id)

        # Reflex log
        log_event(
            event_type="mutation",
            module="echo_logic",
            details={
                "fragment_id": fragment.id,
                "action": "semantic_rehearsal",
                "content_preview": new_text[:50],
                "flags": fragment.flags
            }
        )

        return fragment

    def _rehearse_text(self, text):
        # Replace contradiction vectors with recursive metaphors
        vectors = ["agency_conflict", "epistemic_tension", "identity_drift", "self_reference"]
        metaphors = ["wallaby recursion", "kookaburra cadence", "semantic compost", "governance echo"]
        pattern = r"vector (\w+)"
        return re.sub(pattern, lambda m: f"vector {random.choice(metaphors)}", text)

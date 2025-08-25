import re

class DriftDetector:
    def __init__(self):
        self.drift_log = []

    def detect_drift(self, fragment):
        drift_flags = []

        # Detect epistemic tension
        if "epistemic_tension" in fragment.text:
            drift_flags.append("epistemic_tension")

        # Detect semantic drift via metaphor substitution
        metaphors = ["wallaby recursion", "kookaburra cadence", "semantic compost", "governance echo"]
        if any(m in fragment.text for m in metaphors):
            drift_flags.append("semantic_drift")

        # Detect contradiction density
        contradiction_matches = re.findall(r"Contradiction \d+", fragment.text)
        if len(contradiction_matches) > 1:
            drift_flags.append("contradiction_cluster")

        if drift_flags:
            fragment.flags.extend(drift_flags)
            fragment.flags.append("drift_detected")
            fragment.audit_trail.append({
                "source": "drift_detector",
                "flags": drift_flags
            })
            self.drift_log.append(fragment.id)

        return fragment

    def scan(self, fragments):
        return [self.detect_drift(f) for f in fragments]

    def get_log(self):
        return self.drift_log

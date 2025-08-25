class MutationTrigger:
    def __init__(self, pulse_detector):
        self.pulse = pulse_detector

    def sweep(self, fragments):
        candidates = []
        for f in fragments:
            if "contradiction" in f.flags or "drift_detected" in f.flags:
                candidates.append(f)
        return candidates

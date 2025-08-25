class GovernanceTrigger:
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def check(self, fragment):
        pulse = fragment.metadata.get("pulse", {})
        cadence = pulse.get("cadence", 0)

        # Normalize cadence to a 0–1 scale (assuming max cadence = 10)
        normalized = cadence / 10.0
        return normalized > self.threshold

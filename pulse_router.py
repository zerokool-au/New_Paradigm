class PulseRouter:
    def __init__(self, pulse_detector):
        self.pulse = pulse_detector

    def tag_fragment(self, fragment):
        summary = self.pulse.summarize()
        for vector in summary:
            if vector in fragment.text:
                fragment.metadata["pulse"] = summary[vector]

    def route_fragment(self, fragment):
        pulse_data = fragment.metadata.get("pulse", {})
        if pulse_data.get("is_latent"):
            return "compost"
        elif pulse_data.get("cadence", 0) > 5:
            return "synthesis"
        else:
            return "rehearsal"

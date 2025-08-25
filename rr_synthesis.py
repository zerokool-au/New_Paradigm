class SynthesisEngine:
    def __init__(self, registry):
        self.registry = registry

    def synthesize_from_overload(self, threshold=5):
        overload = [r for r in self.registry.get_all() if len(r["vectors"]) >= 2]
        synthesized = []
        for item in overload[:threshold]:
            text = item["text"] + " [synthesized]"
            synthesized.append(text)
        return synthesized

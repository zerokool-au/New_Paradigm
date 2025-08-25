class ContradictionRegistry:
    def __init__(self):
        self.registry = []

    def register_contradiction(self, text, vectors):
        self.registry.append({
            "text": text,
            "vectors": vectors
        })

    def get_all(self):
        return self.registry

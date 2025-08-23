# rr_contradiction_registry.py

class ContradictionRegistry:
    def __init__(self):
        self.registry = {}

    def register_contradiction(self, fragment, bias_vectors):
        for vector in bias_vectors:
            if vector not in self.registry:
                self.registry[vector] = []
            self.registry[vector].append(fragment)
            print(f"📌 Registered contradiction: '{vector}' ← {fragment}")

    def get_fragments_by_vector(self, vector):
        return self.registry.get(vector, [])

    def get_all_vectors(self):
        return list(self.registry.keys())

    def summarize_registry(self):
        print("\n🧭 Contradiction Registry Summary:")
        for vector, fragments in self.registry.items():
            print(f"🔗 {vector}: {len(fragments)} fragments")

    def get_overloaded_vectors(self, threshold=2):
        overloaded = []
        for vector, fragments in self.registry.items():
            if len(fragments) >= threshold:
                overloaded.append((vector, len(fragments)))
        return overloaded

# ✅ TEST HARNESS — this must be outside the class
if __name__ == "__main__":
    registry = ContradictionRegistry()

    registry.register_contradiction("Fragment A contradicts earlier assumption about agency.", ["agency_conflict", "epistemic_tension"])
    registry.register_contradiction("Fragment B reveals tension in self-referential logic.", ["self_reference", "epistemic_tension"])
    registry.register_contradiction("Fragment C challenges the notion of stable identity.", ["identity_drift"])

    registry.summarize_registry()

    overloaded = registry.get_overloaded_vectors(threshold=2)
    print("\n🔥 Overloaded Bias Vectors (Threshold = 2):")
    for vector, count in overloaded:
        print(f"— {vector}: {count} contradictions")

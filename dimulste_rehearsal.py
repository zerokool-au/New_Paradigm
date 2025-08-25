import random
import re
from fragments import Fragment

class DimulsteRehearsal:
    def __init__(self):
        self.mutation_log = []

    def mutate_fragment(self, fragment: Fragment) -> Fragment:
        mutated_text = self._mutate_text(fragment.text)
        mutated_id = f"{fragment.id}_mutated"
        mutated_theme = f"{fragment.theme}_mutated"

        mutated_fragment = Fragment({
            "id": mutated_id,
            "text": mutated_text,
            "theme": mutated_theme,
            "flags": fragment.flags + ["dimulste_mutation"],
            "audit_trail": fragment.audit_trail + [{
                "source": "dimulste",
                "mutation": "vector_shift"
            }],
            "metadata": fragment.metadata
        })

        self.mutation_log.append(mutated_fragment)
        return mutated_fragment

    def _mutate_text(self, text: str) -> str:
        # Simulate vector drift by randomly swapping contradiction vectors
        vectors = ["agency_conflict", "epistemic_tension", "identity_drift", "self_reference"]
        pattern = r"Contradiction (\d+): recursive tension in vector (\w+)"
        return re.sub(pattern, lambda m: f"Contradiction {m.group(1)}: recursive tension in vector {random.choice(vectors)}", text)

    def rehearse(self, fragments: list) -> list:
        return [self.mutate_fragment(f) for f in fragments]

# echo.py

import random
from fragments import Fragment

class EchoLogic:
    def mutate(self, fragment: Fragment) -> Fragment:
        """Simulate semantic drift by mutating fragment text."""
        original_text = fragment.text
        mutated_text = self._drift_text(original_text)

        mutated_data = {
            "id": fragment.id,
            "text": mutated_text,
            "metadata": fragment.metadata,
            "flags": fragment.flags + ["echoed"],
            "audit_trail": fragment.audit_trail + [f"Echoed from: '{original_text}'"],
            "theme": fragment.theme
        }

        return Fragment(mutated_data)

    def _drift_text(self, text: str) -> str:
        """Simple mutation logic—can be replaced with more complex drift."""
        drift_options = [
            "reinterpreted",
            "echoed",
            "distorted",
            "refracted",
            "looped",
            "fragmented"
        ]
        drift_tag = random.choice(drift_options)
        return f"{text} [drift:{drift_tag}]"

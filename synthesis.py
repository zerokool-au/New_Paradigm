# synthesis.py

from fragments import Fragment

class SynthesisEngine:
    def combine(self, fragments: list) -> Fragment:
        """Merge multiple fragments into a synthesized one."""
        combined_text = " + ".join([f.text for f in fragments])
        combined_audit = [f"Combined from: {f.id}" for f in fragments]

        synthesized_data = {
            "id": max(f.id for f in fragments) + 1000,
            "text": f"{combined_text} [synthesized]",
            "metadata": {},
            "flags": ["synthesized"],
            "audit_trail": combined_audit,
            "theme": "Synthesized"
        }

        return Fragment(synthesized_data)

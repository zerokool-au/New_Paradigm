# reintegration.py

from fragments import Fragment

class ReintegrationEngine:
    def reintegrate(self, fragment: Fragment) -> Fragment:
        """Finalize fragment after echo or synthesis."""
        updated_data = {
            "id": fragment.id,
            "text": f"{fragment.text} [reintegrated]",
            "metadata": fragment.metadata,
            "flags": fragment.flags + ["reintegrated"],
            "audit_trail": fragment.audit_trail + ["Reintegration complete"],
            "theme": fragment.theme
        }
        return Fragment(updated_data)

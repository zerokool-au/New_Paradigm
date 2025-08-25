# rr_core/audit.py

class DriftLogger:
    def evaluate(self, fragment) -> float:
        """
        Returns a drift score based on fragment metadata.
        Placeholder logic: score based on age and revision count.
        """
        age_factor = fragment.age_days / 30  # Normalize to monthly scale
        revision_factor = fragment.revision_count / 10
        return age_factor + revision_factor

    def detect_tension(self, fragment) -> bool:
        """
        Detects semantic tension.
        Placeholder: flags if fragment contains contradiction markers.
        """
        return any(marker in fragment.content for marker in ["[!]", "[conflict]", "[drift]"])


class GovernanceTrigger:
    def __init__(self, threshold=1.5):
        self.threshold = threshold
        self.flags = []

    def flag(self, fragment, reason=""):
        """
        Records flagged fragment and reason.
        """
        self.flags.append({
            "id": fragment.id,
            "reason": reason,
            "content": fragment.content
        })
        print(f"[GovernanceTrigger] Fragment {fragment.id} flagged: {reason}")

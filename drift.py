# drift.py

from fragments import Fragment

class DriftDetector:
    def detect(self, fragment: Fragment) -> float:
        """Estimate semantic drift based on text mutations and flags."""
        text = fragment.text.lower()
        drift_keywords = ["drift", "echo", "mutate", "refract", "distort", "fragment"]

        score = sum(1 for word in drift_keywords if word in text)
        normalized_score = min(score / len(drift_keywords), 1.0)

        # Boost score if 'echoed' flag is present
        if "echoed" in fragment.flags:
            normalized_score += 0.2

        return round(min(normalized_score, 1.0), 2)

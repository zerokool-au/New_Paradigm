from datetime import datetime, timezone
import json
import os

class ContradictionHarness:
    def __init__(self, log_path="logs/contradiction_log.json"):
        self.log_path = log_path
        self.log = []
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def detect_contradiction(self, frag_a, frag_b):
        # Semantic contradiction: opposing themes or drift reversal
        theme_conflict = frag_a['theme'] != frag_b['theme']
        drift_violation = frag_a.get('drift_intensity', 0) > frag_b.get('drift_intensity', 0)
        resurrection_loop = frag_b.get('resurrected', False) and frag_a.get('composted', False)
        return theme_conflict or drift_violation or resurrection_loop

    def rehearse(self, frag_a, frag_b):
        contradiction = self.detect_contradiction(frag_a, frag_b)
        if contradiction:
            result = self.simulate_reinterpretation(frag_a, frag_b)
            self.log_event(frag_a, frag_b, result, contradiction=True)
            return result
        else:
            self.log_event(frag_a, frag_b, {"status": "aligned"}, contradiction=False)
            return "No contradiction detected"

    def simulate_reinterpretation(self, frag_a, frag_b):
        # Placeholder: simulate_pair integration point
        return {
            "status": "reinterpreted",
            "notes": f"Reframed {frag_a['id']} with {frag_b['id']}",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    def log_event(self, frag_a, frag_b, result, contradiction):
        entry = {
            "frag_a": {
                "id": frag_a['id'],
                "theme": frag_a.get('theme'),
                "drift": frag_a.get('drift_intensity'),
                "composted": frag_a.get('composted', False)
            },
            "frag_b": {
                "id": frag_b['id'],
                "theme": frag_b.get('theme'),
                "drift": frag_b.get('drift_intensity'),
                "resurrected": frag_b.get('resurrected', False)
            },
            "contradiction": contradiction,
            "result": result,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        self.log.append(entry)
        with open(self.log_path, "w") as f:
            json.dump(self.log, f, indent=2)

# Example usage
if __name__ == "__main__":
    harness = ContradictionHarness()
    frag1 = {"id": "f001", "theme": "hope", "drift_intensity": 3, "composted": False}
    frag2 = {"id": "f002", "theme": "despair", "drift_intensity": 1, "resurrected": True}
    print(harness.rehearse(frag1, frag2))

# rr_echo_resonance.py

import math
from datetime import datetime

class EchoResonance:
    def __init__(self):
        self.weights = {
            "contradiction_density": 0.4,
            "semantic_latency": 0.3,
            "cluster_depth": 0.2,
            "timestamp_decay": 0.1
        }

    def score(self, fragment_text, origin_vectors, cluster, timestamp):
        density = self._contradiction_density(origin_vectors)
        latency = self._semantic_latency(fragment_text)
        depth = self._cluster_depth(cluster)
        decay = self._timestamp_decay(timestamp)

        score = (
            self.weights["contradiction_density"] * density +
            self.weights["semantic_latency"] * latency +
            self.weights["cluster_depth"] * depth +
            self.weights["timestamp_decay"] * decay
        )

        return round(score, 4)

    def _contradiction_density(self, vectors):
        return min(len(vectors) / 5.0, 1.0)

    def _semantic_latency(self, text):
        return 1.0 if "self" in text or "identity" in text else 0.5

    def _cluster_depth(self, cluster):
        depth_map = {
            "Agency Conflict": 0.9,
            "Epistemic Tension": 0.8,
            "Identity Drift": 0.7,
            "Surface Tension": 0.4
        }
        return depth_map.get(cluster, 0.5)

    def _timestamp_decay(self, timestamp):
        try:
            ts = datetime.fromisoformat(timestamp)
            age = (datetime.utcnow() - ts).total_seconds() / 3600  # hours
            return max(1.0 - (age / 72.0), 0.0)  # decay over 3 days
        except Exception:
            return 0.5

if __name__ == "__main__":
    resonance = EchoResonance()
    score = resonance.score(
        fragment_text="Fragment B reveals tension in self-referential logic.",
        origin_vectors=["self_reference", "epistemic_tension"],
        cluster="Agency Conflict",
        timestamp=datetime.utcnow().isoformat()
    )
    print(f"🔊 Resonance Score: {score}")

# rr_tension_clusters.py

class TensionClusters:
    def __init__(self):
        self.clusters = {
            "Selfhood Drift": ["identity_drift", "self_reference"],
            "Agency Conflict": ["agency_conflict", "epistemic_tension"],
            "Recursive Tension": ["contradiction", "epistemic_tension", "self_reference"]
        }

    def get_cluster_for_vector(self, vector):
        for name, vectors in self.clusters.items():
            if vector in vectors:
                return name
        return "Unclustered"

    def summarize_clusters(self):
        print("\n🧭 Tension Clusters:")
        for name, vectors in self.clusters.items():
            print(f"— {name}: {vectors}")

if __name__ == "__main__":
    tc = TensionClusters()
    tc.summarize_clusters()

    sample_vectors = ["identity_drift", "epistemic_tension", "agency_conflict", "unknown_vector"]
    for v in sample_vectors:
        cluster = tc.get_cluster_for_vector(v)
        print(f"🔍 {v} → Cluster: {cluster}")

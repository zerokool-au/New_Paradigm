# rr_synthesis.py (modified)

from rr_tension_clusters import TensionClusters
from rr_echo_lineage import EchoLineage
from rr_echo_resonance import EchoResonance

class SynthesisEngine:
    def __init__(self, contradiction_registry):
        self.registry = contradiction_registry
        self.clusters = TensionClusters()
        self.lineage = EchoLineage()
        self.resonance = EchoResonance()

    def synthesize_from_overload(self, threshold=2):
        overloaded = self.registry.get_overloaded_vectors(threshold=threshold)
        for vector, count in overloaded:
            fragments = self.registry.get_fragments_by_vector(vector)
            cluster = self.clusters.get_cluster_for_vector(vector)
            print(f"\n🧬 Synthesizing from '{vector}' ({count} contradictions) in cluster '{cluster}':")
            synthesis = self.synthesize(vector, fragments, cluster)
            print(f"🧠 New Fragment: {synthesis}")

            origin_vectors = [vector]
            fid = self.lineage.register_fragment(
                fragment_text=synthesis,
                source="synthesis",
                cluster=cluster,
                origin_vectors=origin_vectors
            )

            # Score resonance
            timestamp = self.lineage.get_lineage(fid)["timestamp"]
            score = self.resonance.score(synthesis, origin_vectors, cluster, timestamp)

            # Echo ingestion
            try:
                from rr_echo_logic import EchoLogic
                echo = EchoLogic()
                echo.ingest_fragment(synthesis, source="synthesis", cluster=cluster)
                self.lineage.mark_echoed(fid, resonance_score=score)
            except ImportError:
                print("⚠️ EchoLogic module not found. Skipping echo rehearsal.")

if __name__ == "__main__":
    from rr_contradiction_registry import ContradictionRegistry

    registry = ContradictionRegistry()
    registry.register_contradiction("Fragment A contradicts earlier assumption about agency.", ["agency_conflict", "epistemic_tension"])
    registry.register_contradiction("Fragment B reveals tension in self-referential logic.", ["self_reference", "epistemic_tension"])
    registry.register_contradiction("Fragment C challenges the notion of stable identity.", ["identity_drift"])

    engine = SynthesisEngine(registry)
    engine.synthesize_from_overload(threshold=2)

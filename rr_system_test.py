# rr_system_test.py

from rr_contradiction_registry import ContradictionRegistry
from rr_tension_clusters import TensionClusters
from rr_echo_lineage import EchoLineage
from rr_echo_resonance import EchoResonance
from rr_dimulste_bridge import DimulsteBridge
from rr_drift_audit import DriftAudit
from rr_release_gate import ReleaseGate

# Step 1: Setup
registry = ContradictionRegistry()
registry.register_contradiction("Fragment A contradicts earlier assumption about agency.", ["agency_conflict", "epistemic_tension"])
registry.register_contradiction("Fragment B reveals tension in self-referential logic.", ["self_reference", "epistemic_tension"])
registry.register_contradiction("Fragment C challenges the notion of stable identity.", ["identity_drift"])

clusters = TensionClusters()
lineage = EchoLineage()
resonance = EchoResonance()

# Step 2: Synthesis
overloaded = registry.get_overloaded_vectors(threshold=2)
for vector, count in overloaded:
    fragments = registry.get_fragments_by_vector(vector)
    cluster = clusters.get_cluster_for_vector(vector)
    print(f"\n🧬 Synthesizing from '{vector}' ({count} contradictions) in cluster '{cluster}':")
    synthesis = f"[{cluster}] Synthesized Insight: " + " | ".join(fragments)
    print(f"🧠 New Fragment: {synthesis}")

    fid = lineage.register_fragment(
        fragment_text=synthesis,
        source="synthesis",
        cluster=cluster,
        origin_vectors=[vector]
    )

    timestamp = lineage.get_lineage(fid)["timestamp"]
    score = resonance.score(synthesis, [vector], cluster, timestamp)
    lineage.mark_echoed(fid, resonance_score=score)

# Step 3: Dimulste Routing
bridge = DimulsteBridge(lineage, threshold=0.65)
bridge.route_high_resonance()

# Step 4: Governance Audit
audit = DriftAudit(lineage)

# Step 5: Release Validation
gate = ReleaseGate(lineage, audit, bridge.get_log())
report = gate.validate_release()

# Step 6: Output Results
print("\n✅ Release Report:")
for r in report["released"]:
    print(f"🟢 Released: {r['fragment_id']} → {r['dimulste_outcome']}")

for b in report["blocked"]:
    print(f"🔴 Blocked: {b['fragment_id']} → {b['reason']}")

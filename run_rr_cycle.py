# run_rr_cycle.py

from policy_frag_queue import PolicyFragment, PolicyFragQueue
from governance_drift_log import DriftVector, GovernanceDriftLogger
from contradiction_router import route_to_dimulste
from lineage_map import FragmentLineage, LineageMap
from feedback_synthesizer import EchoChain, SemanticInversionLog, ResolutionLog, synthesize_feedback

# Step 1: Seed fragments
queue = PolicyFragQueue()
queue.add_fragment(PolicyFragment("F001", "Policy mandates transparency but restricts disclosure.", 0.82, {"topic": "privacy"}))
queue.add_fragment(PolicyFragment("F002", "AI systems must be corrigible, unless under national security constraints.", 0.76, {"topic": "safety"}))
queue.add_fragment(PolicyFragment("F003", "Data retention should be minimized, except for audit compliance.", 0.68, {"topic": "governance"}))

# Step 2: Route for contradiction rehearsal
frags_for_rehearsal = queue.route_for_rehearsal()

# Step 3: Log governance drift
logger = GovernanceDriftLogger()
for frag in frags_for_rehearsal:
    logger.record_drift(DriftVector(frag.fragment_id, "ambiguity", "Conflicting mandates detected"))

# Step 4: Route to Dimulste (simulated)
route_to_dimulste(frags_for_rehearsal, logger)

# Step 5: Trace lineage
lineage_map = LineageMap()
lineage_map.add_lineage(FragmentLineage("F001", None, ["transparency → suppression"], [0.82, 0.74], "Dream synthesis: paradox resolved via layered access"))
lineage_map.render_lineage_trace("F001")

# Step 6: Confirm recursive synthesis
chain = EchoChain("C001")
chain.add_fragment("F001", 0.82)
chain.add_fragment("F001", 0.74)

inversion_log = SemanticInversionLog()
resolution_log = ResolutionLog()

synthesize_feedback(chain, inversion_log, resolution_log)

# Optional: Print resolution log
print("\n✅ Resolution Log:")
for entry in resolution_log.get_all():
    print(entry)

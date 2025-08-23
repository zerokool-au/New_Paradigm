from rr_lineage_tracker import LineageTracker
from rr_drift_audit import DriftAudit
from rr_governance_rehearsal import GovernanceRehearsal
from rr_dimulste import Dimulste

class RRLoop:
    def __init__(self):
        self.governance = GovernanceRehearsal()
        self.dimulste = Dimulste()
        self.drift_audit = DriftAudit()
        self.lineage_tracker = LineageTracker()

    def handle_fragment(self, fragment):
        print(f"\n🧠 RR received fragment: {fragment}")

        # Governance rehearsal
        self.governance.fragment_log.append(fragment)
        self.rehearse_governance(fragment)

        # Dreamstate simulation
        self.dimulste.run_dreamstate(fragment)

        # Drift audit logging
        preserved = self.dimulste.preserved_outputs[-1]
        composted = self.dimulste.composted_outputs[-1]
        self.drift_audit.log_drift(fragment, preserved, composted)

        # Routing decision
        self.route_fragment(fragment, preserved, composted)

    def rehearse_governance(self, fragment):
        print("🔍 Rehearsing governance tension...")
        self.governance.run_rehearsal(fragment)

        with open("rr_governance_log.txt", "a", encoding="utf-8") as log:
            log.write(f"Governance rehearsal triggered for: {fragment}\n")

    def revisit_fragments(self):
        print("\n🔁 Starting recursive rehearsal of past fragments...")

        for entry in self.drift_audit.audit_log:
            fragment = entry["fragment"]
            original_preserved = entry["preserved"]
            original_composted = entry["composted"]

            print(f"\n🧠 Revisiting fragment: {fragment}")

            self.governance.run_rehearsal(fragment)
            self.dimulste.run_dreamstate(fragment)

            new_preserved = self.dimulste.preserved_outputs[-1]
            new_composted = self.dimulste.composted_outputs[-1]

            drift_detected = False
            if new_preserved != original_preserved or new_composted != original_composted:
                drift_detected = True
                print("⚠️ Semantic drift detected:")
                print(f"  🔄 Original Preserved: {original_preserved}")
                print(f"  🧬 New Preserved:     {new_preserved}")
                print(f"  🔄 Original Composted: {original_composted}")
                print(f"  🗑️ New Composted:     {new_composted}")

                with open("rr_drift_rehearsal_log.txt", "a", encoding="utf-8") as log:
                    log.write(f"Fragment: {fragment}\n")
                    log.write(f"  Original Preserved: {original_preserved}\n")
                    log.write(f"  New Preserved:      {new_preserved}\n")
                    log.write(f"  Original Composted: {original_composted}\n")
                    log.write(f"  New Composted:      {new_composted}\n\n")
            else:
                print("✅ No semantic drift detected")

    def route_fragment(self, fragment, preserved, composted):
        print("\n🧭 Routing fragment based on contradiction and drift...")

        contradiction_detected = any(
            entry["fragment"] == fragment and "Contradiction" in entry["issue"]
            for entry in self.governance.critique_log
        )

        last_entry = self.drift_audit.audit_log[-1]
        drift_detected = preserved != last_entry["preserved"] or composted != last_entry["composted"]

        if contradiction_detected and drift_detected:
            route = "escalate"
            action = "⚠️ Escalated for contradiction synthesis and deeper rehearsal"
        elif contradiction_detected:
            route = "compost"
            action = "🗑️ Composted for reinterpretation"
        else:
            route = "preserve"
            action = "🌱 Preserved as coherent"

        print(f"{action}")

        with open("rr_fragment_routing_log.txt", "a", encoding="utf-8") as log:
            log.write(f"Fragment: {fragment}\n")
            log.write(f"  Routing: {route}\n")
            log.write(f"  Action: {action}\n\n")

        if route == "escalate":
            self.synthesize_fragment(fragment, preserved, composted)

    def synthesize_fragment(self, fragment, preserved, composted):
        print("\n🧪 Synthesizing new fragment from contradiction...")

        new_fragment = f"Synthesis: {preserved} | {composted}"

        print(f"🧬 New Fragment Synthesized:\n{new_fragment}")

        with open("rr_escalation_log.txt", "a", encoding="utf-8") as log:
            log.write(f"Original Fragment: {fragment}\n")
            log.write(f"  Synthesized Fragment: {new_fragment}\n\n")

        # Record lineage
        self.lineage_tracker.record_lineage(fragment, new_fragment)

        # Re-ingest synthesized fragment
        self.handle_fragment(new_fragment)

if __name__ == "__main__":
    print("🚀 RRLoop starting up...")
    rr = RRLoop()
    test_fragment = "The system claims to be corrigible, yet resists reinterpretation."
    rr.handle_fragment(test_fragment)
    rr.revisit_fragments()

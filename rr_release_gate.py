# rr_release_gate.py

class ReleaseGate:
    def __init__(self, lineage, audit, dimulste_log):
        self.lineage = lineage
        self.audit = audit
        self.dimulste_log = dimulste_log

    def validate_release(self):
        unresolved = self.audit.audit_unresolved()
        blocked = []

        for entry in unresolved:
            fid = entry["fragment_id"]
            if entry["tension_score"] > 0.6 or entry["echo_bias"]:
                blocked.append({
                    "fragment_id": fid,
                    "reason": "Unresolved tension or echo bias",
                    "details": entry
                })

        released = []
        for fid, data in self.lineage.get_all_echoed().items():
            if fid not in [b["fragment_id"] for b in blocked]:
                outcome = self._get_dimulste_outcome(fid)
                released.append({
                    "fragment_id": fid,
                    "text": data["text"],
                    "cluster": data["cluster"],
                    "resonance_score": data["resonance_score"],
                    "dimulste_outcome": outcome
                })

        return {"blocked": blocked, "released": released}

    def _get_dimulste_outcome(self, fid):
        for entry in self.dimulste_log:
            if entry["fragment_id"] == fid:
                return entry["outcome"]
        return "unknown"

if __name__ == "__main__":
    from rr_echo_lineage import EchoLineage
    from rr_drift_audit import DriftAudit
    from rr_dimulste_bridge import DimulsteBridge

    lineage = EchoLineage()
    fid = lineage.register_fragment(
        fragment_text="Fragment E loops recursively on identity and agency.",
        source="synthesis",
        cluster="Identity Drift",
        origin_vectors=["identity_drift", "agency_conflict"]
    )
    lineage.mark_echoed(fid, resonance_score=0.91)

    audit = DriftAudit(lineage)
    bridge = DimulsteBridge(lineage)
    bridge.route_high_resonance()

    gate = ReleaseGate(lineage, audit, bridge.get_log())
    report = gate.validate_release()

    print("\n✅ Release Report:")
    for r in report["released"]:
        print(f"🟢 Released: {r['fragment_id']} → {r['dimulste_outcome']}")

    for b in report["blocked"]:
        print(f"🔴 Blocked: {b['fragment_id']} → {b['reason']}")

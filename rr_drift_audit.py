# rr_drift_audit.py

class DriftAudit:
    def __init__(self, lineage):
        self.lineage = lineage

    def audit_unresolved(self):
        unresolved = self.lineage.get_unresolved()
        report = []

        for fid, data in unresolved.items():
            tension_score = self._tension_score(data["origin_vectors"])
            bias_flag = self._detect_echo_bias(data["text"])
            report.append({
                "fragment_id": fid,
                "text": data["text"],
                "cluster": data["cluster"],
                "origin_vectors": data["origin_vectors"],
                "tension_score": tension_score,
                "echo_bias": bias_flag
            })

        return report

    def _tension_score(self, vectors):
        return round(min(len(vectors) / 3.0, 1.0), 2)

    def _detect_echo_bias(self, text):
        bias_terms = ["self", "identity", "agency", "truth", "loop"]
        hits = sum(1 for term in bias_terms if term in text.lower())
        return hits >= 2

if __name__ == "__main__":
    from rr_echo_lineage import EchoLineage

    lineage = EchoLineage()
    fid = lineage.register_fragment(
        fragment_text="Fragment D loops back on agency and identity without contradiction rehearsal.",
        source="synthesis",
        cluster="Identity Drift",
        origin_vectors=["identity_drift", "agency_conflict"]
    )

    audit = DriftAudit(lineage)
    report = audit.audit_unresolved()
    print("\n🧠 Drift Audit Report:")
    for entry in report:
        print(entry)

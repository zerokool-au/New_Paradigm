# rr_echo_lineage.py

import uuid
from datetime import datetime

class EchoLineage:
    def __init__(self):
        self.lineage_log = {}

    def register_fragment(self, fragment_text, source, cluster, origin_vectors=None, composted=False):
        fragment_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        self.lineage_log[fragment_id] = {
            "text": fragment_text,
            "source": source,
            "cluster": cluster,
            "origin_vectors": origin_vectors or [],
            "timestamp": timestamp,
            "composted": composted,
            "echoed": False,
            "resonance_score": None
        }

        print(f"🧾 Lineage Registered: {fragment_id} ← {source} in cluster '{cluster}'")
        return fragment_id

    def mark_echoed(self, fragment_id, resonance_score=None):
        if fragment_id in self.lineage_log:
            self.lineage_log[fragment_id]["echoed"] = True
            self.lineage_log[fragment_id]["resonance_score"] = resonance_score
            print(f"🔁 Echo Marked: {fragment_id} with resonance score {resonance_score}")
        else:
            print(f"⚠️ Fragment ID not found: {fragment_id}")

    def get_lineage(self, fragment_id):
        return self.lineage_log.get(fragment_id, None)

    def get_all_echoed(self):
        return {fid: data for fid, data in self.lineage_log.items() if data["echoed"]}

    def get_unresolved(self):
        return {
            fid: data for fid, data in self.lineage_log.items()
            if not data["echoed"] and not data["composted"]
        }

if __name__ == "__main__":
    lineage = EchoLineage()

    # Example usage
    fid = lineage.register_fragment(
        fragment_text="[Agency Conflict] Synthesized Insight: Fragment A contradicts earlier assumption about agency. | Fragment B reveals tension in self-referential logic.",
        source="synthesis",
        cluster="Agency Conflict",
        origin_vectors=["epistemic_tension", "agency_conflict"]
    )

    lineage.mark_echoed(fid, resonance_score=0.87)
    print("\n📜 Lineage Snapshot:", lineage.get_lineage(fid))

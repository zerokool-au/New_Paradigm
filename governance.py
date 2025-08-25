# governance.py

from fragments import Fragment

class GovernanceTrigger:
    def __init__(self, threshold: float = 0.7):
        self.threshold = threshold

    def check(self, drift_score: float) -> bool:
        return drift_score >= self.threshold

class DriftAuditHook:
    def log(self, original: Fragment, mutated: Fragment, drift_score: float, governance_flag: bool):
        print(f"[Audit] Fragment ID: {original.id} | Drift: {drift_score:.2f} | Governance Triggered: {governance_flag}")

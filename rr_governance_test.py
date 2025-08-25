# rr_governance_test.py

from fragments import Fragment
from echo import EchoLogic
from drift import DriftDetector
from pulse import PulseDetector, PulseRouter
from governance import GovernanceTrigger, DriftAuditHook
from synthesis import SynthesisEngine
from reintegration import ReintegrationEngine

def run_governance_test():
    # Contradiction storm: conflicting semantic vectors
    raw_fragments = [
        {"id": 101, "text": "Truth is stable."},
        {"id": 102, "text": "Truth is always shifting."},
        {"id": 103, "text": "Memory preserves."},
        {"id": 104, "text": "Memory distorts."},
        {"id": 105, "text": "Silence is clarity."},
        {"id": 106, "text": "Silence is confusion."},
    ]

    echo = EchoLogic()
    drift = DriftDetector()
    pulse = PulseDetector()
    router = PulseRouter()
    governance = GovernanceTrigger(threshold=0.6)
    audit = DriftAuditHook()
    synthesis = SynthesisEngine()
    reintegration = ReintegrationEngine()

    for raw in raw_fragments:
        fragment = Fragment(raw)
        echoed = echo.mutate(fragment)
        drift_score = drift.detect(echoed)
        pulse_tag = pulse.tag(echoed)
        routed = router.route(echoed, pulse_tag)
        governance_flag = governance.check(drift_score)
        audit.log(fragment, echoed, drift_score, governance_flag)

        if governance_flag:
            print(f"[Governance Triggered] Drift Score: {drift_score:.2f}")
            synthesized = synthesis.combine([fragment, echoed])
            reintegrated = reintegration.reintegrate(synthesized)
            print(f"→ Synthesized Reintegration:\n{reintegrated.text}\n")
        else:
            print(f"[No Governance Trigger] Drift Score: {drift_score:.2f}")
            reintegrated = reintegration.reintegrate(echoed)
            print(f"→ Standard Reintegration:\n{reintegrated.text}\n")

if __name__ == "__main__":
    run_governance_test()

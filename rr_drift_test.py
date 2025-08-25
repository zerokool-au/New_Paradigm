# rr_drift_test.py

from fragments import Fragment
from echo import EchoLogic
from drift import DriftDetector
from reintegration import ReintegrationEngine
from pulse import PulseDetector, PulseRouter
from governance import GovernanceTrigger, DriftAuditHook
from synthesis import SynthesisEngine

def run_drift_test():
    # Seed fragments as dicts
    raw_fragments = [
        {"id": 1, "text": "The wallaby watches the wind."},
        {"id": 2, "text": "Contradiction is compost."},
        {"id": 3, "text": "Echoes mutate when ignored."},
    ]

    # Initialize modules
    echo = EchoLogic()
    drift = DriftDetector()
    reintegration = ReintegrationEngine()
    pulse = PulseDetector()
    router = PulseRouter()
    governance = GovernanceTrigger(threshold=0.7)
    audit = DriftAuditHook()
    synthesis = SynthesisEngine()

    # Rehearsal loop
    for raw in raw_fragments:
        fragment = Fragment(raw)
        echoed = echo.mutate(fragment)
        drift_score = drift.detect(echoed)
        pulse_tag = pulse.tag(echoed)
        routed = router.route(echoed, pulse_tag)
        governance_flag = governance.check(drift_score)
        audit.log(fragment, echoed, drift_score, governance_flag)

        if governance_flag:
            synthesized = synthesis.combine([fragment, echoed])
            reintegrated = reintegration.reintegrate(synthesized)
            print(f"[Governance Triggered] Reintegration Output:\n{reintegrated.text}\n")
        else:
            reintegrated = reintegration.reintegrate(echoed)
            print(f"[Standard Reintegration] Output:\n{reintegrated.text}\n")

if __name__ == "__main__":
    run_drift_test()

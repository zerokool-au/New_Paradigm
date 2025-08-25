class DriftLogger:
    def __init__(self):
        self.entries = []

    def log(self, fragment_id, tension_type):
        self.entries.append((fragment_id, tension_type))

class DriftAuditHook:
    def __init__(self, logger, trigger):
        self.logger = logger
        self.trigger = trigger

    def audit(self, fragment):
        if self.trigger.check(fragment):
            self.logger.log(fragment.id, "governance_tension")

def integrate_drift_audit(engine, hook):
    original_synthesize = engine.synthesize_from_overload

    def wrapped(threshold=5):
        results = original_synthesize(threshold)
        for i, text in enumerate(results):
            fragment = Fragment({
                "id": f"synth_{i+1}",
                "text": text,
                "flags": [],
                "metadata": {}
            })
            hook.audit(fragment)
        return results

    engine.synthesize_from_overload = wrapped

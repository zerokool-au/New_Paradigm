# governance_drift_log.py
class DriftVector:
    def __init__(self, fragment_id, tension_type, notes):
        self.fragment_id = fragment_id
        self.tension_type = tension_type  # suppression, ambiguity, recursion
        self.notes = notes

class GovernanceDriftLogger:
    def __init__(self):
        self.log = []

    def record_drift(self, drift: DriftVector):
        self.log.append(drift)

    def get_by_tension(self, tension_type):
        return [d for d in self.log if d.tension_type == tension_type]

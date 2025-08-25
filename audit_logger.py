import datetime

class AuditLogger:
    def __init__(self):
        self.logs = []

    def log(self, fragment_id, action, metadata=None):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "fragment_id": fragment_id,
            "action": action,
            "metadata": metadata or {}
        }
        self.logs.append(entry)

    def get_logs(self):
        return self.logs

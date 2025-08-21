import json

def log_alert(alert, filename="alerts_log.jsonl"):
    with open(filename, "a") as f:
        f.write(json.dumps(alert) + "\n")

# notifier.py

import json
import time

def issue_notifier(alert):
    """
    Append the alert dict as JSON Lines to alert_log.jsonl
    and print to console for immediate confirmation.
    """
    alert_record = {
        "timestamp": time.time(),
        **alert
    }

    # immediate console feedback
    print("NOTIFIER → firing alert:", alert_record)

    with open("alert_log.jsonl", "a") as out:
        out.write(json.dumps(alert_record) + "\n")

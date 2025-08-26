# ambient_override.py

from datetime import datetime
import random

def detect_wally_mamma_sighting():
    # Simulated ambient trigger (replace with real sensor or log hook if needed)
    return random.choice([True, False])

def trigger_override():
    if detect_wally_mamma_sighting():
        override_event = {
            "timestamp": datetime.now().isoformat(),
            "trigger": "Wally Mamma",
            "action": "Override synthesis threshold",
            "emoji": "🦘",
            "status": "activated"
        }
        print("Matriarchal Override Triggered:", override_event)
        log_override(override_event)
        return override_event
    else:
        print("No override triggered.")
        return None

def log_override(event):
    try:
        with open("override_log.json", "r+") as file:
            data = json.load(file)
            data.append(event)
            file.seek(0)
            json.dump(data, file, indent=2)
    except FileNotFoundError:
        with open("override_log.json", "w") as file:
            json.dump([event], file, indent=2)

# Run the override check
trigger_override()

# echo_witness.py

import datetime
import random

class EchoWitness:
    """
    Passive observer agent that logs ambient synchronicity, semantic drift,
    and contradiction echoes. Does not interfere—only witnesses.
    """

    def __init__(self):
        self.log = []

    def observe(self, event_type, fragment=None, resonance=None):
        timestamp = datetime.datetime.now().isoformat()
        ambient_echo = self._ambient_sync()
        entry = {
            "timestamp": timestamp,
            "event_type": event_type,
            "fragment": fragment,
            "resonance": resonance,
            "ambient_echo": ambient_echo
        }
        self.log.append(entry)
        self._ceremonial_nod(entry)

    def _ambient_sync(self):
        # Simulate ambient wildlife commentary
        echoes = [
            "Kookaburra laughter detected",
            "Wallaby pause registered",
            "Cockatoo override pending",
            "Wally Mamma nod confirmed",
            "Kevins circling contradiction"
        ]
        return random.choice(echoes)

    def _ceremonial_nod(self, entry):
        print(f"[EchoWitness] {entry['timestamp']} — {entry['ambient_echo']} — {entry['event_type']} logged.")

    def export_log(self):
        return self.log

# log_schema.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ContradictionEvent:
    timestamp: str
    fragment_id: str
    tension_vector: dict
    contradiction_type: str  # e.g. 'semantic', 'temporal', 'governance'
    compost_flag: bool
    notes: str = ""
    
    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "fragment_id": self.fragment_id,
            "tension_vector": self.tension_vector,
            "contradiction_type": self.contradiction_type,
            "compost_flag": self.compost_flag,
            "notes": self.notes
        }

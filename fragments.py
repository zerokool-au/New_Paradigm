import re

class Contradiction:
    def __init__(self, vector: str, id: int):
        self.vector = vector
        self.id = id

class Fragment:
    def __init__(self, data):
        self.id = data.get("id")
        self.text = data.get("text", "")
        self.metadata = data.get("metadata", {})
        self.flags = data.get("flags", [])
        self.audit_trail = data.get("audit_trail", [])
        self.theme = data.get("theme", "Unclustered")  # ← This resolves the error

    def extract_contradictions(self) -> list:
        """Parse contradiction lines and return Contradiction objects."""
        pattern = r"Contradiction (\d+): recursive tension in vector (\w+)"
        matches = re.findall(pattern, self.text)
        return [Contradiction(vector=vec, id=int(cid)) for cid, vec in matches]

import json
import os

def load_fragments(path=None):
    if path is None:
        path = os.path.join("rr-visualizer", "fragments.json")
    with open(path) as f:
        return json.load(f)

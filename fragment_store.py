# fragment_store.py

import json

def load_fragments(path):
    with open(path, "r") as f:
        return json.load(f)

def save_fragments(path, fragments):
    with open(path, "w") as f:
        json.dump(fragments, f, indent=2)

def add_fragment(path, fragment):
    fragments = load_fragments(path)
    fragments.append(fragment)
    save_fragments(path, fragments)

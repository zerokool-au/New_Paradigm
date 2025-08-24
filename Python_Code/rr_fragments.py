import json

FRAGMENTS_PATH = "fragments.json"

def load_fragments(path=FRAGMENTS_PATH):
    with open(path) as f:
        return json.load(f)

def retire_fragment(fragments, frag_id):
    for frag in fragments:
        if frag["id"] == frag_id:
            frag["status"] = "retired"
            frag["retired_reason"] = "semantic exhaustion"
            return

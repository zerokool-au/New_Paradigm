# reintegration_logic.py

import json
from fragment_store import load_fragments
from synthesis_queue import enqueue_fragment

def reintegrate_fragments(store_path, threshold=0.7):
    fragments = load_fragments(store_path)
    for frag in fragments:
        if frag.get("drift_score", 1.0) < threshold and frag.get("status") == "composted":
            frag["status"] = "reintegrated"
            enqueue_fragment(frag)
            print(f"Reintegrated: {frag['id']}")

if __name__ == "__main__":
    reintegrate_fragments("fragment_store.json")

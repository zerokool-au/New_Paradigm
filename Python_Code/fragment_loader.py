# fragment_loader.py

import os
import json
from contradiction_harness import ContradictionHarness

DRIFT_PROFILE_PATH = "drift_profile.json"

class FragmentLoader:
    def __init__(self, source_dir="dimulste_outputs", max_pairs=5):
        self.source_dir = source_dir
        self.max_pairs = max_pairs
        self.harness = ContradictionHarness()

    def load_fragments(self):
        fragments = []
        for filename in sorted(os.listdir(self.source_dir), reverse=True):
            if filename.endswith(".json"):
                with open(os.path.join(self.source_dir, filename), "r") as f:
                    data = json.load(f)
                    fragments.extend(data)
            if len(fragments) >= self.max_pairs * 2:
                break
        return fragments[:self.max_pairs * 2]

    def log_drift_profile(self, frag_a, frag_b, result):
        profile_entry = {
            "pair": [frag_a["id"], frag_b["id"]],
            "drift_type": "semantic",  # Placeholder—can evolve later
            "intensity": 0.7,          # Placeholder—can be dynamic
            "bias_vector": [frag_a["theme"], frag_b["theme"]],
            "notes": result["notes"]
        }

        if os.path.exists(DRIFT_PROFILE_PATH):
            with open(DRIFT_PROFILE_PATH, "r") as f:
                profile = json.load(f)
        else:
            profile = []

        profile.append(profile_entry)

        with open(DRIFT_PROFILE_PATH, "w") as f:
            json.dump(profile, f, indent=2)

    def pair_and_rehearse(self):
        fragments = self.load_fragments()
        for i in range(0, len(fragments) - 1, 2):
            frag_a = fragments[i]
            frag_b = fragments[i + 1]
            result = self.harness.rehearse(frag_a, frag_b)
            print(f"Pair {frag_a['id']} vs {frag_b['id']}: {result}")
            self.log_drift_profile(frag_a, frag_b, result)

# Example usage
if __name__ == "__main__":
    loader = FragmentLoader()
    loader.pair_and_rehearse()

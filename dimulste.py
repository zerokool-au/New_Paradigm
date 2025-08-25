import json
import random

random.seed(0)

THRESHOLD = 0.9

def reinterpret(fragment):
    """
    Apply a simple drift heuristic and decide
    whether to compost or preserve the fragment.
    """
    drift_score = random.uniform(0, 1)
    if drift_score > THRESHOLD:
        return {
            "id": fragment["id"],
            "status": "composted",
            "reinterpretation": (
                f"Echoes bloom in the void where silence once slept. "
                f"[drift={drift_score:.2f}]"
            )
        }
    else:
        return {
            "id": fragment["id"],
            "status": "preserved",
            "reinterpretation": (
                fragment["content"] +
                f" [drift={drift_score:.2f}]"
            )
        }

if __name__ == "__main__":
    # Step 1: Load fragments
    with open("fragments.json", "r") as f:
        fragments = json.load(f)

    # Step 2: Reinterpret each fragment
    results = [reinterpret(frag) for frag in fragments]

    # Step 3: Write out the results
    with open("dimulste_output.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Dimulste loop complete. Check dimulste_output.json for results.")

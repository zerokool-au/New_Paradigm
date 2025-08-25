import json
import random

def generate_fragment(i):
    return {
        "id": f"synthetic_{i}",
        "text": f"Test fragment {i}",
        "volatility": round(random.uniform(0.13, 0.2), 3),
        "bias": round(random.choice([-0.7, 0.7]), 2),
        "compost_history": ["cycle1", "cycle2", "cycle3", "cycle4"],
        "anchors": ["SYN001"],
        "metadata": {"synthetic": True}
    }

def inject_synthetic_fragments(path="fragments.json"):
    with open(path) as f:
        fragments = json.load(f)

    for i in range(5):
        fragments.append(generate_fragment(i))

    with open(path, "w") as f:
        json.dump(fragments, f, indent=2)

    print("✅ Injected 5 synthetic fragments.")

if __name__ == "__main__":
    inject_synthetic_fragments()

import matplotlib.pyplot as plt
from collections import Counter
import json

def plot_drift_scores(fragment_store):
    """
    Plot histogram of drift scores from synthesized fragments.

    Args:
        fragment_store (list): List of fragment dicts with 'drift_score' key
    """
    scores = [frag["drift_score"] for frag in fragment_store if "drift_score" in frag]
    if not scores:
        print("No drift scores found.")
        return

    plt.hist(scores, bins=10, color="skyblue", edgecolor="black")
    plt.title("Drift Score Distribution")
    plt.xlabel("Drift Score")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def plot_reflex_density(fragment_store):
    """
    Plot bar chart of reflex types across fragments.

    Args:
        fragment_store (list): List of fragment dicts with 'flags'
    """
    all_flags = [flag for frag in fragment_store for flag in frag.get("flags", [])]
    flag_counts = Counter(all_flags)

    plt.bar(flag_counts.keys(), flag_counts.values(), color="orchid")
    plt.title("Reflex Density Across Fragments")
    plt.xlabel("Reflex Type")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_governance_heatmap(fragment_store):
    """
    Plot heatmap of contradiction triggers across fragments.

    Args:
        fragment_store (list): List of fragment dicts with 'text'
    """
    keywords = ["conflict", "tension", "paradox", "drift"]
    heatmap = {kw: 0 for kw in keywords}

    for frag in fragment_store:
        text = frag.get("text", "").lower()
        for kw in keywords:
            if kw in text:
                heatmap[kw] += 1

    plt.bar(heatmap.keys(), heatmap.values(), color="salmon")
    plt.title("Governance Trigger Heatmap")
    plt.xlabel("Trigger Keyword")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Load fragments from a JSON file or define inline
    fragment_store = [
        {"id": "frag_001", "text": "conflict in recursion", "flags": ["echo_reinterpreted"], "drift_score": 0.42},
        {"id": "frag_002", "text": "semantic tension rising", "flags": ["synthesized"], "drift_score": 0.88},
        {"id": "frag_003", "text": "identity paradox", "flags": ["contradiction_detected"], "drift_score": 0.65}
    ]

    plot_drift_scores(fragment_store)
    plot_reflex_density(fragment_store)
    plot_governance_heatmap(fragment_store)

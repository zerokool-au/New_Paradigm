import json
import matplotlib.pyplot as plt
from rr_metrics import compost_count, calculate_volatility, calculate_bias

def load_fragments(path="fragments.json"):
    with open(path) as f:
        return json.load(f)

def analyze_fragments(fragments):
    fatigue = [compost_count(f) for f in fragments]
    volatility = [calculate_volatility(f) for f in fragments]
    bias = [calculate_bias(f) for f in fragments]
    ids = [f["id"] for f in fragments]

    return ids, fatigue, volatility, bias

def plot_analytics(ids, fatigue, volatility, bias):
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 3, 1)
    plt.bar(ids, fatigue, color="brown")
    plt.title("Compost Fatigue")
    plt.xticks(rotation=90)

    plt.subplot(1, 3, 2)
    plt.bar(ids, volatility, color="purple")
    plt.title("Volatility Index")
    plt.xticks(rotation=90)

    plt.subplot(1, 3, 3)
    plt.bar(ids, bias, color="orange")
    plt.title("Bias Score")
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    fragments = load_fragments()
    ids, fatigue, volatility, bias = analyze_fragments(fragments)
    plot_analytics(ids, fatigue, volatility, bias)

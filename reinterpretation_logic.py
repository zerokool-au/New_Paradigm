import json
from rr_fragments import load_fragments
from rr_metrics import calculate_volatility, calculate_bias, compost_count

REINTERPRETATION_POOL = []

def should_reinterpret(fragment):
    volatility = calculate_volatility(fragment)
    bias = calculate_bias(fragment)
    composts = compost_count(fragment)

    return (
        volatility > 0.08 or
        abs(bias) > 0.6 or
        composts >= 3
    )

def route_fragments_for_reinterpretation(fragments):
    for frag in fragments:
        if should_reinterpret(frag):
            REINTERPRETATION_POOL.append(frag)
            print(f"Fragment {frag['id']} routed for reinterpretation.")

def save_pool(path="reinterpretation_pool.json"):
    with open(path, "w") as f:
        json.dump(REINTERPRETATION_POOL, f, indent=2)
    print(f"Saved {len(REINTERPRETATION_POOL)} fragments to pool.")

if __name__ == "__main__":
    fragments = load_fragments()
    route_fragments_for_reinterpretation(fragments)
    save_pool()

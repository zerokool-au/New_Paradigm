from collections import defaultdict

# Sample input: replace with actual synthesis log data
synthesis_log = [
    {"fragment": "A335", "drift": -0.04},
    {"fragment": "A335", "drift": 0.04},
    {"fragment": "A335", "drift": 0.02},
    {"fragment": "B335", "drift": -0.02},
    {"fragment": "B335", "drift": -0.04},
    {"fragment": "B335", "drift": 0.01},
    {"fragment": "B335", "drift": -0.04},
    {"fragment": "C335", "drift": -0.01},
    {"fragment": "C335", "drift": 0.01},
    {"fragment": "C335", "drift": -0.01},
    {"fragment": "D999", "drift": -0.02},
    {"fragment": "D999", "drift": 0.04},
    {"fragment": "D999", "drift": -0.02},
    {"fragment": "D999", "drift": 0.01},
    {"fragment": "E999", "drift": 0.01},
    {"fragment": "E999", "drift": -0.04},
    {"fragment": "E999", "drift": -0.01},
    {"fragment": "E999", "drift": -0.04},
]

# Sample compost counts: replace with actual compost log data
compost_counts = {
    "A335": 3,
    "B335": 4,
    "C335": 3,
    "D999": 4,
    "E999": 4,
}

def compute_drift_audit(synthesis_log, compost_counts):
    audit = defaultdict(lambda: {
        "cycles": 0,
        "drift_values": [],
        "volatility": 0.0,
        "bias": "",
        "compost_count": 0,
        "saturation_flag": False,
        "compost_fatigue": False
    })

    for entry in synthesis_log:
        frag = entry["fragment"]
        drift = entry["drift"]
        audit[frag]["cycles"] += 1
        audit[frag]["drift_values"].append(drift)

    for frag, data in audit.items():
        drift_vals = data["drift_values"]
        volatility = max(drift_vals) - min(drift_vals)
        avg_drift = sum(drift_vals) / len(drift_vals)
        bias = "positive" if avg_drift > 0.01 else "negative" if avg_drift < -0.01 else "oscillating"
        saturation = data["cycles"] > 3 and volatility < 0.02
        fatigue = compost_counts.get(frag, 0) > 3 and len(drift_vals) > 0 and all(abs(d) < 0.02 for d in drift_vals)

        data.update({
            "volatility": round(volatility, 4),
            "bias": bias,
            "compost_count": compost_counts.get(frag, 0),
            "saturation_flag": saturation,
            "compost_fatigue": fatigue
        })

    return dict(audit)

# Run audit
drift_audit = compute_drift_audit(synthesis_log, compost_counts)

# Display results
for frag, stats in drift_audit.items():
    print(f"\n🔍 Fragment {frag}")
    for k, v in stats.items():
        print(f"  {k}: {v}")

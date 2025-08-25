import json
import argparse

def load_queue(path):
    with open(path, 'r') as f:
        return json.load(f)

def flag_recursive(fragment):
    return fragment.get("id", "").startswith("echo_") or "recursive" in fragment.get("tags", [])

def flag_bias(fragment, threshold=0.5):
    bias = fragment.get("bias_score", 0)
    return abs(bias) >= threshold

def flag_drift(fragment, threshold=0.3):
    drift = fragment.get("drift_score", 0)
    return abs(drift) >= threshold

def flag_contradiction(fragment):
    return fragment.get("contradiction_score", 0) > 0 or "contradiction" in fragment.get("tags", [])

def audit(queue_path, flags):
    queue = load_queue(queue_path)
    flagged = []

    for frag in queue:
        if (
            (flags["recursive"] and flag_recursive(frag)) or
            (flags["bias"] and flag_bias(frag)) or
            (flags["drift"] and flag_drift(frag)) or
            (flags["contradiction"] and flag_contradiction(frag))
        ):
            flagged.append(frag)

    with open("synthesis_audit_log.json", "w") as f:
        json.dump(flagged, f, indent=2)

    print(f"Audit complete. {len(flagged)} fragments flagged.")
    print("Output written to synthesis_audit_log.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to synthesis_queue.json")
    parser.add_argument("--flag-recursive", action="store_true")
    parser.add_argument("--log-bias", action="store_true")
    parser.add_argument("--log-drift", action="store_true")
    parser.add_argument("--log-contradiction", action="store_true")
    args = parser.parse_args()

    flags = {
        "recursive": args.flag_recursive,
        "bias": args.log_bias,
        "drift": args.log_drift,
        "contradiction": args.log_contradiction
    }

    audit(args.input, flags)

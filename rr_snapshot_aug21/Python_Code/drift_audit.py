import json
from collections import defaultdict

def drift_audit(log_file="alert_log.jsonl", threshold=0.5):
    drift_counts = defaultdict(lambda: {"stable": 0, "convergent": 0, "divergent": 0, "unknown": 0})
    score_totals = defaultdict(list)
    contradictions = []
    compost_candidates = []

    line_count = 0

    with open(log_file, "r") as f:
        for line in f:
            try:
                alert = json.loads(line)
                line_count += 1

                if line_count <= 5:
                    print(f"🔍 Sample alert #{line_count}: {alert}")

                agentA = alert.get("agentA", "UnknownA")
                agentB = alert.get("agentB", "UnknownB")
                pair = f"{agentA}–{agentB}"

                # Infer drift direction from history_sample
                history = alert.get("history_sample", [])
                if len(history) >= 2:
                    delta = history[-1] - history[-2]
                    if abs(delta) < 0.05:
                        direction = "stable"
                    elif delta > 0.05:
                        direction = "convergent"
                    else:
                        direction = "divergent"
                else:
                    direction = "unknown"

                score = alert.get("score", 0.0)
                fragment = alert.get("fragment", "No fragment")

                drift_counts[pair][direction] += 1
                score_totals[pair].append(score)

                if score < threshold:
                    contradictions.append((pair, score, fragment))
                    if direction == "divergent":
                        compost_candidates.append((pair, score, fragment, direction))

            except Exception as e:
                print(f"⚠️ Error parsing line: {e}")

    print(f"\n✅ Parsed {line_count} lines from {log_file}")

    print("\n📊 Drift Summary:")
    for pair, counts in drift_counts.items():
        scores = score_totals.get(pair, [])
        avg_score = sum(scores) / len(scores) if scores else 0.0
        print(f"Pair: {pair}")
        print(f"  Avg Score: {avg_score:.3f}")
        print(f"  Drift → Stable: {counts['stable']}, Convergent: {counts['convergent']}, Divergent: {counts['divergent']}, Unknown: {counts['unknown']}\n")

    print("⚠️ Contradictions Detected:")
    for pair, score, fragment in contradictions:
        print(f"  {pair} → Score: {score:.3f} → Fragment: {fragment}")

    print("\n🧹 Compost Candidates:")
    for pair, score, fragment, direction in compost_candidates:
        print(f"  {pair} → Score: {score:.3f} → Drift: {direction} → Compost: ✅")

    # ✅ Write compost candidates to file
    with open("compost_log.jsonl", "w") as out:
        for pair, score, fragment, direction in compost_candidates:
            entry = {
                "pair": pair,
                "score": score,
                "drift": direction,
                "fragment": fragment,
                "tag": "compost"
            }
            out.write(json.dumps(entry) + "\n")

# Run the audit when script is executed directly
if __name__ == "__main__":
    drift_audit()

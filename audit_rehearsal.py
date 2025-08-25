from collections import Counter
import json

# Load rehearsal log
with open("rehearsal_log.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Parse and count outcomes
outcome_counter = Counter()
drift_types = Counter()

for line in lines:
    line = line.strip()
    if not line:
        continue  # Skip empty lines
    entry = json.loads(line)
    outcome = entry.get("outcome", "Unknown")
    drift = entry.get("drift_type", "Unclassified")
    outcome_counter[outcome] += 1
    drift_types[drift] += 1

# Display summary
print("📊 Rehearsal Outcome Summary:")
for k, v in outcome_counter.items():
    print(f"  {k}: {v}")

print("\n🔍 Drift Type Distribution:")
for k, v in drift_types.items():
    print(f"  {k}: {v}")

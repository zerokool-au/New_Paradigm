import json

# Load rehearsal log
with open("rehearsal_log.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Filter reinterpreted fragments
reinterpreted = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    entry = json.loads(line)
    if entry.get("outcome") == "reinterpreted":
        reinterpreted.append(entry["original"])

# Save to second-pass input file
with open("second_pass_input.jsonl", "w", encoding="utf-8") as f:
    for fragment in reinterpreted:
        json.dump({"fragment": fragment}, f)
        f.write("\n")

print(f"✅ Extracted {len(reinterpreted)} fragments for second-pass rehearsal.")

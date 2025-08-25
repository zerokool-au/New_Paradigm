import json

INPUT_FILE = "reinterpretation_log.jsonl"
OUTPUT_FILE = "reinterpretation_log_cleaned.jsonl"

required_fields = ["status", "source_stage", "pair"]

def is_valid(entry):
    return all(field in entry for field in required_fields)

with open(INPUT_FILE, "r", encoding="utf-8") as infile, open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    for line_num, line in enumerate(infile, 1):
        try:
            entry = json.loads(line.strip())
            if is_valid(entry):
                outfile.write(json.dumps(entry) + "\n")
            else:
                print(f"Line {line_num}: Missing required fields. Skipped.")
        except json.JSONDecodeError:
            print(f"Line {line_num}: Malformed JSON. Skipped.")

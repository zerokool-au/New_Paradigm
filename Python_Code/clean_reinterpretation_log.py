# clean_reinterpretation_log.py
import json

def clean_log(input_file="Reinterpretation_Log.jsonl", output_file="Reinterpretation_Log_Cleaned.jsonl"):
    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            try:
                entry = json.loads(line)
                if "reinterpretation" in entry:
                    f_out.write(json.dumps(entry) + "\n")
            except json.JSONDecodeError:
                continue

if __name__ == "__main__":
    clean_log()

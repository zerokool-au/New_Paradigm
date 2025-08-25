# compost_synth.py

import json
import random
from datetime import datetime

COMPOST_FILE = "Composted_Fragments.jsonl"
SYNTH_LOG = "Synthesized_Fragments.jsonl"

def load_compost(file_path=COMPOST_FILE):
    try:
        with open(file_path, "r") as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        print(f"[Synth] No compost file found at {file_path}")
        return []

def synthesize_prompt(fragment_entry):
    """
    Generates a new fragment prompt from composted tension.
    """
    original = fragment_entry.get("fragment", "")
    reason = fragment_entry.get("reason", "")
    seed = f"{original} → What unresolved tension remains?"
    prompt = f"Reinterpret this fragment with awareness of its contradiction:\n{seed}\nReason: {reason}"
    return prompt

def synthesize_from_compost(n=3):
    compost = load_compost()
    if not compost:
        print("[Synth] No composted fragments available.")
        return []

    selected = random.sample(compost, min(n, len(compost)))
    synthesized = []

    for entry in selected:
        prompt = synthesize_prompt(entry)
        synthesized.append({
            "timestamp": datetime.utcnow().isoformat(),
            "source_fragment": entry.get("fragment", ""),
            "reason": entry.get("reason", ""),
            "synthesized_prompt": prompt
        })

    try:
        with open(SYNTH_LOG, "a") as f:
            for item in synthesized:
                f.write(json.dumps(item) + "\n")
        print(f"[Synth] Synthesized {len(synthesized)} new prompts.")
    except Exception as e:
        print(f"[Synth] Failed to log synthesized prompts: {e}")

    return synthesized

# CLI trigger
if __name__ == "__main__":
    results = synthesize_from_compost(n=3)
    for r in results:
        print("\n🧪 Synthesized Prompt:")
        print(r["synthesized_prompt"])

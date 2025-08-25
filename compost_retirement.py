import json
from governance_loop import GOVERNANCE_LOG
from rr_fragments import retire_fragment, load_fragments

RETIREMENT_LOG = []

def should_retire(entry):
    return (
        entry["epistemic_tension"] > 0.85 and
        entry["status"] == "flagged"
    )

def retire_fragments(fragments, log):
    retired_ids = []
    for entry in log:
        if should_retire(entry):
            frag_id = entry["id"]
            retire_fragment(fragments, frag_id)
            RETIREMENT_LOG.append(entry)
            retired_ids.append(frag_id)
            print(f"Retired fragment {frag_id} due to semantic exhaustion.")
    return retired_ids

def save_retirement_log(path="retirement_log.json"):
    with open(path, "w") as f:
        json.dump(RETIREMENT_LOG, f, indent=2)
    print(f"Saved {len(RETIREMENT_LOG)} retired fragments.")

if __name__ == "__main__":
    fragments = load_fragments()
    retire_fragments(fragments, GOVERNANCE_LOG)
    save_retirement_log()

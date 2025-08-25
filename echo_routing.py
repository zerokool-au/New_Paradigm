import json

SYNTHESIS_QUEUE = []
RETIREMENT_QUEUE = []
HOLD_QUEUE = []

def load_logs(echo_path="echo_log.json", gov_path="governance_log.json"):
    with open(echo_path) as e, open(gov_path) as g:
        echo_log = json.load(e)
        gov_log = json.load(g)
    return echo_log, gov_log

def route_fragments(echo_log, gov_log):
    gov_map = {entry["id"]: entry for entry in gov_log}

    for echo_entry in echo_log:
        fid = echo_entry["id"]
        echo_score = echo_entry["echo_score"]
        tension = gov_map.get(fid, {}).get("epistemic_tension", 0)

        if echo_score < 0.4 and tension > 0.7:
            SYNTHESIS_QUEUE.append(fid)
        elif echo_score > 0.6 and tension > 0.7:
            RETIREMENT_QUEUE.append(fid)
        else:
            HOLD_QUEUE.append(fid)

    print(f"🔁 Routed {len(SYNTHESIS_QUEUE)} to synthesis.")
    print(f"🪦 Routed {len(RETIREMENT_QUEUE)} to retirement.")
    print(f"⏸️ Routed {len(HOLD_QUEUE)} to hold.")

def save_queues():
    with open("synthesis_queue.json", "w") as s:
        json.dump(SYNTHESIS_QUEUE, s, indent=2)
    with open("retirement_queue.json", "w") as r:
        json.dump(RETIREMENT_QUEUE, r, indent=2)
    with open("hold_queue.json", "w") as h:
        json.dump(HOLD_QUEUE, h, indent=2)
    print("✅ Queues saved.")

if __name__ == "__main__":
    echo_log, gov_log = load_logs()
    route_fragments(echo_log, gov_log)
    save_queues()

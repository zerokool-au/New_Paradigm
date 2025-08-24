import json
import matplotlib.pyplot as plt

def load_logs():
    with open("governance_log.json") as g, open("retirement_log.json") as r:
        governance = json.load(g)
        retirement = json.load(r)
    return governance, retirement

def plot_tension_trajectory(governance, retirement):
    ids = [entry["id"] for entry in governance]
    tensions = [entry["epistemic_tension"] for entry in governance]
    retired_ids = {entry["id"] for entry in retirement}

    colors = ["red" if fid in retired_ids else "blue" for fid in ids]

    plt.figure(figsize=(12, 6))
    plt.bar(ids, tensions, color=colors)
    plt.axhline(0.85, color="gray", linestyle="--", label="Retirement Threshold")
    plt.title("Epistemic Tension Trajectory")
    plt.xlabel("Fragment ID")
    plt.ylabel("Tension Score")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    governance_log, retirement_log = load_logs()
    plot_tension_trajectory(governance_log, retirement_log)

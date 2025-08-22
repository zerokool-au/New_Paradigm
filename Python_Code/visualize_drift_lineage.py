import json
import plotly.graph_objects as go

# Load entries from all relevant log files
def load_all_entries():
    files = [
        "reinterpretation_log.json",
        "second_pass_log.jsonl",
        "resurrection_log.jsonl"
    ]
    entries = []
    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                if file.endswith(".json"):
                    entry = json.load(f)
                    entries.append(entry)
                else:
                    for line in f:
                        try:
                            entry = json.loads(line.strip())
                            entries.append(entry)
                        except json.JSONDecodeError:
                            print(f"Skipping malformed line in {file}")
        except FileNotFoundError:
            print(f"{file} not found. Skipping.")
    return entries

# Build Sankey diagram data from log entries
def build_sankey_data(entries):
    stages = []
    links = []

    def get_stage_label(entry):
        source = entry.get("source_stage", "unknown_stage")
        status = entry.get("status", "unknown_status")
        return f"{source} ({status})"

    for entry in entries:
        source = get_stage_label(entry)
        target_status = entry.get("status", "unknown_status")
        target = f"{target_status}_output"

        if source not in stages:
            stages.append(source)
        if target not in stages:
            stages.append(target)

        source_idx = stages.index(source)
        target_idx = stages.index(target)

        pair_label = " ↔ ".join(entry.get("pair", ["?", "?"]))
        links.append({
            "source": source_idx,
            "target": target_idx,
            "value": 1,
            "label": pair_label
        })

    return stages, links

# Render the Sankey diagram
def visualize_sankey(stages, links):
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=stages,
            color="blue"
        ),
        link=dict(
            source=[link["source"] for link in links],
            target=[link["target"] for link in links],
            value=[link["value"] for link in links],
            label=[link["label"] for link in links]
        )
    )])

    fig.update_layout(title_text="RR Drift Lineage", font_size=12)
    fig.show()

# Main execution
if __name__ == "__main__":
    entries = load_all_entries()
    stages, links = build_sankey_data(entries)
    visualize_sankey(stages, links)

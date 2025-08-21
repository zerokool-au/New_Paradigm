#!/usr/bin/env python3
"""
scripts/update_status.py
Generate a STATUS.md from project_state.json.
"""

import json
from datetime import datetime
import sys
import os

# Path to the JSON state file
STATE_FILE = os.path.join(os.path.dirname(__file__), "..", "project_state.json")
# Output markdown file
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "STATUS.md")

def main():
    # 1) Load your milestone definitions and completion percentages
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
    except FileNotFoundError:
        print(f"Error: {STATE_FILE} not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

    # 2) Build markdown
    lines = [
        "# Corrigible Cognition: Status Report",
        "",
        f"_Last updated: {datetime.utcnow().isoformat()}Z_",
        "",
        "| Milestone                                   | % Complete |",
        "|---------------------------------------------|-----------:|",
    ]
    for item in state.get("milestones", []):
        name = item.get("name", "")
        pct  = item.get("percent", 0)
        lines.append(f"| {name:<43} | {pct:>9}% |")

    lines.extend([
        "",
        f"**Overall**: {state.get('overall_percent', 0)}% complete",
        "",
        "## Notes",
    ])
    for note in state.get("notes", []):
        lines.append(f"- {note}")

    # 3) Write STATUS.md
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Updated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

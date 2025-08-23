# rr_lineage_tracker.py

class LineageTracker:
    def __init__(self):
        self.lineage_log = []

    def record_lineage(self, parent_fragment, child_fragment):
        entry = {
            "parent": parent_fragment,
            "child": child_fragment
        }
        self.lineage_log.append(entry)

        # Optional: write to file
        with open("rr_lineage_log.txt", "a", encoding="utf-8") as log:
            log.write(f"Parent Fragment: {parent_fragment}\n")
            log.write(f"Child Fragment:  {child_fragment}\n\n")

        print(f"\n🧬 Lineage recorded: {parent_fragment} → {child_fragment}")

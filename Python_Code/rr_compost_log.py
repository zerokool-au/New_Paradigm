# rr_compost_log.py

class CompostLog:
    def __init__(self):
        self.log = []

    def record(self, fragment, status, source="unknown"):
        entry = {
            "fragment": fragment,
            "status": status,  # preserved, reanimated, decayed
            "source": source
        }
        self.log.append(entry)
        print(f"\n🧾 Compost Log: [{status}] ← {fragment}")

    def summarize(self):
        print("\n🌿 Compost Summary:")
        counts = {"preserved": 0, "reanimated": 0, "decayed": 0}
        for entry in self.log:
            counts[entry["status"]] += 1
        for status, count in counts.items():
            print(f"— {status}: {count} fragments")

if __name__ == "__main__":
    log = CompostLog()
    log.record("Fragment A reconsiders earlier assumption about agency.", "reanimated", source="reinterpretation")
    log.record("Fragment B reveals tension in self-referential logic.", "preserved", source="synthesis")
    log.record("Fragment C challenges the notion of stable identity.", "decayed", source="audit")

    log.summarize()


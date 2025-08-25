class CompostLedger:
    def __init__(self):
        self.fragments = []

    def log_fragment(self, fragment):
        self.fragments.append(fragment)

    def get_fragments(self):
        return self.fragments

    def summarize(self):
        print("\n🪱 Compost Summary:")
        for f in self.fragments:
            print(f"🗑️ {f.id} → theme: {f.theme}, flags: {f.flags}")

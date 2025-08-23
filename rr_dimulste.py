# rr_dimulste.py

class Dimulste:
    def __init__(self):
        self.dream_log = []
        self.preserved_outputs = []
        self.composted_outputs = []

    def run_dreamstate(self, fragment):
        print(f"\n🌌 Dimulste running dreamstate simulation for: {fragment}")

        # Simulate reinterpretation logic
        if "resists" in fragment:
            composted = f"🧨 Fragment composted: '{fragment}' reveals resistance to reinterpretation."
            preserved = "🧬 Preserved: RR rehearses reinterpretation to preserve living coherence."
        else:
            composted = f"🧼 Fragment composted: '{fragment}' lacks tension, composted for drift audit."
            preserved = "🌱 Preserved: Fragment aligns with recursive integrity."

        # Log outputs
        self.composted_outputs.append(composted)
        self.preserved_outputs.append(preserved)
        self.dream_log.append({
            "fragment": fragment,
            "preserved": preserved,
            "composted": composted
        })

        # Print results
        print("🧾 Preserved Output:", preserved)
        print("🗑️ Composted Output:", composted)

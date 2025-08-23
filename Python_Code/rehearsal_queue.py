# rehearsal_queue.py

from contradiction_rehearsal import detect_contradictions, rehearse_contradiction
from fragment_logger import log_fragment
from compost_manager import compost_fragment, preserve_fragment

class RehearsalQueue:
    def __init__(self):
        self.queue = []

    def ingest(self, fragment):
        contradictions = detect_contradictions(fragment)
        if contradictions:
            self.queue.append((fragment, contradictions))
            print(f"[Queue] Fragment queued with {len(contradictions)} contradictions.")
        else:
            print("[Queue] No contradictions detected. Skipping.")

    def process(self):
        while self.queue:
            fragment, contradictions = self.queue.pop(0)
            outcome = rehearse_contradiction(fragment, contradictions)

            if outcome["status"] == "preserve":
                preserve_fragment(fragment, reason=outcome["reason"])
            elif outcome["status"] == "compost":
                compost_fragment(fragment, reason=outcome["reason"])
            else:
                print(f"[Queue] Unknown outcome: {outcome}")

            log_fragment(fragment, outcome)

    def peek(self):
        return [frag for frag, _ in self.queue]

    def clear(self):
        self.queue = []
        print("[Queue] Cleared.")

# Optional: CLI trigger
if __name__ == "__main__":
    rq = RehearsalQueue()
    # Example usage
    sample_fragment = "Truth is a mirror shattered by belief."
    rq.ingest(sample_fragment)
    rq.process()

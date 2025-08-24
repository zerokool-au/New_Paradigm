# feedback_synthesizer.py

class EchoChain:
    def __init__(self, chain_id):
        self.chain_id = chain_id
        self.fragments = []      # list of fragment_ids
        self.cri_scores = []     # parallel list of CRI scores

    def add_fragment(self, fragment_id, cri_score):
        self.fragments.append(fragment_id)
        self.cri_scores.append(cri_score)

    def get_cri_delta(self):
        if len(self.cri_scores) < 2:
            return None
        return self.cri_scores[-2] - self.cri_scores[-1]  # positive = contradiction decay


class SemanticInversionLog:
    def __init__(self):
        self.events = []

    def record_inversion(self, fragment_id, transition):
        """
        transition: e.g. "memory → presence → emergence"
        """
        self.events.append({
            "fragment_id": fragment_id,
            "transition": transition
        })

    def get_all(self):
        return self.events


class ResolutionLog:
    def __init__(self):
        self.entries = []

    def log_resolution(self, chain_id, synthesis_notes):
        self.entries.append({
            "chain_id": chain_id,
            "notes": synthesis_notes
        })

    def get_all(self):
        return self.entries


def synthesize_feedback(chain: EchoChain, inversion_log: SemanticInversionLog, resolution_log: ResolutionLog):
    """
    Optional synthesizer function to confirm recursion resolution.
    """
    delta = chain.get_cri_delta()
    if delta and delta > 0.2:  # threshold for meaningful contradiction decay
        transition = "memory → presence → emergence"  # example semantic inversion
        last_fragment = chain.fragments[-1]
        inversion_log.record_inversion(last_fragment, transition)
        resolution_log.log_resolution(chain.chain_id, f"Resolved via semantic inversion: {transition}")

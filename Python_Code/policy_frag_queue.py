# policy_frag_queue.py
class PolicyFragment:
    def __init__(self, fragment_id, content, cri_score, metadata):
        self.fragment_id = fragment_id
        self.content = content
        self.cri_score = cri_score
        self.metadata = metadata
        self.status = "pending"

class PolicyFragQueue:
    def __init__(self):
        self.queue = []

    def add_fragment(self, fragment: PolicyFragment):
        self.queue.append(fragment)

    def route_for_rehearsal(self):
        return [frag for frag in self.queue if frag.cri_score >= 0.7]

# lineage_map.py

class FragmentLineage:
    def __init__(self, fragment_id, parent_id, drift_vector, cri_history, dream_payload=None):
        """
        Represents a single fragment's lineage node.

        Args:
            fragment_id (str): Unique ID of the fragment.
            parent_id (str): ID of the parent fragment.
            drift_vector (list): Semantic drift transitions (e.g. ["memory → presence"]).
            cri_history (list): List of CRI scores over reinterpretation cycles.
            dream_payload (str, optional): Snapshot of Dimulste dreamstate output.
        """
        self.fragment_id = fragment_id
        self.parent_id = parent_id
        self.drift_vector = drift_vector
        self.cri_history = cri_history
        self.dream_payload = dream_payload


class LineageMap:
    def __init__(self):
        """
        Initializes the lineage map as a dictionary keyed by fragment_id.
        """
        self.map = {}

    def add_lineage(self, lineage: FragmentLineage):
        """
        Adds a lineage node to the map.

        Args:
            lineage (FragmentLineage): The lineage object to store.
        """
        self.map[lineage.fragment_id] = lineage

    def trace_ancestry(self, fragment_id):
        """
        Recursively traces the ancestry of a fragment.

        Args:
            fragment_id (str): The fragment to trace.

        Returns:
            list: Ordered list of FragmentLineage objects from oldest to newest.
        """
        lineage = []
        current = self.map.get(fragment_id)
        while current:
            lineage.append(current)
            current = self.map.get(current.parent_id)
        return lineage[::-1]  # oldest to newest

    def render_lineage_trace(self, fragment_id):
        """
        Renders a human-readable trace of a fragment's lineage.

        Args:
            fragment_id (str): The fragment to visualize.
        """
        trace = self.trace_ancestry(fragment_id)
        for node in trace:
            print(f"🧩 Fragment: {node.fragment_id}")
            print(f"↪️ Parent: {node.parent_id}")
            print(f"🌱 Drift: {' → '.join(node.drift_vector)}")
            print(f"📉 CRI History: {node.cri_history}")
            if node.dream_payload:
                print(f"💭 Dream Output: {node.dream_payload[:100]}...")  # Truncated for clarity
            print("—" * 40)

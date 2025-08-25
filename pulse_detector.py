class PulseDetector:
    def __init__(self):
        self.echo_registry = {}

    def register_echo(self, vector, fragment_id):
        if vector not in self.echo_registry:
            self.echo_registry[vector] = []
        self.echo_registry[vector].append(fragment_id)

    def summarize(self):
        summary = {}
        for vector, ids in self.echo_registry.items():
            summary[vector] = {
                "cadence": len(ids),
                "is_latent": len(ids) < 3
            }
        return summary

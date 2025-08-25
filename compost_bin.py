class CompostBin:
    def __init__(self):
        self.bin = []

    def discard(self, fragment):
        self.bin.append(fragment)

    def audit(self):
        return [f.id for f in self.bin]

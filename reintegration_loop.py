class ReintegrationLoop:
    def __init__(self, memory_bank, compost_bin=None, audit_logger=None):
        self.memory_bank = memory_bank
        self.compost_bin = compost_bin
        self.audit_logger = audit_logger

    def reintegrate(self, fragments):
        for fragment in fragments:
            if self._is_valid(fragment):
                self.memory_bank[fragment.id] = fragment
                if self.audit_logger:
                    self.audit_logger.log(fragment.id, "reintegrated", {"source": "reintegration_loop"})
            else:
                if self.compost_bin:
                    self.compost_bin.discard(fragment)
                if self.audit_logger:
                    self.audit_logger.log(fragment.id, "discarded", {"reason": "invalid fragment"})
        return True

    def _is_valid(self, fragment):
        # Basic validity check: must have text and at least one flag
        return bool(fragment.text) and bool(fragment.flags)

# rr_bias_utils.py

def detect_bias_vectors(fragment):
    vectors = []
    if "agency" in fragment:
        vectors.append("agency_conflict")
    if "self" in fragment:
        vectors.append("self_reference")
    if "identity" in fragment:
        vectors.append("identity_drift")
    if "contradicts" in fragment or "tension" in fragment:
        vectors.append("epistemic_tension")
    return vectors

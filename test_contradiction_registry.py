# test_contradiction_registry.py

from rr_contradiction_registry import ContradictionRegistry

# Initialize registry
registry = ContradictionRegistry()

# Sample fragments and bias vectors
fragment1 = "Fragment A contradicts earlier assumption about agency."
fragment2 = "Fragment B reveals tension in self-referential logic."
fragment3 = "Fragment C challenges the notion of stable identity."

bias_vectors1 = ["agency_conflict", "epistemic_tension"]
bias_vectors2 = ["self_reference"]
bias_vectors3 = ["identity_drift", "epistemic_tension"]

# Register contradictions
registry.register_contradiction(fragment1, bias_vectors1)
registry.register_contradiction(fragment2, bias_vectors2)
registry.register_contradiction(fragment3, bias_vectors3)

# Summarize registry
registry.summarize_registry()

# Retrieve by vector
print("\n🔍 Fragments tagged with 'epistemic_tension':")
for f in registry.get_fragments_by_vector("epistemic_tension"):
    print(f"— {f}")

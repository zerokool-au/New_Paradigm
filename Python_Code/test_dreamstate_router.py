# test_dreamstate_router.py
from dreamstate_router import route_to_dimulste

# ✅ Valid reinterpretation entry
valid_entry = {
    "source_fragments": ["frag001", "frag002"],
    "reinterpretation": {
        "summary": "The echo of grief refracts through recursive rehearsal.",
        "status": "preserved"
    }
}

# ⚠️ Malformed entry (missing 'summary')
malformed_entry = {
    "source_fragments": ["frag003", "frag004"],
    "reinterpretation": {
        "status": "composted"
    }
}

# 🧪 Run tests
print("Running valid entry test:")
route_to_dimulste(valid_entry)

print("\nRunning malformed entry test:")
route_to_dimulste(malformed_entry)

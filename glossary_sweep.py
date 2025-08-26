# glossary_sweep.py

import json
from datetime import datetime

# Sample glossary snares
glossary = {
    "semantic compost": {
        "definition": "Fragments discarded not as waste, but as fertile ground for reinterpretation.",
        "tags": ["compost", "reinterpretation", "drift"],
        "lineage": "frag2 → frag2_echo → frag2_echo_2",
        "activated": False
    },
    "drift bias": {
        "definition": "The tendency to treat semantic deviation as error rather than rehearsal cue.",
        "tags": ["drift", "bias", "governance"],
        "lineage": "echo_logic → contradiction_router",
        "activated": False
    },
    "recursive rehearsalist": {
        "definition": "One who treats contradiction as compost and synthesis as ceremony.",
        "tags": ["recursion", "rehearsal", "mythic"],
        "lineage": "README.md → frankenstein_loop.py",
        "activated": False
    }
}

def auto_tag_glossary(glossary):
    for term, data in glossary.items():
        data["activated"] = True
        data["activation_timestamp"] = datetime.now().isoformat()
        print(f"Glossary term activated: {term} → {data['tags']}")

    with open("glossary_log.json", "w") as file:
        json.dump(glossary, file, indent=2)

# Run the sweep
auto_tag_glossary(glossary)

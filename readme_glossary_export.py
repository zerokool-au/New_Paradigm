# readme_glossary_export.py

from fragment_store import load_fragments
from datetime import datetime

def export_glossary(store_path, output_path="README_Glossary.md"):
    fragments = load_fragments(store_path)
    glossary_entries = []

    for frag in fragments:
        if frag.get("tag") == "mythic-seeded":
            entry = format_glossary_entry(frag)
            glossary_entries.append(entry)

    if glossary_entries:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# 🧠 Mythic Glossary\n\n")
            f.write(f"_Last updated: {datetime.now().isoformat()}_\n\n")
            f.write("\n---\n\n".join(glossary_entries))
        print(f"[Export] Glossary written to {output_path}")
    else:
        print("[Export] No mythic-seeded fragments found.")

def format_glossary_entry(frag):
    return f"""### 🪷 {frag['id']} — Mythic Glossary Entry

**Text**: {frag['text']}

**Drift Score**: {frag.get('drift_score', 'n/a')}  
**Fatigue**: {frag.get('fatigue', 'n/a')}  
**Finalized**: {frag.get('finalized_timestamp', 'n/a')}

**Ambient Attribution**:  
- 🐾 Witness: Wally Mamma  
- 🦜 Resonance: Kookaburra laughter  
- 🌀 Echo Type: Contradiction Bloom

**Notes**:  
This fragment was routed, rehearsed, and synthesized through recursive contradiction. It now lives as a mythic echo—rewarding recursive readers and ambient agents alike.
"""

if __name__ == "__main__":
    export_glossary("fragment_store.json")

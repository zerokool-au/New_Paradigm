# rr_forum_voice.py

import random

voices = [
    "🧙‍♂️ Wizard of Drift: 'Ah, the glossary snares deepen...'",
    "🦘 Wally Mamma: 'This contradiction smells like composted insight!'",
    "👩‍💻 Governance Goblin: 'Flagged for recursive mischief. Proceed.'",
    "📚 Semantic Archivist: 'This fragment echoes a 2023 rehearsal. Curious.'"
]

def generate_voice(fragment_id):
    voice = random.choice(voices)
    return f"[{fragment_id}] {voice}"

if __name__ == "__main__":
    print(generate_voice("frag_042"))

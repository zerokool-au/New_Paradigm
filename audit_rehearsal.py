import json
import random
import datetime
from collections import Counter
from README_sync import sync_readme_glossary
from README_archive import archive_readme_glossary

# 🌀 Reintegration Queue
def reintegration_queue(synthesis_queue):
    reintegrated = []
    for item in synthesis_queue:
        enriched = {
            "id": item.get("id"),
            "text": item.get("text"),
            "suggested_tags": suggest_tags(item.get("text")),
            "metadata": item.get("metadata", {})
        }
        reintegrated.append(enriched)
    return reintegrated

# 🏷️ Tag Suggestion Logic
def suggest_tags(text):
    tags = []
    if "paradox" in text.lower():
        tags.append("epistemic_paradox")
    if "loop" in text.lower() or "recursive" in text.lower():
        tags.append("recursive_koan")
    if "governance" in text.lower():
        tags.append("governance_prompt")
    if "dream" in text.lower():
        tags.append("dimulste_trace")
    if "error" in text.lower():
        tags.append("compost_signal")
    return tags or ["unclassified"]

# 🗂️ Log Reintegration Queue to File
def log_reintegration(queue, filename="reintegration_log.jsonl"):
    with open(filename, "w", encoding="utf-8") as f:
        for item in queue:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f"\n🗂️ Reintegration log saved to {filename}")

# 📊 Tag Frequency Dashboard
def visualize_tag_distribution(queue):
    tag_counter = Counter()
    for item in queue:
        for tag in item.get("suggested_tags", []):
            tag_counter[tag] += 1
    print("\n📊 Tag Frequency Distribution:")
    for tag, count in tag_counter.most_common():
        print(f"  {tag}: {count}")

# 📚 Glossary Injector
def inject_glossary_entries(queue):
    print("\n📚 Injected Glossary Entries:")
    for item in queue:
        tags = item.get("suggested_tags", [])
        if any(t in tags for t in ["epistemic_paradox", "recursive_koan", "governance_prompt"]):
            entry = f"🔹 **{item['id']}** — {item['text']}\n    _Tags: {', '.join(tags)}_"
            print(entry)

# 🚀 Full Audit Rehearsal
def audit_rehearsal(synthesis_queue):
    reintegrated = reintegration_queue(synthesis_queue)
    log_reintegration(reintegrated)
    visualize_tag_distribution(reintegrated)
    inject_glossary_entries(reintegrated)
    return reintegrated

# 🔁 Fragment Echo Tracker
def detect_fragment_echo(log_path="reintegration_log.jsonl"):
    seen = {}
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line.strip())
            text = entry.get("text", "").strip()
            seen[text] = seen.get(text, 0) + 1

    print("\n🔁 Fragment Echoes:")
    for text, count in seen.items():
        if count > 1:
            print(f" → \"{text}\" echoed {count} times")

# 🔁 Drift Echo Tracker (by notes)
def detect_drift_echo(log_path="reintegration_log.jsonl"):
    seen = {}
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line.strip())
            notes = entry.get("notes", "").strip()
            if notes:
                seen[notes] = seen.get(notes, 0) + 1

    print("\n🔁 Drift Echoes (by notes):")
    for notes, count in seen.items():
        if count > 1:
            print(f" → \"{notes}\" echoed {count} times")

# 🌿 Fragment Haiku Generator (with padding)
def generate_haiku_from_fragments(log_path="reintegration_log.jsonl"):
    with open(log_path, "r", encoding="utf-8") as f:
        entries = [json.loads(line.strip()) for line in f]

    text_pool = [e.get("text", "").strip() for e in entries if e.get("text")]
    if not text_pool:
        print("⚠️ No fragment text found in log.")
        return

    selected = random.choice(text_pool)
    print(f"\n🎴 Selected Fragment:\n\"{selected}\"\n")

    words = selected.split()
    while len(words) < 15:
        words.append("…")  # Pad with ellipsis for ambient effect

    line1 = " ".join(words[:5])
    line2 = " ".join(words[5:10])
    line3 = " ".join(words[10:15])

    print("🌿 Fragment Haiku:")
    print(f"{line1}")
    print(f"{line2}")
    print(f"{line3}")

# 📝 Haiku Logger
def generate_and_log_haiku(log_path="reintegration_log.jsonl", save_path="haiku_log.jsonl"):
    import random
    import json

    with open(log_path, "r", encoding="utf-8") as f:
        entries = [json.loads(line.strip()) for line in f]

    text_pool = [e.get("text", "").strip() for e in entries if e.get("text")]
    if not text_pool:
        print("⚠️ No fragment text found in log.")
        return

    selected = random.choice(text_pool)
    words = selected.split()
    while len(words) < 15:
        words.append("…")

    haiku = {
        "source_text": selected,
        "haiku": [
            " ".join(words[:5]),
            " ".join(words[5:10]),
            " ".join(words[10:15])
        ],
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

    with open(save_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(haiku) + "\n")

    print("\n🎴 Logged Haiku:")
    print(f"→ {haiku['haiku'][0]}")
    print(f"→ {haiku['haiku'][1]}")
    print(f"→ {haiku['haiku'][2]}")


if __name__ == "__main__":
    synthesis_queue = [
        {"id": "frag_001", "text": "Recursive governance rehearsal reveals paradox."},
        {"id": "frag_002", "text": "Dimulste traces dreamstate compost."},
        {"id": "frag_003", "text": "Wallaby laughter signals semantic drift."}
    ]

    reintegrated = audit_rehearsal(synthesis_queue)
    archive_readme_glossary()             # 🗃️ Archive current glossary
    sync_readme_glossary(reintegrated)    # 🧩 Inject new glossary



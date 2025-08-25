import re

# 📚 Format Glossary Entries
def format_glossary_entries(queue):
    entries = []
    for item in queue:
        tags = item.get("suggested_tags", [])
        if any(t in tags for t in ["epistemic_paradox", "recursive_koan", "governance_prompt"]):
            entry = f"🔹 **{item['id']}** — {item['text']}\n    _Tags: {', '.join(tags)}_"
            entries.append(entry)
    return "\n".join(entries)

# 📝 Inject into README.md
def inject_glossary_to_readme(glossary_text, readme_path="README.md"):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match the Living Glossary block
    pattern = r"(## 🧩 Living Glossary – Mischief Layer\n)(.*?)(?=\n## |\Z)"
    new_block = f"## 🧩 Living Glossary – Mischief Layer\n{glossary_text}\n"

    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, new_block, content, flags=re.DOTALL)
        print("🔄 Replaced existing glossary section in README.md")
    else:
        content += f"\n\n{new_block}"
        print("➕ Appended new glossary section to README.md")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

# 🚀 Sync Glossary
def sync_readme_glossary(queue):
    glossary_text = format_glossary_entries(queue)
    inject_glossary_to_readme(glossary_text)

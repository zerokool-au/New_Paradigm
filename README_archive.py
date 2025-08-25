import re
from datetime import datetime

# 🗃️ Extract Glossary Block
def extract_glossary_block(readme_path="README.md"):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"(## 🧩 Living Glossary – Mischief Layer\n)(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, flags=re.DOTALL)
    return match.group(0) if match else None

# 🗂️ Archive to Timestamped File
def archive_glossary(block, archive_dir="GLOSSARY_legacy.md"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archive_entry = f"\n\n### 🕰️ Archived Glossary — {timestamp}\n{block}"
    with open(archive_dir, "a", encoding="utf-8") as f:
        f.write(archive_entry)
    print(f"📦 Archived glossary to {archive_dir}")

# 🚀 Archive Ritual
def archive_readme_glossary():
    block = extract_glossary_block()
    if block:
        archive_glossary(block)
    else:
        print("⚠️ No glossary block found to archive.")

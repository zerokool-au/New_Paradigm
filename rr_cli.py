# rr_cli.py

import argparse
from fragment_store import load_fragments
from reintegration_logic import reintegrate_fragments
from rr_forum_voice import generate_voice

def glossary_lookup(term):
    glossary = {
        "Echo Logic": "Recursive framework for semantic drift detection.",
        "Dimulste": "Dreamstate rehearsal loop for fragment synthesis.",
        "Wally": "Ambient override flag. Trust the matriarch."
    }
    print(glossary.get(term, "Term not found."))

def tail_audit(store_path, count=5):
    fragments = load_fragments(store_path)
    for frag in fragments[-count:]:
        print(f"{frag['id']}: {frag.get('status')}")

def contradiction_sweep(store_path):
    fragments = load_fragments(store_path)
    for frag in fragments:
        if frag.get("status") == "contradiction":
            print(generate_voice(frag["id"]))

parser = argparse.ArgumentParser()
parser.add_argument("--glossary", help="Lookup glossary term")
parser.add_argument("--tail", action="store_true", help="Tail audit log")
parser.add_argument("--sweep", action="store_true", help="Run contradiction sweep")
parser.add_argument("--wally", action="store_true", help="Ambient override")

args = parser.parse_args()

if args.glossary:
    glossary_lookup(args.glossary)
if args.tail:
    tail_audit("fragment_store.json")
if args.sweep:
    contradiction_sweep("fragment_store.json")
if args.wally:
    print("🦘 Ambient override engaged. Wally Mamma approves.")
    reintegrate_fragments("fragment_store.json", threshold=0.9)

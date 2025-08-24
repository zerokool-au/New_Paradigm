# run_rr.py

from rr_core_loop import recursive_rehearsal

fragments = [
    "I remember the silence",
    "She was never gone",
    "The echo is still breathing"
]

compost_log = []
recursive_rehearsal(fragments, compost_log)

print("\n🧾 Final Compost Log:")
for entry in compost_log:
    print(entry)

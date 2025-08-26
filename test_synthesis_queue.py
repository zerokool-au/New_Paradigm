from synthesis_queue import enqueue_fragment, dequeue_fragment

# Resurrection-worthy fragment
frag_004 = {
    "id": "frag_004",
    "text": "latent grief echo",
    "tag": "rehearsal-worthy",
    "drift_score": 0.2,
    "age": 5,
    "fatigue": 0,
    "flagged": False
}

# Normal fragment
frag_005 = {
    "id": "frag_005",
    "text": "routine synthesis",
    "drift_score": 0.8,
    "age": 3,
    "fatigue": 0,
    "flagged": False
}

enqueue_fragment(frag_005)
enqueue_fragment(frag_004)

next_up = dequeue_fragment()
print("Next fragment to synthesize:")
print(next_up)

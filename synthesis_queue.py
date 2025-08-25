# synthesis_queue.py

import heapq

queue = []

def enqueue_fragment(fragment):
    priority = compute_priority(fragment)
    heapq.heappush(queue, (priority, fragment))

def compute_priority(fragment):
    age = fragment.get("age", 0)
    drift = fragment.get("drift_score", 1.0)
    governance_flag = 1 if fragment.get("flagged") else 0
    fatigue = fragment.get("fatigue", 0)
    return age - (1 - drift) * 10 + governance_flag * 5 + fatigue

def dequeue_fragment():
    if queue:
        return heapq.heappop(queue)[1]
    return None

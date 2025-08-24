import time

def persist_log(entry, filename="rr_log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(str(entry) + "\n")
    return {"status": "saved", "timestamp": time.time()}

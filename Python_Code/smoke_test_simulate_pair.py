#!/usr/bin/env python3

import sys
import time
import psutil
import random
import json
import argparse

from simulate_pair import simulate_pair  # adjust import path if needed
from agents import Agent                 # ensure your Agent class is importable
from notifier import issue_notifier      # ensures notifier is loaded

random.seed(42)
ALERT_LOG = "alert_log.jsonl"


def measure_run(func, metric_name, extra_info=None):
    """
    Runs `func`, measures wall-clock time and RSS memory delta via psutil,
    and returns an output dict with status, metrics, and result (or error).
    """
    start_time = time.time()
    proc = psutil.Process()
    start_mem = proc.memory_info().rss

    try:
        result = func()
        status = "success"
    except Exception as e:
        result = None
        status = "error"
        extra_info = (extra_info or {})
        extra_info["error"] = str(e)

    end_time = time.time()
    end_mem = proc.memory_info().rss

    metrics = {
        "metric": metric_name,
        "duration_sec": end_time - start_time,
        "memory_delta_bytes": end_mem - start_mem,
    }
    if extra_info:
        metrics.update(extra_info)

    return {
        "status": status,
        "metrics": metrics,
        "result": result
    }


def random_context():
    return {
        "history": [random.random() for _ in range(5)],
        "shared_context_score": random.random()
    }


def parse_args():
    parser = argparse.ArgumentParser(
        description="Smoke-test harness: run your simulation N times and report a percentile threshold."
    )
    parser.add_argument(
        "--runs", type=int, default=100,
        help="Number of simulation runs to execute (default: 100)"
    )
    parser.add_argument(
        "--percentile", type=float, default=99.0,
        help="Which percentile to compute on your results (default: 99.0)"
    )
    parser.add_argument(
        "--batch", action="store_true",
        help="suppress human-readable prints and emit only JSON metrics"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="pretty-print JSON metrics for each run"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # PHASE 1: collect shared_context_scores
    recorded = [random_context()["shared_context_score"]
                for _ in range(args.runs)]

    # compute percentile threshold
    sorted_scores = sorted(recorded)
    idx = int(len(sorted_scores) * args.percentile / 100)
    idx = min(idx, len(sorted_scores) - 1)
    threshold = sorted_scores[idx]

    if not args.batch:
        print(f"\nComputed {args.percentile}th percentile threshold -> {threshold:.3f}\n")

    # PHASE 2: re-run simulations with dynamic threshold
    alert_count = 0
    open(ALERT_LOG, "w").close()  # clear old log

    scores = []
    for i in range(1, args.runs + 1):
        A = Agent(id=f"A{i}")
        B = Agent(id=f"B{i}")
        ctx = random_context()
        score = ctx["shared_context_score"]
        scores.append(score)

        if score < threshold:
            alert_count += 1

        output = measure_run(
            lambda: simulate_pair(A, B, ctx, threshold=threshold),
            metric_name="simulate_pair",
            extra_info={"agents": (A.id, B.id), "threshold": threshold}
        )

        # per-run JSON metrics
        if args.batch:
            print(json.dumps(output))
        elif args.verbose:
            print(json.dumps(output, indent=2))

        if i % 10 == 0 or i == args.runs:
            if not args.batch:
                print(f"Completed {i}/{args.runs} runs")

    # interactive alerts detail + summary
    if not args.batch:
        print("\n--- Alerts detail ---")
        with open(ALERT_LOG, "r") as f:
            for idx, line in enumerate(f, start=1):
                if idx > args.runs:
                    break
                alert = json.loads(line)
                print(f"Run {idx}:", json.dumps(alert, indent=2))

        print("\n=== Summary ===")
        print(f"Total runs:   {args.runs}")
        print(f"Alerts fired: {alert_count}")
        print(f"Non-alerts:   {args.runs - alert_count}")
        print(
            f"Scores -> "
            f"min: {min(scores):.3f}, "
            f"avg: {(sum(scores)/len(scores)):.3f}, "
            f"max: {max(scores):.3f}"
        )

    # exit code
    if alert_count > 0:
        print(
            f"\n❌ Smoke tests failed with {alert_count} alert(s)\n",
            file=sys.stderr
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

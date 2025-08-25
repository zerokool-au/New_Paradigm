#!/usr/bin/env python3
"""
debug_alert.py: Replay simulation, compute threshold, log score + JSONL record,
with an optional “test breach” mode to force the alert path.
"""

import argparse
import json
import os
import time
import logging
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from simulate_pair import simulate_pair
from agents import Agent


def configure_console_logging(level: int) -> None:
    """
    Configure the root logger for console output.
    """
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S"
    )


def configure_file_logger(path: str) -> logging.Logger:
    """
    Create and return a logger that writes JSON lines to `path`,
    rotating at 5 MB with up to 3 backups, and does not
    propagate writes back to the console.
    """
    logger = logging.getLogger("alert_logger")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = RotatingFileHandler(
            filename=path,
            mode="a",
            maxBytes=5 * 1024 * 1024,  # 5 MB threshold
            backupCount=3,             # keep .1, .2, .3
            encoding="utf-8",
            delay=False
        )
        fmt_fields = ["timestamp", "agentA", "agentB", "score", "history_sample"]
        fmt_str = " ".join(f"%({f})s" for f in fmt_fields)
        handler.setFormatter(jsonlogger.JsonFormatter(fmt_str))
        logger.addHandler(handler)

    return logger


def main():
    parser = argparse.ArgumentParser(
        description="Replay a saved alert, simulate, and log the result."
    )
    parser.add_argument(
        "--alert-json",
        type=str,
        help="Path to alert JSON file; if omitted uses built-in example."
    )
    parser.add_argument(
        "--log-path",
        type=str,
        default="alert_log.jsonl",
        help="JSONL file to append alerts to."
    )
    parser.add_argument(
        "--fail-path",
        action="store_true",
        help="Write to a protected path (overrides --log-path)."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show debug-level logs."
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Show warnings and errors only."
    )
    parser.add_argument(
        "--test-breach",
        action="store_true",
        help="Force threshold above raw_score to test ALERT logic."
    )
    args = parser.parse_args()

    # 1) Console logging level
    if args.quiet:
        level = logging.WARNING
    elif args.verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    configure_console_logging(level)

    # 2) Load or default the alert JSON
    if args.alert_json:
        with open(args.alert_json, "r", encoding="utf-8") as f:
            alert_json = f.read()
    else:
        alert_json = (
            '{"status": "success", "metrics": {"metric": "simulate_pair", '
            '"duration_sec": 0.000215, "memory_delta_bytes": 0, '
            '"agents": ["A335", "B335"], "threshold": 0.0119569}, '
            '"result": {"agentA": "A335", "agentB": "B335", '
            '"score": 0.3362058, "history_sample": [0.49250445, 0.17990723]}}'
        )
    alert = json.loads(alert_json)

    # 3) Instantiate agents and context
    A = Agent(id=alert["result"]["agentA"])
    B = Agent(id=alert["result"]["agentB"])
    ctx = {
        "history": alert["result"]["history_sample"],
        "shared_context_score": alert["result"]["score"]
    }
    threshold = alert["metrics"]["threshold"]

    # 4) Log inputs to console
    logging.info("Replaying %s vs %s", A.id, B.id)
    logging.info("History sample: %s", ctx["history"])
    logging.info("Threshold: %s", threshold)

    # 5) Run simulation
    result = simulate_pair(A, B, ctx, threshold=threshold)
    raw_score = result.get("score") if isinstance(result, dict) else result

    logging.debug("Full result dict: %s", result)
    logging.info("Raw simulation score: %s", raw_score)

    # 5a) Test‐breach override
    if args.test_breach:
        threshold = raw_score + 1.0
        logging.info("Test breach: overriding threshold to %s", threshold)

    # 6) Notify if score dips below threshold
    if raw_score < threshold:
        logging.error("ALERT: Score %s fell below threshold %s!", raw_score, threshold)
        # Place your notifier integration here (Slack, PagerDuty, email, etc.)

    # 7) Determine log path (fail-path vs normal)
    if args.fail_path:
        log_path = "C:\\Windows\\system32\\nope.jsonl"
    else:
        log_path = args.log_path
        try:
            os.remove(log_path)
        except FileNotFoundError:
            pass

    # 8) Configure file logger and append exactly one JSON line
    file_logger = configure_file_logger(log_path)
    record = {
        "timestamp": time.time(),
        "agentA": A.id,
        "agentB": B.id,
        "score": raw_score,
        "history_sample": ctx["history"]
    }
    file_logger.info("", extra=record)
    logging.info("Appended one record to %s", log_path)


if __name__ == "__main__":
    main()

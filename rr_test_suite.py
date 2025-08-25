# rr_test_suite.py

import time
from rr_drift_test import run_drift_test
from rr_governance_test import run_governance_test

def log_header(title):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== {title} @ {timestamp} ===\n")

def run_suite():
    log_header("RR Drift Test")
    run_drift_test()

    log_header("RR Governance Test")
    run_governance_test()

    log_header("Suite Complete")

if __name__ == "__main__":
    run_suite()

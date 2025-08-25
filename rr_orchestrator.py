from echo_logic import run_echo_logic, save_echo_log
from rr_fragments import load_fragments
from reinterpretation_logic import route_fragments_for_reinterpretation, save_pool
from governance_loop import run_governance_loop, save_log
from compost_retirement import retire_fragments, save_retirement_log
from compost_analytics import analyze_fragments, plot_analytics
from rr_drift_audit import DriftAuditHook, integrate_drift_audit
from rr_core.audit import DriftLogger, GovernanceTrigger
from rr_core.synthesis import SynthesisQueue
import json

def load_governance_log(path="governance_log.json"):
    with open(path) as f:
        return json.load(f)

def load_reinterpretation_pool(path="reinterpretation_pool.json"):
    with open(path) as f:
        return json.load(f)

def run_rr_cycle():
    print("\n🔁 Loading fragments...")
    fragments = load_fragments()

    print("\n🧩 Initializing synthesis queue with drift audit...")
    synthesis_queue = SynthesisQueue(config={})  # Replace with actual config if needed
    audit_hook = DriftAuditHook(
        logger=DriftLogger(),
        trigger=GovernanceTrigger(threshold=1.5)
    )
    integrate_drift_audit(synthesis_queue, audit_hook)

    print("\n🧠 Routing for reinterpretation...")
    route_fragments_for_reinterpretation(fragments)
    save_pool()

    print("\n🔊 Running echo logic...")
    reinterpretation_pool = load_reinterpretation_pool()
    run_echo_logic(reinterpretation_pool)
    save_echo_log()

    print("\n🧭 Running governance rehearsal...")
    run_governance_loop()
    save_log()

    print("\n🪦 Retiring exhausted fragments...")
    governance_log = load_governance_log()
    retire_fragments(fragments, governance_log)
    save_retirement_log()

    print("\n📊 Running compost analytics...")
    ids, fatigue, volatility, bias = analyze_fragments(fragments)
    plot_analytics(ids, fatigue, volatility, bias)

    print("\n✅ RR cycle complete.")

if __name__ == "__main__":
    run_rr_cycle()

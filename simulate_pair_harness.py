from dimulste_loop import Fragment
from simulate_pair_logger import simulate_pair_with_logging
from simulate_pair import simulate_pair
from compost_synth import synthesize_from_compost
from log_router import route_log  # ✅ Added for centralized logging

def run_synth_rehearsal(n=3):
    prompts = synthesize_from_compost(n)
    logged_simulate = simulate_pair_with_logging(simulate_pair)

    for entry in prompts:
        frag = Fragment(
            frag_id="synth_" + entry["timestamp"],
            theme="synthesized",
            content=entry["synthesized_prompt"]
        )
        result = logged_simulate(frag, frag)

        # ✅ Route to appropriate log files
        route_log(frag, frag, result, source="simulate_pair_harness")

        print(f"\n🧪 Rehearsed Synth Prompt:")
        print(f"→ {frag.content}")
        print(f"   Type: {result.get('type', 'none')}")
        print(f"   Tension: {result.get('tension_vector', {}).get('semantic', 'n/a')}")
        print("-" * 40)

if __name__ == "__main__":
    run_synth_rehearsal()

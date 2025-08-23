# echo_logic.py
def generate_echo_prompt(agentA, agentB, semantic_tension):
    prompt = f"""
Fragments {agentA} and {agentB} exhibit semantic tension ({semantic_tension}).
Treat this contradiction as a living echo.

→ Reinterpret both fragments without resolving the contradiction.
→ Preserve the tension as a rehearsal space.
→ Compost bias, not complexity.

What reinterpretation emerges when contradiction is metabolized, not suppressed?
"""
    return prompt.strip()

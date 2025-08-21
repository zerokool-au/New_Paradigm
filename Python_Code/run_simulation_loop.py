from simulate_pair import simulate_pair
from logger import log_alert

# Sample agents with .id attributes
class Agent:
    def __init__(self, agent_id):
        self.id = agent_id

agent_list = [
    Agent("alpha"),
    Agent("beta"),
    Agent("gamma"),
    Agent("delta")
]

# Sample contexts with history and fragment
contexts = [
    {"history": [0.4, 0.6, 0.5], "fragment": "Echoes of recursion"},
    {"history": [0.9, 0.8, 0.85], "fragment": "Semantic drift detected"},
    {"history": [0.2, 0.3], "fragment": "Contradiction metabolized"},
    {"history": [], "fragment": "No prior rehearsal"}
]

# Threshold for alert triggering
threshold = 0.5

# Run simulation loop
for i in range(len(agent_list) - 1):
    agent_a = agent_list[i]
    agent_b = agent_list[i + 1]
    context = contexts[i % len(contexts)]

    alert = simulate_pair(agent_a, agent_b, context, threshold)
    print(f"Alert returned: {alert}")
    log_alert(alert)

from echo_witness import EchoWitness

witness = EchoWitness()

# Log a contradiction echo
witness.observe(event_type="contradiction", fragment="Matriarchal override triggered", resonance="CRI spike")

# Log a semantic drift
witness.observe(event_type="drift", fragment="Glossary snare reinterpreted", resonance="latent trigger")

# Export log for synthesis queue or audit trail
log = witness.export_log()

# Optional: print full log
for entry in log:
    print(entry)

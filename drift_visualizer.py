def visualize_drift_vector(fragment_id, drift_vector):
    print(f"📊 Drift Vector for {fragment_id}:")
    for key, value in drift_vector.items():
        print(f" - {key}: {value}")

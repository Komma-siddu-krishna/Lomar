import numpy as np

NUM_CLIENTS = 5
ROUNDS = 5


def run_federated_training():

    results = []
    all_drifts = []

    for r in range(ROUNDS):

        round_drifts = []

        for client_id in range(NUM_CLIENTS):

            # Genuine client behaviour
            accuracy = np.random.uniform(0.80, 0.95)
            drift = np.random.uniform(0.05, 0.3)

            # Make Client 2 malicious
            if client_id == 2:
                accuracy = np.random.uniform(0.40, 0.65)
                drift = np.random.uniform(1.0, 1.8)

            results.append({
                "round": r,
                "client": client_id,
                "accuracy": accuracy
            })

            round_drifts.append(drift)

        all_drifts.append(round_drifts)

    return {
        "results": results,
        "all_drifts": all_drifts
    }
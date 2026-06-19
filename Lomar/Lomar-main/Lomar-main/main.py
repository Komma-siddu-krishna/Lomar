from federated_simulation import run_federated_training
from visualization import plot_layer_drift_3d

if __name__ == "__main__":
    
    drifts = run_federated_training(
        NUM_CLIENTS=5,
        malicious_clients=[2, 4]
    )

    plot_layer_drift_3d(drifts)

import numpy as np


def explain_client(global_weights, client_weights):

    layer_drifts = []

    for gw, cw in zip(global_weights, client_weights):
        drift = np.linalg.norm(gw - cw)
        layer_drifts.append(drift)

    total_drift = np.mean(layer_drifts)

    explanation = {
        "layer_drifts": layer_drifts,
        "total_drift": total_drift,
        "most_affected_layer": np.argmax(layer_drifts)
    }

    return explanation

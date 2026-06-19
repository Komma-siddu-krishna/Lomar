import numpy as np

def compute_layer_drift(global_weights, client_weights):
    layer_drifts = []
    for gw, cw in zip(global_weights, client_weights):
        drift = np.linalg.norm(cw - gw)
        layer_drifts.append(drift)
    return layer_drifts


def explain_client(global_weights, client_weights, threshold=5.0):
    
    layer_drifts = compute_layer_drift(global_weights, client_weights)
    total_drift = sum(layer_drifts)
    
    explanation = {
        "total_drift": total_drift,
        "layer_drifts": layer_drifts,
        "most_impacted_layer": int(np.argmax(layer_drifts))
    }
    
    if total_drift > threshold:
        explanation["status"] = "Malicious"
        explanation["reason"] = "High model drift detected"
    else:
        explanation["status"] = "Benign"
        explanation["reason"] = "Drift within acceptable range"
    
    return explanation


def compute_trust(total_drift, max_drift=20):
    trust = max(0, 1 - (total_drift / max_drift))
    return trust

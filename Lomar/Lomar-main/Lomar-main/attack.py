# attack.py
import numpy as np

# -----------------------------
# Model poisoning
# -----------------------------
def model_poison(weights, noise_scale=5.0):
    """
    Add Gaussian noise to each layer's weights.
    :param weights: list of numpy arrays
    :param noise_scale: standard deviation of noise
    """
    poisoned = []
    for w in weights:
        noise = np.random.normal(0, noise_scale, w.shape)
        poisoned.append(w + noise)
    return poisoned

# -----------------------------
# Label flip attack
# -----------------------------
def label_flip(y):
    """
    Randomly flip labels for malicious client.
    :param y: numpy array of labels
    """
    return np.random.randint(0, 10, len(y))

# -----------------------------
# Gradient scaling attack
# -----------------------------
def gradient_scale(weights, factor=5.0):
    """
    Multiply model weights by a factor to simulate extreme updates.
    :param weights: list of numpy arrays
    :param factor: scaling factor
    """
    return [w * factor for w in weights]
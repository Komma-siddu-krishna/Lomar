# compression.py
import numpy as np

def compress_weights(weights, decimals=2):
    """
    Simple weight compression: rounds all model weights to given decimals.
    :param weights: list of numpy arrays (model weights)
    :param decimals: number of decimal places to keep
    :return: list of compressed weights
    """
    compressed = [np.round(w, decimals=decimals) for w in weights]
    return compressed
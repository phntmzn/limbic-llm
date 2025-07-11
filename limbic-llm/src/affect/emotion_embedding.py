

import numpy as np

# Fixed emotion embedding dictionary (could be learned or extended)
EMOTION_VECTORS = {
    "joy":      np.array([1.0, 0.0, 0.0, 0.0]),
    "sadness":  np.array([0.0, 1.0, 0.0, 0.0]),
    "anger":    np.array([0.0, 0.0, 1.0, 0.0]),
    "fear":     np.array([0.0, 0.0, 0.0, 1.0]),
}

def emotion_to_embedding(emotion_label):
    """
    Convert an emotion label into a fixed-size embedding vector.
    Unknown labels return a zero vector.
    """
    return EMOTION_VECTORS.get(emotion_label.lower(), np.zeros(4))
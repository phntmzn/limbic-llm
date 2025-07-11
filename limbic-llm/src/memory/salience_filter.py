def filter_by_salience(items, threshold=0.7):
    """
    Filter items based on a salience score threshold.
    Each item is expected to be a tuple: (text, salience_score).
    """
    return [text for text, score in items if score >= threshold]

def rank_by_salience(items):
    """
    Sort items by salience score in descending order.
    Each item is expected to be a tuple: (text, salience_score).
    """
    return sorted(items, key=lambda x: x[1], reverse=True)

def get_salient_items_above_threshold(entries, threshold=0.7):
    """
    Return only items with salience scores greater than or equal to the threshold.
    Each entry should be a tuple of the form (text, salience_score).
    """
    return [text for text, score in entries if score >= threshold]

def sort_items_by_salience_descending(entries):
    """
    Return items sorted by salience score in descending order.
    Each entry should be a tuple of the form (text, salience_score).
    """
    return sorted(entries, key=lambda x: x[1], reverse=True)

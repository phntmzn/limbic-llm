


from transformers import pipeline

# Load sentiment analysis pipeline (zero-shot or finetuned on emotion)
sentiment_pipeline = pipeline("sentiment-analysis")

def score_response(prompt, response, target_emotion="POSITIVE"):
    """
    Score a response based on how well it aligns with the target emotion.
    """
    try:
        result = sentiment_pipeline(response)[0]
        label = result["label"]
        score = result["score"]

        if label == target_emotion.upper():
            return score
        else:
            return 1.0 - score
    except Exception as e:
        print(f"Sentiment analysis failed: {e}")
        return 0.0
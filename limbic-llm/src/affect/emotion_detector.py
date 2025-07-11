

from transformers import pipeline

# Load zero-shot or fine-tuned emotion classifier
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def detect_emotion(text):
    """
    Detect the primary emotion of a given text input.
    Returns a string label such as 'joy', 'sadness', 'anger', or 'fear'.
    """
    try:
        result = emotion_pipeline(text)[0]
        return result["label"].lower()
    except Exception as e:
        print(f"Emotion detection failed: {e}")
        return "neutral"
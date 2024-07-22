from transformers import pipeline

# Load pre-trained sentiment analysis pipeline
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text: str) -> str:
    """
    Analyze the sentiment of the provided text using a pre-trained model.

    Args:
        text (str): The text to be analyzed.

    Returns:
        str: The sentiment of the text (positive, negative, or neutral).
    """
    result = sentiment_model(text)[0]
    return result['label'].lower()
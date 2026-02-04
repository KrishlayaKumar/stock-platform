from app.config import CONFIDENCE_THRESHOLD

def make_recommendation(direction, confidence, sentiment):
    if direction == "UP" and confidence >= CONFIDENCE_THRESHOLD and sentiment == "POSITIVE":
        return "BUY"
    elif direction == "DOWN" and confidence >= CONFIDENCE_THRESHOLD and sentiment == "NEGATIVE":
        return "SELL"
    else:
        return "HOLD"

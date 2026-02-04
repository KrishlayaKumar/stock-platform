# app/pipeline.py

from ml.fetch import fetch_stock_data
from ml.preprocess import preprocess_stock
from ml.predict import predict_price
from ml.sentiment import analyze_sentiment
from ml.recommend import make_recommendation


def run_pipeline(symbol: str):
    """
    Runs the full stock analysis pipeline and returns results as a dictionary
    """

    symbol = symbol.upper()

    # 1️⃣ Fetch historical stock data
    fetch_stock_data(symbol)

    # 2️⃣ Preprocess & feature engineering
    preprocess_stock(symbol)

    # 3️⃣ Price prediction
    direction, confidence = predict_price(symbol)

    # 4️⃣ News sentiment analysis
    sentiment = analyze_sentiment(symbol)

    # 5️⃣ Final recommendation
    recommendation = make_recommendation(
        direction=direction,
        confidence=confidence,
        sentiment=sentiment
    )

    # 6️⃣ Return structured result
    return {
        "stock": symbol,
        "direction": direction,
        "confidence": round(confidence, 2),
        "sentiment": sentiment,
        "recommendation": recommendation
    }

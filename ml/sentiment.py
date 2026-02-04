import yfinance as yf
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(symbol):
    news = yf.Ticker(symbol).news
    sia = SentimentIntensityAnalyzer()

    scores = []
    for article in news[:15]:
        title = article.get("title")
        if title:
            scores.append(sia.polarity_scores(title)["compound"])

    if not scores:
        return "NEUTRAL"

    avg = sum(scores) / len(scores)
    if avg > 0.05:
        return "POSITIVE"
    elif avg < -0.05:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

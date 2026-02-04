import pandas as pd
import joblib

PROC_DIR = r"D:\wear\stock-platform\data\processed"
MODEL_DIR = r"D:\wear\stock-platform\models"

FEATURES = [
    "Daily_Return", "MA_5", "MA_10",
    "Volatility_5", "Price_Change", "Volume"
]

def predict_price(symbol):
    df = pd.read_csv(f"{PROC_DIR}/{symbol}_processed.csv")
    model = joblib.load(f"{MODEL_DIR}/{symbol}_rf_model.pkl")

    X = df[FEATURES].iloc[-1:]
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][pred] * 100

    direction = "UP" if pred == 1 else "DOWN"
    return direction, prob

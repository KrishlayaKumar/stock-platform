import pandas as pd
import os

RAW_DIR = r"D:\wear\stock-platform\data\raw"
PROC_DIR = r"D:\wear\stock-platform\data\processed"

def preprocess_stock(symbol):
    os.makedirs(PROC_DIR, exist_ok=True)

    df = pd.read_csv(f"{RAW_DIR}/{symbol}_data.csv")
    df.dropna(inplace=True)

    df["Daily_Return"] = df["Close"].pct_change()
    df["MA_5"] = df["Close"].rolling(5).mean()
    df["MA_10"] = df["Close"].rolling(10).mean()
    df["Volatility_5"] = df["Close"].rolling(5).std()
    df["Price_Change"] = df["Close"] - df["Open"]
    df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

    df.dropna(inplace=True)
    df.to_csv(f"{PROC_DIR}/{symbol}_processed.csv", index=False)

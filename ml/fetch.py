import yfinance as yf
import os

RAW_DIR = r"D:\wear\stock-platform\data\raw"

def fetch_stock_data(symbol):
    os.makedirs(RAW_DIR, exist_ok=True)
    df = yf.Ticker(symbol).history(period="5y")
    df.to_csv(f"{RAW_DIR}/{symbol}_data.csv")

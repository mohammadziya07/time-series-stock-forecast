import yfinance as yf

def load_stock_data(ticker: str, start: str, end: str):
    df = yf.download(ticker, start=start, end=end)
    df = df[['Close']].dropna()
    return df
from ta.momentum import RSIIndicator
from ta.trend import MACD

class FeatureEngineer:
    def build_features(self, df):
        df["Returns"] = df["Close"].pct_change()
        df["MA_20"]   = df["Close"].rolling(20).mean()
        df["MA_50"]   = df["Close"].rolling(50).mean()
        df["RSI"]     = RSIIndicator(df["Close"].squeeze()).rsi()
        df["MACD"]    = MACD(df["Close"].squeeze()).macd()
        df["Target"]  = (df["Close"].shift(-1) > df["Close"]).astype(int)
        df.dropna(inplace=True)
        return df
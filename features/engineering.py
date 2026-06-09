from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands

class FeatureEngineer:
    def build_features(self, df):
        df["Returns"] = df["Close"].pct_change()
        df["MA_20"]   = df["Close"].rolling(20).mean()
        df["MA_50"]   = df["Close"].rolling(50).mean()
        df["RSI"]     = RSIIndicator(df["Close"].squeeze()).rsi()
        df["MACD"]    = MACD(df["Close"].squeeze()).macd()
        # df["Volume_MA20"] = df["Volume"].rolling(20).mean()
        # df["Volume_ratio"] = df["Volume"] / df["Volume_MA20"]

        "tried BollingerBands to see if a stock is overvalued or undervalued"
        # bb = BollingerBands(df["Close"].squeeze())
        # df["BB_high"] = bb.bollinger_hband()
        # df["BB_low"]  = bb.bollinger_lband()
        # df["BB_width"] = bb.bollinger_wband()

        df["MA_cross"] = (df["MA_20"] - df["MA_50"]) / df["MA_50"]
        df["Price_MA20_dist"] = (df["Close"].squeeze() - df["MA_20"]) / df["MA_20"]
        df["day_of_week"] = df.index.dayofweek
        df["RSI_lag1"] = df["RSI"].shift(1)  # RSI d'hier (qui a l'avantage vendeur ou achteteur)
        df["RSI_lag2"] = df["RSI"].shift(2)  # RSI d'avant hier
        df["MACD_lag1"] = df["MACD"].shift(1) #Moyenne mobile d'hier
        df["MACD_lag2"] = df["MACD"].shift(2) #Moyenne mobile d'avant hier 
        # df["Returns_lag1"] = df["Returns"].shift(1)
        # df["Returns_lag2"] = df["Returns"].shift(2)
        # df["Returns_lag3"] = df["Returns"].shift(3)
        
        df["Target"]  = (df["Close"].shift(-1) > df["Close"]).astype(int)
        df.dropna(inplace=True)
        return df
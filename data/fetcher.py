import yfinance as yf

class DataFetcher:
    def __init__(self, ticker: str, period: str = "5y"):
        self.ticker = ticker
        self.period = period

    def fetch(self):
        df = yf.download(self.ticker, period=self.period)
        df.columns = df.columns.get_level_values(0)
        df.dropna(inplace=True)
        return df
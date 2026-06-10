import matplotlib.pyplot as plt
import pandas as pd

class BackTester:
    def __init__(self, df, split_index, predictions):
        self.test_data = df.iloc[split_index:].copy()
        self.test_data["Predictions"] = pd.Series(predictions, index=self.test_data.index)

    
    
    def simulate(self):
        self.test_data["Strategy_returns"] = self.test_data["Predictions"].shift(1) * self.test_data["Returns"]
        self.test_data.fillna(0, inplace=True)
        self.test_data["Cumulative_market"] = (1 + self.test_data["Returns"]).cumprod()
        self.test_data["Cumulative_strategy"] = (1 + self.test_data["Strategy_returns"]).cumprod()

    def show_metrics(self):
        results_strat = (self.test_data["Cumulative_strategy"].iloc[-1] - 1)
        results_market = (self.test_data["Cumulative_market"].iloc[-1] - 1)

        print(f"Market Results : {results_market:.2%}\nStrategy Results : {results_strat:.2%}")

    def plot_results(self):
        plt.figure(figsize=(10, 5))

        plt.plot(self.test_data.index, self.test_data["Cumulative_market"],color="red", label='market')
        plt.plot(self.test_data.index, self.test_data["Cumulative_strategy"],color="green", label ='my strat')

        plt.title("Backtest : Strategy vs Market")
        plt.legend()
        plt.show()

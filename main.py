from data.fetcher import DataFetcher
from features.engineering import FeatureEngineer
from models.trainer import ModelTrainer
from backtest.strategy import BackTester

def main():
    
    fetcher = DataFetcher("AAPL","5y")
    df = fetcher.fetch()

    engineer = FeatureEngineer()
    df = engineer.build_features(df)


    trainer = ModelTrainer()
    X_train, X_test, y_train, y_test = trainer.split_data(df)

    trainer.train(X_train,y_train)

    result = trainer.evaluate(X_test,y_test)

    
    
    split_index = int(len(df)*0.8)
    backtest = BackTester(df, split_index, result) 
    backtest.simulate()
    backtest.show_metrics()
    backtest.plot_results()


if __name__ == "__main__":
    main()
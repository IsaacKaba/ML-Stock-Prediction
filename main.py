from data.fetcher import DataFetcher
from features.engineering import FeatureEngineer
from models.trainer import ModelTrainer

def main():

    fetcher = DataFetcher("AAPL","5y")
    df = fetcher.fetch()

    engineer = FeatureEngineer()
    df = engineer.build_features(df)


    trainer = ModelTrainer()
    X_train, X_test, y_train, y_test = trainer.split_data(df)

    trainer.train(X_train,y_train)

    result = trainer.evaluate(X_test,y_test)



if __name__ == "__main__":
    main()
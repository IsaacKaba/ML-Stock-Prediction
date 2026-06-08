from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ModelTrainer:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.features = ["Returns", "MA_20", "MA_50", "RSI", "MACD"]

    def split_data(self, df):
        X = df[self.features]
        y = df["Target"]

        split = int(len(X) * 0.8)

        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]

        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        print("Modèle entraîné ✅")

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Précision : {accuracy:.2%}")
        return predictions
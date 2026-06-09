from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

class ModelTrainer:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, class_weight="balanced")
        self.features = ["Returns", "MA_20", "MA_50", "RSI", "MACD"]

    def split_data(self, df):
        X = df[self.features]
        y = df["Target"]

        split = int(len(X) * 0.8)

        X_train, X_test, y_train, y_test  = train_test_split(X,y, train_size=0.80)
       

        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        print("Modèle entraîné ✅")

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        cm = confusion_matrix(y_test,predictions)

        print(f"Précision : {accuracy:.2%}")
        print(f"\nMatrice de confusion :")
        print(f"                Prédit 0  Prédit 1")
        print(f"Réel 0 (baisse)   {cm[0][0]}      {cm[0][1]}")
        print(f"Réel 1 (hausse)   {cm[1][0]}      {cm[1][1]}")
        
        return predictions
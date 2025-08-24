# Simple training script to create a demo fraud detection model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import joblib, os

def main():
    X, y = make_classification(
        n_samples=5000,
        n_features=10,
        n_informative=6,
        n_redundant=2,
        weights=[0.9, 0.1],
        random_state=42,
    )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:,1])
    os.makedirs("app/models", exist_ok=True)
    joblib.dump(model, "app/models/model.pkl")
    print(f"Saved model to app/models/model.pkl (AUC={auc:.3f})")

if __name__ == "__main__":
    main()

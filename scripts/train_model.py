import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def train_random_forest():

    # load clean train data
    df = pd.read_csv("output/cleaned_training_data.csv")

    # separate features amd target
    X = df.drop("Survived", axis=1)
    y = df["Survived"]

    print("[INFO] Loaded training data")
    print(f"X shape: {X.shape}")

    # train random forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    print("[INFO] Model Trained")

    return model


if __name__ == "__main__":

    df = pd.read_csv("output/cleaned_training_data.csv")

    X = df.drop("Survived", axis=1)
    y = df["Survived"]

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000), 
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42)
    }

    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
        print(f"[INFO] {name}: {scores.mean():.4f} (std: {scores.std():.4f})")

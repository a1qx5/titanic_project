from train_model import train_random_forest
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

model = train_random_forest()
new_data = pd.DataFrame([{
    "Pclass": 1,
    "Sex": 0,             # 0 = male, 1 = female (based on your encoding)
    "Age": 20,
    "SibSp": 0,
    "Parch": 2,
    "Fare": 500.0,
    "Embarked_Q": 0,
    "Embarked_S": 1
}])

pred = model.predict(new_data)[0]
prob = model.predict_proba(new_data)[0][1]
print(f"Chance of survival: {prob * 100:.2f}%")
if prob >= 0.5:
    print(f"Final Verdict: YOU LIVE (prediction: {pred})")
else:
    print(f"Final Verdict: YOU DIE (prediction: {pred})")

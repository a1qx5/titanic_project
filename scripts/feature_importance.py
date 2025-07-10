from train_model import train_random_forest
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

model = train_random_forest()

importances = model.feature_importances_
features = model.feature_names_in_

feat_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
}).sort_values("Importance", ascending=True)

plt.figure(figsize=(8, 5))
sns.barplot(x="Importance", y="Feature", data=feat_df, palette="viridis")
plt.title("Feature importance (random forest)")
plt.tight_layout()
plt.show()
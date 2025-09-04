import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/raw/diabetes.csv")
X = df.drop("Outcome", axis=1).values
y = df["Outcome"].values

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler().fit(Xtr)
Xtr_s, Xte_s = scaler.transform(Xtr), scaler.transform(Xte)

model = LogisticRegression(max_iter=1000).fit(Xtr_s, ytr)
print("Accuracy:", accuracy_score(yte, model.predict(Xte_s)))

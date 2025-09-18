from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib, pathlib

X, y = load_iris(return_X_y=True, as_frame=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = LogisticRegression(max_iter=1000)
model.fit(X_tr, y_tr)
acc = accuracy_score(y_te, model.predict(X_te))
print(f"test_accuracy={acc:.3f}")

pathlib.Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/iris_logreg.joblib")

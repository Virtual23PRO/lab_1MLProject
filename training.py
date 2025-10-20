from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def load_data():
    iris = load_iris()
    X, y = iris.data, iris.target
    return X, y


def train_model(X, y):
    clf = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000, multi_class="auto")),
        ]
    )
    clf.fit(X, y)
    return clf


def save_model(model, path="models/iris_model.joblib"):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    return path


if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)

    out = save_model(model)
    print(f"Path to model: {out.resolve()}")

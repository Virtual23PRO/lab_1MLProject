from pathlib import Path
import numpy as np
import joblib
from sklearn.datasets import load_iris

DEFAULT_MODEL_PATH = Path("models/iris_model.joblib")


def load_model(path=DEFAULT_MODEL_PATH):
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"There is no model in path: {path}")
    return joblib.load(p)


def predict(model, features):
    X = np.array(features, dtype=float).reshape(1, -1)
    pred_idx = int(model.predict(X)[0])

    target_names = load_iris().target_names
    return str(target_names[pred_idx])


if __name__ == "__main__":
    model = load_model()
    sample = [5.1, 3.5, 1.4, 0.2]
    print("Prediction:", predict(model, sample))

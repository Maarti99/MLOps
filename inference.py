import joblib
import numpy as np


def load_model(filename="model.joblib"):
    return joblib.load(filename)


def predict(model, data: dict) -> str:
    features = np.array(
        [
            [
                data["sepal_length"],
                data["sepal_width"],
                data["petal_length"],
                data["petal_width"],
            ]
        ]
    )

    prediction_idx = model.predict(features)[0]
    classes = ["setosa", "versicolor", "virginica"]
    return classes[prediction_idx]

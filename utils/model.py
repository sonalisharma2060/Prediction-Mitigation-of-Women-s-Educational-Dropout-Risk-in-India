"""
model.py
--------
Trains a Random Forest classifier to predict dropout risk, and
exposes a function to score a single student's details.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from utils.data_processing import load_data, encode_features, TARGET_COLUMN


def train_model(data_path: str = "data/dropout_data.csv"):
    df = load_data(data_path)
    X, encoders = encode_features(df)
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200, max_depth=8, random_state=42, class_weight="balanced"
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "report": classification_report(y_test, y_pred, output_dict=True),
        "feature_importances": dict(zip(X.columns, model.feature_importances_)),
    }

    return model, encoders, metrics


def predict_risk(model, encoded_input) -> float:
    proba = model.predict_proba(encoded_input)[0]
    return float(proba[1])

"""
data_processing.py
-------------------
Loads the student dataset and prepares it for model training:
encodes categorical columns and splits features from the target.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

DATA_PATH = "data/dropout_data.csv"

CATEGORICAL_COLUMNS = [
    "state",
    "area_type",
    "family_income",
    "father_education",
    "mother_education",
    "toilet_facility",
    "internet_access",
    "scholarship",
    "early_marriage_risk",
]

NUMERIC_COLUMNS = [
    "age",
    "siblings_count",
    "distance_to_school_km",
    "attendance_percentage",
    "academic_performance",
]

FEATURE_COLUMNS = CATEGORICAL_COLUMNS + NUMERIC_COLUMNS
TARGET_COLUMN = "dropout"


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def encode_features(df: pd.DataFrame):
    df = df.copy()
    encoders = {}
    for col in CATEGORICAL_COLUMNS:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
    return df[FEATURE_COLUMNS], encoders


def encode_single_input(input_dict: dict, encoders: dict) -> pd.DataFrame:
    row = {}
    for col in CATEGORICAL_COLUMNS:
        le = encoders[col]
        row[col] = le.transform([input_dict[col]])[0]
    for col in NUMERIC_COLUMNS:
        row[col] = input_dict[col]
    return pd.DataFrame([row])[FEATURE_COLUMNS]

"""
app.py
------
Streamlit front-end for the Women's Educational Dropout Risk
Prediction & Mitigation tool.
"""

import streamlit as st
import pandas as pd

from utils.model import train_model, predict_risk
from utils.data_processing import encode_single_input, CATEGORICAL_COLUMNS
from utils.mitigation import get_mitigation_suggestions

st.set_page_config(page_title="Dropout Risk Prediction", page_icon="🎓", layout="wide")


@st.cache_resource
def get_trained_model():
    return train_model()


model, encoders, metrics = get_trained_model()

st.title("🎓 Prediction & Mitigation of Women's Educational Dropout Risk in India")
st.caption("Machine Learning (Random Forest) + Rule-based Mitigation Suggestions")

with st.expander("ℹ️ About this model"):
    st.write(
        f"Trained on a sample dataset of Indian students. "
        f"Test accuracy: **{metrics['accuracy']*100:.1f}%**. "
        "Note: this uses a synthetic/sample dataset for demonstration - "
        "replace `data/dropout_data.csv` with real survey data (e.g. from "
        "UDISE+ or NFHS) for production use."
    )

st.subheader("Enter Student Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 11, 17, 14)
    state = st.selectbox(
        "State",
        ["Uttar Pradesh", "Bihar", "Rajasthan", "Madhya Pradesh", "Maharashtra",
         "West Bengal", "Tamil Nadu", "Karnataka", "Gujarat", "Odisha"],
    )
    area_type = st.selectbox("Area Type", ["Rural", "Urban"])
    family_income = st.selectbox(
        "Family Income", ["Below 1 Lakh", "1-3 Lakh", "3-5 Lakh", "Above 5 Lakh"]
    )
    siblings_count = st.slider("Number of Siblings", 0, 6, 2)

with col2:
    father_education = st.selectbox(
        "Father's Education", ["Illiterate", "Primary", "Secondary", "Graduate"]
    )
    mother_education = st.selectbox(
        "Mother's Education", ["Illiterate", "Primary", "Secondary", "Graduate"]
    )
    distance_to_school_km = st.slider("Distance to School (km)", 0.0, 15.0, 2.0, 0.5)
    toilet_facility = st.selectbox("Toilet Facility at School", ["Yes", "No"])
    internet_access = st.selectbox("Internet Access at Home", ["Yes", "No"])

with col3:
    scholarship = st.selectbox("Receiving Scholarship", ["Yes", "No"])
    early_marriage_risk = st.selectbox("Early Marriage Risk", ["Yes", "No"])
    attendance_percentage = st.slider("Attendance %", 30, 100, 75)
    academic_performance = st.slider("Academic Performance %", 20, 100, 60)

if st.button("Predict Dropout Risk", type="primary", use_container_width=True):
    input_dict = {
        "age": age,
        "state": state,
        "area_type": area_type,
        "family_income": family_income,
        "father_education": father_education,
        "mother_education": mother_education,
        "siblings_count": siblings_count,
        "distance_to_school_km": distance_to_school_km,
        "toilet_facility": toilet_facility,
        "internet_access": internet_access,
        "scholarship": scholarship,
        "early_marriage_risk": early_marriage_risk,
        "attendance_percentage": attendance_percentage,
        "academic_performance": academic_performance,
    }

    encoded = encode_single_input(input_dict, encoders)
    risk = predict_risk(model, encoded)

    st.divider()
    st.subheader("Prediction Result")

    risk_col, chart_col = st.columns([1, 2])

    with risk_col:
        st.metric("Predicted Dropout Risk", f"{risk*100:.1f}%")
        if risk >= 0.6:
            st.error("⚠️ High Risk")
        elif risk >= 0.35:
            st.warning("⚠️ Moderate Risk")
        else:
            st.success("✅ Low Risk")

    with chart_col:
        st.write("**Top factors driving dropout risk (overall model):**")
        importances = pd.Series(metrics["feature_importances"]).sort_values(ascending=True)
        st.bar_chart(importances)

    st.subheader("Suggested Mitigation Actions")
    for suggestion in get_mitigation_suggestions(input_dict):
        st.markdown(f"- {suggestion}")

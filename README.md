# 🎓 Prediction & Mitigation of Women's Educational Dropout Risk in India

A machine learning mini project that predicts a female student's risk
of dropping out of school, and suggests concrete mitigation actions
based on her specific risk factors.

## Features
- **Random Forest classifier** trained on student data (income,
  parental education, distance to school, sanitation, early marriage
  risk, attendance, academic performance, etc.)
- Interactive **Streamlit form** to enter a student's details
- **Predicted dropout risk %** with a Low/Moderate/High risk label
- **Feature importance chart** showing which factors matter most overall
- **Rule-based mitigation suggestions** tailored to that student's
  specific risk factors (e.g. scholarship schemes, sanitation
  advocacy, child-marriage prevention resources)

## Project structure
```
women_dropout_prediction/
├── app.py                      # Streamlit UI
├── requirements.txt
├── runtime.txt                  # pins Python 3.11
├── data/
│   └── dropout_data.csv         # sample dataset (synthetic, 800 students)
├── utils/
│   ├── __init__.py
│   ├── data_processing.py       # loading + encoding
│   ├── model.py                 # training + prediction
│   └── mitigation.py            # rule-based suggestions
└── README.md
```

## About the dataset
`data/dropout_data.csv` is a **synthetic sample dataset** (800
students) generated to reflect known, research-backed dropout risk
factors for girls in India: household income, parental (especially
maternal) education, distance to school, lack of separate school
toilets, early/child marriage risk, siblings count, and academic
performance/attendance. Test accuracy is ~65-70%, which is realistic
for this type of social prediction problem.

**For a stronger project**, replace this file with real data - e.g.
anonymized data from **UDISE+** (Unified District Information System
for Education) or **NFHS** (National Family Health Survey) district-level
indicators - keeping the same column names, or updating
`utils/data_processing.py` to match your real column names.

## Running locally
```
pip install -r requirements.txt
streamlit run app.py
```

## Setup — deploying from a phone (no laptop needed)
1. Create a **GitHub** account and a new **public** repository, e.g.
   `dropout-risk-prediction`.
2. Upload these files to the repo:
   - `app.py`, `requirements.txt`, `runtime.txt`, `README.md` at the root
   - `data/dropout_data.csv` (type the path `data/dropout_data.csv`
     when uploading - GitHub creates the folder automatically)
   - `utils/__init__.py`, `utils/data_processing.py`, `utils/model.py`,
     `utils/mitigation.py` (type the path `utils/filename.py` when
     creating each file)
3. Go to **share.streamlit.io**, sign in with GitHub, tap **Create app**,
   select the repo, branch `main`, main file path `app.py`, then **Deploy**.
4. No API tokens or external accounts needed for this project — it's
   entirely self-contained (unlike an LLM-based chatbot, there's no
   external API call).
5. Once live, fill in the student details form and tap **Predict
   Dropout Risk** to see the result.

## For your report / viva
Be ready to explain:
- **Why Random Forest?** Handles mixed categorical/numeric features
  well, and gives interpretable feature importances (unlike a black-box
  neural net) - useful when the goal is understanding *why*, not just
  predicting.
- **Why label encoding, not one-hot?** Keeps the feature set compact
  for a small dataset; Random Forests handle ordinal-style encoded
  categories reasonably well.
- **Why rule-based mitigation, not just prediction?** The project title
  says "prediction AND mitigation" - the ML model answers "how at-risk?",
  the rule layer answers "what can be done about it?", which a pure
  classifier can't provide on its own.
- **Limitation to acknowledge**: this uses synthetic data for
  demonstration; real deployment would need validated survey data and
  ethical review (this is sensitive, personal data about minors).

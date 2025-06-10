# California Housing Price Prediction with XGBoost and FastAPI

This project focuses on predicting median house prices in California districts using the XGBoost regression model. The full data pipeline includes data preprocessing, model training and tuning, and finally deploying the model with a FastAPI backend.

---

## Project Summary

- **Dataset**: California Housing (from sklearn)
- **Goal**: Predict median house value using demographic and location features
- **ML Model**: XGBoost (with comparison to Ridge, Lasso, Random Forest)
- **Deployment**: FastAPI (local)
- **Explainability**: SHAP analysis to interpret feature contributions

---

## Technologies Used

- Python
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn, XGBoost
- SHAP
- FastAPI
- Joblib
- GitHub Desktop

---

## Files in This Repository

```bash
California_Housing_Price_Prediction_XGBoost/
│
├── main.py                                 # FastAPI backend code
├── xgb_best_model.joblib                   # Trained XGBoost model
├── Predicting_House_Prices_in_California.ipynb  # EDA + modeling
├── README.md                               # This file
├── .gitattributes                          # GitHub settings

---

## Running the FastAPI Server (Locally)

- **Install dependencies**: pip install fastapi uvicorn scikit-learn xgboost joblib

- **Start the FastAPI server**: uvicorn main:app --reload

- **Open the API documentation in your browser**: http://127.0.0.1:8000/docs

---

## Model Performance (on Test Data)

Model	RMSE	R² Score
Ridge	0.77	0.547
Lasso	0.805	0.506
Random Forest	0.608	0.718
XGBoost	0.593	0.732

---

## SHAP for Model Interpretability

SHAP (SHapley Additive exPlanations) was used to identify which features most impacted the predicted house prices. This helps build model transparency, which is crucial in real-world deployments.

---

## About Me

Borun Mukherjee
- PG Certificate in Data Science & AI – IIT Roorkee + Intellipaat
- 6+ Years of SaaS Sales Experience (US Market)
- Transitioning into Data Science & Machine Learning
- LinkedIn ← https://www.linkedin.com/in/borun-m-9bb146148/

---







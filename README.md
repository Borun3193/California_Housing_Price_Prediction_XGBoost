# California Housing Price Prediction

This project predicts housing prices in California using various machine learning models like Linear Regression, Ridge, Lasso, Random Forest, and XGBoost.

## Project Structure

- `Predicting_House_Prices_in_California.ipynb`: Full analysis and model building
- `xgb_best_model.joblib`: Saved XGBoost model used for prediction
- `main.py`: FastAPI backend to serve the trained model as an API

## How to Run the API

1. Install FastAPI and Uvicorn: pip install fastapi uvicorn joblib

2. Run the API: uvicorn main:app --reload

## Model Used
The best model selected using hyperparameter tuning was **XGBoost**, with the following metrics:
- RMSE: ~0.59
- R² Score: ~0.73

## Security
This project is meant for learning and runs locally. No security risk to your personal files.

## Author
Borun Mukherjee


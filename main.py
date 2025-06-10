from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load model
model = joblib.load("xgb_best_model.joblib")

# Define input format
class InputData(BaseModel):
    MedInc_log: float
    AveRooms_log: float
    AveOccup_log: float
    HouseAge: float
    Latitude: float

# Create app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "XGBoost model is ready!"}

@app.post("/predict")
def predict(data: InputData):
    # Convert input to NumPy array
    features = np.array([[data.MedInc_log, data.AveRooms_log, data.AveOccup_log, data.HouseAge, data.Latitude]])
    prediction = model.predict(features)[0]
    return {"prediction": float(prediction)}
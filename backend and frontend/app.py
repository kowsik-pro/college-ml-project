from pathlib import Path
import pickle

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


# loading the model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "best_fraud_model.pkl"

with open(MODEL_PATH, "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
MODEL_NAME = model_data["model_name"]
THRESHOLD = model_data["threshold"]
FEATURES = model_data["features"]


app = FastAPI(title="Vehicle Insurance Fraud Detection API")


app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])


@app.get("/")
def home():
    return {"message": "Vehicle Insurance Fraud Detection API","model": MODEL_NAME}


@app.get("/api/health")
def health():
    return {"status": "healthy","model": MODEL_NAME}


@app.get("/api/features")
def features():
    return {"features": FEATURES}


@app.post("/api/predict")
def predict(data: dict):

 
    missing = [feature for feature in FEATURES if feature not in data]

    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Missing features: {missing}"
        )

    input_data = pd.DataFrame(
        [[data[feature] for feature in FEATURES]],
        columns=FEATURES
    )
    probability = model.predict_proba(input_data)[0][1]

    prediction = int(probability >= THRESHOLD)

    if prediction == 1:
        result = "Potentially Fraudulent"
        risk = "High"
    else:
        result = "Likely Genuine"
        risk = "Low"

    return {
    "prediction": int(prediction),
    "result": result,
    "risk_level": risk,
    "fraud_probability": float(round(float(probability) * 100, 2)),
    "threshold": float(round(float(THRESHOLD) * 100, 2)),
    "model": MODEL_NAME
}
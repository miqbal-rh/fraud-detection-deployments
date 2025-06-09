
from fastapi import FastAPI, Request
import joblib
import numpy as np
import pandas as pd

app = FastAPI()
model = joblib.load("model.joblib")

@app.post("/predict")
async def predict(request: Request):
    input_data = await request.json()
    df = pd.DataFrame([input_data])
    score = model.predict_proba(df)[0][1]
    return {"fraud_probability": float(score)}

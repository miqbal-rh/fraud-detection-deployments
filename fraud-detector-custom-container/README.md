# Fraud Detector — Custom Container Deployment

This directory contains assets for running the fraud detection model inside a custom Docker container using FastAPI and Uvicorn.

## Directory Structure

```
fraud-detector-custom-container/
├── app/
│   ├── app.py                # FastAPI application code
│   ├── model.joblib          # Trained model artifact (XGBoost)
│   └── requirements.txt      # Python dependencies
├── Dockerfile                # Build spec for the container
└── README.md                 # This file
```

## Step-by-Step Instructions

### 1. Build the Docker Image

From inside this directory:

```bash
docker build -t fraud-detector-app .
```

### 2. Run the Container

```bash
docker run -p 8000:8000 fraud-detector-app
```

This will start the FastAPI app on port `8000`.

### 3. Send a Test Request

In a separate terminal, test the prediction endpoint:

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"claimant_age": 45, "claim_amount": 1200.50, "incident_description": "Theft reported after midnight"}'
```

You should receive a JSON response with a predicted fraud probability:

```json
{
  "fraud_probability": 0.8423792123794556
}
```

### Notes

- The `model.joblib` file is expected to be generated via the training script (`train_model.py`) and placed manually into the `app/` directory.
- This container is suitable for local testing or single-node inference scenarios. For scalable, production-grade deployment, refer to the Red Hat Inference Server setups in the other directories.

# Fraud Detector Deployment on OpenShift using Red Hat Inference Server

This directory contains everything needed to deploy a scikit-learn based fraud detection model using the official Red Hat Inference Server on OpenShift.

## 📁 Directory Structure

```
fraud-detector-openshift/
├── models/
│   └── model.joblib         # Place your trained model here
├── fraud-inference.yaml     # KServe InferenceService definition
├── README.md
```

## 🚀 Steps to Deploy

### 1. Push this Repo to GitHub

Make sure this entire directory is pushed to a public or private GitHub repo.

### 2. Create Namespace in OpenShift

```bash
oc new-project fraud-inference
```

### 3. Install RHAIIS Operator from OperatorHub

Search for **Red Hat Inference Server** and install it into the `fraud-inference` namespace.

### 4. Apply the InferenceService Resource

```bash
oc apply -f fraud-inference.yaml
```

If you're using a private Git repo, create a Kubernetes secret and add its key in the YAML.

### 5. Verify Deployment

```bash
oc get inferenceservice fraud-detector -n fraud-inference
```

Check pod logs for troubleshooting:
```bash
oc logs deployment/<fraud-detector-deployment> -n fraud-inference
```

### 6. Send Inference Request

```bash
curl -X POST http://<service-route>/v1/models/fraud-detector:predict   -H "Content-Type: application/json"   -d '{"inputs": [{"name": "predict", "shape": [1], "datatype": "BYTES", "data": [{"claimant_age": 45, "claim_amount": 1200.5, "incident_description": "Theft reported after midnight"}]}]}'
```


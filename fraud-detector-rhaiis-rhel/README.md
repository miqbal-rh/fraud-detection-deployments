# Red Hat Inference Server RHEL Example

This repository is a working directory layout for running a Scikit-learn model using Red Hat Inference Server (RHAIIS) on a RHEL box.

## Steps

1. Place your trained model file named `model.joblib` inside the `models/` directory.
2. Use the following Podman command to run inference:

```bash
podman run -it --rm \
  -v $(pwd)/models:/models \
  -v $(pwd)/inference.yaml:/etc/inference.yaml \
  -p 8080:8080 \
  registry.redhat.io/openshift-serverless-1/inference-service-rhel8:latest \
  --config /etc/inference.yaml
```

## Requirements

- RHEL with Podman installed
- Access to Red Hat container registry
- Red Hat Inference Server image
# MLOps Continuous Delivery Demo

A hands-on implementation of the MLOps Continuous Delivery (CD) tutorial.

## 📋 Overview

This project implements a complete CI/CD pipeline for an ML inference API using:
- Flask for the ML API
- Docker for containerization  
- GitHub Actions for CI/CD
- GHCR for artifact storage
- Semantic Versioning
- GitHub Environments

## 🚀 Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
python app.py
```

## 📊 API Endpoints

### GET /health
```json
{
  "application_version": "1.1.0",
  "model_version": "1.1",
  "git_commit": "abc123f",
  "status": "healthy"
}
```

### POST /predict
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"value": 5}'
```

## 🔄 Release Process

1. Create tag: `git tag v1.1.0 && git push origin v1.1.0`
2. GitHub Actions:
   - Runs tests
   - Builds Docker image
   - Pushes to GHCR
   - Deploys to staging
   - Runs smoke test
3. Manual approval → Production deployment

## 🔙 Rollback

```bash
docker pull ghcr.io/muneebsardar69-cmd/mlops-cd-demo:1.0.0
docker stop mlops-api && docker rm mlops-api
docker run -d --name mlops-api -p 5000:5000 \
  ghcr.io/muneebsardar69-cmd/mlops-cd-demo:1.0.0
curl http://localhost:5000/health
```

## ✅ Deliverables

- [x] Flask ML API with health endpoint
- [x] Unit tests
- [x] Dockerfile
- [x] GitHub Actions workflow with test job
- [x] GHCR integration
- [x] Semantic versioning (v1.0.0, v1.1.0)
- [x] Staging environment (auto-deploy)
- [x] Production environment (manual approval)
- [x] Smoke test validation
- [x] Rollback capability

## 👤 Author

Muneeb Sardar (muneebsardar69-cmd)

**Submitted**: September 10, 2026

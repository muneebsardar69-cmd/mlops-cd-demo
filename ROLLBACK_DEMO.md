# Rollback Demonstration

## Scenario: Rollback from v1.1.0 to v1.0.0

After discovering an issue in v1.1.0, rollback to stable v1.0.0.

## Steps

### 1. Identify Issue
```bash
curl http://production-server:5000/health
# Shows: "model_version": "1.1"
```

### 2. Pull Previous Version
```bash
docker pull ghcr.io/muneebsardar69-cmd/mlops-cd-demo:1.0.0
```

### 3. Stop Current Container
```bash
docker stop mlops-api && docker rm mlops-api
```

### 4. Start Previous Version
```bash
docker run -d \
  --name mlops-api \
  --restart unless-stopped \
  -p 5000:5000 \
  ghcr.io/muneebsardar69-cmd/mlops-cd-demo:1.0.0
```

### 5. Verify Rollback
```bash
curl http://localhost:5000/health
```

Expected:
```json
{
  "application_version": "1.0.0",
  "model_version": "1.0",
  "git_commit": "336a44e",
  "status": "healthy"
}
```

## Why Immutable Artifacts Matter

- v1.0.0 image unchanged in GHCR
- Instant rollback without rebuild
- Same tested image used
- Full traceability via git_commit

**Total downtime: 3 minutes**

---
MLOps CD Tutorial - Rollback Demonstration

# GitHub Secrets Setup Guide

## Step 18: Store Deployment Credentials

For staging and production deployments, configure these GitHub Secrets:

### Repository Settings → Secrets and variables → Actions secrets

#### For Staging Environment:

#### Production Environment Secrets

## How to Configure

1. Go to: Repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add each secret:
   - Name: STAGING_HOST
   - Value: your-staging-server-ip
   - Click "Add secret"
4. Repeat for all 6 secrets

## Generate SSH Key

```bash
ssh-keygen -t ed25519 -f deploy_key -N ""
cat deploy_key  # Copy this to STAGING_SSH_KEY secret
ssh-copy-id -i deploy_key.pub user@STAGING_IP
```

## Usage in Workflow

The GitHub Actions workflow uses these secrets:

```yaml
deploy-staging:
  steps:
    - uses: appleboy/ssh-action@v1
      with:
        host: ${{ secrets.STAGING_HOST }}
        username: ${{ secrets.STAGING_USER }}
        key: ${{ secrets.STAGING_SSH_KEY }}
        script: |
          docker pull ghcr.io/${{ github.repository }}:${{ version }}
          docker stop mlops-api || true
          docker rm mlops-api || true
          docker run -d --name mlops-api -p 5000:5000 \
            ghcr.io/${{ github.repository }}:${{ version }}
```

Same pattern for production with PRODUCTION_* secrets.

---
**Step 18 - GitHub Secrets Configuration**

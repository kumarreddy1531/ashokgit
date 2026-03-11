# FastAPI on Azure App Service (F1) — CI/CD with GitHub Actions

A minimal FastAPI API with a ready-to-use GitHub Actions workflow that deploys to **Azure App Service (Linux, F1 free tier)**.

## What you'll need
- An Azure subscription (Free tier is fine) and a Web App (Linux, Python) created on the **F1 (Free)** plan.
- A GitHub repository (Free plan is fine).

## Files in this repo
- `main.py` – Minimal FastAPI app with one `GET /` endpoint.
- `requirements.txt` – Python dependencies.
- `.github/workflows/deploy-appservice.yml` – CI/CD pipeline to build & deploy on push to `main`.
- `.gitignore`

## One-time Azure setup
1. In the Azure portal, create **Web App** → Runtime: **Python 3.12 / Linux** → Plan: **F1 Free**.
2. Open the Web App → **Get publish profile** (download the `.PublishSettings` XML file).

## One-time GitHub setup
1. Create a new repo and push this code.
2. In the repo, go to **Settings → Secrets and variables → Actions → New repository secret**.
3. Secret name: `AZURE_PUBLISH_PROFILE` → paste the **entire** publish profile XML → Save.

## Configure CI/CD
1. Open `.github/workflows/deploy-appservice.yml`.
2. Replace `"<YOUR_APP_SERVICE_NAME>"` with your actual App Service name (e.g., `fastapi-azure-demo-1234`).

## Deploy
- Push to the `main` branch. The GitHub Actions workflow will build and deploy automatically.
- Browse your app at: `https://<YOUR_APP_SERVICE_NAME>.azurewebsites.net/`

## Local run (optional)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Visit http://127.0.0.1:8000

## Notes
- The F1 (Free) plan is intended for dev/test and has shared compute/quotas; for production, consider a higher tier.
- You can add tests in the workflow before the deploy step.

---
### References
- Quickstart: Deploy a Python (Django/Flask/**FastAPI**) web app to Azure App Service — Microsoft Learn
  https://learn.microsoft.com/en-us/azure/app-service/quickstart-python
- What are Azure App Service plans? (F1/Free tier characteristics) — Microsoft Learn
  https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans
- What is GitHub Actions for Azure? — Microsoft Learn
  https://learn.microsoft.com/en-us/azure/developer/github/github-actions

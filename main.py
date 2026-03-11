from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"status": "ok", "message": "FastAPI CI/CD on Azure App Service (F1) is working fine!"}

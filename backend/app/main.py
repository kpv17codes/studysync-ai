
from fastapi import FastAPI

app = FastAPI(title="StudySync AI")


@app.get("/health")
def health_check():
    return {"status": "ok"}

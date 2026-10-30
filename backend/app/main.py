
from fastapi import FastAPI
from app.tasks import router as tasks_router

app = FastAPI(title="StudySync AI")

app.include_router(tasks_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}

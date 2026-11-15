
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.tasks import router as tasks_router

app = FastAPI(title="StudySync AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(tasks_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}

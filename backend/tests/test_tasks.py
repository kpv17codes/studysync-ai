

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


def override_get_db():
    with Session(engine) as session:
        yield session


@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.pop(get_db, None)
        Base.metadata.drop_all(bind=engine)


def sample_task():
    return {
        "title": "Finish homework",
        "course": "COMP 425",
        "due_date": "2026-11-13",
    }


def test_create_task(client):
    response = client.post("/tasks/", json=sample_task())

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Finish homework"


def test_get_tasks(client):
    client.post("/tasks/", json=sample_task())

    response = client.get("/tasks/")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["course"] == "COMP 425"


def test_create_task_without_title(client):
    task = sample_task()
    task["title"] = ""

    response = client.post("/tasks/", json=task)

    assert response.status_code == 422


def test_create_task_without_course(client):
    task = sample_task()
    task["course"] = ""

    response = client.post("/tasks/", json=task)

    assert response.status_code == 422


def test_create_multiple_tasks(client):
    client.post("/tasks/", json=sample_task())
    client.post("/tasks/", json=sample_task())

    response = client.get("/tasks/")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_create_task_missing_course_field(client):
    task = sample_task()
    del task["course"]

    response = client.post("/tasks/", json=task)

    assert response.status_code == 422


from fastapi.testclient import TestClient
from app.main import app
from app.tasks import tasks

client = TestClient(app)


def setup_function():
    tasks.clear()


def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Finish Networking Homework",
        "course": "COMP 343",
        "due_date": "2026-11-02"
    })

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Finish Networking Homework"


def test_get_tasks():
    client.post("/tasks/", json={
        "title": "Study for Exam",
        "course": "COMP 343",
        "due_date": "2026-11-05"
    })

    response = client.get("/tasks/")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Study for Exam"


def test_create_task_without_title():
    response = client.post("/tasks/", json={
        "title": "",
        "course": "COMP 343",
        "due_date": "2026-11-02"
    })

    assert response.status_code == 422


def test_create_task_without_course():
    response = client.post("/tasks/", json={
        "title": "Finish Homework",
        "course": "",
        "due_date": "2026-11-02"
    })

    assert response.status_code == 422

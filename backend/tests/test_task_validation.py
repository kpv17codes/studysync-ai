import pytest
from pydantic import ValidationError

from app.tasks import TaskCreate


def test_valid_task():
    task = TaskCreate(
        title="Study for Exam",
        course="COMP 343",
        due_date="2026-11-10"
    )
    assert task.title == "Study for Exam"


def test_single_character_title():
    task = TaskCreate(
        title="A",
        course="COMP 343",
        due_date="2026-11-10"
    )
    assert task.title == "A"


def test_empty_title():
    with pytest.raises(ValidationError):
        TaskCreate(
            title="",
            course="COMP 343",
            due_date="2026-11-10"
        )


def test_single_character_course():
    task = TaskCreate(
        title="Homework",
        course="A",
        due_date="2026-11-10"
    )
    assert task.course == "A"


def test_empty_course():
    with pytest.raises(ValidationError):
        TaskCreate(
            title="Homework",
            course="",
            due_date="2026-11-10"
        )


def test_missing_due_date():
    with pytest.raises(ValidationError):
        TaskCreate(
            title="Homework",
            course="COMP 343"
        )
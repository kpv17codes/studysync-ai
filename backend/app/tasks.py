from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import get_db
from .models import TaskDB

router = APIRouter(prefix="/tasks", tags=["Tasks"])


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    course: str = Field(min_length=1)
    due_date: str


class Task(TaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


DbSession = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=Task, status_code=201)
def create_task(task: TaskCreate, db: DbSession):
    new_task = TaskDB(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/", response_model=list[Task])
def get_tasks(db: DbSession):
    return db.scalars(select(TaskDB).order_by(TaskDB.id)).all()

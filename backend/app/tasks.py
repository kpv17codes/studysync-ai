
from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/tasks", tags=["Tasks"])


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    course: str = Field(min_length=1)
    due_date: str


class Task(TaskCreate):
    id: int


tasks = []


@router.post("/", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    new_task = Task(
        id=len(tasks) + 1,
        **task.model_dump()
    )
    tasks.append(new_task)
    return new_task


@router.get("/", response_model=list[Task])
def get_tasks():
    return tasks

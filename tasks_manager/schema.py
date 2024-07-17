from pydantic import BaseModel
from typing import Optional


class SchemaTaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class Task(SchemaTaskAdd):
    id: int


class TaskMessage(BaseModel):
    status:  str = 'OK'
    task_id: int
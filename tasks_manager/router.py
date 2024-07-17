from fastapi import APIRouter, Depends
from typing import Annotated
from tasks_manager.schema import SchemaTaskAdd, Task, TaskMessage
from tasks_manager.repository import TaskRepository


router = APIRouter(
    prefix = '/tasks',
    tags = ['Tasks app'],
)


@router.get('')
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all()
    return tasks


@router.post('')
async def add_task(
    task: Annotated[SchemaTaskAdd, Depends()]
) -> TaskMessage:
    task_id = await TaskRepository.add_one(task)
    return {'message': 'add success', 'task_id': task_id}

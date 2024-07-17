from sqlalchemy import select
from tasks_manager.db import TaskTable, new_session
from tasks_manager.schema import SchemaTaskAdd, Task


class TaskRepository:

    @classmethod
    async def add_one(cls, data: SchemaTaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            task_model = result.scalars().all()
            tasks_schema = [Task.model_validate(task) for task in task_model]
            return tasks_schema

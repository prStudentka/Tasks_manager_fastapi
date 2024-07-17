from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks_manager.db import create_tables, delete_tables
from tasks_manager.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('INFO: BD cleary')
    await create_tables()
    print('INFO: BD ready')
    yield
    print('INFO: Opened connect')


app = FastAPI(lifespan=lifespan)
app.include_router(router)

from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from helpers.config import get_settings
from routes import base, data


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()

    app.mongodb_conn = AsyncIOMotorClient(settings.MONGODB_URI)
    app.db_client = app.mongodb_conn[settings.MONGODB_DATABASE]

    try:
        yield
    finally:
        app.mongodb_conn.close()


app = FastAPI(lifespan=lifespan)

app.include_router(base.base_router)
app.include_router(data.data_router)


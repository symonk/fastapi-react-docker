import logging

from app.core.config import DATABASE_URL
from databases import Database
from fastapi import FastAPI

logger = logging.getLogger(__name__)


async def connect_to_database(app: FastAPI) -> None:
    database = Database(DATABASE_URL, min_size=2, max_size=10)
    try:
        await database.connect()
        app.state._database = database
    except Exception:
        logger.warning("Database error establishing connection", exc_info=True)


async def close_database_connection(app: FastAPI) -> None:
    try:
        await app.state._database.disconnect()
    except Exception:
        logger.warning("Database error closing connection", exc_info=True)

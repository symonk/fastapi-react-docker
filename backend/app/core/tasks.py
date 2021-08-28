from typing import Any
from typing import Callable
from typing import Coroutine

from app.database.tasks import close_database_connection
from app.database.tasks import connect_to_database
from fastapi import FastAPI


def create_start_app_handler(app: FastAPI) -> Callable[[], Coroutine[Any, Any, None]]:
    async def start_app() -> None:
        await connect_to_database(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable[[], Coroutine[Any, Any, None]]:
    async def stop_app() -> None:
        await close_database_connection(app)

    return stop_app

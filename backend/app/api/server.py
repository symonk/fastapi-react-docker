import logging

from app.core import config
from app.core import tasks
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routing import router as api_router

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def configure_app() -> FastAPI:
    app = FastAPI(title="Bootstrapped", version=config.VERSION)
    app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )
    app.include_router(api_router, prefix="/api")
    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))
    return app


app = configure_app()

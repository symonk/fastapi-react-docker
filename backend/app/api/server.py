from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routing import router as api_router


def configure_app() -> FastAPI:
    app = FastAPI(title="Bootstrapped", version="0.0.1")
    app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )
    app.include_router(api_router, prefix="/api")
    return app


app = configure_app()

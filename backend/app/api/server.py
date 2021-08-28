from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def configure_app() -> FastAPI:
    app = FastAPI(title="Bootstrapped", version="0.0.1")
    app.add_middleware(CORSMiddleware,
                       allow_origins=['*'],
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=['*']
                       )
    return app


app = configure_app()

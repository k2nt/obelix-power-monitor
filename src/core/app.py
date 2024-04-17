import uvicorn
from fastapi import FastAPI

from src.api.router import router
from dependency_injector.wiring import Provide, inject


def asgi_app_factory() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI(app_name="obelix-power-monitor")
    app.include_router(router)
    return app


def start():
    """Start FastAPI application."""
    uvicorn.run(
        app=asgi_app_factory(),
        host='localhost',
        port=3000,
        # log_config=config_dict['logging'],
        # log_level=logging.DEBUG,
        )

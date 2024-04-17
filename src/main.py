import uvicorn
from fastapi import FastAPI
from dependency_injector.wiring import Provide, inject

from src.core import di
from src.api.router import router
from src.domain.logging import LogLevel


def asgi_app_factory() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI(app_name="obelix-power-monitor")
    app.include_router(router)
    return app


@inject
def start(
        config_dict = Provide[di.App.config_dict]
):
    """Start FastAPI application."""    
    uvicorn.run(
        app=asgi_app_factory(),
        host=config_dict["HOST"],
        port=config_dict["PORT"],
        log_level=LogLevel.DEBUG,
        )
    
    
def start_app():
    di.build()
    start()


if __name__ == '__main__':
    start_app()
    
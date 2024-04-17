import uvicorn
from fastapi import FastAPI
from dependency_injector.wiring import Provide, inject

from .infra import di
from .infra.logging import logger_store
from .infra.logging import LogLevel
from .infra.logging.formatter import DEFAULT_LOGGING_CONFIG
from .api.router import router


def build():
    # loggers
    _ = logger_store.new_logger(name='pm', level=LogLevel.DEBUG)
    
    # initialize dependency injection
    di.build(["src.main"])
    

def asgi_app_factory() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI(app_name="obelix-power-monitor")
    app.include_router(router)
    return app


@inject
def start(
        app: FastAPI,
        config_dict = Provide[di.App.config_dict]
):
    """Start FastAPI application."""    
    uvicorn.run(
        app=app,
        host=config_dict["HOST"],
        port=config_dict["PORT"],
        log_config=DEFAULT_LOGGING_CONFIG,
        log_level=LogLevel.DEBUG,
        )
    
    
def start_app():
    build()
    start(asgi_app_factory())


if __name__ == '__main__':
    start_app()
    
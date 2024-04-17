import uvicorn
from fastapi import FastAPI

from src.api.router import router


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


def start_app():
    start()


if __name__ == '__main__':
    start_app()
    
from fastapi import FastAPI

from miles_app.api.health import router as health_router
from miles_app.api.programs import router as programs_router
from miles_app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name)
    app.include_router(health_router)
    app.include_router(programs_router)
    return app


app = create_app()

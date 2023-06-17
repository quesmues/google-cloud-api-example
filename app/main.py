from fastapi import FastAPI

from app.api.v1.routes import router as v1_router
from app.config.settings import settings

app = FastAPI(debug=settings.debug, title=settings.app_name, version=settings.version)

app.include_router(v1_router)
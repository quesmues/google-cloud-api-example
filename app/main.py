from fastapi import FastAPI

from app.api.v1.fipe.routes import router as v1_fipe_router
from app.api.v1.tasks.routes import router as v1_tasks_router
from app.config.settings import settings

app = FastAPI(debug=settings.debug, title=settings.app_name, version=settings.version)

app.include_router(v1_fipe_router)
app.include_router(v1_tasks_router)
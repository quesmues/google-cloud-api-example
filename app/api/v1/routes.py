from fastapi import APIRouter

from app.api.v1.models import HelloWorldModel
from app.config.settings import settings

router = APIRouter(prefix=settings.prefix_v1)


@router.get("/hello-wold", response_model=HelloWorldModel)
async def api_hello_world():
    return HelloWorldModel(details="Hello World")

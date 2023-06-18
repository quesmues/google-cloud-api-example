from fastapi import APIRouter

from app.api.v1.fipe.models import Marca
from app.config.settings import settings

router = APIRouter(prefix=settings.prefix_v1)


@router.post("/task/get-modelos", status_code=200)
async def task_modelos_veiculo(marca: Marca):
     return {}

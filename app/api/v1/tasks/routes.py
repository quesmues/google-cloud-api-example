from typing import List

from fastapi import APIRouter, status
from pydantic import UUID4

from app.api.v1.shared_models import Marca
from app.api.v1.tasks.models import Veiculo
from app.api.v1.tasks.views import (edit_veiculo_view, get_veiculos_view,
                                    task_set_veiculos_view)
from app.config.settings import settings

router = APIRouter(tags=["API 2"], prefix=f"{settings.prefix_v1}/api2")


@router.post("/task/set-veiculos", status_code=status.HTTP_200_OK)
async def task_set_veiculos(marca: Marca):
     return await task_set_veiculos_view(marca)


@router.get("/veiculos", status_code=status.HTTP_200_OK, response_model=List[Veiculo])
async def get_modelos():
     return await get_veiculos_view()


@router.patch("/veiculos/edit")
async def edit_veiculo(veiculo: Veiculo):
    return await edit_veiculo_view(veiculo)

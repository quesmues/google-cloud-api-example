from typing import List

from fastapi import APIRouter, status

from app.api.v1.fipe.models import Marca, TipoVeiculo
from app.api.v1.fipe.views import (carga_inicial_view, enviar_marca_fila_view,
                                   enviar_marcas_fila_view, get_marcas_view)
from app.config.settings import settings
from app.core.messages import Message

router = APIRouter(prefix=settings.prefix_v1)


@router.get("/carga-inicial/{veiculo}", response_model=Message, status_code=status.HTTP_201_CREATED)
async def carga_inicial(veiculo: TipoVeiculo):
    return await carga_inicial_view(veiculo)


@router.get("/{veiculo}/marcas", response_model=List[Marca], status_code=status.HTTP_200_OK)
async def get_marcas(veiculo: TipoVeiculo):
    return await get_marcas_view(veiculo)


@router.post("/enviar/{veiculo}/marcas", response_model=Message, status_code=status.HTTP_200_OK, 
            description="Envia todas as marcas do tipo de veiculo para processamento da fila")
async def enviar_marcas_fila(veiculo: TipoVeiculo):
    return await enviar_marcas_fila_view(veiculo)


@router.post("/enviar/marca", response_model=Message, status_code=status.HTTP_200_OK,  
            description="Envia apenas a marca informada para processamento da fila")
async def enviar_marca_fila(marca: Marca):
    return await enviar_marca_fila_view(marca)
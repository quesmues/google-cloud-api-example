from typing import List

from fastapi import APIRouter, status

from app.api.v1.fipe.models import Marca
from app.api.v1.fipe.views import (carga_inicial_view, enviar_marca_fila_view,
                                   enviar_marcas_fila_view, get_marcas_view)
from app.config.settings import settings
from app.core.messages import Message

router = APIRouter(prefix=settings.prefix_v1)


@router.get("/carga-inicial", response_model=Message, status_code=status.HTTP_201_CREATED)
async def carga_inicial():
    return await carga_inicial_view()

@router.get("/marcas", response_model=List[Marca], status_code=status.HTTP_200_OK)
async def get_marcas():
    return await get_marcas_view()

@router.post("/enviar/marcas", response_model=Message, status_code=status.HTTP_200_OK, 
            description="Envia todas as marcas para processamento da fila")
async def enviar_marcas_fila():
    return await enviar_marcas_fila_view()

@router.post("/enviar/marca", response_model=Message, status_code=status.HTTP_200_OK,  
            description="Envia apenas a marca informada para processamento da fila")
async def enviar_marca_fila(marca: Marca):
    return await enviar_marca_fila_view(marca)
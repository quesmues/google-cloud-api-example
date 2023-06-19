
import asyncio
from typing import List

from fastapi import HTTPException, status

from app.api.v1.fipe.models import Marca, TaskRequest, TipoVeiculo
from app.api.v1.fipe.services import (db_add_marcas, db_get_marcas,
                                      db_marcas_exist, get_marcas)
from app.config.settings import settings
from app.core.google.tasks import create_http_task
from app.core.messages import (CARGA_INICIAL_REALIZADA, CARGA_INICIAL_SUCESSO,
                               CRIAR_TASK_SUCESSO, CRIAR_TASKS_SUCESSO,
                               Message)


async def carga_inicial_view(veiculo: TipoVeiculo) -> List[Marca]:
    # Checa se existe no firestore
    marcas = await db_marcas_exist(veiculo)
    # Caso não exista coleta as marcas da API da FIPE
    if not marcas:
      marcas = await get_marcas(veiculo)
      # Salva no firestore
      await db_add_marcas(marcas, veiculo)
      return Message(detail=CARGA_INICIAL_SUCESSO)
    raise HTTPException(status_code=status.HTTP_200_OK, detail=CARGA_INICIAL_REALIZADA)


async def get_marcas_view(veiculo: TipoVeiculo) -> List[Marca]:
    # Pega as marcas do Firestore
    marcas = await db_get_marcas(veiculo)
    return sorted(marcas, key=lambda x: int(x.codigo))


async def enviar_marcas_fila_view(veiculo: TipoVeiculo) -> List[Marca]:
    # Pega as marcas do Firestore
    marcas = await db_get_marcas(veiculo)
    # Enviar as marcas, marca por marca para a API de processamento dos modelos
    tasks = [create_http_task(relative_uri=f"{settings.prefix_v1}/task/get-modelos",
                              payload=TaskRequest(marca=marca)) 
             for marca in marcas]
    await asyncio.gather(*tasks)
    return Message(detail=CRIAR_TASKS_SUCESSO.format(veiculo=veiculo.value))
  

async def enviar_marca_fila_view(marca: Marca) -> List[Marca]:
    # Enviar a marca a API de processamento dos modelos
    await create_http_task(relative_uri=f"{settings.prefix_v1}/task/get-modelos",
                           payload=TaskRequest(marca=marca))
    return Message(detail=CRIAR_TASK_SUCESSO.format(marca=marca.dict()))
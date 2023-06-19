
import asyncio
from typing import List

from fastapi import HTTPException, status

from app.api.v1.fipe.services import (db_add_marcas, db_get_marcas,
                                      db_get_veiculos, db_marcas_exist,
                                      get_marcas)
from app.api.v1.shared_models import Marca
from app.config.settings import settings
from app.core.google.tasks import create_http_task
from app.core.messages import (CARGA_INICIAL_REALIZADA, CARGA_INICIAL_SUCESSO,
                               CRIAR_TASK_SUCESSO, CRIAR_TASKS_SUCESSO,
                               Message)


async def carga_inicial_view() -> Message:
    # Checa se existe no firestore
    marcas = await db_marcas_exist()
    # Caso não exista coleta as marcas da API da FIPE
    if not marcas:
      marcas = await get_marcas()
      # Salva no firestore
      await db_add_marcas(marcas)
      return Message(detail=CARGA_INICIAL_SUCESSO)
    raise HTTPException(status_code=status.HTTP_200_OK, detail=CARGA_INICIAL_REALIZADA)


async def get_marcas_view() -> List[Marca]:
    # Pega as marcas do Firestore
    marcas = await db_get_marcas()
    return sorted(marcas, key=lambda x: int(x.codigo))


async def get_veiculos_view(marca: Marca) -> List[Marca]:
    # Pega as marcas do Firestore
    marcas = await db_get_veiculos(marca)
    return sorted(marcas, key=lambda x: int(x.codigo))


async def enviar_marcas_fila_view() -> Message:
    # Pega as marcas do Firestore
    marcas = await db_get_marcas()
    # Enviar as marcas, marca por marca para a API de processamento dos modelos
    tasks = [create_http_task(relative_uri=f"{settings.prefix_v1}/api2/task/set-veiculos",
                              payload=marca) 
             for marca in marcas]
    await asyncio.gather(*tasks)
    return Message(detail=CRIAR_TASKS_SUCESSO)
  

async def enviar_marca_fila_view(marca: Marca) -> Message:
    # Enviar a marca a API de processamento dos modelos
    await create_http_task(relative_uri=f"{settings.prefix_v1}/api2/task/set-veiculos",
                           payload=marca)
    return Message(detail=CRIAR_TASK_SUCESSO.format(marca=marca.dict()))
import uuid
from typing import List

from fastapi import HTTPException, status

from app.api.v1.tasks.models import Marca, Modelo, Veiculo
from app.api.v1.tasks.services import (db_add_veiculos, db_edit_veiculo,
                                       db_get_marca, db_get_veiculos,
                                       get_modelos)
from app.core.messages import Message


async def mount_veiculos(marca: Marca, modelos: List[Modelo]) -> List[Veiculo]:
  return [
    Veiculo(codigo=uuid.uuid4(), marca=marca.dict(), modelo=modelo.dict()) for modelo in modelos
  ]


async def task_set_veiculos_view(marca: Marca) -> Message:
    # Checa se existe no firestore
    marca = await db_get_marca(marca)
    if marca:
      # Get modelos marca
      modelos = await get_modelos(marca)
      # Salva no firestore
      await db_add_veiculos(await mount_veiculos(marca, modelos))
      return Message()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def get_veiculos_view() -> List[Veiculo]:
  return await db_get_veiculos()


async def edit_veiculo_view(veiculo: Veiculo) -> Message:
  await db_edit_veiculo(veiculo)
  return Message()

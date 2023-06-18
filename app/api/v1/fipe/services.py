import asyncio
from typing import List

from app.api.v1.fipe.models import Marca, TipoVeiculo
from app.config.settings import settings
from app.core.google.firestore import client
from app.core.services import get_data


async def get_marcas(veiculo: TipoVeiculo) -> List:
  marcas = await get_data(f"{settings.fipe_url}/{veiculo.value}/marcas")
  return [Marca(**marca) for marca in marcas]


async def db_marcas_exist(veiculo: TipoVeiculo) -> bool:
  marcas = client.collection(veiculo.value).limit(1).stream()
  marcas = [i.to_dict() async for i in marcas]
  return len(marcas) > 0 


async def db_get_marcas(veiculo: TipoVeiculo) -> List:
  marcas = client.collection(veiculo.value).stream()
  marcas = [i.to_dict() async for i in marcas]
  return [Marca(**marca) for marca in marcas]


async def db_add_marcas(marcas: List[Marca], veiculo: TipoVeiculo) -> List:
  tasks = [client.collection(veiculo.value).add(marca.dict()) for marca in marcas]
  await asyncio.gather(*tasks)
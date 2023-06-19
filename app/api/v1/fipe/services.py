import asyncio
from typing import List

from google.cloud.firestore_v1.base_query import And, FieldFilter

from app.api.v1.fipe.models import Veiculo
from app.api.v1.shared_models import Marca
from app.config.settings import settings
from app.core.google.firestore import client
from app.core.services import get_data


async def get_marcas() -> List:
  marcas = await get_data(f"{settings.fipe_url}/carros/marcas")
  return [Marca(**marca) for marca in marcas]


async def db_marcas_exist() -> bool:
  marcas = client.collection("marcas").limit(1).stream()
  marcas = [i.to_dict() async for i in marcas]
  return len(marcas) > 0 


async def db_get_marcas() -> List:
  marcas = client.collection("marcas").stream()
  marcas = [i.to_dict() async for i in marcas]
  return [Marca(**marca) for marca in marcas]


async def db_get_veiculos(codigo: str) -> List:
  veiculos = client.collection("veiculos"). \
    where("marca.codigo", "==", str(codigo)). \
    stream()
  veiculos = [i.to_dict() async for i in veiculos]
  return [Veiculo(**veiculo) for veiculo in veiculos]


async def db_add_marcas(marcas: List[Marca]) -> None:
  tasks = [client.collection("marcas").add(marca.dict()) for marca in marcas]
  await asyncio.gather(*tasks)
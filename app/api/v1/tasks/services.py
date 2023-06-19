import asyncio
import json
from typing import List

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from google.cloud.firestore_v1.base_query import And, FieldFilter
from google.cloud.firestore_v1.document import DocumentSnapshot
from pydantic import UUID4

from app.api.v1.tasks.models import Marca, Modelo, Veiculo
from app.core.google.firestore import client


async def get_modelos(marca: Marca) -> List:
#   modelos = await get_data(f"{settings.fipe_url}/carros/marcas/{marca.codigo}/modelos")
#   return [Modelo(**modelo) for modelo in modelos["modelos"]]
  return [Modelo(codigo="1", nome="teste")]


async def db_add_veiculos(veiculos: List[Veiculo]):
  tasks = [client.collection("veiculos").add(jsonable_encoder(veiculo)) for veiculo in veiculos]
  await asyncio.gather(*tasks)


async def db_edit_veiculo(veiculo: Veiculo):
  veiculo_d = veiculo.dict()
  id: UUID4 = veiculo_d.pop('codigo')
  veiculos = client.collection("veiculos"). \
    where("codigo", "==", str(id)). \
    stream()
  try:
    db_veiculo: DocumentSnapshot = [i async for i in veiculos][0]
  except IndexError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  veiculo = jsonable_encoder(veiculo, exclude_unset=True)
  await client.collection("veiculos").document(db_veiculo.id).update(veiculo)


async def db_get_veiculos() -> List[Veiculo]:
  veiculos = client.collection("veiculos").stream()
  return [Veiculo(**i.to_dict()) async for i in veiculos]


async def db_get_marca(marca: Marca) -> Marca:
  filter_codigo = FieldFilter("codigo", "==", str(marca.codigo))
  filter_nome = FieldFilter("nome", "==", str(marca.nome))
  and_filter = And(filters=[filter_codigo, filter_nome])
  marcas = client.collection("marcas"). \
    where(filter=and_filter). \
    stream()
  marcas = [i.to_dict() async for i in marcas]
  return Marca(**marcas[0])
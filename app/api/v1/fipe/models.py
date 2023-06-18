from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class TipoVeiculo(str, Enum):
    carros = 'carros'
    motos = 'motos'
    caminhoes = 'caminhoes'
        

class Marca(BaseModel):
    codigo: str = Field(title="Código da Marca", max_length=100)
    nome: str = Field(title="Nome da Marca", max_length=100)
    

class RequestForm(BaseModel):
    veiculo: TipoVeiculo
    

class TaskRequest(BaseModel):
    marca: Marca
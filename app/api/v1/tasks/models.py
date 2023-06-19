from typing import Optional

from pydantic import UUID4, BaseModel, Field


class Marca(BaseModel):
    codigo: str = Field(title="Código da Marca", max_length=100)
    nome: str = Field(title="Nome da Marca", max_length=100)


class Modelo(BaseModel):
    codigo: str = Field(title="Código do Modelo", max_length=100)
    nome: str = Field(title="Nome do Modelo", max_length=100)


class Veiculo(BaseModel):
    codigo: UUID4
    marca: Optional[Marca]
    modelo: Optional[Modelo]
    observacoes: str | None = Field(default=None, title="Observações do Veiculo", max_length=500)
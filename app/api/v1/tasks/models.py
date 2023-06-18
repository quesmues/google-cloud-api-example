from pydantic import BaseModel, Field


class Modelo(BaseModel):
    codigo: str = Field(title="Código do Modelo", max_length=100)
    marca: str = Field(title="Marca do Modelo", max_length=100)
    modelo: str = Field(title="Nome do Modelo", max_length=100)
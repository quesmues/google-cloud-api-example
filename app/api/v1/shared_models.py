from pydantic import BaseModel, Field


class Marca(BaseModel):
    codigo: str = Field(title="Código da Marca", max_length=100)
    nome: str = Field(title="Nome da Marca", max_length=100)
    
    
class Modelo(BaseModel):
    codigo: str = Field(title="Código do Modelo", max_length=100)
    nome: str = Field(title="Nome do Modelo", max_length=100)
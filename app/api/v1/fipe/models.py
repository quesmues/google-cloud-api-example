from pydantic import UUID4, BaseModel, Field

from app.api.v1.shared_models import Marca, Modelo


class Veiculo(BaseModel):
    codigo: UUID4
    modelo: Modelo
    observacoes: str | None = Field(default=None, title="Observações do Veiculo", max_length=500)

class MarcaForm(BaseModel):
    marca: Marca
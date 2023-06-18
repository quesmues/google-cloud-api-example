
from pydantic import BaseModel


class Message(BaseModel):  
  detail: str
      

CARGA_INICIAL_SUCESSO = "Carga inicial realizada com sucesso"
CARGA_INICIAL_REALIZADA = "Carga inicial já realizada para este veiculo"
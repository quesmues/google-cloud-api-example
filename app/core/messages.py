
from pydantic import BaseModel


class Message(BaseModel):  
  detail: str = "Ok"
      

CARGA_INICIAL_SUCESSO = "Carga inicial realizada com sucesso"
CARGA_INICIAL_REALIZADA = "Carga inicial já realizada"

CRIAR_TASKS_SUCESSO = "Marcas foram enviadas com sucesso"

CRIAR_TASK_SUCESSO = "Marca <{marca}> foi enviada com sucesso"
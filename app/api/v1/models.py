from pydantic import BaseModel


class HelloWorldModel(BaseModel):
    detail: str
from pydantic import BaseModel


class HelloWorldModel(BaseModel):
    details: str
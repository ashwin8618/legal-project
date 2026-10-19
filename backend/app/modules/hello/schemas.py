from pydantic import BaseModel, ConfigDict


class HelloResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    message: str

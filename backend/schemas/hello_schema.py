
from pydantic import BaseModel


class HelloSchema(BaseModel):
    message: str
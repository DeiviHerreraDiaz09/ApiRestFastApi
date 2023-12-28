from pydantic import BaseModel

class User(BaseModel):
    id: str | None = None
    name: str
    lastname: str
    age: int
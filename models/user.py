from pydantic import BaseModel, constr

class User(BaseModel):
    id: str | None = None
    name: constr(min_length=1, max_length=50)
    lastname: constr(min_length=1, max_length=50)
    age: int
    password: str
from pydantic import BaseModel
from models.user import User


class Producto(BaseModel):
    id: str | None = None
    name: str
    descripcion: str

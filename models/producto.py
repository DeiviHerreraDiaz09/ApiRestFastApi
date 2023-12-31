from pydantic import BaseModel

from fastapi import  File


class Producto(BaseModel):
    id: str | None = None
    name: str
    descripcion: str
    jefe: str
    img: str 

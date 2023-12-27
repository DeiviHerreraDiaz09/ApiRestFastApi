from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Entidad de usuarios

   
router = APIRouter(prefix="/products", tags=["products"],responses={404: {"message":"No encontrado"}} )

# PETICIONES

# Traer todos los usuarios

@router.get("/prueba")
async def prueba():
    return "Esto es una prueba"
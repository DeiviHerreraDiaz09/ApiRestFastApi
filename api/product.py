from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Entidad de usuarios

   
router = APIRouter(prefix="/products")

# PETICIONES

# Traer todos los usuarios

@router.get("/prueba")
async def prueba():
    return "Esto es una prueba"
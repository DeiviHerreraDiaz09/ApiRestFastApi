from fastapi import APIRouter, HTTPException,Depends
from models.producto import Producto
from db.client import db_client
from services.producto import *

router = APIRouter(prefix="/products", tags=["products"], responses={404:{"message": "No encontrado"}})

exception = HTTPException(status_code=400, detail="ERROR")


@router.get("/list")
async def products():
    lista = listar_productos()
    if not lista:
        raise HTTPException(status_code=400, detail="Identificador incorrecto")
    return lista

@router.post("/add")
async def addProducto(producto: Producto):
    nuevo_producto = guardar_producto(producto)
    return nuevo_producto

@router.get("/{id}")
async def productoId(id: str):
    producto = listar_producto(id)
    return producto

@router.put("/update/{id}")
async def updateUser(id: str, producto: Producto):
    resultado_actualizacion = actualizar_producto(id, producto)
    if resultado_actualizacion:
        return {"success": resultado_actualizacion.modified_count > 0}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

from fastapi import APIRouter, HTTPException
from models.user import User
from db.client import db_client
from services.user import *

router = APIRouter(prefix="/users", tags=["users"], responses={404:{"message": "No encontrado"}})

exception = HTTPException(status_code=400, detail="ERROR")

@router.get("/list")
async def users():
    lista = listar_usuarios()
    return lista

@router.get("/{id}")
async def userid(id: str):
    usuario = listar_usuario(id) 
    if usuario:     
        return "Usuario encontrado: ",usuario
    else:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

@router.post("/add", status_code=201)
async def addUser(user: User):
    nuevo_usuario = guardar_user(user)
    return nuevo_usuario

@router.put("/update")
async def updateUser(user: User):
    usuario = actualizar_usuario(user)
    if usuario:
        return "Usuario actualizado", usuario
    else:
        return exception

@router.delete("/delete")
async def deleteUser(id: str):    
    usuario = borrar_usuario(id)
    if usuario: 
        return {"Success":"Borrado exitosamente"}
    else: 
        return {"Error":"No se pudo borrar el usuario"}





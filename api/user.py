from fastapi import APIRouter, HTTPException
from models.user import User
from db.client import db_client
from services.user import *

router = APIRouter(prefix="/users", tags=["users"], responses={404:{"message": "No encontrado"}})

# @router.get("/{id}")
# async def usersid(id: str):
#     users = filter(lambda user: user.id == id, users_list)
#     try:
#         return list(users)[0]
#     except:
#         raise HTTPException(status_code=400, detail="Usuario no existente")
    

@router.post("/add", status_code=201)
async def addUser(user: User):
    nuevo_usuario = guardar_user(user)
    return nuevo_usuario

@router.get("/list")
async def users():
    lista = listar_usuarios()
    return lista

# @router.put("/update")
# async def updateUser(user: User):
    
#     found = False

#     for index, saved_user in enumerate(users_list):
#         if saved_user.id == user.id:
#             users_list[index] = user
#             found = True
#             return {"response", "Usuario actualizado correctamente"}
#     if not found:
#         raise HTTPException(status_code=404, detail="Usuario no actualizado")


    
# @router.delete("/delete/{id}")
# async def deleteUser(id: int):
#     for index,delete_user in enumerate(users_list):
#         if delete_user.id == id:
#             users_list.pop(index)
#             return "Usuario borrado"
#         else: 
#             raise HTTPException(status_code=404, detail="Usuario no borrado")





from models.user import User
from fastapi import Depends
from db.client import db_client
from pymongo import ReturnDocument 
from bson.objectid import ObjectId
from api.user import User
import bcrypt

# Traer la estructura de la siguiente manera:

def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "name": user["name"],
            "lastname": user["lastname"],
            "age": user["age"],
            "password": user["password"]}

# CRUD

def guardar_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]  

    bcyp = bcrypt.hashpw(user_dict["password"].encode("utf-8"), bcrypt.gensalt())

    user_dict["password"] = bcyp.decode("utf-8")

    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({"_id": id}))
    return User(**new_user)

def listar_usuarios():
    users = db_client.users.find().sort("age",1)
    user_list = [user_schema(user) for user in users]
    return user_list

def listar_usuario(id: str):
    print(id)
    user = db_client.users.find_one({"_id":ObjectId(id)})
    print(user)
    if user:
        return user_schema(user)
    else:
        return None

def actualizar_usuario(user: User):    
    usuario_dict = dict(user)
    usuario_id = usuario_dict["id"]
    if usuario_id:
            actualizar = db_client.users.find_one_and_update({"_id":ObjectId(user.id)},{"$set": usuario_dict}, return_document=ReturnDocument.AFTER)
            print(actualizar.get("id"))
            if actualizar:
                 return User(**user_schema(actualizar))
            else: 
                 return None
    else:
        return None

def borrar_usuario(id: str):
    usuario_borrar = db_client.users.delete_one({"_id": ObjectId(id)})
    if usuario_borrar:
        return "Usuario borrado con exito", usuario_borrar
    else:
        return None

# Login 
    
        
def buscarUsuario(name: str):
    usuario_nombre = db_client.users.find_one({"name":name})
    if usuario_nombre:
        return usuario_nombre
    else:
        return "No se encontró el usuario"







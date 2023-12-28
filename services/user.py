from models.user import User
from db.client import db_client

# Traer la estructura de la siguiente manera:

def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "name": user["name"],
            "lastname": user["lastname"],
            "age": user["age"]}


def guardar_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]  
    id = db_client.local.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.local.users.find_one({"_id": id}))
    return User(**new_user)

def listar_usuarios():
    users = db_client.local.users.find()
    user_list = [user_schema(user) for user in users]
    return user_list

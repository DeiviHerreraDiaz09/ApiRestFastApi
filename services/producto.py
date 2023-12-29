from models.producto import Producto
from fastapi import Depends
from db.client import db_client
from pymongo import ReturnDocument 
from bson.objectid import ObjectId

# Traer la estructura de la siguiente manera:

def producto_schema(producto) -> dict:
    return {"id": str(producto["_id"]),
            "name": producto["name"],
            "descripcion": producto["descripcion"]}

# CRUD 

def guardar_producto(producto: Producto):
    producto_dict = dict(producto)
    del producto_dict["id"]

    id = db_client.productos.insert_one(producto_dict).inserted_id
    new_producto = db_client.productos.find_one({"_id": id})

    return producto_schema(new_producto)

def listar_productos():
    productos = db_client.productos.find()
    lista_productos = [producto_schema(producto) for producto in productos]
    return lista_productos


def listar_producto(id: str):
    producto = db_client.productos.find_one({"_id": ObjectId(id)})
    if producto: 
        return producto_schema(producto)
    else: 
        return None
    

def actualizar_producto(id: str, producto: Producto):
    producto_db = db_client.productos.find_one({"_id": ObjectId(id)})
    if producto_db:
        producto_dict = producto.dict()
        if "id" in producto_dict:
            del producto_dict["id"]
        actualizar = db_client.productos.update_one({"_id": ObjectId(id)}, {"$set": producto_dict})
        return actualizar
    else: 
        return None

    

    
    

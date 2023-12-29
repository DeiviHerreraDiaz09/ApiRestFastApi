from fastapi import APIRouter, HTTPException,Depends
from models.user import User
from db.client import db_client
from services.user import *
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta


router = APIRouter(prefix="/users", tags=["users"], responses={404:{"message": "No encontrado"}})

exception = HTTPException(status_code=400, detail="ERROR")

ALGORITH = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"


oauth2 = OAuth2PasswordBearer(tokenUrl="login",)

crypt = CryptContext(schemes=["bcrypt"]) 

# Autentificador

async def auth_user(token: str = Depends(oauth2)):
    print(token)
    username = jwt.decode(token, SECRET, algorithms=ALGORITH).get("sub")
    return username

@router.get("/list")
async def users(current_user: str = Depends(auth_user)):
    lista = listar_usuarios()

    if not lista: 
        raise HTTPException(status_code=400, detail="Identificador incorrecto")

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


@router.put("/update/{id}")
async def updateUser(id: str, user: User):
    resultado_actualizacion = actualizar_usuario(id, user)
    if resultado_actualizacion:
        return {"success": resultado_actualizacion.modified_count > 0}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


@router.delete("/delete/{id}")
async def deleteUser(id: str):    
    usuario = borrar_usuario(id)
    if usuario: 
        return {"Success":"Borrado exitosamente"}
    else: 
        return {"Error":"No se pudo borrar el usuario"}
    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    
    user = buscarUsuario(form.username)
    print("Usuario", user)

    verificar = crypt.verify(form.password, user["password"])

    print(verificar)

    if not verificar:
        raise HTTPException(status_code=400, detail="La contraseña no es la correcta")

    access_token_expiration = timedelta(hours=ACCESS_TOKEN_DURATION)

    expire = datetime.utcnow() + access_token_expiration

    access_token = {"sub": user["name"], "exp": expire} 

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITH),"token_type":"bearer"}




        


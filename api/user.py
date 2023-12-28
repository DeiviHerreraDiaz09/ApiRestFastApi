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


# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")

#     return {"access_token": user.username, "token_type": "bearer"}
# LOGIN 
    
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

@router.post("/prueba")
async def auth_user(token: str = Depends(oauth2)):
    print(token)
    username = jwt.decode(token, SECRET, algorithms=ALGORITH).get("sub")
    return username


        


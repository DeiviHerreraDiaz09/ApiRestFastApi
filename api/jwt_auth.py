# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import jwt, JWTError
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from db.client import db_client
# from models.user import User


# ALGORITH = "HS256"
# ACCESS_TOKEN_DURATION = 1
# SECRET = "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"

# app = FastAPI()

# oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# crypt = CryptContext(schemes=["bcrypt"]) 

# def buscarUsuario(username: str):
#     if username in users_db:
#         return UserDB(**users_db[username])

# async def auth_user(token: str = Depends(oauth2)):
    
#     exception = HTTPException(status_code=401, detail="Credenciales de autorización invalidas", headers={"WWW-Authenticate": "Bearer"})
    
#     try:
#         username = jwt.decode(token, SECRET, algorithms=ALGORITH).get("sub")
#         if username is None:
#             raise exception
    
#     except JWTError:
#         raise exception

#     return buscarUsuario(username) 

# @app.post("/login")
# async def login(form: OAuth2PasswordRequestForm = Depends()):
    
#     user_db = users_db.get(form.username)
#     print("Usuario", user_db)

#     if not user_db:
#         raise HTTPException(status_code=400, detail="El usuario no es correcto")
    
#     user = buscarUsuario(form.username)
    
#     print("contraseña", user.password)

#     verificar = crypt.verify(form.password, user.password)

#     if not verificar:
#         raise HTTPException(status_code=400, detail="La contraseña no es la correcta")
    
#     access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)

#     expire = datetime.utcnow() + access_token_expiration

#     access_token = {"sub": user.username, "exp": expire} 


#     return {"access_token": jwt.encode(access_token, SECRET,algorithm=ALGORITH), "token_type": "bearer"}

  
# async def current_user(user: User = Depends(auth_user)):  
#     if user.disabled:
#         raise HTTPException(status_code=401, detail="Usuario inactivo")
#     return user 

# @app.get("/users/me")
# async def me(user: User = Depends(current_user)):
#     return user

# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


# app = FastAPI()

# oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# # Clase

# class User(BaseModel):
#     username: str
#     full_name: str
#     email: str
#     disabled: bool


# class UserDB(User):
#     password: str

# users_db = {
#     "Deivi":{
#         "username": "Deivi",
#         "full_name": "Deivi Herrera",
#         "email": "dherrerad@g.com",
#         "password":"123456",
#         "disabled": False
#     },
#     "Dayana":{
#         "username": "Dayana",
#         "full_name": "Dayana Herrera",
#         "email": "dayana@g.com",
#         "password":"123456",
#         "disabled": True
#     }
# }

# # Buscar usuario por nombre

# def buscarUsuario(username: str):
#     if username in users_db:
#         return UserDB(**users_db[username])
    
# # Autentificar

# async def current_user(token: str = Depends(oauth2)):
#     user = buscarUsuario(token)
#     if not user:
#         raise HTTPException(status_code=401, detail="Credenciales de autorización invalidas", headers={"WWW-Authenticate": "Bearer"})
    
#     if user.disabled:
#         raise HTTPException(status_code=401, detail="Usuario inactivo")


#     return user    


# @app.post("/login")
# async def login(form: OAuth2PasswordRequestForm = Depends()):
    
#     user_db = users_db.get(form.username)
#     print("Usuario", user_db)

#     if not user_db:
#         raise HTTPException(status_code=400, detail="El usuario no es correcto")
    
#     user = buscarUsuario(form.username)
    
#     print("contraseña", user.password)
#     if not form.password == user.password:
#         raise HTTPException(status_code=400, detail="La contraseña no es la correcta")
    
#     return {"access_token": user.username, "token_type": "bearer"}



# @app.get("/users/me")
# async def me(user: User = Depends(current_user)):
#     return user

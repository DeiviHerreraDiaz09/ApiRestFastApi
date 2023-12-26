from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Entidad de usuarios

class Usuario(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int

# Base de datos provisional

users_list = [Usuario(id=1,name="Deivi",lastname="Herrera",url="GrupoASD.co",age= 19),
         Usuario(id=2,name="Dayana",lastname="Herrera",url="GrupoASD.co",age=18),
         Usuario(id=3,name="Sebastian",lastname="Herrera",url="GrupoASD.co",age=19)] 
   
   
router = APIRouter(prefix="/users")

# PETICIONES

# Traer todos los usuarios

@router.get("/list")
async def users():
    if not(users_list == []):
        return users_list
    else:
        raise HTTPException(status_code=204, detail="Lista de usuarios vacia")        
    
# Traer usuario con id

@router.get("/{id}")
async def usersid(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=400, detail="Usuario no existente")
    
# Operación por Query, en la mayoria de casos se utiliza de manera opcional, traer usuario con id 
    
@router.get("/userquery/")
async def usersid(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se encuentra usuario"}

# Solicitud POST, registrar usuario por la memoria

@router.post("/add", status_code=201)
async def addUser(user: Usuario):
    
    users_list.append(user)
    
    try:
        return {"True", "Agrego a un nuevo usuario" + user.name}
    except:
        raise HTTPException(status_code=404, detail="asdasdasdasd")



# Solicitud PUT, actualizar usuario por la memoria

@router.put("/update")
async def updateUser(user: Usuario):
    
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return {"response", "Usuario actualizado correctamente"}
    if not found:
        raise HTTPException(status_code=404, detail="Usuario no actualizado")

# Solicitud DELETE, borrar usuario por la memoria 
    
@router.delete("/delete/{id}")
async def deleteUser(id: int):
    for index,delete_user in enumerate(users_list):
        if delete_user.id == id:
            # En este caso se utiliza del para borrarlo de la memoria
            # del users_list(index)
            # En tal caso de que se maneje base de datos
            users_list.pop(index)
            return "Usuario borrado"
        else: 
            raise HTTPException(status_code=404, detail="Usuario no borrado")





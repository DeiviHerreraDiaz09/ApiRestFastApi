from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import FileResponse,JSONResponse
from models.producto import Producto
from services.producto import *
import os


router = APIRouter(prefix="/products", tags=["products"], responses={404:{"message": "No encontrado"}})
path_img = "resources\\img\\"

exception = HTTPException(status_code=400, detail="ERROR")


@router.get("/list")
async def products():
    lista = listar_productos()
    if not lista:
        raise HTTPException(status_code=400, detail="Identificador incorrecto")
    return lista

@router.get("/{id}")
async def productoId(id: str):
    producto = listar_producto(id)
    return producto

@router.post("/add")
async def addProducto(
    name: str,
    descripcion: str,
    jefe: str,
    img: UploadFile = File(...),
):
        archivo = img.filename
        print(archivo)
        contents = await img.read()       
        with open(f"{path_img}{archivo}", "wb") as f:
            f.write(contents)
        producto = Producto(name=name, descripcion=descripcion, jefe=jefe, img=archivo)
        nuevo_producto = guardar_producto(producto)
        if nuevo_producto:
            return "archivo insertado correctamente"
        else:
            return "archivo insertado incorrectamente"

@router.put("/update/{id}")
async def updateProducto(id: str, producto: Producto):
    resultado_actualizacion = actualizar_producto(id, producto)
    if resultado_actualizacion:
        return {"success": resultado_actualizacion.modified_count > 0}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

@router.delete("/delete/{id}")
async def deleteProducto(id: str):
    usuario = borrar_producto(id)

    if usuario: 
        return {"Success":"Borrado exitosamente"}
    else:
        return {"Error":"No se pudo borrar el producto"}
    

@router.get("/show/{archivo}")
async def mostrar_archivo(archivo: str):
    files = os.listdir(path_img)

    if archivo not in files:
        return f"No existe el archivo: {archivo}"
    ubicacion = os.path.join(path_img, archivo)
    if archivo.lower().endswith('.pdf'):
        headers = {
            "Content-Disposition": f"attachment; filename={archivo}"
        }
        return FileResponse(ubicacion, headers=headers, media_type='application/pdf')
    else:
        return FileResponse(ubicacion)
    


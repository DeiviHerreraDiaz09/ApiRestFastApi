# Project API REST con FastApi

## Tabla de Contenidos
1. Descripción
2. Requisitos
3. Instalación
4. Configuración
5. Uso
6. API Endpoints
7. Estructura del Proyecto

## Descripción
Este proyecto de prueba fue creado para explorar y demostrar diversas funcionalidades de FastAPI, incluyendo la gestión de productos y usuarios con operaciones CRUD, manipulación de archivos y lógica de imágenes. Además, se ha implementado un sistema de autenticación y autorización para asegurar ciertas rutas y funcionalidades del proyecto. La estructura modular del código permite una fácil expansión y adaptación a necesidades futuras.

## Requisitos
Lista de requisitos necesarios para ejecutar el proyecto, por ejemplo:

- Python 3.x
- FastAPI
- MongoDB 

## Instalación 

## Instalación

Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto. Puedes seguir estos pasos:

1. **Crear un entorno virtual:**
      
    ```python -m venv venv```
    

2. **Activar el entorno virtual (Windows):**
  
    ```venv\Scripts\activate```

   **Activar el entorno virtual (Linux/Mac):**
   
    ```source venv/bin/activate```

3. **Instalar las dependencias:**
    
    ``` pip install -r requirements.txt ```

Este procedimiento creará un entorno virtual, lo activará y luego instalará las dependencias del proyecto en ese entorno. Asegúrate de ajustar la plataforma específica para activar el entorno virtual (puede variar entre Windows y sistemas basados en Unix).

## Configuración
Configura la conexión a la base de datos en db/client.py.
Asegúrate de tener los permisos necesarios para acceder a la base de datos.

## Uso

Para iniciar el proyecto, simplemente ejecuta el siguiente comando en tu terminal:
```uvicorn main:app --reload```

Esto iniciará el servidor FastAPI y permitirá que accedas a las API y servicios definidos en el archivo main.py. Asegúrate de tener todas las dependencias instaladas y que estás dentro del entorno virtual si has optado por utilizar uno.

Una vez que el servidor esté en funcionamiento, puedes acceder a las rutas definidas en los routers de api/ para interactuar con las diferentes funcionalidades del proyecto.

##  API Endpoints

| Productos                | Usuarios               |
| ----------------------- | ----------------------- |
| GET /products/list: Obtiene la lista de productos.| GET /users/list: Obtiene la lista de usuarios. |
| GET /products/{id}: Obtiene un producto por ID. | GET /users/{id}: Obtiene un usuario por ID. |
| POST /products/add: Agrega un nuevo producto.| POST /users/add: Agrega un nuevo usuario. |
| PUT /products/update/{id}: Actualiza un producto por ID. | PUT /users/update/{id}: Actualiza un usuario por ID. |
| DELETE /products/delete/{id}: Elimina un producto por ID. | DELETE /users/delete/{id}: Elimina un usuario por ID. |
| GET /products/show/{archivo}: Muestra un archivo asociado a un producto. | POST /users/login: Inicia sesión y obtiene un token de acceso. |


## Estructura del Proyecto
```
project-root/
│
├── api/
│   ├── __init__.py
│   ├── product.py
│   └── user.py
│
├── db/
│   ├── __init__.py
│   └── client.py
│
├── models/
│   ├── __init__.py
│   ├── producto.py
│   └── user.py
│
├── services/
│   ├── __init__.py
│   ├── producto.py
│   └── user.py
│
├── main.py
└── requirements.txt
```

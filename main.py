from fastapi import FastAPI
from api import user
from api import producto



app = FastAPI()

# Routers

app.include_router(user.router)
app.include_router(producto.router)

 
from fastapi import FastAPI
from user import router
from product import router

app = FastAPI()

# Routers

app.include_router(router)

# Endpoint de prueba

@app.get("/")
async def prueba():
    return "Hello world"



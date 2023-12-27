from fastapi import FastAPI
from api import user, product
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Routers

app.include_router(user.router)
app.include_router(product.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
 
from fastapi import FastAPI
from api import user, product

app = FastAPI()

# Routers

app.include_router(user.router)
app.include_router(product.router)





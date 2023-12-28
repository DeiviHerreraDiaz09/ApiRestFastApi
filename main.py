from fastapi import FastAPI
from api import user



app = FastAPI()

# Routers

app.include_router(user.router)

 
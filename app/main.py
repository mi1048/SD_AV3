from fastapi import FastAPI
from app.controllers import user_controller, client_controller, server_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(client_controller.router)
app.include_router(server_controller.router)

@app.get("/")
async def root():
    return {"message": "Sistema de Jogos API"}
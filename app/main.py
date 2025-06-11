from fastapi import FastAPI
from app.controllers.usuario_controller import rota as usuario_router
from app.controllers.servidor_controller import rota as servidor_router

app = FastAPI()

app.include_router(usuario_router, prefix="/api/usuarios")
app.include_router(servidor_router, prefix="/api/servidores")

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao Sistema de Jogos!"}

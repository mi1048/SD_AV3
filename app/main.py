from fastapi import FastAPI
from app.controllers.usuario_controller import rota as usuario_router

app = FastAPI()

# Prefixo "/api/usuarios" para todas as rotas de usuário
app.include_router(usuario_router, prefix="/api/usuarios")

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao Sistema de Jogos!"}
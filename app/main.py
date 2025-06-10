from fastapi import FastAPI
from app.controllers import (
    cliente_controller,
    servidor_controller,
    usuario_controller
)

app = FastAPI(
    title="Sistema de Jogos API",  # Título da API
    description="API para gerenciamento de clientes, servidores e usuários"  # Descrição da API
)

# Inclui as rotas dos controllers com prefixo "/api"
app.include_router(cliente_controller.rota, prefix="/api")
app.include_router(servidor_controller.rota, prefix="/api")
app.include_router(usuario_controller.rota, prefix="/api")

@app.get("/")
async def root():
    # Endpoint raiz com mensagem de boas-vindas e link para documentação
    return {
        "message": "Bem-vindo ao Sistema de Jogos",
        "docs": "/docs"
    }
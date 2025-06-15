from fastapi import FastAPI
from app.controllers import (
    usuario_controller,
    servidor_controller,
    pergunta_controller,
    resposta_controller
)

app = FastAPI()

# Inclui as rotas dos controllers, cada uma com seu prefixo
app.include_router(usuario_controller.rota, prefix="/api/usuarios")
app.include_router(servidor_controller.rota, prefix="/api/servidores")
app.include_router(pergunta_controller.rota, prefix="/api/perguntas")
app.include_router(resposta_controller.rota, prefix="/api/respostas")


@app.get("/")
async def root():
    # Endpoint raiz p/ teste rápido da API
    return {"message": "Bem-vindo ao Sistema de Jogos!"}

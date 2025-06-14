from fastapi import FastAPI
from app.controllers import (
    usuario_controller,
    servidor_controller,
    pergunta_controller,
    resposta_controller
)

app = FastAPI()

app.include_router(usuario_controller.rota, prefix="/api/usuarios")
app.include_router(servidor_controller.rota, prefix="/api/servidores")
app.include_router(pergunta_controller.rota, prefix="/api/perguntas")
app.include_router(resposta_controller.rota, prefix="/api/respostas")


@app.get("/")
async def root():
    return {"message": "Bem-vindo ao Sistema de Jogos!"}

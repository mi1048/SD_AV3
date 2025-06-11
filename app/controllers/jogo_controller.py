from fastapi import APIRouter, HTTPException
from app.services.jogo_service import ServicoJogo

rota = APIRouter()
servico = ServicoJogo()

@rota.post("/responder")
async def responder_pergunta(nome_usuario: str, pergunta_id: str, alternativa: str):
    acertou = servico.responder_pergunta(nome_usuario, pergunta_id, alternativa)
    return {"acertou": acertou}
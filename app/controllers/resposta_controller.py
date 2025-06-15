from fastapi import APIRouter, HTTPException
from app.services.usuario_service import ServicoUsuario
from app.services.servidor_service import ServicoServidor
from app.services.pergunta_service import ServicoPergunta
from bson import ObjectId, errors as bson_errors
from pydantic import BaseModel
from typing import Dict

rota = APIRouter()


class RespostaEnvio(BaseModel):
    usuario_nome: str
    servidor_id: str
    respostas: Dict[str, int]


@rota.post("/")
async def responder_perguntas(payload: RespostaEnvio):
    usuario_nome = payload.usuario_nome
    servidor_id = payload.servidor_id
    respostas = payload.respostas

    # Obter usuário
    usuario = ServicoUsuario().obter_usuario(usuario_nome)
    if not usuario:
        raise HTTPException(404, "Usuário não encontrado")
    
    # Obter pontuação atual
    pontuacao_atual = usuario.get("pontuacao", 0)
    acertos = 0
    servico_pergunta = ServicoPergunta()

    # Verificar cada resposta
    for pergunta_id, resposta in respostas.items():
        pergunta = servico_pergunta.obter_pergunta_por_id(pergunta_id, servidor_id)
        
        if pergunta and pergunta["resposta_correta"] == resposta:
            acertos += 1

    # Atualizar pontuação
    nova_pontuacao = pontuacao_atual + acertos
    ServicoUsuario().atualizar_pontuacao(usuario_nome, nova_pontuacao)

    # Obter nome do servidor
    servidor_nome = ServicoServidor().obter_nome_servidor(servidor_id)
    if not servidor_nome:
        raise HTTPException(404, "Servidor não encontrado")
    
    return {
        "message": "Respostas processadas",
        "servidor_id": servidor_id,
        "servidor_nome": servidor_nome,
        "acertos": acertos,
        "nova_pontuacao": nova_pontuacao
    }
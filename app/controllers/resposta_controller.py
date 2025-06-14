from fastapi import APIRouter, HTTPException
from app.services.usuario_service import ServicoUsuario
from app.services.servidor_service import ServicoServidor
from app.services.pergunta_service import ServicoPergunta  # NOVO IMPORT
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

    usuario = ServicoUsuario().obter_usuario(usuario_nome)
    if not usuario:
        raise HTTPException(404, "Usuário não encontrado")

    pontuacao_atual = usuario.get("pontuacao", 0)
    acertos = 0

    # Obtém o serviço de pergunta
    servico_pergunta = ServicoPergunta()
    
    for pergunta_id, resposta in respostas.items():
        # Busca a pergunta diretamente pelo serviço
        pergunta = servico_pergunta.obter_pergunta_por_id(pergunta_id, servidor_id)
        
        if not pergunta:
            continue  # Pula se não encontrar a pergunta
            
        # Verifica se a resposta está correta
        if pergunta["resposta_correta"] == resposta:
            acertos += 1

    nova_pontuacao = pontuacao_atual + acertos
    ServicoUsuario().atualizar_pontuacao(usuario_nome, nova_pontuacao)

    servidor_nome = ServicoServidor().obter_nome_servidor(servidor_id)
    return {
        "message": "Respostas processadas",
        "servidor_id": servidor_id,
        "servidor_nome": servidor_nome,
        "acertos": acertos,
        "nova_pontuacao": nova_pontuacao
    }

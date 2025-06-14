from fastapi import APIRouter, HTTPException
from app.services.usuario_service import ServicoUsuario
from app.services.servidor_service import ServicoServidor
from app.models.pergunta import Pergunta
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

    for pergunta_id, resposta in respostas.items():
        try:
            obj_id = ObjectId(pergunta_id)
        except bson_errors.InvalidId:
            continue  # pula ids inválidos

        pergunta = Pergunta.colecao().find_one({"_id": obj_id})
        if pergunta and pergunta["resposta_correta"] == resposta:
            acertos += 1

    nova_pontuacao = pontuacao_atual + acertos
    usuario_atualizado = ServicoUsuario().atualizar_pontuacao(
        usuario_nome, nova_pontuacao)
    print("Pontuação atualizada:", usuario_atualizado.get("pontuacao"))

    servidor = ServicoServidor().listar_servidores()
    servidor_nome = next((s["nome"]
                         for s in servidor if s["_id"] == servidor_id), None)
    return {
        "message": "Respostas processadas",
        "servidor_id": servidor_id,
        "servidor_nome": servidor_nome,
        "acertos": acertos,
        "nova_pontuacao": nova_pontuacao
    }

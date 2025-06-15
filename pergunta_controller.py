from fastapi import APIRouter, HTTPException
from app.services.pergunta_service import ServicoPergunta
from app.services.servidor_service import ServicoServidor
from pydantic import BaseModel
from typing import List

rota = APIRouter()
servico = ServicoPergunta()


class PerguntaCriacao(BaseModel):
    servidor_id: str
    enunciado: str
    alternativas: List[str]
    resposta_correta: int


@rota.post("/")
async def criar_pergunta(pergunta: PerguntaCriacao):
    if servico.criar_pergunta(
        pergunta.servidor_id,
        pergunta.enunciado,
        pergunta.alternativas,
        pergunta.resposta_correta
    ) is None:
        raise HTTPException(400, "Dados inválidos ou servidor não existe")
    return {"message": "Pergunta criada com sucesso!"}


@rota.get("/{servidor_id}")
async def obter_perguntas(servidor_id: str):
    perguntas = servico.listar_perguntas_por_servidor(servidor_id)
    if not perguntas:
        raise HTTPException(
            404, "Nenhuma pergunta encontrada para este servidor")
    # Buscar nome do servidor
    servidor = ServicoServidor().listar_servidores()
    servidor_nome = next((s["nome"]
                         for s in servidor if s["_id"] == servidor_id), None)
    return {
        "servidor_id": servidor_id,
        "servidor_nome": servidor_nome,
        "perguntas": perguntas
    }
from app.models.pergunta import Pergunta
from bson import ObjectId


class ServicoPergunta:
    def criar_pergunta(self, servidor_id: str, enunciado: str, alternativas: list, resposta_correta: int):
        if len(alternativas) != 4:
            return None

        nova_pergunta = Pergunta(
            servidor_id=servidor_id,
            enunciado=enunciado,
            alternativas=alternativas,
            resposta_correta=resposta_correta
        )

        result = Pergunta.colecao().insert_one(nova_pergunta.model_dump())
        if result.inserted_id:
            return Pergunta.serializar_mongo(nova_pergunta.model_dump() | {"_id": result.inserted_id})
        return None

    def listar_perguntas_por_servidor(self, servidor_id: str):
        perguntas = Pergunta.colecao().find({"servidor_id": servidor_id})
        return [Pergunta.serializar_mongo(p) for p in perguntas]

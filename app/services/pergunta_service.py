from app.models.pergunta import Pergunta
from app.models.servidor import Servidor
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
        servidor = Servidor.colecao().find_one({"_id": ObjectId(servidor_id)})
        servidor_nome = servidor["nome"] if servidor else "Servidor Desconhecido"
        
        return [{
            **Pergunta.serializar_mongo(p),
            "servidor_nome": servidor_nome  # Adiciona o nome sem alterar a estrutura original
        } for p in perguntas]

    def obter_pergunta_por_id(self, pergunta_id: str, servidor_id: str):
        try:
            obj_id = ObjectId(pergunta_id)
        except:
            return None
        
        pergunta = Pergunta.colecao().find_one({
            "_id": obj_id,
            "servidor_id": servidor_id
        })
        
        if not pergunta:
            return None
            
        servidor = Servidor.colecao().find_one({"_id": ObjectId(servidor_id)})
        servidor_nome = servidor["nome"] if servidor else "Servidor Desconhecido"
        
        return {
            **Pergunta.serializar_mongo(pergunta),
            "servidor_nome": servidor_nome  # Adiciona o nome dinamicamente
        }

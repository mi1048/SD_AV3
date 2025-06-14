from app.models.servidor import Servidor
from datetime import datetime
from bson import ObjectId  

def serializar_mongo(doc):
    if not doc:
        return doc
    doc = dict(doc)
    doc["_id"] = str(doc["_id"])
    return doc


class ServicoServidor:
    def criar_servidor(self, nome: str):
        if Servidor.colecao().find_one({"nome": nome}):
            return None  # Servidor já existe
        servidor = Servidor(nome=nome)
        Servidor.colecao().insert_one(servidor.model_dump())
        return servidor

    def listar_servidores(self):
        # Serializa cada documento para evitar erro com ObjectId
        return [serializar_mongo(s) for s in Servidor.colecao().find({})]

    def obter_nome_servidor(self, servidor_id: str):
        servidor = Servidor.colecao().find_one({"_id": ObjectId(servidor_id)})
        return servidor["nome"] if servidor else None

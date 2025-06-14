from pydantic import BaseModel
from app.database import bd
from datetime import datetime
from typing import List
from bson import ObjectId


class Pergunta(BaseModel):
    servidor_id: str
    enunciado: str
    alternativas: List[str]
    resposta_correta: int  # 0 a 3
    data_criacao: datetime = datetime.now()

    class Config:
        collection_name = "perguntas"

    @classmethod
    def colecao(cls):
        return bd[cls.Config.collection_name]

    @classmethod
    def serializar_mongo(cls, doc):
        doc = dict(doc)
        doc["_id"] = str(doc["_id"])
        return doc

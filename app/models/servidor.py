from pydantic import BaseModel
from app.database import bd
from datetime import datetime

class Servidor(BaseModel):
    nome: str
    data_criacao: datetime = datetime.now()

    class Config:
        collection_name = "servidores"

    @classmethod
    def colecao(cls):
        return bd[cls.Config.collection_name]
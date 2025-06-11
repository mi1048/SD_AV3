from pydantic import BaseModel
from app.database import bd

class Servidor(BaseModel):
    id: str
    nome: str  # Ex: "Matemática", "História"
    perguntas: list = []  # IDs das perguntas

    class Config:
        collection_name = "servidores"

    @classmethod
    def colecao(cls):
        return bd[cls.Config.collection_name]
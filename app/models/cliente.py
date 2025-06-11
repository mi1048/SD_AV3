from pydantic import BaseModel
from app.database import bd

class Cliente(BaseModel):
    id: str
    conectado: bool = False  # Indica se o cliente está conectado
    ultima_atividade: str = ""  # Armazena a data/hora da última atividade

    class Config:
        collection_name = "clientes"  # Nome da coleção no banco de dados

    @classmethod
    def colecao(cls):
        # Retorna a referência da coleção no banco
        return bd[cls.Config.collection_name]
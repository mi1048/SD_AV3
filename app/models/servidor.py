from pydantic import BaseModel
from app.database import bd

class Servidor(BaseModel):
    id: str
    status: str = "offline"  # Online ou offline no banco de dados
    clientes_conectados: int = 0  # Número de clientes conectados ao servidor

    class Config:
        collection_name = "servidores"  # Nome da coleção no banco de dados

    @classmethod
    def colecao(cls):
        # Retorna a referência da coleção no banco
        return bd[cls.Config.collection_name]
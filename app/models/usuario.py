from pydantic import BaseModel
from app.database import bd
from datetime import datetime

class Usuario(BaseModel):
    nome: str
    senha: str  # Obs: Em produção, use bcrypt!
    pontuacao: int = 0
    conectado: bool = False
    ultimo_login: datetime = None
    ultimo_logout: datetime = None

    class Config:
        collection_name = "usuarios"

    @classmethod
    def colecao(cls):
        return bd[cls.Config.collection_name]
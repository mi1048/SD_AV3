from pydantic import BaseModel
from app.database import bd

class Usuario(BaseModel):
    # Informações do usuário
    nome: str  
    senha: str  
    pontuacao: int = 0  

    class Config:
        collection_name = "usuarios"  # Nome da coleção no banco de dados

    @classmethod
    def colecao(cls):
        # Retorna a referência da coleção no banco
        return bd[cls.Config.collection_name]

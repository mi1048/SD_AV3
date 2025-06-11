from app.models.usuario import Usuario
from datetime import datetime

class AuthService:
    def criar_usuario(self, nome: str, senha: str):
        if Usuario.colecao().find_one({"nome": nome}):
            return None  # Usuário já existe
        usuario = Usuario(nome=nome, senha=senha)
        Usuario.colecao().insert_one(usuario.dict())
        return usuario

    def login(self, nome: str, senha: str):
        usuario = Usuario.colecao().find_one({"nome": nome})
        if not usuario or usuario["senha"] != senha:
            return None
        Usuario.colecao().update_one(
            {"nome": nome},
            {"$set": {"conectado": True, "ultimo_login": datetime.now()}}
        )
        return usuario

    def logout(self, nome: str):
        Usuario.colecao().update_one(
            {"nome": nome},
            {"$set": {"conectado": False, "ultimo_logout": datetime.now()}}
        )
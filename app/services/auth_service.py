from app.models.usuario import Usuario
from datetime import datetime


class AuthService:
    def criar_usuario(self, nome: str, senha: str):
        # Verifica se o usuário já existe
        if Usuario.colecao().find_one({"nome": nome}):
            return None  # Usuário já existe
        usuario = Usuario(nome=nome, senha=senha)
        Usuario.colecao().insert_one(usuario.dict())  # <-- CORRIGIDO AQUI
        return usuario

    def login(self, nome: str, senha: str):
        usuario = Usuario.colecao().find_one({"nome": nome})
        if not usuario or usuario["senha"] != senha:
            return None
        # Marca o usuário como conectado e atualiza o último login
        Usuario.colecao().update_one(
            {"nome": nome},
            {"$set": {"conectado": True, "ultimo_login": datetime.now()}}
        )
        return usuario

    def logout(self, nome: str):
        # Marca o usuário como desconectado e atualiza o último logout
        Usuario.colecao().update_one(
            {"nome": nome},
            {"$set": {"conectado": False, "ultimo_logout": datetime.now()}}
        )

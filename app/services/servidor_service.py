from app.models.servidor import Servidor
from datetime import datetime

class ServicoServidor:
    def criar_servidor(self, nome: str):
        if Servidor.colecao().find_one({"nome": nome}):
            return None  # Servidor já existe
        servidor = Servidor(nome=nome)
        Servidor.colecao().insert_one(servidor.dict())
        return servidor

    def listar_servidores(self):
        return list(Servidor.colecao().find({}))
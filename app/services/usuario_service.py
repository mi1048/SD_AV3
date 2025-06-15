from app.models.usuario import Usuario


def serializar_mongo(doc):
    if not doc:
        return doc
    doc = dict(doc)
    doc["_id"] = str(doc["_id"])
    return doc


class ServicoUsuario:
    def criar_usuario(self, nome: str, senha: str):
        if self.obter_usuario(nome):
            return None
        usuario = Usuario(nome=nome, senha=senha)
        Usuario.colecao().insert_one(usuario.model_dump())
        return serializar_mongo(usuario.model_dump())

    def obter_usuario(self, nome_usuario: str):
        usuario = Usuario.colecao().find_one({"nome": nome_usuario})
        return serializar_mongo(usuario) if usuario else None

    def atualizar_pontuacao(self, nome_usuario: str, pontuacao: int):
        # Atualização mais eficiente
        result = Usuario.colecao().update_one(
            {"nome": nome_usuario},
            {"$set": {"pontuacao": pontuacao}}
        )
        return result.modified_count > 0

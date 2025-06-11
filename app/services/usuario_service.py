from app.models.usuario import Usuario

class ServicoUsuario:
    def criar_usuario(self, usuario: Usuario):
        # Verifica se usuário já existe para evitar duplicidade
        if self.obter_usuario(usuario.nome):
            return None
        # Insere um novo usuário na coleção
        Usuario.colecao().insert_one(usuario.dict())
        return usuario

    def obter_usuario(self, nome_usuario: str):
        # Busca o usuário pelo nome no banco
        return Usuario.colecao().find_one({"nome": nome_usuario})

    def atualizar_pontuacao(self, nome_usuario: str, pontuacao: int):
        # Atualiza a pontuação do usuário
        Usuario.colecao().update_one(
            {"nome": nome_usuario},
            {"$set": {"pontuacao": pontuacao}}
        )
        # Retorna o usuário atualizado
        return self.obter_usuario(nome_usuario)
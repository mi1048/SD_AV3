from fastapi import APIRouter, HTTPException
from app.models.usuario import Usuario
from app.services.usuario_service import ServicoUsuario

rota = APIRouter()
servico = ServicoUsuario()

@rota.post("/usuarios/")
async def criar_usuario(usuario: Usuario):
    # Verifica se o usuário já existe
    if servico.obter_usuario(usuario.nome):
        raise HTTPException(400, detail="Usuário já existe")
    return servico.criar_usuario(usuario)

@rota.get("/usuarios/{nome_usuario}")
async def obter_usuario(nome_usuario: str):
    # Busca usuário pelo nome
    usuario = servico.obter_usuario(nome_usuario)
    if not usuario:
        raise HTTPException(404, detail="Usuário não encontrado")
    return usuario

@rota.put("/usuarios/{nome_usuario}/pontuacao")
async def atualizar_pontuacao(nome_usuario: str, pontuacao: int):
    # Atualiza a pontuação do usuário
    usuario = servico.atualizar_pontuacao(nome_usuario, pontuacao)
    if not usuario:
        raise HTTPException(404, detail="Usuário não encontrado")
    return usuario

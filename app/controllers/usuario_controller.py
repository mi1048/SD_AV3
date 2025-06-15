from fastapi import APIRouter, HTTPException
from app.services.auth_service import AuthService

rota = APIRouter()
auth = AuthService()


@rota.post("/")
async def criar_usuario(nome: str, senha: str):
    # Cria um novo usuário
    if auth.criar_usuario(nome, senha) is None:
        raise HTTPException(400, "Usuário já existe")
    return {"message": f"Usuário {nome} criado!"}


@rota.post("/login")
async def login(nome: str, senha: str):
    # Realiza login do usuário
    usuario = auth.login(nome, senha)
    if not usuario:
        raise HTTPException(401, "Usuário ou senha inválidos")
    return {"message": "Login bem-sucedido"}


@rota.post("/logout")
async def logout(nome: str):
    # Realiza logout do usuário
    auth.logout(nome)
    return {"message": "Logout realizado"}

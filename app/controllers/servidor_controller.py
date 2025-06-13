from fastapi import APIRouter, HTTPException
from app.services.servidor_service import ServicoServidor

rota = APIRouter()
servico = ServicoServidor()

@rota.post("/")
async def criar_servidor(nome: str):
    if servico.criar_servidor(nome) is None:
        raise HTTPException(400, "Servidor já existe")
    return {"message": f"Servidor {nome} criado!"}

@rota.get("/")
async def listar_servidores():
    return servico.listar_servidores()
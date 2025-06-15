from fastapi import APIRouter, HTTPException
from app.services.servidor_service import ServicoServidor  # Importação adicionada

rota = APIRouter()
servico = ServicoServidor()  # Serviço de servidores

# Endpoint p/ criar servidor
@rota.post("/")
async def criar_servidor(nome: str):  # Nome alterado
    if servico.criar_servidor(nome) is None:
        raise HTTPException(400, "Servidor já existe")
    return {"message": f"Servidor {nome} criado!"}

# Novo endpoint p/ listar servidores
@rota.get("/")
async def listar_servidores():
    servidores = servico.listar_servidores()
    if not servidores:
        raise HTTPException(404, "Nenhum servidor encontrado")
    return servidores
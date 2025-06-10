from fastapi import APIRouter, HTTPException
from app.models.servidor import Servidor
from app.services.servidor_service import ServicoServidor

rota = APIRouter()
servico = ServicoServidor()

@rota.post("/servidores/")
async def registrar_servidor(servidor: Servidor):
    # Verifica se o servidor já está registrado
    if servico.obter_servidor(servidor.id):
        raise HTTPException(400, detail="Servidor já registrado!")
    return servico.registrar_servidor(servidor)

@rota.get("/servidores/{servidor_id}")
async def obter_servidor(servidor_id: str):
    # Busca servidor pelo ID
    servidor = servico.obter_servidor(servidor_id)
    if not servidor:
        raise HTTPException(404, detail="Servidor não encontrado...")
    return servidor

@rota.put("/servidores/{servidor_id}/status")
async def atualizar_status(servidor_id: str, status: str, clientes: int = 0):
    # Atualiza o status do servidor e a quantidade de clientes
    servidor = servico.atualizar_status(servidor_id, status, clientes)
    if not servidor:
        raise HTTPException(404, detail="Servidor não encontrado...")
    return servidor

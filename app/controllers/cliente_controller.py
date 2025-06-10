from fastapi import APIRouter, HTTPException
from app.models.cliente import Cliente
from app.services.cliente_service import ServicoCliente

rota = APIRouter()
servico = ServicoCliente()

@rota.post("/clientes/")
async def registrar_cliente(cliente: Cliente):
    # Verifica se o cliente já está registrado
    if servico.obter_cliente(cliente.id):
        raise HTTPException(400, detail="Cliente já registrado")
    return servico.registrar_cliente(cliente)

@rota.get("/clientes/{cliente_id}")
async def obter_cliente(cliente_id: str):
    # Busca cliente pelo ID
    cliente = servico.obter_cliente(cliente_id)
    if not cliente:
        raise HTTPException(404, detail="Cliente não encontrado")
    return cliente

@rota.put("/clientes/{cliente_id}/status")
async def atualizar_status(cliente_id: str, status: bool):
    # Atualiza o status do cliente (ativo/inativo)
    cliente = servico.atualizar_status(cliente_id, status)
    if not cliente:
        raise HTTPException(404, detail="Cliente não encontrado")
    return cliente

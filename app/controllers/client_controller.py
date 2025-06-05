from fastapi import APIRouter, HTTPException
from app.models.client import Client
from app.services.client_service import ClientService

router = APIRouter()
client_service = ClientService()

@router.post("/clients/")
async def register_client(client: Client):
    if client_service.get_client(client.id):
        raise HTTPException(status_code=400, detail="Client already registered")
    return client_service.register_client(client)

@router.get("/clients/{client_id}")
async def get_client(client_id: str):
    client = client_service.get_client(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/clients/{client_id}/status")
async def update_client_status(client_id: str, status: bool):
    client = client_service.update_status(client_id, status)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

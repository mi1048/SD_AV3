from fastapi import APIRouter, HTTPException
from app.models.server import Server
from app.services.server_service import ServerService

router = APIRouter()
server_service = ServerService()

@router.post("/servers/")
async def register_server(server: Server):
    if server_service.get_server(server.id):
        raise HTTPException(status_code=400, detail="Server already registered")
    return server_service.register_server(server)

@router.get("/servers/{server_id}")
async def get_server(server_id: str):
    server = server_service.get_server(server_id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@router.put("/servers/{server_id}/status")
async def update_server_status(server_id: str, status: str, clients: int = 0):
    server = server_service.update_status(server_id, status, clients)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server
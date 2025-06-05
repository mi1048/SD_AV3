from pydantic import BaseModel

class Server(BaseModel):
    id: str
    status: str = "offline"
    connected_clients: int = 0

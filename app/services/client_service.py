from app.models.client import Client
    
class ClientService:
    def __init__(self):
        self.clients = []

    def register_client(self, client: Client):
        self.clients.append(client)
        return client

    def get_client(self, client_id: str):
        for client in self.clients:
            if client.id == client_id:
                return client
        return None

    def update_status(self, client_id: str, status: bool):
        client = self.get_client(client_id)
        if client:
            client.connected = status
            return client
        return None
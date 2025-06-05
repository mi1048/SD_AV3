from app.models.server import Server

class ServerService:
    def __init__(self):
        self.servers = []

    def register_server(self, server: Server):
        self.servers.append(server)
        return server

    def get_server(self, server_id: str):
        for server in self.servers:
            if server.id == server_id:
                return server
        return None

    def update_status(self, server_id: str, status: str, clients: int = 0):
        server = self.get_server(server_id)
        if server:
            server.status = status
            server.connected_clients = clients
            return server
        return None
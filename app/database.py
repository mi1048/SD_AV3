from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

# Lê a URI do MongoDB do ambiente (definida no docker-compose)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")

cliente_mongo = None

try:
    # Tenta conectar ao MongoDB
    cliente_mongo = MongoClient(MONGO_URI)
    cliente_mongo.server_info()  # Testa a conexão
    print("A conexão com o MongoDB teve sucesso!")
except ConnectionFailure as e:
    # Se falhar, mostra o erro no log do container
    print(f"Falha ao conectar com o MongoDB: {e}")

# Seleciona o banco de dados (cria se não existir)
bd = cliente_mongo["sistema_jogos"]

# Lista as coleções existentes (útil para debug)
print(bd.list_collection_names())

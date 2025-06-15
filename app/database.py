from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Configuração da conexão com o MongoDB 
MONGO_URI = "mongodb://localhost:27017"  # O servidor será local

# Variável global para a conexão
cliente_mongo = None

try:
    # Tenta estabelecer a conexão
    cliente_mongo = MongoClient(MONGO_URI)
    cliente_mongo.server_info()  # Testa se a conexão está ativa
    print("A conexão com o MongoDB teve sucesso!")
except ConnectionFailure as e: #e = erro
    print(f"Falha ao conectar com o MongoDB: {e}")

# Acessa o banco de dados "sistema_jogos" (cria se não existir)
bd = cliente_mongo["sistema_jogos"]  

print(bd.list_collection_names()) # Lista as coleções no banco de dados
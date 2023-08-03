import psycopg2
from .config import db_config

# Função para conectar ao banco de dados
def connect():
    try:
        conn = psycopg2.connect(**db_config)
        conn.set_client_encoding('UTF8')  # Adicione esta linha para definir o suporte a UTF-8
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

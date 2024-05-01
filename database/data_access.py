import psycopg2
from database.models import Pessoa, db
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

# ======================
# Região: Banco de Dados
# ======================

def get_db_connection():
    conn = psycopg2.connect(
        dbname='xelfcdut',
        user='xelfcdut',
        password='2DHCHniJlOswtUcXjf0CuPlkZJUy3Zri',
        host='kesavan.db.elephantsql.com'
    )
    return conn

# ======================
# Região: Pessoa
# ======================
def consultar_pessoa_por_nome(nome):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)  # Usar RealDictCursor
    try:
        cur.execute("SELECT * FROM tb_pessoas WHERE nome ILIKE %s", ('%' + nome + '%',))
        pessoa = cur.fetchone()
    except Exception as e:
        print(f"Erro ao consultar pessoa por nome: {e}")
    finally:
        cur.close()
        conn.close()
    return pessoa

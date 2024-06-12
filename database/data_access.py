import psycopg2
from psycopg2.extras import RealDictCursor
from database.database import get_db_connection
from database.models import Produto

# ======================
# Região: Banco de Dados
# ======================
def __init__(self):
        pass

def execute_query(self, query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
        raise
    finally:
        cur.close()
        conn.close()

def log_error(self, action, error, user):
    query = "INSERT INTO tb_logsErros (acao, Erro, usuario) VALUES (%s, %s, %s)"
    params = (action, str(error), user)
    self.execute_query(query, params)

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
        pessoa = None
    finally:
        cur.close()
        conn.close()
    return pessoa

# ======================
# Região: login
# ======================
def consultar_usuario(email, senha):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM tb_pessoas WHERE email = %s AND senha = %s", (email, senha))
        usuario = cur.fetchone()
        return usuario
    except Exception as e:
        print(f"Erro ao validar login: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# ======================
# Região: Produtos
# ======================
def cadastro_produto(marca, modelo, tamanho_tela, tipo_iluminacao, proporcao, taxa_contraste, tempo_resposta, interface_saida, cor, brilho, resolucao_maxima, taxa_atualizacao, descricao, caminho_imagem, valor, monitor):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        
        
        sql = """
        INSERT INTO tb_produtos (marca, modelo, tamanhotela, tipoiluminacao, proporcao, taxacontraste, temporesposta, interfasesaida, cor, brilho, resolucaomaxima, taxaatualizacao, descricao, caminhoimagem, valor, monitor)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql, (marca, modelo, tamanho_tela, tipo_iluminacao, proporcao, taxa_contraste, tempo_resposta, interface_saida, cor, brilho, resolucao_maxima, taxa_atualizacao, descricao, caminho_imagem, valor, monitor))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")
        return False
    finally:
        cur.close()
        conn.close()

def consultar_produto_card(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM tb_produtos WHERE id = %s", (id))
        produto_data = cur.fetchone()
        
        if produto_data is not None:
            produto = {
                'id': produto_data['id'],
                'marca': produto_data['marca'],
                'modelo': produto_data['modelo'],
                'tamanho_tela': produto_data['tamanho_tela'],
                'tipo_iluminacao': produto_data['tipo_iluminacao'],
                'proporcao': produto_data['proporcao'],
                'taxa_contraste': produto_data['taxa_contraste'],
                'tempo_resposta': produto_data['tempo_resposta'],
                'interfase_saida': produto_data['interfase_saida'],
                'cor': produto_data['cor'],
                'brilho': produto_data['brilho'],
                'resolucao_maxima': produto_data['resolucao_maxima'],
                'taxa_atualizacao': produto_data['taxa_atualizacao'],
                'descricao': produto_data['descricao'],
                'caminho_imagem': produto_data['caminho_imagem'],
                'valor': produto_data['valor'],
                'monitor': produto_data['monitor']
            }
            return produto
        else:
            return None
    except Exception as e:
        print(f"Erro ao consultar produto: {e}")
        return None
    finally:
        cur.close()
        conn.close()

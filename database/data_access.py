import psycopg2
from psycopg2.extras import RealDictCursor
from database.database import get_db_connection
from database.models import Produto

# ======================
# Região: Banco de Dados
# ======================

# Função get_db_connection já importada do database

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
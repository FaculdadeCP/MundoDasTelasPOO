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
# Região: Usuario
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
        
def cadastrar_usuario(nome, sobrenome, cpf, rg, email, senha, funcionario_loja):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        sql = """
        INSERT INTO tb_pessoas (nome, sobrenome, cpfcnpj, rg, email, senha, funcionarioloja)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id  -- Adiciona isto para retornar o ID do usuário inserido
        """
        cur.execute(sql, (nome, sobrenome, cpf, rg, email, senha, funcionario_loja))
        id_usuario = cur.fetchone()['id']  # Captura o ID retornado pela query
        conn.commit()
        print(f"Usuário cadastrado com sucesso! ID: {id_usuario}")
        return id_usuario  # Retorna o ID do usuário
    except psycopg2.Error as e:
        print(f"Erro ao cadastrar usuário: {e}")
        conn.rollback()
        return None  # Retorna None se houver falha
    finally:
        cur.close()
        conn.close()
     
def consultar_Email(email):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        # Certifique-se de passar o e-mail como uma tupla, ou seja, (email,)
        cur.execute("SELECT * FROM tb_pessoas WHERE email = %s", (email,))
        retorno = cur.fetchone()
        print(f"RETORNO CONSULTA SQL: {retorno}")
        # Retorna True se um registro for encontrado, caso contrário, retorna False
        return retorno is not None
    except Exception as e:
        print(f"Erro ao validar email: {e}")
        return False
    finally:
        cur.close()
        conn.close()

def Vincular_Usuario_Endereco(usuarioId,EnderecoId,residencial,comercial):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        sql = """
        INSERT INTO tb_enderecoslista (pessoa_id, endereco_id,residencial,comercial)
        VALUES (%s, %s, %s,%s)
        """
        cur.execute(sql, (usuarioId,EnderecoId,residencial,comercial))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")
        return False
    finally:
        cur.close()
        conn.close()

def Vincular_usuario_cargo(usuarioId,cargo,ativo):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        sql = """
        INSERT INTO tb_funcionarios (pessoa_id, cargo_id,ativo)
        VALUES (%s, %s, %s)
        """
        cur.execute(sql, (usuarioId,cargo,ativo))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")
        return False
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
        
# ======================
# Região: Funcionarios
# ======================

def consultar_funcionarios():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT PS.id, PS.nome, PS.sobrenome, PS.cpfcnpj, CG.cargo, FN.ativo FROM tb_funcionarios FN INNER JOIN tb_pessoas PS ON PS.id = FN.pessoa_id LEFT JOIN tb_cargos CG ON CG.id = FN.cargo_id ORDER BY FN.ativo DESC")
        lstFuncionarios = cur.fetchall()
        return lstFuncionarios
    except Exception as e:
        print(f"Erro ao carregar os Funcionários: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def consultar_funcionario(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        sql = """
        SELECT PS.*, CG.cargo, enlst.residencial,enlst.comercial, EN.cep,EN.logradouro, EN.numero,EN.bairro, EN.complemento,EN.estado, EN.cidade, EN.telefone  FROM tb_pessoas PS inner join tb_funcionarios FN on FN.pessoa_id = PS.id left join tb_cargos cg  on CG.id = FN.cargo_id  inner join tb_enderecoslista enlst on enlst.pessoa_id = PS.id inner join tb_enderecos EN on EN.id = enlst.endereco_id WHERE PS.id = %s
        """
        cur.execute(sql,(id))
        lstFuncionarios = cur.fetchall()
        return lstFuncionarios
    except Exception as e:
        print(f"Erro ao carregar os Funcionários: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def atualizar_funcionario(id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("")
        lstFuncionarios = cur.fetchall()
        return lstFuncionarios
    except Exception as e:
        print(f"Erro ao carregar os Funcionários: {e}")
        return None
    finally:
        cur.close()
        conn.close()


# ======================
# Região: Endereço
# ======================
def cadastro_endereco(cep, logradouro, numero, complemento, estado, cidade, telefone, bairro):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        sql = """
        INSERT INTO tb_enderecos (cep, logradouro, numero, complemento, estado, cidade, telefone, bairro)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id  -- Aqui estamos pedindo para retornar o ID do novo endereço
        """
        cur.execute(sql, (cep, logradouro, numero, complemento, estado, cidade, telefone, bairro))
        id_endereco = cur.fetchone()[0]  # Captura o ID retornado pela query
        conn.commit()
        print(f"Cadastrou o endereço com sucesso! ID: {id_endereco}")
        return id_endereco
    except Exception as e:
        print(f"Erro ao cadastrar endereço: {e}")
        return None
    finally:
        cur.close()
        conn.close()
# ======================
# Região: Cargos
# ======================
def consultar_Cargos():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM tb_cargos")
        lstCargos = cur.fetchall()
        print(lstCargos)  # Veja o que está sendo retornado
        return lstCargos
    except Exception as e:
        print(f"Erro ao carregar os cargos: {e}")
        return None
    finally:
        cur.close()
        conn.close()
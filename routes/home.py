from flask import Blueprint, render_template
from flask import Blueprint, render_template
from database.data_access import get_db_connection
import psycopg2.extras

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        cur.execute("SELECT * FROM tb_produtos")
        produtos_data = cur.fetchall()
        
        produtos = []
        for produto_data in produtos_data:
            produto = {
                'id': produto_data['id'],
                'marca': produto_data['marca'],
                'modelo': produto_data['modelo'],
                'tamanho_tela': produto_data['tamanhotela'],
                'tipo_iluminacao': produto_data['tipoiluminacao'],
                'proporcao': produto_data['proporcao'],
                'taxa_contraste': produto_data['taxacontraste'],
                'tempo_resposta': produto_data['temporesposta'],
                'interfase_saida': produto_data['interfasesaida'],
                'cor': produto_data['cor'],
                'brilho': produto_data['brilho'],
                'resolucao_maxima': produto_data['resolucaomaxima'],
                'taxa_atualizacao': produto_data['taxaatualizacao'],
                'descricao': produto_data['descricao'],
                'caminho_imagem': produto_data['caminhoimagem'],
                'valor': produto_data['valor'],
                'monitor': produto_data['monitor']
            }
            produtos.append(produto)
        return render_template('index.html', produtos=produtos)
    except Exception as e:
        print(f"Erro ao consultar produtos: {e}")
        return render_template('error.html', message=f"{e}")
    finally:
        cur.close()
        conn.close()



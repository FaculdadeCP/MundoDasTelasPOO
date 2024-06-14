import os
from flask import Blueprint, render_template, request, redirect, url_for
from classes.cls_produto import Produto
from static.s3_config import upload_to_s3

produto_bp = Blueprint('produto', __name__)

# Instancia a classe Produto
produto_obj = Produto()

@produto_bp.route('/produtos/tvs')
def produtos_tvs():
    return render_template('produtos_tvs.html')

@produto_bp.route('/produtos/monitores')
def produtos_monitores():
    return render_template('produtos_monitores.html')

@produto_bp.route('/produtos/cadastro', methods=['GET', 'POST'])
def produtos_cadastro():
    if request.method == 'POST':
        # Recupera os dados do formulário
        caminho_imagem = request.files.get('caminho_imagem')
        
        # Verifica se o arquivo foi enviado
        if caminho_imagem and caminho_imagem.filename != '':
            caminho_imagem.save(caminho_imagem.filename)  # Salva temporariamente
            caminho_imagem_url = upload_to_s3(caminho_imagem.filename, caminho_imagem.filename)
            os.remove(caminho_imagem.filename)  # Remove o arquivo temporário
        else:
            caminho_imagem_url = None
        
        dados_produto = {
            "marca": request.form.get('marca'),
            "modelo": request.form.get('modelo'),
            "tamanho_tela": request.form.get('tamanho_tela'),
            "tipo_iluminacao": request.form.get('tipo_iluminacao'),
            "proporcao": request.form.get('proporcao'),
            "taxa_contraste": request.form.get('taxa_contraste'),
            "tempo_resposta": request.form.get('tempo_resposta'),
            "interfase_saida": request.form.get('interfase_saida'),
            "cor": request.form.get('cor'),
            "brilho": request.form.get('brilho'),
            "resolucao_maxima": request.form.get('resolucao_maxima'),
            "taxa_atualizacao": request.form.get('taxa_atualizacao'),
            "descricao": request.form.get('descricao'),
            "caminho_imagem": caminho_imagem_url,  # O link da imagem no S3
            "valor": request.form.get('valor'),
            "monitor": request.form.get('monitor') == 'on'
        }

        # Chama o método de cadastro de produto passando os dados do formulário
        sucesso = produto_obj.cadastrar_produto(dados_produto)
        
        if sucesso:
            # Redireciona para uma página de sucesso ou outra página
            return redirect(url_for('index.html'))
        else:
            return "Erro ao cadastrar produto", 500
    
    return render_template('produtos_cadastro.html')

@produto_bp.route('/produtos/consulta')
def produtos_consulta():
    return render_template('produto_consulta.html')

@produto_bp.route('estoque/consulta')
def consulta_estoque():
    return render_template('entrada_estoque.html')

@produto_bp.route('estoque/cadastro')
def cadastro_estoque():
    return render_template('entrada_estoque_atualizar.html')
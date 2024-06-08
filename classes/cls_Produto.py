from database.data_access import cadastro_produto

class Produto:
    def consultar_produto(self):
        # Lógica para consultar produtos
        pass

    def cadastrar_produto(self, dados):
        # Extrai os dados do dicionário e chama a função de cadastro
        sucesso = cadastro_produto(
            dados['marca'], dados['modelo'], dados['tamanho_tela'], dados['tipo_iluminacao'], 
            dados['proporcao'], dados['taxa_contraste'], dados['tempo_resposta'], 
            dados['interfase_saida'], dados['cor'], dados['brilho'], dados['resolucao_maxima'], 
            dados['taxa_atualizacao'], dados['descricao'], dados['caminho_imagem'], 
            dados['valor'], dados['monitor']
        )
        return sucesso

    def atualizar_produto(self):
        # Lógica para atualizar produto
        pass

    def remover_produto(self):
        # Lógica para remover produto
        pass

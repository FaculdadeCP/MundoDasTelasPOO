from flask import render_template
from database.data_access import consultar_carrinho,inserir_produto_carrinho,Atualizar_produto_carrinho,consultar_produto_carrinho,remover_todos_produtos_carrinho,consultar_valor_carrinho,remover_produto_carrinho
class carrinho:
    def AdicionarProduto(usuario,produto,quantidade):
        retornoConsulta = consultar_produto_carrinho(usuario,produto)
        if retornoConsulta == 1:
            Atualizar_produto_carrinho(usuario,produto,quantidade)
        if retornoConsulta == 2:
            inserir_produto_carrinho(usuario,produto,quantidade)
        if retornoConsulta == 3:
            return "Ocorreu um erro!"
    
    def CarregarCarrinho(usuario):
        produtos_carrinho = consultar_carrinho(usuario)
        if produtos_carrinho is None:
            print("carrinho VAZIO!!!!")
            return [] 
        return produtos_carrinho
      
    def LimparCarrinho(usuario):
        try:
            resultado = remover_todos_produtos_carrinho(usuario)
            return resultado
        except Exception as e:
            print(f"Erro ao limpar o carrinho: {e}")
            return None
        
    def AtualizarProduto(usuario,produto,quantidade):
        return Atualizar_produto_carrinho(usuario,produto,quantidade)
    
    def AtualizarValorCarrinho(usuario):
        return consultar_valor_carrinho(usuario)
    
    def removerProduto(usuario, produto):
        return remover_produto_carrinho(usuario,produto)
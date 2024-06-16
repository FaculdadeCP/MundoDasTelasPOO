from database.data_access import consultar_carrinho,inserir_produto_carrinho,Atualizar_produto_carrinho,consultar_produto_carrinho
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
      carrinhoUsuario = consultar_carrinho(usuario)
from database.data_access import cadastrar_usuario

class Usuario:
    def cadastrar_usuario(self,dados):
        
        sucesso = cadastrar_usuario(dados['nome'],dados['sobrenome'],dados['cpf'],dados['rg'],dados['email'],dados['senha'],dados['funcionario_loja'])
        
        if sucesso: return True
        else: return False
    

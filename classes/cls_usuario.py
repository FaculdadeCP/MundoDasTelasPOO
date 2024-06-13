from database.data_access import cadastrar_usuario,consultar_Email

class Usuario:
    def cadastrar_usuario(self,dados):
        
        temEmail = consultar_Email(dados['email'])
        if temEmail: 
            return 'Email já cadastrado!'
        else: 
            sucesso = cadastrar_usuario(dados['nome'],dados['sobrenome'],dados['cpf'],dados['rg'],dados['email'],dados['senha'],dados['funcionario_loja'])
    
            if sucesso: return 'Usuário Cadastrado com sucesso!'
            else: return 'Falha ao cadastrar!'
        
        
from database.data_access import consultar_funcionarios,cadastrar_usuario,consultar_Email
class Funcionario:
    def CarregarFuncionarios():
        return  consultar_funcionarios()
    
    def CarregarFuncionario(id):
        return consultar_funcionarios(id)
    
    def Cadastrar_Funcionario(self,dados):
        temEmail = consultar_Email(dados['email'])
        if temEmail: 
            return 'Email já cadastrado!'
        else: 
            sucesso = cadastrar_usuario(dados['nome'],dados['sobrenome'],dados['cpf'],dados['rg'],dados['email'],dados['senha'],dados['funcionario_loja'])
    
            if sucesso: return 'Usuário Cadastrado com sucesso!'
            else: return 'Falha ao cadastrar!'
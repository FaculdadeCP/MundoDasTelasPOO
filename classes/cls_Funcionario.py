from database.data_access import consultar_funcionarios,cadastrar_usuario,consultar_Email,cadastro_endereco,atualizar_funcionario,Vincular_Usuario_Endereco,Vincular_usuario_cargo
class Funcionario:
    def CarregarFuncionarios():
        return  consultar_funcionarios()
    
    def CarregarFuncionario(id):
        return consultar_funcionarios(id)
    
    def Cadastrar_Funcionario(self, dados):
        temEmail = consultar_Email(dados['email'])
        if temEmail: 
            return 'Email já cadastrado!'
        else:
            idUsuario = cadastrar_usuario(dados['nome'], dados['sobrenome'], dados['cpf'], dados['rg'], dados['email'], dados['senha'], dados['funcionario_loja'])
            print(f"Cadastou o usuário: {idUsuario}")

            Idendereco = cadastro_endereco(dados['cep'], dados['logradouro'],dados['numero'], dados['complemento'], dados['estado'], dados['cidade'], dados['telefone'],dados['bairro'])
            print(f"Cadastrou o endereço do usuário {idUsuario}")

            Vincular_Usuario_Endereco(idUsuario, Idendereco, dados['residencial'], dados['comercial'])
            print(f"Vinculou o endereço do usuário {idUsuario}")
            
            print(f"dados do cargo: {idUsuario,dados['cargo'],dados['funcionarioAtivo']}")
            
            Vincular_usuario_cargo(idUsuario,dados['cargo'],dados['funcionarioAtivo'])
            print(f"Vinculou o cargo do usuário {idUsuario}")
            
            print(f"Cadastro Finalizado com sucesso!")
        
            return 'Cadastro Realizado com sucesso!'
            
    def Atualizar_Funcionario(self,dados):
        temEmail = consultar_Email(dados['email'])
        if temEmail: 
            return 'Email já cadastrado!'
        else: 
            sucesso = atualizar_funcionario(dados['nome'],dados['sobrenome'],dados['cpf'],dados['rg'],dados['email'],dados['senha'],dados['funcionario_loja'])
    
            if sucesso: return 'Usuário Cadastrado com sucesso!'
            else: return 'Falha ao cadastrar!'
from database.data_access import consultar_funcionarios

class Funcionario:
    def CarregarFuncionarios():
        return  consultar_funcionarios()
from database.data_access import consultar_Cargos
class Cargo:
    def CarregarCargos():
            try:
                cargos = consultar_Cargos()
                if cargos is None:
                    return []  # Retorna uma lista vazia se não houver cargos
                return cargos
            except Exception as e:
                print(f"Erro ao carregar os cargos: {e}")
                return []  # Retorna uma lista vazia em caso de erro
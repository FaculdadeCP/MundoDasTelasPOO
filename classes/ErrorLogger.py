from flask import flash

class ErrorLogger:
    def __init__(self, data_access):
        self.data_access = data_access

    def handle_exception(self, action, error, user):
        try:
            self.data_access.log_error(action, error, user)
        except Exception as e:
            print(f"Falha ao registrar o erro no banco de dados: {e}")
        flash("Um erro inesperado aconteceu! Tente novamente mais tarde!", "error")

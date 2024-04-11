import traceback
from Controller.operationUserFlagee import FlageeOperations

class FlageeExecutor:
    def __init__(self, connect, response):
        self.cnn = connect
        self.browser = response
        self.op = FlageeOperations(response)

    def run(self, user):
        try:
            self.conecction = self.cnn.login()
            if self.conecction == "Logged in successfully!":
                self.seach_user = self.op.find_mail_user(user)
                if self.seach_user == 'Busca por email concluído!':
                    self.result = self.op.change_status_user()
                    if self.result == "Status do email alterado para 'Bloqueado'!":
                        response = (self.result)
                    else:
                        response = (self.result)  
                else:
                    response = ("Finalizando. ", self.seach_user)
                return response
            else:
                response = (f"Finalizando. \n{self.connection}\n{self.seach_user}")
        except Exception as e:
            print(f'Error: {e}')
            traceback.print_exc()
        finally:
            if self.browser:
                self.cnn.close_connection()
                # concat = (f"{response}\n{end}")
                return response
